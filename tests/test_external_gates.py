"""External-source gates (CLAUDE.md rule 10): every executable method must reproduce an
INDEPENDENT published worked example. We validate the source for self-consistency and assert the
ENGINE reproduces the published answer — checking someone else's homework, not our own.
"""
import os
import sys

import pytest
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.external_gates import (EXTERNAL_GATES, CAPABILITY_GATES,               # noqa: E402
                                               CAPTURED_GATES, gated_methods)
from integral_explainer.strategies import solve_integral, COVERAGE                            # noqa: E402
from integral_explainer.curvature import equal                                                # noqa: E402


@pytest.mark.parametrize(
    "g",
    [pytest.param(g, marks=pytest.mark.slow) if g.get("slow") else g for g in EXTERNAL_GATES],
    ids=[f"{g['method']}:{g['integrand']}" for g in EXTERNAL_GATES])
def test_engine_reproduces_published_source(g):
    x = sp.Symbol("x", positive=True)
    integrand = sp.sympify(g["integrand"], locals={"x": x})
    published = sp.sympify(g["published"], locals={"x": x})
    eng = solve_integral(g["integrand"], g["a"], g["b"])["best"][1]
    def _zero(e):  # symbolic, then numeric over in-domain points (equivalent forms SymPy won't reduce)
        if sp.simplify(e) == 0:
            return True
        vals = []
        for p in (sp.Rational(3, 5), sp.Rational(7, 10), sp.Rational(11, 10), sp.Rational(3, 2)):
            try:
                v = complex(e.subs(x, p))
            except Exception:
                continue
            if v == v and abs(v) != float("inf"):       # skip nan/inf (out-of-domain)
                vals.append(abs(v))
        return len(vals) >= 2 and max(vals) < 1e-9
    if g["a"] is None:                                  # indefinite
        assert _zero(sp.diff(published, x) - integrand), f"SOURCE inconsistent: {g['source']}"
        assert _zero(sp.diff(eng, x) - integrand), f"engine not a valid antiderivative ({g['source']})"
    else:                                               # definite
        assert (sp.simplify(eng - published) == 0
                or abs(complex(sp.N(eng)) - complex(sp.N(published))) < 1e-9), \
            f"engine {eng} != published {published} ({g['source']})"


@pytest.mark.parametrize("g", CAPABILITY_GATES, ids=[g["method"] for g in CAPABILITY_GATES])
def test_capability_reproduces_published_source(g):
    computed, expected = g["run"](), g["expected"]()
    assert equal(computed, expected), \
        f"{g['method']}: engine {computed} != published {expected} ({g['source']})"


def test_every_executable_method_is_gated():
    execs = {k for k, (kind, st, strat) in COVERAGE.items() if st == "executable"}
    missing = execs - gated_methods()
    assert not missing, f"executable methods with NO external gate (rule 10): {missing}"


def test_captured_gates_are_real_and_sourced():
    assert len(CAPTURED_GATES) >= 3               # u_sub, abel_plana, dim_reg (euler_maclaurin promoted)
    for g in CAPTURED_GATES:
        assert g["source"].startswith("http"), g["method"]
        assert g["published"], g["method"]
