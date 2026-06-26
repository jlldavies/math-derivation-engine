"""Paper gates (rule 10): reproduce published maths from the physics-paper corpus
(tests/papers/). The ENGINE does the maths; we only verify against the paper / numeric ground
truth. Plus a regression test for the definite-integration-by-parts boundary-term bug these
papers surfaced.

arXiv:2606.23785 — "Controlled Chaos in 4D SCFTs" (RMT level statistics).
"""
import os
import sys

import pytest
import sympy as sp
import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.strategies import solve_integral                       # noqa: E402
from integral_explainer import strategies as S                                # noqa: E402


# ---- Wigner surmise eq.(338)-(343): the constants are fixed by ∫ρ=1 and ∫sρ=1 (unit mean) ---
WIGNER = {
    1: "(pi/2)*x*exp(-(pi/4)*x**2)",
    2: "(32/pi**2)*x**2*exp(-(4/pi)*x**2)",
    4: "(2**18/(3**6*pi**3))*x**4*exp(-(64/(9*pi))*x**2)",
}


@pytest.mark.parametrize("beta", [1, 2, 4])
def test_wigner_surmise_normalized_and_unit_mean(beta):
    rho = WIGNER[beta]
    assert sp.simplify(solve_integral(rho, 0, "oo")["best"][1]) == 1            # normalized
    assert sp.simplify(solve_integral(f"x*({rho})", 0, "oo")["best"][1]) == 1   # unit mean spacing


# ---- GE r-statistics eq.(346) normalization: N_β = ∫_0^∞ (1+x)^β/(1+x+x^2)^(1+3β/2) dx -------
@pytest.mark.parametrize("beta", [1, 2, 4])      # β=1 now closed by complete_square_sub
def test_r_statistics_normalization_matches_numeric(beta):
    e = (3 * beta + 2)
    res = solve_integral(f"(1+x)**{beta}/(1+x+x**2)**(Rational({e},2))", 0, "oo")["best"]
    assert res is not None, f"β={beta} unexpectedly unevaluated"
    num = mp.quad(lambda t: (1 + t) ** beta / (1 + t + t ** 2) ** (e / 2.0), [0, mp.inf])
    assert abs(complex(sp.N(res[1], 25)) - complex(num)) < 1e-15


def test_r_statistics_beta1_now_exact():
    # the gap complete_square_sub was built to close; exact value 14/27
    assert sp.simplify(solve_integral("(1+x)/(1+x+x**2)**(Rational(5,2))", 0, "oo")["best"][1]
                       - sp.Rational(14, 27)) == 0


# ---- regression: _by_parts on a DEFINITE integral must use the boundary term [u*v]_a^b -------
# (surfaced by the r-statistics integral: the un-evaluated u*v gave a wrong -oo result)
def test_by_parts_definite_uses_boundary_term():
    x = sp.Symbol("x", positive=True)
    st = S._by_parts(sp.Integral(x * sp.exp(x), (x, 0, 1)))[0]
    assert sp.simplify(st.doit() - 1) == 0, "definite IBP must give [u*v]_a^b - ∫v du = 1"
    # and a definite integral that routes through parts must give the correct finite value
    assert sp.simplify(solve_integral("x*exp(x)", 0, 1)["best"][1] - 1) == 0
