"""Numeric oracle: the verification substrate.

For divergent / regularized integrals you cannot differentiate-and-check. The
strategy is to evaluate a (regularized) integral to high precision and then
either compare against a proposed closed form or *recognize* the constant via
PSLQ. This module is the concrete, runnable core of that strategy.

M0 milestone uses mpmath. M2+ should add an Arb/python-flint backend for
*certified* error bounds (see DESIGN.md §3).
"""
from __future__ import annotations

from typing import Iterable, Optional
import mpmath as mp


def high_precision(integrand: str, a, b, *, dps: int = 60, var: str = "x") -> mp.mpf:
    """Evaluate the definite integral of `integrand` from a to b to `dps` digits.

    `integrand` is a Python/mpmath expression string in `var`, e.g. "1/(1+x**2)".
    `a`, `b` may be numbers or the strings "inf"/"-inf".

    NOTE: this evaluates a *convergent* integral. Divergent integrals must first
    be regularized (cutoff, analytic continuation, zeta, ...) into a convergent
    form — that regularization is exactly the method the engine is meant to make
    explicit. This function is the ground-truth check on the regularized value.
    """
    mp.mp.dps = dps

    def f(x):
        return eval(integrand, {"__builtins__": {}}, {var: x, "mp": mp, **_mp_ns()})

    lo = mp.inf if a == "inf" else (-mp.inf if a == "-inf" else mp.mpf(a))
    hi = mp.inf if b == "inf" else (-mp.inf if b == "-inf" else mp.mpf(b))
    return mp.quad(f, [lo, hi])


def high_precision_osc(integrand: str, a, b, *, dps: int = 60, var: str = "x",
                       omega: float = 1.0, zeros=None) -> mp.mpf:
    """Evaluate an *oscillatory* definite integral via mpmath.quadosc.

    Plain `mp.quad` fails on rapidly oscillating tails (e.g. cos(x), e^{i b x}) —
    exactly the integrands in the Blitz computation, which the paper handled with
    "Fourier methods". `quadosc` integrates between the zeros instead.

    Provide EITHER `omega` (for a fixed angular frequency, integrand ~ f(x)·trig(omega·x))
    OR `zeros` (a function n -> nth zero, for chirped integrands like cos(x**2)).
    Substitute away any endpoint singularity (e.g. t=u**2 for 1/sqrt(t)) BEFORE
    calling this — that substitution is itself one of the engine's methods.
    """
    mp.mp.dps = dps

    def f(x):
        return eval(integrand, {"__builtins__": {}}, {var: x, "mp": mp, **_mp_ns()})

    lo = mp.inf if a == "inf" else (-mp.inf if a == "-inf" else mp.mpf(a))
    hi = mp.inf if b == "inf" else (-mp.inf if b == "-inf" else mp.mpf(b))
    if zeros is not None:
        return mp.quadosc(f, [lo, hi], zeros=zeros)
    return mp.quadosc(f, [lo, hi], omega=mp.mpf(omega))


def recognize(value, basis: Optional[Iterable[str]] = None, *, dps: int = 60):
    """Try to identify a high-precision `value` as a closed form (PSLQ-backed).

    Wraps mpmath.identify. `basis` is a list of constant names whose presence you
    suspect, e.g. ["pi", "log(2)", "zeta(3)", "catalan"]. Returns the recognized
    expression string, or None.

    This is the experimental-mathematics half: recognize the *result*. It does
    not tell you the *method* — that is the proposer's job — but a confirmed
    closed form is the acceptance signal for a divergent step.
    """
    mp.mp.dps = dps
    return mp.identify(mp.mpf(value), list(basis) if basis else None)


def agree(value_a, value_b, *, dps: int = 60, tol_digits: int = 50) -> bool:
    """True if two high-precision values agree to ~tol_digits decimal places."""
    mp.mp.dps = dps
    return mp.almosteq(mp.mpf(value_a), mp.mpf(value_b), rel_eps=mp.mpf(10) ** (-tol_digits))


def _mp_ns() -> dict:
    """A safe-ish namespace of common mpmath functions for eval()."""
    names = [
        "pi", "e", "euler", "catalan", "sin", "cos", "tan", "exp", "log", "sqrt",
        "sinh", "cosh", "tanh", "gamma", "zeta", "polylog", "besselj", "bessely",
        "digamma", "atan", "asin", "acos",
    ]
    return {n: getattr(mp, n) for n in names if hasattr(mp, n)}
