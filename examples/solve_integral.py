"""CLOSE THE LOOP: recognise -> execute -> verify -> explain, on an actual integral.

An oscillatory Gaussian  I(w) = ∫_0^∞ e^{-x^2} cos(w x) dx:
  1. RECOGNISE the method  (engine recognizer -> differentiation-under-the-integral),
  2. EXECUTE symbolically  (engine executor / SymPy -> closed form),
  3. VERIFY numerically    (mpmath high-precision quadrature -> agreement to N digits),
  4. EXPLAIN deeply        (Derivation -> levelled why/how/step trace a reader can check).

Unlike examples/bondi_christoffel.py (a hand-coded showcase), the lifting here is the
ENGINE's: recognize + reduce_integral + Derivation. The agent supplies only the method
steps for the recognised pattern. Run:  python examples/solve_integral.py
"""
import os
import sys

import sympy as sp
import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import (load_patterns, recognize_pattern, reduce_integral,  # noqa: E402
                                Derivation, render_leveled, validate_qualification,
                                Problem, Goal)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

INTEGRAND = "exp(-x**2)*cos(w*x)"
HDR = r"I(w)=\int_{0}^{\infty} e^{-x^{2}}\cos(wx)\,dx"


def main():
    # 1. RECOGNISE -----------------------------------------------------------
    pats = load_patterns()
    hits = recognize_pattern("oscillatory gaussian integral differentiate under the "
                             "integral sign with respect to a parameter", pats, k=3)
    top = hits[0][0] if hits else None
    print("1. recognise:", top.id if top else "(none)",
          "| runners-up", [p.id for p, _ in hits[1:]])

    # 2. EXECUTE (symbolic, the engine's executor) ---------------------------
    res = reduce_integral(INTEGRAND, 0, sp.oo)
    closed = res.closed_form
    print(f"2. execute (SymPy): {closed}   [{res.note}]")
    closed_tex = sp.latex(closed)

    # 3. VERIFY (numeric oracle) ---------------------------------------------
    wv = mp.mpf(2)
    num = mp.quad(lambda t: mp.e ** (-t ** 2) * mp.cos(wv * t), [0, mp.inf])
    symv = mp.sqrt(mp.pi) / 2 * mp.e ** (-wv ** 2 / 4)
    digits = 30 if num == symv else int(-mp.log10(abs(num - symv)))
    print(f"3. verify (mpmath @w=2): {mp.nstr(num,16)} = {mp.nstr(symv,16)}  -> {digits} digits")

    # 4. EXPLAIN (Derivation -> levelled contract) ---------------------------
    problem = Problem(latex=HDR,
                      represents="oscillatory Gaussian (a Fresnel cousin); parameter w",
                      goal=Goal.EVALUATE, integral="coefficient-free value I(w)")
    d = Derivation(problem)
    d.why("Why this approach — differentiate under the integral",
          {"plain": r"We cannot find an ordinary antiderivative for $e^{-x^{2}}\cos(wx)$. But the answer is a "
                    r"function of the dial $w$. The trick: watch how the answer changes as you nudge $w$ — that "
                    r"gives a simple equation for the answer, which we can solve.",
           "working": r"There is no elementary antiderivative in $x$, but the whole integral depends on the "
                      r"parameter $w$. Differentiating the integral in $w$ gives a simpler integral that relates "
                      r"back to $I(w)$ itself — an ODE we can solve.",
           "expert": r"$e^{-x^{2}}\cos(wx)$ has no elementary $x$-antiderivative, but $I(w)$ is smooth in the "
                     r"parameter; Leibniz differentiation turns it into a first-order linear ODE in $w$."},
          forced_by=r"the integrand has no elementary antiderivative in $x$, yet depends smoothly on $w$ — the "
                    r"$x$-integration is blocked but the $w$-derivative is open.",
          payoff=r"differentiating in $w$ collapses the problem to a one-line ODE whose solution carries the full "
                 r"$e^{-w^{2}/4}$ structure; a bare number would hide that the answer is itself a Gaussian in $w$.",
          relies_on=r"the Leibniz rule here ($\tfrac{d}{dw}\int=\int\partial_w$): the integrand and its "
                    r"$w$-derivative are continuous and dominated by the integrable $x e^{-x^{2}}$.")
    d.how("How the approach works — the parameter ODE",
          {"plain": r"Differentiating $I(w)$ in $w$ brings a factor $-x\sin(wx)$ inside; one integration by parts "
                    r"turns that back into $I(w)$, giving $I'(w)=-\tfrac{w}{2}I(w)$.",
           "working": r"$I'(w)=\int_0^\infty\partial_w(e^{-x^2}\cos wx)\,dx$, then integrate by parts to relate it "
                      r"to $I(w)$.",
           "expert": r"$I'(w)=-\int_0^\infty x e^{-x^2}\sin(wx)\,dx$; one IBP gives $-\tfrac{w}{2}I(w)$."},
          math=[r"I(w)=\int_{0}^{\infty}e^{-x^{2}}\cos(wx)\,dx,\qquad "
                r"I'(w)=-\int_{0}^{\infty}x\,e^{-x^{2}}\sin(wx)\,dx"])
    # ONE qualification tree. The per-level counts EMERGE from the cut, not by hand:
    #   expert grasps the whole "solve via the parameter ODE" as one move (requires=expert);
    #   working sees its 4 sub-steps; plain decomposes the working steps further still.
    d.step("Solve via the parameter ODE", requires="expert",
           prose=r"$I(0)=\sqrt\pi/2$; differentiating under the integral plus one integration by parts give "
                 r"$I'(w)=-\tfrac{w}{2}I(w)$; integrating that ODE yields the closed form.",
           math=[r"I(0)=\frac{\sqrt{\pi}}{2},\quad I'(w)=-\frac{w}{2}I(w)\ \Rightarrow\ I(w)=\frac{\sqrt{\pi}}{2}e^{-w^{2}/4}"],
           decompose=[
               dict(title="The value at w = 0 (a Gaussian)", requires="plain",
                    prose=r"At $w=0$ the cosine is $1$, so $I(0)$ is the standard Gaussian integral (a known value).",
                    math=[r"I(0)=\int_{0}^{\infty}e^{-x^{2}}\,dx=\frac{\sqrt{\pi}}{2}"],
                    references=["base method → library/gaussian-integral.md"]),
               dict(title="Differentiate under the integral sign", requires="working",
                    prose=r"Differentiate $I(w)$ in $w$; by Leibniz the derivative passes inside.",
                    math=[r"I'(w)=\int_{0}^{\infty}\frac{\partial}{\partial w}\Big(e^{-x^{2}}\cos(wx)\Big)\,dx"
                          r"=-\int_{0}^{\infty}x\,e^{-x^{2}}\sin(wx)\,dx"],
                    decompose=[dict(title="The w-derivative of the integrand", requires="plain",
                                    prose=r"The only $w$ sits inside $\cos(wx)$; its $w$-derivative is $-x\sin(wx)$ "
                                          r"(the chain rule).",
                                    math=[r"\frac{\partial}{\partial w}\cos(wx)=-x\sin(wx)\ \Rightarrow\ "
                                          r"\frac{\partial}{\partial w}\Big(e^{-x^{2}}\cos(wx)\Big)=-x\,e^{-x^{2}}\sin(wx)"],
                                    references=["base method → library/chain-rule.md"])]),
               dict(title="Integrate by parts", requires="working",
                    prose=r"Take $u=\sin(wx),\ dv=-x e^{-x^{2}}dx$; the boundary term vanishes and what is left is $I(w)$.",
                    math=[r"I'(w)=\Big[\tfrac12 e^{-x^{2}}\sin(wx)\Big]_{0}^{\infty}"
                          r"-\frac{w}{2}\int_{0}^{\infty}e^{-x^{2}}\cos(wx)\,dx=-\frac{w}{2}\,I(w)"],
                    decompose=[
                        dict(title="Set up u and dv", requires="plain",
                             prose=r"Choose the pieces so $x e^{-x^{2}}$ integrates (to $-\tfrac12 e^{-x^{2}}$).",
                             math=[r"u=\sin(wx),\ dv=-x e^{-x^{2}}dx\ \Rightarrow\ du=w\cos(wx)\,dx,\ v=\tfrac12 e^{-x^{2}}"],
                             references=["base method → library/integration-by-parts.md"]),
                        dict(title="The boundary term vanishes", requires="plain",
                             prose=r"At $\infty$ the Gaussian $\to0$; at $0$, $\sin0=0$.",
                             math=[r"\Big[\tfrac12 e^{-x^{2}}\sin(wx)\Big]_{0}^{\infty}=0"]),
                        dict(title="What is left is I(w) again", requires="plain",
                             prose=r"The remaining $-\int v\,du$ rebuilds the original integral, with a factor $-\tfrac{w}{2}$.",
                             math=[r"I'(w)=-\frac{w}{2}\int_{0}^{\infty}e^{-x^{2}}\cos(wx)\,dx=-\frac{w}{2}I(w)"]),
                    ]),
               dict(title="Solve the ODE  I'(w) = -(w/2) I(w)", requires="working",
                    prose=r"A separable first-order ODE with $I(0)=\sqrt\pi/2$.",
                    math=[r"\frac{dI}{I}=-\frac{w}{2}\,dw\ \Rightarrow\ I(w)=\frac{\sqrt{\pi}}{2}e^{-w^{2}/4}"],
                    decompose=[
                        dict(title="Separate the variables", requires="plain",
                             prose=r"Put every $I$ on one side, every $w$ on the other.",
                             math=[r"\frac{dI}{I}=-\frac{w}{2}\,dw"]),
                        dict(title="Integrate both sides", requires="plain",
                             prose=r"Left gives $\ln I$; right gives $-w^{2}/4+C$.",
                             math=[r"\int\frac{dI}{I}=-\int\frac{w}{2}\,dw\ \Rightarrow\ \ln I=-\frac{w^{2}}{4}+C"]),
                        dict(title="Use I(0) to fix the constant", requires="plain",
                             prose=r"At $w=0$, $I=\sqrt\pi/2$, so $e^{C}=\sqrt\pi/2$.",
                             math=[r"I(w)=\frac{\sqrt{\pi}}{2}\,e^{-w^{2}/4}"]),
                    ]),
           ])
    d.verify(
        r"Two independent checks, neither used to *derive* the answer. The symbolic engine "
        r"(SymPy's integrator) returns the same closed form; and high-precision quadrature agrees with it.",
        math=[r"\text{SymPy: }\ \int_{0}^{\infty}e^{-x^{2}}\cos(wx)\,dx=" + closed_tex,
              r"\text{numeric }(w=2):\ " + mp.nstr(num, 16) + r"\ \approx\ " + mp.nstr(symv, 16)
              + r"\ \ (\text{agree to }" + str(digits) + r"\text{ digits})"],
        references=["SymPy meijer-G integrator — engine executor.reduce_integral",
                    "mpmath high-precision quadrature — the numeric oracle",
                    "method: library/differentiation-under-integral.md"])
    d.result(latex=r"I(w)=\int_{0}^{\infty}e^{-x^{2}}\cos(wx)\,dx=\frac{\sqrt{\pi}}{2}\,e^{-w^{2}/4}",
             note=f"verified two ways — SymPy closed form + numeric agreement to {digits} digits at w=2.")

    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}   # EMERGENT from the tree cut
    qwarn = validate_qualification(tracks)        # every shown step's qualification <= its level
    print(f"   levels (steps, emergent): {counts} ", "-> every step within reach" if not qwarn else f"-> {qwarn}")
    assert not qwarn, qwarn
    out = os.path.join(os.path.dirname(__file__), "solve_output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "oscillatory_gaussian.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_leveled(tracks))
    print("4. explain ->", path)


if __name__ == "__main__":
    main()
