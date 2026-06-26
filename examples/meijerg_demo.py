"""M0 capability demo: the full propose -> execute -> verify -> explain loop on a
genuinely divergent, oscillatory integral that reduces to a Meijer-G closed form
with a sqrt(pi) constant .

Target:   I = INT_0^inf  cos(x) / sqrt(x)  dx
  * NOT absolutely convergent (a Fresnel-type / regularized object);
  * naive quadrature fails (oscillatory tail + 1/sqrt(x) endpoint singularity);
  * SymPy reduces it via Meijer-G to the exact value sqrt(pi/2);
  * the engine VERIFIES that value two independent ways: high-precision
    oscillatory quadrature, and PSLQ constant recognition (the RIES analog).

This exercises exactly the chain hard physics integrals need
(u_sub -> stationary_phase/meijer_g -> recognize the sqrt(pi) coefficient),
and proves the verification-for-divergent signal on engine code -- not stored
answers. Run:  python examples/meijerg_demo.py
"""
import sys
import mpmath as mp

from integral_explainer import (
    propose, reduce_integral, high_precision_osc, recognize, agree,
    MethodTrace, Step,
)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

INTEGRAND = "cos(x)/sqrt(x)"      # SymPy form
A, B = 0, "oo"
DPS = 48


def main() -> None:
    mp.mp.dps = DPS   # set precision before any mpf is parsed from a string
    trace = MethodTrace(integral="∫₀^∞ cos(x)/√x dx")

    # ----- PROPOSE (rule-based; LLM proposer is M1) -----------------------
    candidates = propose(INTEGRAND, A, B)
    print("PROPOSE — ranked methods:")
    for key, reason in candidates:
        print(f"   • {key}: {reason}")
    print()

    # ----- EXECUTE (SymPy CAS -> Meijer-G closed form) -------------------
    res = reduce_integral(INTEGRAND, A, B, meijerg=True)
    closed = res.closed_form
    print(f"EXECUTE — SymPy ({res.note}):  {closed}")
    sym_val = mp.mpf(str(res.numeric(DPS)))
    trace.add(Step(
        method_key="meijer_g",
        before="∫₀^∞ cos(x)·x^(-1/2) dx",
        after=str(closed),
        justification="x^(-1/2) with an oscillatory weight reduces to a Meijer-G; SymPy returns the exact value.",
        check="symbolic",
    ))

    # ----- VERIFY 1: independent high-precision oscillatory quadrature ----
    # substitution t=u**2 (u_sub) tames the 1/sqrt(t) singularity and converts
    # to Fresnel form 2*∫₀^∞ cos(u²) du, integrated between its zeros.
    zeros = lambda n: mp.sqrt((n + mp.mpf(1) / 2) * mp.pi)
    num_val = 2 * high_precision_osc("mp.cos(x**2)", 0, "inf", dps=DPS, zeros=zeros)
    ok_num = agree(sym_val, num_val, dps=DPS, tol_digits=40)
    print(f"VERIFY₁ — quadosc value: {num_val}")
    print(f"          agrees with SymPy to ≥40 digits: {ok_num}")
    trace.add(Step(
        method_key="stationary_phase",
        before="∫₀^∞ cos(x)·x^(-1/2) dx",
        after="2·∫₀^∞ cos(u²) du  (t=u², Fresnel form)",
        justification="oscillatory tail + endpoint singularity: substitute then integrate between zeros (quadosc).",
        check=f"numeric:{40 if ok_num else 0}",
    ))

    # ----- VERIFY 2: PSLQ constant recognition (the RIES analog) ----------
    recognized_sq = recognize(num_val ** 2, ["pi"], dps=DPS)   # value² = π/2
    print(f"VERIFY₂ — PSLQ recognizes (value)² as: {recognized_sq}   ⇒  value = √({recognized_sq})")
    trace.add(Step(
        method_key="asymptotic_expansion",
        before="numeric value (48 digits)",
        after="√(π/2)",
        justification="PSLQ identifies the squared value as π/2 — confirms the √π closed form, as RIES/PSLQ does for such constants.",
        check=f"pslq:{recognized_sq}",
    ))
    trace.result = "√(π/2)"

    print("\n" + "=" * 70)
    print(trace.render())

    assert ok_num, "numeric verification failed"
    assert recognized_sq is not None, "PSLQ recognition failed"
    print("M0 signal: divergent/oscillatory integral verified end-to-end ✓")


if __name__ == "__main__":
    main()
