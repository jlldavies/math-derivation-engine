"""External gates (CLAUDE.md rule 10): every executable method must reproduce an INDEPENDENT,
published worked example — we check SOMEONE ELSE'S homework, not our own. `published`/`expected`
is verbatim from the cited source; the test validates the source and asserts the ENGINE
reproduces it. `CAPTURED_GATES` hold examples for the still-recognition-only methods.

Found by the external-gates campaign; the capability realizations by the recognition-only
campaign (both 2026-06-24), all re-verified by hand.
"""
import sympy as sp

from . import special_methods as sm

# ---- integral-search-method gates (engine's solve_integral must reproduce `published`) -----
EXTERNAL_GATES = [
    dict(method="parts", integrand="x*exp(6*x)", a=None, b=None,
         published="x*exp(6*x)/6 - exp(6*x)/36",
         source="https://tutorial.math.lamar.edu/classes/calcII/IntegrationByParts.aspx"),
    dict(method="partial_fractions", integrand="(3*x+11)/(x**2-x-6)", a=None, b=None,
         published="4*log(x-3) - log(x+2)",
         source="https://tutorial.math.lamar.edu/classes/calcII/PartialFractions.aspx"),
    dict(method="meijer_g", integrand="exp(-x**2)*cos(2*x)", a="-oo", b="oo",
         published="sqrt(pi)*exp(-1)",
         source="https://en.wikipedia.org/wiki/Gaussian_integral"),
    dict(method="meijer_g", integrand="1/x**2", a=1, b="oo", published="1",
         source="https://tutorial.math.lamar.edu/classes/calcII/ImproperIntegrals.aspx"),
    dict(method="hyperbolic_exp_rewrite", integrand="sech(x)**2", a=None, b=None, published="tanh(x)",
         source="https://en.wikipedia.org/wiki/List_of_integrals_of_hyperbolic_functions"),
    dict(method="inverse_function_parts", integrand="acosh(2*x)", a=None, b=None,
         published="x*acosh(2*x) - sqrt(4*x**2-1)/2",
         source="https://en.wikipedia.org/wiki/List_of_integrals_of_inverse_hyperbolic_functions"),
    dict(method="complete_square_sub", integrand="(1+x)/(1+x+x**2)**(Rational(5,2))", a=0, b="oo",
         published="Rational(14,27)",   # ~2s now (staged escalation); exact, numerically checked
         source="arXiv:2606.23785 (Controlled Chaos in 4D SCFTs), r-statistics normalization eq.(346) β=1"),
]

# ---- direct-capability / identity-method gates (run the real computation, check published) --
_x = sp.Symbol("x", positive=True)
_z = sp.Symbol("z", positive=True)
_s = sp.Symbol("s")
_a = sp.Symbol("a", positive=True)
_b = sp.Symbol("b", positive=True)
_w = sp.Symbol("w", positive=True)   # dilogarithm argument (0<w<1 for the reflection range)
_ss = sp.Symbol("s", positive=True)  # Wigner-surmise level spacing (matches wigner_surmise's internal s)
_jspin = sp.Symbol("j", positive=True)   # su(2) spin label (Casimir gate)
_nu = sp.Symbol("nu", positive=True)     # Bessel order (0F1 gate)
_nbox = sp.Symbol("n", positive=True, integer=True)   # Sturm-Liouville mode number
_Lbox = sp.Symbol("L", positive=True)                 # box length (match sturm_liouville_box internals)
_aq = sp.Symbol("a")                                  # q-Pochhammer argument
_qq = sp.Symbol("q", positive=True)                   # q-Pochhammer base (|q|<1)
_pb = sp.Symbol("p", positive=True)                   # Bessel/Hankel Gaussian width
_ab = sp.Symbol("a", positive=True)                   # Bessel/Hankel transform variable
_nh = sp.Symbol("n", positive=True)                   # Euler-Maclaurin harmonic-number index
_Delta = sp.Symbol("Delta", positive=True)            # conformal weight (conformal Casimir)
_hblk = sp.Symbol("h")
_xv1, _xv2, _xv3 = sp.symbols("x1 x2 x3")
_Mkomar = sp.Symbol("M", positive=True)

# su(1,1) bosonic-oscillator realization (for the oscillator_commutator gate)
from sympy.physics.quantum.boson import BosonOp                                  # noqa: E402
from sympy.physics.quantum import Dagger                                         # noqa: E402
from sympy.physics.quantum.operatorordering import normal_ordered_form as _no    # noqa: E402
_osc = BosonOp("a"); _oscd = Dagger(_osc)
_K0 = (_oscd * _osc + sp.Rational(1, 2)) / 2
_Kp = _oscd * _oscd / 2
_Km = _osc * _osc / 2
CAPABILITY_GATES = [
    dict(method="contour", run=lambda: sm.contour_real_line(1 / (_x ** 2 + 1), _x),
         expected=lambda: sp.pi,
         source="https://phys.libretexts.org/Bookshelves/Mathematical_Physics_and_Pedagogy/Complex_Methods_for_the_Sciences_(Chong)/09:_Contour_Integration"),
    dict(method="feynman_parameter", run=lambda: sm.feynman_frullani(), expected=lambda: sp.log(_a),
         source="https://en.wikipedia.org/wiki/Leibniz_integral_rule#Examples"),
    dict(method="mellin", run=lambda: sm.mellin_transform_of(sp.exp(-_x))[0], expected=lambda: sp.gamma(_s),
         source="https://en.wikipedia.org/wiki/Mellin_transform"),
    dict(method="zeta_reg", run=lambda: sm.zeta_regularize(1), expected=lambda: sp.Rational(-1, 12),
         source="https://en.wikipedia.org/wiki/Zeta_function_regularization"),
    dict(method="analytic_continuation", run=lambda: sm.residue_of_gamma(3), expected=lambda: sp.Rational(-1, 6),
         source="https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/af8c9c78c3915aaf3fd1695f8d32a3b3_MIT18_04S18_topic13.pdf"),
    dict(method="asymptotic_expansion", run=lambda: sm.erfc_asymptotic(4)[1],
         expected=lambda: 1 - sp.Rational(1, 2) / _z ** 2 + sp.Rational(3, 4) / _z ** 4 - sp.Rational(15, 8) / _z ** 6,
         source="https://dlmf.nist.gov/7.12"),
    dict(method="gamma_ratio_asymptotic",
         run=lambda: sm.gamma_ratio_asymptotic([_z + _a], [_z + _b], _z, 1),
         expected=lambda: _z ** (_a - _b) * (1 + (_a - _b) * (_a + _b - 1) / (2 * _z)),
         source="https://dlmf.nist.gov/5.11.E13"),
    dict(method="oscillator_commutator",
         run=lambda: sm.oscillator_commutator(_Kp, _Km),     # su(1,1): [K+,K-]
         expected=lambda: _no((-2 * _K0)),                   # = -2 K0  (standard bosonic realization)
         source="https://en.wikipedia.org/wiki/Ladder_operator#su(1,1)  (K+=a^2/2, K-=a^2/2, K0=(N+1/2)/2)"),
    dict(method="dilogarithm",
         run=lambda: sm.dilogarithm_reflection(_w),          # Li2(w)+Li2(1-w)
         expected=lambda: sp.pi ** 2 / 6 - sp.log(_w) * sp.log(1 - _w),
         source="https://dlmf.nist.gov/25.12.E4  (Euler reflection for the dilogarithm)"),
    dict(method="wigner_surmise",
         run=lambda: sm.wigner_surmise(1),                   # GOE level spacing
         expected=lambda: (sp.pi / 2) * _ss * sp.exp(-(sp.pi / 4) * _ss ** 2),
         source="https://en.wikipedia.org/wiki/Random_matrix#Spacing_distributions (GOE Wigner surmise)"),
    dict(method="q_pochhammer",
         run=lambda: sm.q_pochhammer_log(_aq, _qq, 4),       # log (a;q)_inf
         expected=lambda: -sum(_aq ** n / (n * (1 - _qq ** n)) for n in range(1, 5)),
         source="https://dlmf.nist.gov/17.2 (Euler; log of the q-Pochhammer as a Lambert series)"),
    dict(method="bessel_hankel",
         run=lambda: sm.bessel_hankel(_pb, _ab, "gaussian"),  # Hankel transform of a Gaussian
         expected=lambda: sp.exp(-_ab ** 2 / (4 * _pb)) / (2 * _pb),
         source="https://dlmf.nist.gov/10.22 (Gradshteyn-Ryzhik 6.631; Hankel transform of a Gaussian)"),
    dict(method="airy",
         run=lambda: sm.airy_asymptotic(),                    # WKB asymptotic of Ai(x)
         expected=lambda: sp.exp(-sp.Rational(2, 3) * _x ** sp.Rational(3, 2)) / (2 * sp.sqrt(sp.pi) * _x ** sp.Rational(1, 4)),
         source="https://dlmf.nist.gov/9.7 (DLMF 9.7.5; Ai(x) ~ e^{-2/3 x^{3/2}}/(2 sqrt(pi) x^{1/4}))"),
    dict(method="euler_maclaurin",
         run=lambda: sm.euler_maclaurin_harmonic(2),          # H_n asymptotic via Euler-Maclaurin
         expected=lambda: (sp.log(_nh) + sp.EulerGamma + sp.Rational(1, 2) / _nh
                           - sp.Rational(1, 12) / _nh ** 2 + sp.Rational(1, 120) / _nh ** 4),
         source="https://dlmf.nist.gov/2.10 (Euler-Maclaurin; harmonic-number asymptotic)"),
    dict(method="casimir",
         run=lambda: sm.su2_casimir(_jspin),                 # su(2) quadratic Casimir
         expected=lambda: _jspin * (_jspin + 1),             # = j(j+1)
         source="https://en.wikipedia.org/wiki/Angular_momentum_operator#Casimir_operator (J^2=j(j+1))"),
    dict(method="conformal_casimir",
         run=lambda: sm.conformal_casimir(3),                # SO(4,1) on a scalar primary, d=3
         expected=lambda: _Delta * (_Delta - 3),            # = Delta(Delta-d), d=3
         source="https://arxiv.org/abs/1602.07982 (Simmons-Duffin TASI; conformal Casimir Delta(Delta-d))"),
dict(method="conformal_block",
         run=lambda: sm.conformal_block_casimir()[0],       # SL(2) Casimir eigenvalue of k_h = z^h 2F1(h,h;2h;z)
         expected=lambda: _hblk * (_hblk - 1),              # = h(h-1)
         source="https://arxiv.org/abs/hep-th/0011040 (Dolan-Osborn) / https://arxiv.org/abs/1602.07982 (Simmons-Duffin TASI; D_z k_h = h(h-1) k_h)"),
dict(method="jacobi_trudi",
         run=lambda: sm.jacobi_trudi_schur([2, 1], [_xv1, _xv2, _xv3]),   # s_(2,1)(x1,x2,x3)
         expected=lambda: (_xv1**2*_xv2 + _xv1**2*_xv3 + _xv1*_xv2**2 + _xv2**2*_xv3
                           + _xv1*_xv3**2 + _xv2*_xv3**2 + 2*_xv1*_xv2*_xv3),
         source="https://en.wikipedia.org/wiki/Schur_polynomial  (Jacobi-Trudi; s_(2,1)(x1,x2,x3))"),
dict(method="komar_mass",
         run=lambda: sm.komar_mass_schwarzschild(),          # Schwarzschild Komar mass from xi=d/dt
         expected=lambda: _Mkomar,                           # = M, the Schwarzschild mass parameter
         source="https://arxiv.org/abs/gr-qc/9707012 (Townsend, Black Holes; Komar mass of Schwarzschild = M; Wald GR ch.11, Poisson Toolkit 4.3.3)"),
    dict(method="confluent_0F1",
         run=lambda: sm.confluent_0F1_bessel(_nu, _z),       # 0F1(;nu+1;-z^2/4) -> Bessel
         expected=lambda: sp.besselj(_nu, _z),               # = J_nu(z)
         source="https://dlmf.nist.gov/10.16.E9 (J_nu as a 0F1)"),
    dict(method="sturm_liouville",
         run=lambda: sm.sturm_liouville_box()[0],            # eigenvalue lambda_n
         expected=lambda: (_nbox * sp.pi / _Lbox) ** 2,      # = (n pi / L)^2
         source="https://en.wikipedia.org/wiki/Sturm-Liouville_theory (particle-in-a-box spectrum)"),
    dict(method="stationary_phase", run=lambda: sm.stationary_phase_J0(),
         expected=lambda: sp.sqrt(2 / (sp.pi * _x)) * sp.cos(_x - sp.pi / 4),
         source="https://www.phys.uconn.edu/~rozman/Courses/P2400_16S/downloads/stationary-phase.pdf"),
    dict(method="sym_antisym", run=lambda: sm.prove_sym_antisym(3)["best"][1], expected=lambda: sp.Integer(0),
         source="https://www.damtp.cam.ac.uk/user/reh10/lectures/nst-mmii-chapter3.pdf"),
]

# ---- still recognition-only (the 4 rejected as covering): gates captured for the future -----
CAPTURED_GATES = [
    dict(method="u_sub", problem="∫ 2x·cos(x^2) dx", published="sin(x^2) + C",
         source="https://www.sfu.ca/math-coursenotes/Math%20158%20Course%20Notes/sec_SubRule.html"),
    dict(method="abel_plana", problem="Abel–Plana on (z+a)^{-s} -> Hurwitz zeta integral rep",
         published="zeta(s,a) = a^{1-s}/(s-1)+1/(2a^s)+2∫_0^∞ sin(s·atan(t/a))/(a^2+t^2)^{s/2}·dt/(e^{2πt}-1)",
         source="https://en.wikipedia.org/wiki/Abel%E2%80%93Plana_formula"),
    dict(method="dim_reg", problem="One-loop ∫ d^d p/(2π)^d 1/(p^2+m^2)^2 in d=4-ε",
         published="1/(8π^2 ε) - 1/(16π^2)(ln(m^2/4π)+gamma) + O(ε)",
         source="https://en.wikipedia.org/wiki/Dimensional_regularization"),
]


def gated_methods():
    """Methods that have at least one live external gate (integral-search or capability)."""
    return {g["method"] for g in EXTERNAL_GATES} | {g["method"] for g in CAPABILITY_GATES}
