"""LEVELED Derivation for the feynman_parameter method (differentiation under the integral),
mirroring the ACTUAL engine computation special_methods.feynman_frullani():

    integrand   = (e^{-x} - e^{-a x}) / x
    I_prime     = sp.integrate(sp.diff(integrand, a), (x, 0, oo))      # = 1/a
    I_at_1      = sp.integrate(integrand.subs(a, 1), (x, 0, oo))       # = 0   (anchor)
    I(a)        = sp.integrate(I_prime.subs(a,t), (t, 1, a)) + I_at_1  # = ln a

The qualification tree's THREE moves are exactly the three engine lines:
  (1) the parameter derivative   ∂_a I  -> the inner integral collapses to 1/a   [feynman: ∂-under-∫]
  (2) the anchor value           I(1) = 0                                        [base: it's the zero integrand]
  (3) integrate the parameter back  ∫_1^a (1/t) dt = ln a                        [feynman: integrate-back / FTC]

requires drives the frontier cut so plain >= working >= expert step counts EMERGE.
Run:  python scratch/expl_feynman_parameter.py     (does NOT modify src/)
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = r"I(a)=\int_{0}^{\infty}\frac{e^{-x}-e^{-ax}}{x}\,dx"

def build_feynman_parameter_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents="a Frullani integral; parameter a (the dial we differentiate in)",
        goal=Goal.EVALUATE,
        integral="value I(a) of the (e^{-x}-e^{-ax})/x Frullani integral")
    d = Derivation(problem)

    # ---- WHY: the recognition / decision (forced-by / payoff / relies-on) -------------------
    d.why("Why this approach — differentiate under the integral",
          {"plain": r"The fraction $\frac{e^{-x}-e^{-ax}}{x}$ has no nice antiderivative in $x$ — the $x$ "
                    r"downstairs blocks it. But the answer is a function of the dial $a$. Trick: watch how the "
                    r"answer changes as you nudge $a$. That change is a much easier integral, and once we know "
                    r"the rate of change we can add it back up to recover the answer.",
           "working": r"There is no elementary antiderivative in $x$, but the integral depends on the parameter "
                      r"$a$. Differentiating in $a$ kills the $\tfrac1x$ and leaves a plain exponential integral; "
                      r"$\partial_a I=1/a$, which we integrate back over $a$.",
           "expert": r"$\frac{e^{-x}-e^{-ax}}{x}$ has no elementary $x$-antiderivative, but $I(a)$ is "
                     r"$C^1$ in the parameter on $a>0$; Leibniz differentiation removes the $1/x$ obstruction, "
                     r"giving $I'(a)=1/a$, recovered by the parameter FTC from the anchor $I(1)=0$."},
          forced_by=r"the $1/x$ makes the $x$-antiderivative non-elementary, yet the integrand depends smoothly "
                    r"on $a$ and $\partial_a$ cancels exactly that $1/x$ — the $x$-integration is blocked but the "
                    r"$a$-derivative is wide open.",
          payoff=r"differentiating in $a$ collapses the whole thing to $\int_0^\infty e^{-ax}dx=1/a$, a one-line "
                 r"exponential; integrating $1/a$ back gives $\ln a$ — the logarithm EMERGES from "
                 r"$\int_1^a dt/t$, it is never written in.",
          relies_on=r"the Leibniz rule $\frac{d}{da}\int=\int\partial_a$ here: on $a\ge a_0>0$ the partial "
                    r"$\partial_a\frac{e^{-x}-e^{-ax}}{x}=e^{-ax}$ is continuous and dominated by the integrable "
                    r"$e^{-a_0 x}$, so differentiation passes under the sign.")

    # ---- HOW: the machinery (the parameter relation) ----------------------------------------
    d.how("How the approach works — the parameter integral",
          {"plain": r"Differentiating $I(a)$ in $a$ cancels the $x$ in the denominator and leaves "
                    r"$\int_0^\infty e^{-ax}dx=1/a$. Since $I(1)=0$, adding up $1/a$ from $1$ to $a$ gives $\ln a$.",
           "working": r"$I'(a)=\int_0^\infty\partial_a\frac{e^{-x}-e^{-ax}}{x}\,dx=\int_0^\infty e^{-ax}dx=\frac1a$; "
                      r"with $I(1)=0$, $I(a)=\int_1^a\frac{dt}{t}=\ln a$.",
           "expert": r"$I'(a)=\int_0^\infty e^{-ax}dx=1/a$; the FTC in the parameter with anchor $I(1)=0$ "
                     r"gives $I(a)=\int_1^a dt/t=\ln a$."},
          math=[r"I'(a)=\int_{0}^{\infty}\frac{\partial}{\partial a}\frac{e^{-x}-e^{-ax}}{x}\,dx"
                r"=\int_{0}^{\infty}e^{-ax}\,dx=\frac{1}{a},\qquad I(1)=0\ \Rightarrow\ I(a)=\int_{1}^{a}\frac{dt}{t}=\ln a"])

    # ---- THE STEPS: one qualification tree -------------------------------------------------
    # EXPERT grasps "evaluate via the parameter integral" as ONE node (requires=expert):
    #   the whole Feynman move (∂-under-∫ -> 1/a, anchor 0, integrate-back -> ln a).
    # WORKING sees its 3 sub-moves (the three engine lines).
    # PLAIN decomposes each of those further (chain rule, the e^{-ax} integral, the FTC).
    d.step("Evaluate via the parameter integral", requires="expert",
           prose=r"Differentiating under the integral cancels the $1/x$ and gives $I'(a)=\int_0^\infty e^{-ax}dx=1/a$; "
                 r"the anchor $I(1)=0$ then integrates this back to $I(a)=\int_1^a dt/t=\ln a$.",
           math=[r"I'(a)=\frac1a,\quad I(1)=0\ \Rightarrow\ I(a)=\int_{1}^{a}\frac{dt}{t}=\ln a"],
           relies_on=r"sub-methods: differentiation under the integral sign (Leibniz) + the parameter FTC.",
           decompose=[

               # ---- MOVE 1: the parameter derivative -> 1/a  (engine line: I_prime) ----------
               dict(title="Differentiate under the integral sign: I'(a) = 1/a", requires="working",
                    prose=r"By Leibniz the $a$-derivative passes inside; the $-e^{-ax}$ term's derivative is "
                          r"$x e^{-ax}$, the $x$ cancels the $1/x$, and the leftover exponential integrates to $1/a$.",
                    math=[r"I'(a)=\int_{0}^{\infty}\frac{\partial}{\partial a}\frac{e^{-x}-e^{-ax}}{x}\,dx"
                          r"=\int_{0}^{\infty}e^{-ax}\,dx=\frac{1}{a}"],
                    references=["sub-method → library/differentiation-under-integral.md (Leibniz rule)"],
                    decompose=[
                        dict(title="The a-derivative of the integrand (chain rule)", requires="plain",
                             prose=r"Only the $-e^{-ax}$ piece holds an $a$. Its $a$-derivative is $+x e^{-ax}$ "
                                   r"(chain rule on $-ax$); dividing by the $x$ already there cancels it.",
                             math=[r"\frac{\partial}{\partial a}\Big(e^{-x}-e^{-ax}\Big)=x\,e^{-ax}"
                                   r"\ \Rightarrow\ \frac{\partial}{\partial a}\frac{e^{-x}-e^{-ax}}{x}=e^{-ax}"],
                             references=["base → library/chain-rule.md"]),
                        dict(title="The exponential integral ∫₀^∞ e^{-ax} dx = 1/a", requires="plain",
                             prose=r"A standard exponential: the antiderivative of $e^{-ax}$ is $-\tfrac1a e^{-ax}$, "
                                   r"which is $0$ at $\infty$ and $-\tfrac1a$ at $0$.",
                             math=[r"\int_{0}^{\infty}e^{-ax}\,dx=\Big[-\tfrac{1}{a}e^{-ax}\Big]_{0}^{\infty}=\frac1a"],
                             references=["base → library/exponential-integral.md"]),
                    ]),

               # ---- MOVE 2: the anchor value  (engine line: I_at_1) --------------------------
               dict(title="Anchor the parameter: I(1) = 0", requires="plain",
                    prose=r"At $a=1$ the two exponentials coincide, so the integrand is identically $0$ — this is "
                          r"the constant of integration the FTC needs.",
                    math=[r"I(1)=\int_{0}^{\infty}\frac{e^{-x}-e^{-x}}{x}\,dx=\int_{0}^{\infty}0\,dx=0"]),

               # ---- MOVE 3: integrate the parameter back -> ln a  (engine line: integrate) ---
               dict(title="Integrate the parameter back: I(a) = ∫₁^a dt/t = ln a", requires="working",
                    prose=r"The FTC in the parameter rebuilds $I$ from its rate $I'(t)=1/t$ starting at the anchor "
                          r"$I(1)=0$; the integral of $1/t$ is $\ln$, and $\ln 1=0$ matches the anchor.",
                    math=[r"I(a)=I(1)+\int_{1}^{a}I'(t)\,dt=0+\int_{1}^{a}\frac{dt}{t}=\ln a"],
                    references=["sub-method → library/parameter-FTC.md (recover I from I' and an anchor)"],
                    decompose=[
                        dict(title="Substitute the rate I'(t) = 1/t", requires="plain",
                             prose=r"From move 1 the rate at any dial value $t$ is $1/t$; drop it into the FTC.",
                             math=[r"I(a)=\int_{1}^{a}I'(t)\,dt=\int_{1}^{a}\frac{dt}{t}"]),
                        dict(title="Integrate 1/t and use the anchor", requires="plain",
                             prose=r"The antiderivative of $1/t$ is $\ln t$; evaluate from $1$ to $a$ and use "
                                   r"$\ln 1=0$ (so the anchor $I(1)=0$ is honoured).",
                             math=[r"\int_{1}^{a}\frac{dt}{t}=\big[\ln t\big]_{1}^{a}=\ln a-\ln 1=\ln a"],
                             references=["base → library/log-as-integral.md (∫dt/t = ln)"]),
                    ]),
           ])

    # ---- VERIFY: independent checks, not used to derive ------------------------------------
    d.verify(
        r"Two checks, neither used to derive the answer. The engine's "
        r"`special_methods.feynman_frullani()` runs these same three lines in SymPy and returns "
        r"$\ln a$ (the log is the OUTPUT of `sp.integrate(1/t,(t,1,a))`, never written in); and "
        r"high-precision quadrature of the original integral agrees with $\ln a$ at sample $a$.",
        math=[r"\text{engine: }\ \texttt{feynman\_frullani()}=\ln a",
              r"\text{numeric }(a=2):\ \int_{0}^{\infty}\frac{e^{-x}-e^{-2x}}{x}\,dx\ \approx\ 0.693147\ =\ \ln 2"],
        references=["engine: special_methods.feynman_frullani — the wired capability",
                    "external gate: external_gates.CAPABILITY_GATES (rule 10)",
                    "method: library/differentiation-under-integral.md"])
    d.result(latex=r"I(a)=\int_{0}^{\infty}\frac{e^{-x}-e^{-ax}}{x}\,dx=\ln a",
             note="ln a EMERGES from integrating the parameter rate 1/a back from the anchor I(1)=0 — "
                  "matches the engine's feynman_frullani() and numeric quadrature.")
    return d

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    d = build_feynman_parameter_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[]  -> VALID (no warnings)")
    assert not qwarn, qwarn
    assert len(set(counts.values())) == 3, f"counts must all differ: {counts}"
    print("OK: 3 bands, counts differ plain>=working>=expert, every step within reach.")
