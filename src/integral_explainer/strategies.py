"""Wire the engine's real methods into the search layer (CLAUDE.md rule 9), and declare a
COVERAGE row for EVERY method so the harness can prove completeness.

The point of the COVERAGE table: a method that isn't declared here is invisible to the harness,
and the harness fails if any `methods.METHODS` key is undeclared — so "we don't go wrong as we
expand": add a method -> declare its coverage (executable strategy, or honest recognition-only
stub) -> the harness checks it. `status`:
  - "executable"        : has a real transform wired as a search Strategy (tested end-to-end).
  - "recognition-only"  : a named method with NO generic executable transform yet (divergent /
                          conceptual: zeta-reg, abel-plana, dim-reg, ...). Honestly flagged,
                          not faked.
"""
from __future__ import annotations

import sympy as sp

from .search import Strategy, search, complexity
from .curvature import is_zero, Curvature                      # noqa: F401  (Curvature: tensor kind)
from .methods import METHODS
from . import special_methods as sm
from .gap_strategies import hyperbolic_exp_rewrite, inverse_function_parts, complete_square_sub

# ---- problem KINDS: a state model + a goal test --------------------------------------------
# INTEGRAL/IDENTITY are SEARCH kinds (a KIND_SOLVERS list + a GOAL); CAPABILITY is a DIRECT
# computation (no search), realized by a function in special_methods and gated externally.
INTEGRAL, IDENTITY, CAPABILITY = "integral", "identity", "capability"


def integral_solved(state):
    return isinstance(state, sp.Basic) and not state.has(sp.Integral)


def identity_solved(state):
    return isinstance(state, sp.Basic) and is_zero(state)


GOAL = {INTEGRAL: integral_solved, IDENTITY: identity_solved}


# ---- integration strategies (real, SymPy-backed) -------------------------------------------
def _integrals(state):
    return list(state.atoms(sp.Integral)) if isinstance(state, sp.Basic) else []


def _csquare_domain(g, x):
    """True if g has a factor (quadratic-with-linear-term)^(non-integer) — the complete_square_sub
    domain on which the default sp.integrate GRINDS (~38s before failing). Let the rewrite handle it."""
    for pw in g.atoms(sp.Pow):
        base, exp = pw.as_base_exp()
        if exp.is_number and not exp.is_integer and base.is_polynomial(x):
            poly = sp.Poly(base, x)
            if poly.degree() == 2 and poly.all_coeffs()[1] != 0:
                return True
    return False


def _direct(state):
    for I in _integrals(state):
        lim = I.limits[0]
        if len(lim) == 3 and _csquare_domain(I.function, lim[0]):
            continue                      # definite + complete-square-able -> defer to the rewrite
        try:
            r = sp.integrate(I.function, *I.limits)
        except Exception:
            continue
        if not r.has(sp.Integral):
            return [state.xreplace({I: r})]
    return []


def _meijerg(state):
    for I in _integrals(state):
        try:
            r = sp.integrate(I.function, *I.limits, meijerg=True)
        except Exception:
            continue
        if isinstance(r, sp.Basic) and not r.has(sp.Integral):
            return [state.xreplace({I: r})]
    return []


def _easy_dv(dv, x):
    """A clean IBP partner: every factor is a constant, x**n, or exp/sin/cos/sinh/cosh of a
    LINEAR argument. Stops by_parts misfiring (expensively, via sp.integrate + sp.limit) on
    radical/rational powers of a quadratic — complete_square_sub / direct handle those."""
    for f in sp.Mul.make_args(dv):
        if f.is_number:
            continue
        if f.func in (sp.exp, sp.sin, sp.cos, sp.sinh, sp.cosh):
            a = f.args[0]
            if a.is_polynomial(x) and sp.Poly(a, x).degree() <= 1:
                continue
            return False
        b, _e = f.as_base_exp()
        if b == x:                                       # x**n
            continue
        return False
    return True


def _by_parts(state):
    for I in _integrals(state):
        g, x = I.function, I.variables[0]
        facs = sp.Mul.make_args(g)
        for u in facs:                                   # LIATE-ish: u = a poly/log factor
            if (u.is_polynomial(x) or u.func == sp.log) and u != 1 and len(facs) > 1:
                dv = sp.Mul(*[f for f in facs if f is not u])
                if not _easy_dv(dv, x):                  # skip expensive non-IBP partners
                    continue
                v = sp.integrate(dv, x)
                if v.has(sp.Integral):
                    continue
                resid = sp.Integral(v * sp.diff(u, x), *I.limits)
                lim = I.limits[0]
                if len(lim) == 3:                        # DEFINITE: boundary term [u*v]_a^b
                    _, a, b = lim                        # (was a real bug: u*v left un-evaluated)
                    uv = u * v
                    end = lambda pt: (sp.limit(uv, x, pt) if pt in (sp.oo, -sp.oo) else uv.subs(x, pt))
                    bt = end(b) - end(a)
                    if bt.has(sp.zoo, sp.nan) or bt in (sp.oo, -sp.oo):
                        continue                         # IBP boundary divergent -> not this route
                    return [state.xreplace({I: bt - resid})]
                return [state.xreplace({I: u * v - resid})]
    return []


def _partial_fractions(state):
    for I in _integrals(state):
        g, x = I.function, I.variables[0]
        if g.is_rational_function(x):
            ap = sp.apart(g, x)
            if ap != g:
                return [state.xreplace({I: sp.Integral(ap, *I.limits)})]
    return []


# ---- identity strategies (the is_zero routes, as explicit search edges) ---------------------
def _simplify(e):
    return [sp.simplify(sp.expand(e))] if isinstance(e, sp.Basic) else []


def _trig_radical(e):
    return [sp.simplify(sp.trigsimp(sp.radsimp(e)))] if isinstance(e, sp.Basic) else []


def _together_numer(e):
    return [sp.expand(sp.fraction(sp.together(e))[0])] if isinstance(e, sp.Basic) else []


def _decompose_derivs(e):
    if isinstance(e, sp.Basic) and (e.atoms(sp.Derivative) or e.atoms(sp.core.function.AppliedUndef)):
        e2 = e.xreplace({d: sp.Dummy() for d in e.atoms(sp.Derivative)})
        return [e2.xreplace({fn: sp.Dummy() for fn in e2.atoms(sp.core.function.AppliedUndef)})]
    return []


# ---- live strategy objects ----------------------------------------------------------------
_S = Strategy
# generic tactics: live search edges that are NOT named METHODS keys
DIRECT         = _S("direct(CAS)", _direct)          # CAS catch-all integrator
R_SIMPLIFY     = _S("simplify", _simplify)
R_TRIG_RADICAL = _S("trig+radical", _trig_radical)
R_TOGETHER     = _S("together->numer", _together_numer)
R_DECOMPOSE    = _S("decompose-derivs", _decompose_derivs)
# named-method transforms (one per executable METHODS key)
M_PARTS    = _S("parts", _by_parts)
M_PARTFRAC = _S("partial_fractions", _partial_fractions)
M_MEIJERG  = _S("meijer_g", _meijerg)
M_HYPREWRITE = _S("hyperbolic_exp_rewrite", hyperbolic_exp_rewrite)   # closes sech^2/csch^2 gaps
M_INVPARTS   = _S("inverse_function_parts", inverse_function_parts)   # closes inverse-hyperbolic gaps
M_CSQUARE    = _S("complete_square_sub", complete_square_sub)         # P(x)/(irreducible quad)^(p/2) over a range

# ---- KIND -> the live solver strategy list (what search() actually runs) -------------------
def integration_strategies():
    return [DIRECT, M_PARTS, M_PARTFRAC, M_MEIJERG, M_HYPREWRITE, M_INVPARTS, M_CSQUARE]


def identity_strategies():
    return [R_SIMPLIFY, R_TRIG_RADICAL, R_TOGETHER, R_DECOMPOSE, sm.SYM_ANTISYM]


KIND_SOLVERS = {INTEGRAL: integration_strategies, IDENTITY: identity_strategies}
GENERIC_STRATEGIES = [DIRECT, R_SIMPLIFY, R_TRIG_RADICAL, R_TOGETHER, R_DECOMPOSE]  # non-METHODS live edges

# direct-capability methods: realized by a function in special_methods (not a search edge),
# each gated by external_gates.CAPABILITY_GATES (rule 10). The wiring proof checks the function
# is registered here; the gate test checks it reproduces the published answer.
CAPABILITIES = {
    "contour": sm.contour_real_line,
    "feynman_parameter": sm.feynman_frullani,
    "mellin": sm.mellin_transform_of,
    "zeta_reg": sm.zeta_regularize,
    "analytic_continuation": sm.residue_of_gamma,
    "asymptotic_expansion": sm.erfc_asymptotic,
    "gamma_ratio_asymptotic": sm.gamma_ratio_asymptotic,
    "oscillator_commutator": sm.oscillator_commutator,
    "dilogarithm": sm.dilogarithm_reflection,
    "wigner_surmise": sm.wigner_surmise,
    "q_pochhammer": sm.q_pochhammer_log,
    "bessel_hankel": sm.bessel_hankel,
    "airy": sm.airy_asymptotic,
    "euler_maclaurin": sm.euler_maclaurin_harmonic,
    "casimir": sm.su2_casimir,
    "conformal_casimir": sm.conformal_casimir,
    "confluent_0F1": sm.confluent_0F1_bessel,
    "sturm_liouville": sm.sturm_liouville_box,
    "stationary_phase": sm.stationary_phase_J0,
    "conformal_block": sm.conformal_block_casimir,
    "jacobi_trudi": sm.jacobi_trudi_schur,
    "komar_mass": sm.komar_mass_schwarzschild,
}

# ---- COVERAGE: one row per METHODS key — (kind, status, Strategy|None) ----------------------
# status "executable" = a DEDICATED named transform is wired AND reachable by its kind's solver.
# The wiring proof (coverage.assert_complete) asserts the strategy is `in` KIND_SOLVERS[kind], so a
# "dead row" (marked executable but run by nothing) is impossible. The CAS catch-all DIRECT may
# ALSO solve a recognition-only method's instances — that is capability, not method attribution.
COVERAGE = {
    "parts":              (INTEGRAL, "executable", M_PARTS),
    "partial_fractions":  (INTEGRAL, "executable", M_PARTFRAC),
    "meijer_g":           (INTEGRAL, "executable", M_MEIJERG),
    "hyperbolic_exp_rewrite": (INTEGRAL, "executable", M_HYPREWRITE),
    "inverse_function_parts": (INTEGRAL, "executable", M_INVPARTS),
    "complete_square_sub":    (INTEGRAL, "executable", M_CSQUARE),
    # direct-capability methods (executable via special_methods, gated externally):
    "contour":              (CAPABILITY, "executable", None),
    "feynman_parameter":    (CAPABILITY, "executable", None),
    "mellin":               (CAPABILITY, "executable", None),
    "stationary_phase":     (CAPABILITY, "executable", None),
    "conformal_block":      (CAPABILITY, "executable", None),
    "jacobi_trudi":         (CAPABILITY, "executable", None),
    "komar_mass":           (CAPABILITY, "executable", None),
    "asymptotic_expansion": (CAPABILITY, "executable", None),
    "gamma_ratio_asymptotic": (CAPABILITY, "executable", None),
    "oscillator_commutator": (CAPABILITY, "executable", None),
    "dilogarithm":          (CAPABILITY, "executable", None),
    "wigner_surmise":       (CAPABILITY, "executable", None),
    "q_pochhammer":         (CAPABILITY, "executable", None),
    "bessel_hankel":        (CAPABILITY, "executable", None),
    "airy":                 (CAPABILITY, "executable", None),
    "casimir":              (CAPABILITY, "executable", None),
    "conformal_casimir":    (CAPABILITY, "executable", None),
    "confluent_0F1":        (CAPABILITY, "executable", None),
    "sturm_liouville":      (CAPABILITY, "executable", None),
    "zeta_reg":             (CAPABILITY, "executable", None),
    "analytic_continuation": (CAPABILITY, "executable", None),
    # identity-search method:
    "sym_antisym":          (IDENTITY, "executable", sm.SYM_ANTISYM),
    # rejected as covering by the anti-covering critic -> honestly recognition-only:
    "u_sub":                (INTEGRAL, "recognition-only", None),
    "abel_plana":           (INTEGRAL, "recognition-only", None),
    "euler_maclaurin":      (CAPABILITY, "executable", None),   # promoted: genuine non-covering executable
    "dim_reg":              (INTEGRAL, "recognition-only", None),
}

# ---- representatives for the registry-driven FIRE check (every live strategy must fire) -----
def _reps():
    x = sp.Symbol("x", positive=True); s = sp.Symbol("s"); a = sp.Symbol("a")
    return {
        "direct(CAS)":       sp.Integral(sp.exp(x), x),
        "parts":             sp.Integral(x * sp.exp(x), x),
        "partial_fractions": sp.Integral(1 / (x ** 2 - 1), x),
        "meijer_g":          sp.Integral(sp.exp(-x ** 2), (x, 0, sp.oo)),
        "simplify":          sp.cos(x) ** 2 + sp.sin(x) ** 2 - 1,
        "trig+radical":      sp.cos(x) ** 2 + sp.sin(x) ** 2 - 1,
        "together->numer":   1 / (x - 1) + 1 / (x + 1),
        "decompose-derivs":  sp.Derivative(sp.Function("f")(s), s) * a,
        "sym_antisym(contract)": (sm._symmetric(2), sm._antisymmetric(2)),
        "hyperbolic_exp_rewrite": sp.Integral(sp.sech(x) ** 2, x),
        "inverse_function_parts": sp.Integral(sp.acosh(2 * x), x),
        "complete_square_sub": sp.Integral((1 + x) / (1 + x + x ** 2) ** sp.Rational(5, 2), (x, 0, sp.oo)),
    }


REPS = _reps()

# ---- real executable CAPABILITIES that are DIRECT computations, not search strategies -------
# Declared (not silently omitted) so "every executable capability is accounted for" is honest.
DIRECT_CAPABILITIES = {
    "curvature.Curvature": "metric -> Christoffel/Riemann/Ricci/Einstein/geodesics (direct compute; tested)",
    "curvature.is_zero/equal": "robust identity test - the engine behind the IDENTITY goal",
    "executor.reduce_integral": "CAS definite integration w/ Meijer-G (wrapped by direct/meijer_g)",
    "executor.verify_closed_form": "numeric verification of a recognised closed form",
}


def solve_integral(integrand, a=None, b=None, *, var="x", budget=200):
    """Evaluate an integral by SEARCH over the integration strategies."""
    x = sp.Symbol(var, positive=True)
    if isinstance(integrand, sp.Integral):
        start = integrand
    else:
        g = sp.sympify(integrand, locals={var: x})
        start = sp.Integral(g, x) if a is None else sp.Integral(g, (x, sp.sympify(a), sp.sympify(b)))
    return search(start, integration_strategies(), GOAL[INTEGRAL], budget=budget)


def prove_identity(expr, *, budget=80):
    """Prove expr == 0 by SEARCH over the identity routes (the generalised is_zero)."""
    return search(sp.sympify(expr), identity_strategies(), GOAL[IDENTITY], budget=budget)
