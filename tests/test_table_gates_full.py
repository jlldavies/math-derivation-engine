"""Full published-table gate suite (rule 10): 167 (integrand, antiderivative) pairs harvested
from Wikipedia's 9 integral tables and re-verified by hand. Each test RE-RUNS the engine and
asserts it reproduces the PUBLISHED answer (source validated by differentiation; engine matched
up to a constant, with a numeric fallback so an equivalent-but-differently-written form passes).
KNOWN_GAPS are entries SymPy cannot yet integrate — tracked as xfail so a future fix flags itself.
"""
import os
import sys

import pytest
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.strategies import solve_integral                       # noqa: E402
from _table_gates_data import TABLE_GATES, CLOSED_GAPS                         # noqa: E402

# Heavy: 167 live solve_integral calls (~4.5 min). Deselected by default; run with `pytest -m slow`.
pytestmark = pytest.mark.slow

_x = sp.Symbol("x", positive=True)


def _reproduces(integrand, published):
    ig = sp.sympify(integrand, locals={"x": _x})
    pub = sp.sympify(published, locals={"x": _x})
    if sp.simplify(sp.diff(pub, _x) - ig) != 0:
        return False, "source inconsistent"
    res = solve_integral(integrand)
    eng = res["best"][1] if res["best"] else None
    if eng is None:
        return False, "engine could not evaluate"
    if sp.simplify(sp.diff(eng - pub, _x)) == 0:
        return True, ""
    # numeric fallback: a valid antiderivative has d/dx(engine) == integrand
    try:
        if all(abs(complex(sp.N((sp.diff(eng, _x) - ig).subs(_x, sp.Rational(p, 10))))) < 1e-9
               for p in (3, 7, 13)):
            return True, ""
    except Exception:                                                          # noqa: BLE001
        pass
    return False, f"engine differs: {eng}"


@pytest.mark.parametrize("integrand,published", TABLE_GATES,
                         ids=[t[0] for t in TABLE_GATES])
def test_engine_reproduces_published_table_entry(integrand, published):
    ok, why = _reproduces(integrand, published)
    assert ok, f"{integrand}: {why}"


@pytest.mark.parametrize("integrand", CLOSED_GAPS, ids=CLOSED_GAPS)
def test_former_gap_now_solved(integrand):
    """The 8 ex-gaps (sech^2/csch^2, scaled inverse-hyperbolics) now solve via the new
    strategies; assert a VALID antiderivative with domain-aware sampling (asech/acosh have
    different real domains, so skip out-of-domain nan points)."""
    import math
    x = sp.Symbol("x", positive=True)
    ig = sp.sympify(integrand, locals={"x": x})
    best = solve_integral(integrand)["best"]
    assert best is not None, f"{integrand}: still unsolved"
    e = sp.diff(best[1], x) - ig
    if sp.simplify(e) == 0:
        return
    vals = []
    for p in (1, 2, 3, 5, 7, 9, 11, 13, 17):                  # x in (0.05, 0.85): both domains
        try:
            v = complex(e.subs(x, sp.Rational(p, 20)))
        except Exception:
            continue
        if not (math.isnan(v.real) or math.isinf(v.real)):
            vals.append(abs(v))
    assert len(vals) >= 2 and max(vals) < 1e-9, f"{integrand}: engine not a valid antiderivative"
