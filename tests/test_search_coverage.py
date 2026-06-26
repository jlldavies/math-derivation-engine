"""The search-coverage harness as tests: completeness invariants (incl. the wiring proof and the
registry-driven fire check) + solve-via-search on each kind + a NEGATIVE test proving a dead row
is actually caught. Adding a method without a coverage row, marking one executable without wiring
it into a live solver, or adding a live strategy with no representative all break these.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import coverage                                    # noqa: E402
from integral_explainer.methods import METHODS                            # noqa: E402
from integral_explainer import strategies as S                            # noqa: E402


# ---- completeness invariants (all six) -----------------------------------------------------
def test_registry_is_complete():
    assert coverage.assert_complete()        # key + consistency + WIRING + kind + orphan + FIRE


def test_every_method_has_exactly_one_row():
    assert set(S.COVERAGE) == set(METHODS)


def test_executable_rows_are_reachable_by_a_live_solver():
    for k, (kind, status, strat) in S.COVERAGE.items():
        if status == "executable":
            if kind == S.CAPABILITY:
                assert k in S.CAPABILITIES, f"{k} capability not registered"
            else:
                assert strat in S.KIND_SOLVERS[kind](), f"{k} is a dead row"


# ---- the harness actually CATCHES a dead row (negative test) --------------------------------
def test_dead_row_is_caught(monkeypatch=None):
    saved = dict(S.COVERAGE)
    try:
        # inject an executable method whose strategy is in NO live solver list
        S.COVERAGE["__fake__"] = (S.IDENTITY, "executable", S.Strategy("__fake__", lambda e: []))
        g = coverage.gaps()
        assert any(name == "__fake__" for name, *_ in g["dead_rows"]) or g["undeclared"], \
            "harness failed to flag a dead/undeclared executable row"
    finally:
        S.COVERAGE.clear()
        S.COVERAGE.update(saved)


# ---- solving routes through search() for each kind -----------------------------------------
def test_integration_search_elementary():
    assert S.solve_integral("x*exp(x)")["best"] is not None


def test_integration_search_gaussian_definite():
    assert S.solve_integral("exp(-x**2)*cos(2*x)", 0, "oo")["best"] is not None


def test_integration_search_partial_fractions():
    assert S.solve_integral("1/(x**2-1)")["best"] is not None      # solves; route is search's choice


def test_identity_search_trig():
    x = sp.Symbol("x")
    assert S.prove_identity(sp.cos(x) ** 2 + sp.sin(x) ** 2 - 1)["best"] is not None


def test_identity_search_polynomial_in_derivatives():
    s = sp.Symbol("s")
    r = sp.Function("r")(s)
    e = sp.diff(r, s, 2) / (1 - 2 / r) - r * sp.diff(r, s, 2) / (r - 2)
    assert S.prove_identity(e)["best"] is not None
