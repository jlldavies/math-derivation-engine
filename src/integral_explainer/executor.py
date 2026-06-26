"""Executor: applies a method to an integral using SymPy (the CAS).

This is the 'execute' stage of propose -> execute -> verify -> explain. It hands
the integral to SymPy and reports both the result and whether it reduced to a
*special function* (Meijer-G / hypergeometric) -- the signature of the class of
problems where the closed form exists but its asymptotic expansion is the hard part.

Deliberately thin: the engine's value is in proposing the method and verifying
the result, not in re-implementing a CAS.
"""
from __future__ import annotations

from dataclasses import dataclass
import sympy as sp


@dataclass
class ExecResult:
    closed_form: sp.Expr | None   # SymPy result, or None if it could not evaluate
    is_special: bool              # True if the result is/contains Meijer-G or hyper
    evaluated: bool               # True if SymPy returned a finite closed form
    note: str = ""

    def numeric(self, dps: int = 50):
        """High-precision float of the closed form (for cross-checks), or None."""
        if self.closed_form is None:
            return None
        try:
            return sp.N(self.closed_form, dps)
        except Exception:
            return None


def _bound(v):
    if v in (0, "0"):
        return sp.Integer(0)
    if v in ("oo", "inf", "+inf"):
        return sp.oo
    if v in ("-oo", "-inf"):
        return -sp.oo
    return sp.sympify(v)


def reduce_integral(integrand: str, a, b, *, var: str = "x", meijerg: bool = True) -> ExecResult:
    """Definite-integrate `integrand` from a to b, preferring the Meijer-G route.

    `meijerg=True` forces SymPy's Meijer-G algorithm, which is what reduces the
    Blitz-type integrands to named special functions. Returns an ExecResult.
    """
    x = sp.symbols(var, positive=True)
    expr = sp.sympify(integrand, locals={var: x})
    lo, hi = _bound(a), _bound(b)

    try:
        result = sp.integrate(expr, (x, lo, hi), meijerg=meijerg)
    except Exception as e:  # SymPy can raise on hard integrands
        return ExecResult(None, False, False, note=f"sympy raised: {type(e).__name__}: {e}")

    # An unevaluated Integral means SymPy could not do it.
    if isinstance(result, sp.Integral) or result.has(sp.Integral):
        return ExecResult(None, False, False, note="unevaluated")

    is_special = result.has(sp.meijerg) or result.has(sp.hyper)
    return ExecResult(result, is_special, True,
                      note="meijer-g/special form" if is_special else "elementary/closed form")


def verify_closed_form(integrand, lo, hi, claimed, *, osc=False, period=None, dps=30):
    """NUMERICS-VERIFY a pattern-rule reduction SymPy could not do symbolically.

    The companion to `reduce_integral`'s elementary route: when the recognised
    pattern supplies a NAMED closed form (Tricomi-U, Meijer-G, …) that blind SymPy
    returns unevaluated, this confirms it — high-precision quadrature of `integrand`
    over [lo,hi] vs the `claimed` value. Numerics VERIFY a recognised form; they do
    not find it. `osc=True` uses oscillatory quadrature (the Blitz complex-s case).
    Returns (digits_agree, numeric_value)."""
    import mpmath as mp
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        num = (mp.quadosc(integrand, [lo, hi], period=period) if osc
               else mp.quad(integrand, [lo, hi]))
        scale = abs(claimed) if claimed != 0 else mp.mpf(1)   # abs() handles complex (mpc)
        diff = abs(num - claimed)
        digits = dps if diff == 0 else max(0, int(-mp.log10(diff / scale)))
        return digits, num
    finally:
        mp.mp.dps = old
