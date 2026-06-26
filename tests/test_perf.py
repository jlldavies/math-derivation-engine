"""Performance regression guards. The solver GUARDS the default `sp.integrate` (DIRECT) against the
complete-square domain it grinds on (~38s), deferring those integrands to the complete_square_sub
rewrite — so a hard integral a rewrite makes tractable must NOT fall through to the default grind.
Generous thresholds — these catch the *pathology* (tens of seconds), not normal machine variance.
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.strategies import solve_integral                       # noqa: E402


def test_complete_square_gate_is_fast():
    # was 38-60s before staged escalation + the simplify fix; now ~2s via complete_square -> meijer_g
    t = time.time()
    r = solve_integral("(1+x)/(1+x+x**2)**(Rational(5,2))", 0, "oo")["best"]
    dt = time.time() - t
    assert r is not None and sp.simplify(r[1] - sp.Rational(14, 27)) == 0, "wrong/no value"
    assert r[2][0] == "complete_square_sub", f"should route via the rewrite, got {r[2]}"
    assert dt < 15, f"DIRECT guard regressed: should solve via the rewrite in ~2s, took {dt:.1f}s"


def test_easy_integrals_stay_fast():
    for ig, a, b in [("x*exp(x)", 0, 1), ("1/(x**2+1)", "-oo", "oo"),
                     ("exp(-x**2)*cos(2*x)", 0, "oo")]:
        t = time.time()
        assert solve_integral(ig, a, b)["best"] is not None
        assert time.time() - t < 10, f"{ig} unexpectedly slow"
