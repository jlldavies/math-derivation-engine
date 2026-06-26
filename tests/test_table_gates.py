"""Published-table gates (CLAUDE.md rule 10) from Wikipedia's common integrals
(https://en.wikipedia.org/wiki/Lists_of_integrals). Each entry is SOMEONE ELSE'S published
(integrand, antiderivative). We validate the source (differentiates back to the integrand) and
assert the ENGINE reproduces it up to a constant. Parameters a,n are pinned to concrete values.
"""
import os
import sys

import pytest
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.strategies import solve_integral                       # noqa: E402

_x = sp.Symbol("x", positive=True)

# (label, integrand, published antiderivative) — verbatim from the table, principal domain (x>0)
TABLE = [
    ("const", "3", "3*x"),
    ("x^n", "x**3", "x**4/4"),
    ("1/x", "1/x", "log(x)"),
    ("e^{ax}", "exp(2*x)", "exp(2*x)/2"),
    ("a^x", "2**x", "2**x/log(2)"),
    ("ln x", "log(x)", "x*log(x)-x"),
    ("sin x", "sin(x)", "-cos(x)"),
    ("cos x", "cos(x)", "sin(x)"),
    ("tan x", "tan(x)", "-log(cos(x))"),
    ("sec^2 x", "sec(x)**2", "tan(x)"),
    ("csc^2 x", "csc(x)**2", "-cot(x)"),
    ("sinh x", "sinh(x)", "cosh(x)"),
    ("cosh x", "cosh(x)", "sinh(x)"),
    ("arcsin x", "asin(x)", "x*asin(x)+sqrt(1-x**2)"),
    ("arctan x", "atan(x)", "x*atan(x)-log(1+x**2)/2"),
    ("sec x tan x", "sec(x)*tan(x)", "sec(x)"),
    ("csc x cot x", "csc(x)*cot(x)", "-csc(x)"),
    ("sin^2 x", "sin(x)**2", "x/2 - sin(2*x)/4"),
    ("cos^2 x", "cos(x)**2", "x/2 + sin(2*x)/4"),
    ("tanh x", "tanh(x)", "log(cosh(x))"),
]


@pytest.mark.parametrize("label,integrand,published", TABLE, ids=[t[0] for t in TABLE])
def test_engine_reproduces_published_table_integral(label, integrand, published):
    ig = sp.sympify(integrand, locals={"x": _x})
    pub = sp.sympify(published, locals={"x": _x})
    assert sp.simplify(sp.diff(pub, _x) - ig) == 0, f"SOURCE inconsistent for {label}"
    eng = solve_integral(integrand)["best"]
    assert eng is not None, f"engine could not evaluate {label}"
    assert sp.simplify(sp.diff(eng[1] - pub, _x)) == 0, f"engine != published for {label}"
