"""End-to-end smoke test of the propose -> execute -> verify -> explain loop.

Run:  python examples/demo_trace.py

Demonstrates two things the rest of the toolchain does NOT do together:
  (1) a convergent integral recognized in closed form via PSLQ;
  (2) a genuinely DIVERGENT object handled by a named method (zeta
      regularization) and verified numerically — the crux capability.
"""
import sys
from integral_explainer.oracle import high_precision, recognize
from integral_explainer.methods import METHODS
from integral_explainer.trace import MethodTrace, Step
import mpmath as mp

# Unicode math symbols below; force UTF-8 stdout so this runs on a Windows
# cp1252 console as well as macOS/Linux.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def convergent_demo() -> None:
    val = high_precision("1/(1+x**2)", 0, "inf", dps=60)
    closed = recognize(val, ["pi"], dps=60)
    print("[convergent]  ∫₀^∞ dx/(1+x²) =", val)
    print("[convergent]  recognized as:", closed, "\n")


def divergent_demo() -> None:
    # The divergent lattice sum  Σ_{n>=1} n.  Named method: zeta regularization.
    method = METHODS["zeta_reg"]
    reg_value = mp.zeta(-1)                       # ζ(-1) = analytic continuation
    closed = recognize(reg_value, dps=60)         # -> '(-1/12)'

    trace = MethodTrace(integral="sum_{n>=1} n  (divergent lattice sum)")
    trace.add(Step(
        method_key=method.key,
        before="Σ_{n>=1} n",
        after="ζ(-1)",
        justification=method.applies_when + " — " + method.explanation,
        check=f"pslq:{closed}",
    ))
    trace.result = closed

    print(trace.render())
    print("[divergent]   numeric ζ(-1) =", reg_value, "(== -1/12:",
          mp.almosteq(reg_value, mp.mpf(-1) / 12), ")")


if __name__ == "__main__":
    convergent_demo()
    divergent_demo()
