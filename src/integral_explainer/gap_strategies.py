"""Gap-closing integration strategies (search edges) — built + critic-vetted by the gap-closing
ultracode campaign (2026-06-24) and re-verified by hand. Each GENUINELY transforms the integrand
(rewrite identity / real IBP) into a state the CAS can finish — never hardcodes the answer
(CLAUDE.md rule 10). They close the 8 Wikipedia integral-table gaps SymPy returns unevaluated.
"""
import sympy as sp

_HYP = (sp.sinh, sp.cosh, sp.tanh, sp.coth, sp.sech, sp.csch)
INV = (sp.acosh, sp.asinh, sp.asech, sp.acsch, sp.atanh, sp.acoth)


# ---- A: rewrite hyperbolic -> exponential, then let direct(CAS) finish ----------------------
def hyperbolic_exp_rewrite(state):
    """Search edge: for each unevaluated Integral whose integrand contains hyperbolic functions,
    rewrite the integrand to exponential form (the exact identity sech(x)=2/(e^x+e^-x), ...),
    yielding a rational function of e^x that direct(CAS) CAN integrate. Returns the rewritten
    Integral state, or [] if nothing changed. It does NOT integrate — it hands a rational-in-e^x
    integrand to the CAS catch-all."""
    if not isinstance(state, sp.Basic):
        return []
    out = []
    for I in list(state.atoms(sp.Integral)):
        g = I.function
        if not any(g.has(h) for h in _HYP):
            continue
        gr = g.rewrite(sp.exp)
        if gr is None or gr == g or any(gr.has(h) for h in _HYP):
            continue
        out.append(state.xreplace({I: sp.Integral(gr, *I.limits)}))
    return out


# ---- B: integration by parts with an inverse-(hyperbolic) factor as u ----------------------
def _inv_base(f):
    """If f is an inverse-hyperbolic factor (possibly an integer power) of a LINEAR argument,
    return its inner inverse-hyperbolic call; else None."""
    base = f.base if (f.is_Pow and getattr(f.exp, "is_integer", False) and f.exp >= 1) else f
    if not isinstance(base, INV):
        return None
    arg = base.args[0]
    if arg.is_polynomial(*base.free_symbols) and base.free_symbols:
        v = next(iter(base.free_symbols))
        try:
            if sp.degree(sp.Poly(arg, v)) <= 1:
                return base
        except sp.PolynomialError:
            return None
    return None


def _combine_radicals(expr):
    """Merge split radicals into ONE sqrt of a polynomial radicand (sqrt(2x-1)*sqrt(2x+1) ->
    sqrt(4x^2-1)) so direct(CAS) returns the clean elementary antiderivative rather than a
    meijerg. Value-preserving; falls back to the input on any failure."""
    try:
        e = sp.powsimp(sp.expand(expr), force=True)
        num, den = sp.fraction(sp.together(e))

        def merge(prod):
            rad = sp.Integer(1)
            other = []
            for f in sp.Mul.make_args(prod):
                b, ex = f.as_base_exp()
                if getattr(ex, "is_Rational", False) and ex.q == 2:
                    rad *= b ** ex.p
                else:
                    other.append(f)
            rad = sp.radsimp(sp.together(rad))
            return sp.Mul(*other) * sp.sqrt(sp.expand(rad))

        return sp.radsimp(merge(num) / merge(den))
    except Exception:
        return expr


def complete_square_sub(state):
    """Search edge: a DEFINITE integral carrying a factor Q(x)^p where Q is a quadratic WITH a
    linear term and p is non-integer (e.g. (1+x+x^2)^(5/2)) — complete the square via the
    substitution u = x + b/(2a), removing the linear term to give (u^2 + c)^p, which the CAS
    integrates. The limits shift by b/(2a). Genuine algebraic substitution; nothing hardcoded.

    Definite-only: shifting the limits keeps the value exact with no back-substitution (an
    indefinite result would be left in the shifted variable). Fires once — the rewritten quadratic
    has no linear term, so it will not re-trigger."""
    out = []
    ints = list(state.atoms(sp.Integral)) if isinstance(state, sp.Basic) else []
    for I in ints:
        lim = I.limits[0]
        if len(lim) != 3:                              # definite integrals only
            continue
        g, x = I.function, lim[0]
        shift = None
        for pw in g.atoms(sp.Pow):
            base, exp = pw.as_base_exp()
            if exp.is_number and not exp.is_integer and base.is_polynomial(x):
                poly = sp.Poly(base, x)
                if poly.degree() == 2:
                    a, b, _c = poly.all_coeffs()
                    if b != 0:
                        shift = sp.together(b / (2 * a))
                        break
        if shift is None:
            continue
        gnew = g.subs(x, x - shift)
        # Expand the (now linear-term-free) quadratic inside any non-integer power, so the CAS /
        # Meijer-G see the clean (x^2 + k)^p form — the unsimplified base x+(x-1/2)^2+1/2 otherwise
        # defeats Meijer-G (-> dead tier-1) and makes the default grind.
        gnew = gnew.replace(lambda e: e.is_Pow and e.exp.is_number and not e.exp.is_integer,
                            lambda e: sp.expand(e.base) ** e.exp)
        out.append(state.xreplace({I: sp.Integral(gnew, (x, lim[1] + shift, lim[2] + shift))}))
    return out


def inverse_function_parts(state):
    """Search edge: for each Integral whose integrand has an inverse-hyperbolic factor of a
    linear argument, do ONE IBP pass with u = that factor, dv = the rest. Returns the new state
    u*v - Integral(v*du); the remaining Integral is left for direct(CAS) / a further pass (the
    edge recurses on a still-inverse-bearing residual, e.g. acosh^2)."""
    out = []
    ints = list(state.atoms(sp.Integral)) if isinstance(state, sp.Basic) else []
    for I in ints:
        g, x = I.function, I.variables[0]
        u, rest = None, []
        for f in sp.Mul.make_args(g):
            if u is None and _inv_base(f) is not None:
                u = f
            else:
                rest.append(f)
        if u is None:
            continue
        try:
            v = sp.integrate(sp.Mul(*rest), x)
        except Exception:
            continue
        if not isinstance(v, sp.Basic) or v.has(sp.Integral):
            continue
        rem = _combine_radicals(v * sp.diff(u, x))
        out.append(state.xreplace({I: u * v - sp.Integral(rem, x)}))
    return out
