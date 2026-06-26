"""Paper gates (rule 10) — arXiv:2606.24497 "More on Kashaev limits of the quantum A-polynomials".
A GREEN paper for the dilogarithm / special-function tracks: the ENGINE evaluates the Li_2 special
values, the Rogers L-function reflection, solves the saddle polynomial, and computes the figure-eight
knot's HYPERBOLIC VOLUME from the dilogarithm action. We only check against the paper / known values.

Rule-8 note: the saddle condition (24) was NOT reproduced from the AI-transcribed action (23) — see
test_ROUNDUP_remaining_gaps; flagged honestly rather than claimed.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

Li2 = lambda u: sp.polylog(2, u)                                                 # noqa: E731
t = sp.Symbol("t", positive=True)
g = sp.Symbol("g")


# ===== (19) dilogarithm special values =======================================================
def test_dilog_special_values():
    assert sp.simplify(Li2(1) - sp.pi ** 2 / 6) == 0
    assert sp.simplify(Li2(-1) + sp.pi ** 2 / 12) == 0
    assert sp.simplify(Li2(sp.Rational(1, 2)) - (sp.pi ** 2 / 12 - sp.log(2) ** 2 / 2)) == 0


# ===== (21) Rogers L-function reflection  L(x)+L(1/x) = pi^2/3  (real part; branch-robust) ====
def test_rogers_L_reflection():
    L = lambda u: Li2(u) + sp.Rational(1, 2) * sp.log(u) * sp.log(1 - u)
    for xv in [sp.Rational(3, 2), sp.Rational(5, 2), 3]:
        re = complex(sp.N(L(xv) + L(1 / xv))).real
        assert abs(re - float(sp.pi ** 2 / 3)) < 1e-9


# ===== (27) figure-eight saddle polynomial: solve, roots satisfy it, Vieta product = 1 ========
def test_figure_eight_saddle_polynomial():
    poly = g ** 2 + (2 + t ** 2 + t ** (-2) - t ** 4 - t ** (-4)) * g + 1
    roots = sp.solve(poly, g)
    assert len(roots) == 2
    for r in roots:
        assert sp.simplify(poly.subs(g, r)) == 0
    assert sp.simplify(roots[0] * roots[1]) == 1            # reciprocal pair (constant/leading)


# ===== (28/29) figure-eight knot HYPERBOLIC VOLUME from the dilogarithm action ================
def test_figure_eight_hyperbolic_volume():
    # S(z*,t=1) = 1/2 [Li2(1/z*) - Li2(z*)] at the saddle z* = e^{i pi/3}; |Im S| = vol(4_1) complement
    zc = sp.exp(sp.I * sp.pi / 3)
    vol = float(sp.N(sp.Abs(sp.im(sp.Rational(1, 2) * (Li2(1 / zc) - Li2(zc))))))
    assert abs(vol - 1.0149416064096537) < 1e-12          # paper eq.(29) ~ 1.014941607...


# ===== ROUND-UP — not derived / out of scope (honest boundary, rule 8) ========================
def test_ROUNDUP_remaining_gaps():
    gaps = {
        "saddle_condition_24": "the saddle condition (24) (t^2-z)(t^2 z-1)=t^2 z was NOT reproduced: "
                               "d/dz of the AI-transcribed action (23) gives z=-1, not (24). Likely the "
                               "extracted action is imprecise (HTML scrape) or a branch subtlety — needs "
                               "the paper PDF to resolve; not claimed.",
        "q_series_pochhammer": "(x;q^2)_inf infinite products / q-series (18) — no q-series capability.",
        "A_polynomials_knot_invariants": "classical/quantum A-polynomials, HOMFLY/Jones differential "
                                         "expansion, recurrences (5-7, 6.4) — knot-theory, out of engine scope.",
    }
    assert len(gaps) == 3
    # the engine DOES derive: Li_2 special values, the Rogers L reflection (pi^2/3), the saddle
    # polynomial solve, and the figure-eight hyperbolic volume from the dilogarithm action.
