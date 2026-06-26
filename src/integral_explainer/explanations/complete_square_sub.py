"""Leveled Derivation for method complete_square_sub (rule 7/11), worked on the integral that
surfaced it: arXiv:2606.23785 r-statistics normalization (β=1),
    int_0^infty (1+x)/(1+x+x^2)^(5/2) dx = 14/27.
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401


def build_complete_square_sub_derivation() -> Derivation:
    problem = Problem(
        latex=r"\int_{0}^{\infty}\frac{1+x}{(1+x+x^{2})^{5/2}}\,dx",
        represents="a polynomial over an irreducible quadratic raised to a half-integer power — "
                   "the complete-the-square (Euler substitution) case",
        goal=Goal.EVALUATE,
        integral=r"(1+x)/(1+x+x^{2})^{5/2}",
    )
    d = Derivation(problem)

    # 1) WHY -----------------------------------------------------------------------------------
    d.why(
        "Why complete the square",
        {"plain": r"The bottom is $1+x+x^2$ raised to the power $5/2$. It will not factor into real "
                  r"pieces (it has no real roots), so partial fractions are out; and the half-power "
                  r"means it is not an ordinary fraction either. The one obstacle is the middle term "
                  r"$x$ in $1+x+x^2$. If we could turn $1+x+x^2$ into something$^2 + $a constant, the "
                  r"integral would become a standard shape we know.",
         "working": r"The integrand is $P(x)/Q(x)^{p}$ with $Q$ an irreducible quadratic and $p=5/2$ "
                    r"non-integer. Neither partial fractions (Q is irreducible) nor the power rule (p "
                    r"non-integer) applies. The linear term in $Q$ is what blocks the standard "
                    r"$(u^2+k)^{-p}$ tables; completing the square removes it.",
         "expert": r"$Q=x^2+x+1$ is irreducible with a linear term, raised to a half-integer power, "
                   r"so the CAS returns it unevaluated. Completing the square is the Euler substitution "
                   r"$u=x+b/2a$ that sends $Q\mapsto u^2+k$, landing in the integrable "
                   r"$(u^2+k)^{-p}$ family."},
        forced_by=r"the denominator $(x^2+x+1)^{5/2}$ is an irreducible quadratic (no real roots, so "
                  r"partial fractions fail) carried to a non-integer power (so the rational-integration "
                  r"rules fail); the obstruction is purely the linear term $x$, which the direct CAS "
                  r"route cannot remove and so leaves the integral unevaluated.",
        payoff=r"one exact substitution deletes the linear term, turning $x^2+x+1$ into $u^2+\tfrac34$ "
               r"and the whole integrand into the standard $(u^2+k)^{-5/2}$ form the CAS integrates in "
               r"closed form; the value $14/27$ then falls out at the shifted limits.",
        relies_on=r"the algebraic identity $a x^2+b x+c=a\!\left(x+\tfrac{b}{2a}\right)^2+\left(c-\tfrac{b^2}{4a}\right)$ "
                  r"(exact for any quadratic), and, for the definite integral, the change of variable "
                  r"$u=x+\tfrac{b}{2a}$ which shifts the limits by $\tfrac{b}{2a}$ with $du=dx$.")

    # 2) HOW -----------------------------------------------------------------------------------
    d.how(
        "How it works — the shift that kills the linear term",
        {"plain": r"Write $1+x+x^2$ as $(x+\tfrac12)^2+\tfrac34$. Then let $u=x+\tfrac12$: the bottom "
                  r"becomes $(u^2+\tfrac34)^{5/2}$, the top $1+x$ becomes $u+\tfrac12$, and the limits "
                  r"$0\to\infty$ become $\tfrac12\to\infty$. Now it is a standard integral.",
         "working": r"Complete the square: $x^2+x+1=(x+\tfrac12)^2+\tfrac34$. Substitute $u=x+\tfrac12$ "
                    r"($du=dx$): the integral becomes $\int_{1/2}^{\infty}(u+\tfrac12)(u^2+\tfrac34)^{-5/2}\,du$.",
         "expert": r"$u=x+\tfrac12$ maps the integrand to $(u+\tfrac12)(u^2+\tfrac34)^{-5/2}$ on "
                   r"$[\tfrac12,\infty)$ — the integrable $(u^2+k)^{-p}$ family."},
        math=[r"x^2+x+1=\Big(x+\tfrac12\Big)^2+\tfrac34,\qquad u=x+\tfrac12,\quad du=dx"])

    # 3) STEPS — one qualification tree; per-level counts EMERGE from the cut --------------------
    d.step(
        "Evaluate by completing the square",
        requires="expert",
        prose=r"Complete the square ($x^2+x+1=(x+\tfrac12)^2+\tfrac34$), substitute $u=x+\tfrac12$ "
              r"(shifting the limits to $[\tfrac12,\infty)$), and integrate the resulting "
              r"$(u^2+\tfrac34)^{-5/2}$ form to get $14/27$.",
        math=[r"\int_{0}^{\infty}\frac{1+x}{(1+x+x^2)^{5/2}}\,dx"
              r"=\int_{1/2}^{\infty}\frac{u+\tfrac12}{(u^2+\tfrac34)^{5/2}}\,du=\frac{14}{27}"],
        references=["sub-method: complete_square_sub (this strategy)"],
        decompose=[
            dict(title="Complete the square in the quadratic", requires="working",
                 prose=r"Match $x^2+x+1$ to $a(x+\tfrac{b}{2a})^2+(c-\tfrac{b^2}{4a})$ with $a=b=c=1$: "
                       r"the shift is $\tfrac{b}{2a}=\tfrac12$ and the constant is $1-\tfrac14=\tfrac34$.",
                 math=[r"x^2+x+1=\Big(x+\tfrac12\Big)^2+\tfrac34"],
                 references=["base -> library/completing-the-square.md"],
                 decompose=[
                     dict(title="Read off a, b, c", requires="plain",
                          prose=r"The quadratic $x^2+x+1$ has $a=1,\ b=1,\ c=1$.",
                          math=[r"a=1,\quad b=1,\quad c=1"]),
                     dict(title="Form the shifted square", requires="plain",
                          prose=r"The shift is $\tfrac{b}{2a}=\tfrac12$; the left-over constant is "
                                r"$c-\tfrac{b^2}{4a}=1-\tfrac14=\tfrac34$.",
                          math=[r"\tfrac{b}{2a}=\tfrac12,\qquad c-\tfrac{b^2}{4a}=\tfrac34"],
                          references=["base -> library/completing-the-square.md"]),
                 ]),
            dict(title="Substitute u = x + 1/2 and shift the limits", requires="working",
                 prose=r"With $u=x+\tfrac12$ ($du=dx$): the denominator is $(u^2+\tfrac34)^{5/2}$, the "
                       r"numerator $1+x=u+\tfrac12$, and the limits $0,\infty$ become $\tfrac12,\infty$.",
                 math=[r"\int_{0}^{\infty}\!\frac{1+x}{(1+x+x^2)^{5/2}}dx"
                       r"=\int_{1/2}^{\infty}\!\frac{u+\tfrac12}{(u^2+\tfrac34)^{5/2}}du"],
                 references=["base -> library/u-substitution.md"],
                 decompose=[
                     dict(title="Rewrite the integrand in u", requires="plain",
                          prose=r"Replace $x$ by $u-\tfrac12$: the top $1+x$ becomes $u+\tfrac12$, the "
                                r"bottom becomes $(u^2+\tfrac34)^{5/2}$.",
                          math=[r"1+x=u+\tfrac12,\qquad 1+x+x^2=u^2+\tfrac34"]),
                     dict(title="Shift the integration limits", requires="plain",
                          prose=r"Since $u=x+\tfrac12$, when $x=0$, $u=\tfrac12$; when $x\to\infty$, "
                                r"$u\to\infty$.",
                          math=[r"x:0\to\infty\ \Longrightarrow\ u:\tfrac12\to\infty"]),
                 ]),
            dict(title="Integrate the standard form", requires="working",
                 prose=r"$(u+\tfrac12)(u^2+\tfrac34)^{-5/2}$ is a standard radical form: the $u$-part "
                       r"integrates by the power rule, the $\tfrac12$-part is the tabulated "
                       r"$\int(u^2+k)^{-5/2}du$. Evaluating at $[\tfrac12,\infty)$ gives $14/27$.",
                 math=[r"\int_{1/2}^{\infty}\frac{u+\tfrac12}{(u^2+\tfrac34)^{5/2}}\,du=\frac{14}{27}"],
                 references=["sub-method: direct(CAS) / strategies._direct (sp.integrate)"],
                 decompose=[
                     dict(title="Split into the u-part and the constant part", requires="plain",
                          prose=r"$\frac{u+\tfrac12}{(u^2+\tfrac34)^{5/2}}=\frac{u}{(u^2+\tfrac34)^{5/2}}"
                                r"+\frac{\tfrac12}{(u^2+\tfrac34)^{5/2}}$; the first is a derivative-over-its-root, "
                                r"the second a standard $(u^2+k)^{-5/2}$ table integral.",
                          math=[r"\frac{u}{(u^2+\tfrac34)^{5/2}}\ \text{(power rule)}\ +\ "
                                r"\frac{1}{2}\,\frac{1}{(u^2+\tfrac34)^{5/2}}\ \text{(table)}"],
                          references=["base -> library/standard-integrals.md"]),
                     dict(title="Evaluate at the shifted limits", requires="plain",
                          prose=r"Plugging the upper limit $\infty$ (everything $\to 0$) and the lower "
                                r"limit $\tfrac12$ into the antiderivative collapses to $14/27$.",
                          math=[r"\Big[\cdots\Big]_{1/2}^{\infty}=\frac{14}{27}"]),
                 ]),
        ])

    d.verify(
        r"Two independent checks: the symbolic engine returns the closed form $14/27$ via the "
        r"complete_square_sub -> direct(CAS) route, and high-precision quadrature of the original "
        r"integral agrees with $14/27$ to many digits.",
        math=[r"\int_{0}^{\infty}\frac{1+x}{(1+x+x^2)^{5/2}}\,dx=\frac{14}{27}=0.5185\ldots"],
        references=["engine: search route ['complete_square_sub','direct(CAS)']",
                    "numeric: mpmath quadrature of the original integral"])
    d.result(
        latex=r"\int_{0}^{\infty}\frac{1+x}{(1+x+x^2)^{5/2}}\,dx=\frac{14}{27}",
        note="completed the square (u=x+1/2), shifted the limits, integrated the standard "
             "(u^2+3/4)^(-5/2) form; verified symbolically and numerically.")
    return d
