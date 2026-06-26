r"""LEVELED Derivation for METHOD dilogarithm (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.dilogarithm_reflection. The engine DERIVES Euler's reflection
    Li_2(z) + Li_2(1-z) = pi^2/6 - log(z) log(1-z)
by matching derivatives (d/dz Li_2(z) = -log(1-z)/z) and fixing the constant at z->1, where it
emerges as Li_2(1)=pi^2/6 — nothing written in. Specialising at z=1/2 gives 2 Li_2(1/2)=pi^2/6-log^2 2.

Sub-methods referenced by the steps:
    dilogarithm -> { derivative of Li_2 (series/integral definition), constant-of-integration
                     fixed at an endpoint, special value Li_2(1)=pi^2/6 (Basel) }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)=\frac{\pi^{2}}{6}-\log(z)\log(1-z)")


def build_dilogarithm_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the dilogarithm $\mathrm{Li}_2(z)=\sum_{n\ge1}z^n/n^2$ and its reflection "
                   r"functional equation (used to evaluate WKB / saddle-point actions built from $\mathrm{Li}_2$)",
        goal=Goal.SIMPLIFY,
        integral="Euler reflection identity for the dilogarithm Li_2")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — relate the two dilogs by calculus, don't sum the series",
          {"plain": r"The dilogarithm $\mathrm{Li}_2(z)=z+\tfrac{z^2}{4}+\tfrac{z^3}{9}+\cdots$ has no neat "
                    r"elementary value at a general $z$. But its slope is simple, so instead of summing the "
                    r"series we compare the SLOPES of the two sides of the claimed identity: if they match "
                    r"and the two sides agree at one easy point, the identity holds everywhere.",
           "working": r"$\mathrm{Li}_2$ is non-elementary, but $\tfrac{d}{dz}\mathrm{Li}_2(z)=-\tfrac{\log(1-z)}{z}$ "
                      r"is elementary. So differentiate the proposed identity: if both sides share a derivative "
                      r"they differ by a constant, fixed by one endpoint value.",
           "expert": r"From $\mathrm{Li}_2'(z)=-\log(1-z)/z$, the reflection identity is a one-line calculus "
                     r"argument: $\partial_z[\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)]=-\log(1-z)/z+\log z/(1-z)=\partial_z[-\log z\log(1-z)]$, "
                     r"so the two differ by a constant fixed at $z\to1$ by $\mathrm{Li}_2(1)=\zeta(2)=\pi^2/6$."},
          forced_by=r"$\mathrm{Li}_2$ has no elementary closed form, but its DERIVATIVE $-\log(1-z)/z$ is "
                    r"elementary — so a functional equation is provable by differentiation rather than summation.",
          payoff=r"gives exact relations between dilog values (and, at $z=\tfrac12$, the closed value "
                 r"$\mathrm{Li}_2(\tfrac12)=\tfrac{\pi^2}{12}-\tfrac12\log^2 2$); a numeric value would hide the "
                 r"functional structure that collapses WKB/saddle-point actions.",
          relies_on=r"the principal branch on $0<z<1$ (so $\log z,\log(1-z)$ are real) and the Basel value "
                    r"$\mathrm{Li}_2(1)=\pi^2/6$ to fix the constant.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — equal derivatives, then fix the constant at an endpoint",
          {"plain": r"Two facts: the slope of $\mathrm{Li}_2(z)$ is $-\log(1-z)/z$; and at $z=1$, "
                    r"$\mathrm{Li}_2(1)=\pi^2/6$ (the Basel sum $1+\tfrac14+\tfrac19+\cdots$). Differentiate both "
                    r"sides, see they match, then plug $z=1$ to pin the leftover constant.",
           "working": r"Differentiate $f(z)=\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)+\log z\log(1-z)$; every term's "
                      r"derivative cancels, so $f$ is constant. Evaluate at $z\to1$: $f=\mathrm{Li}_2(1)=\pi^2/6$.",
           "expert": r"$\mathrm{Li}_2'(z)=-\log(1-z)/z$ and the chain rule give $f'(z)\equiv0$; the constant is "
                     r"$\lim_{z\to1}f(z)=\mathrm{Li}_2(1)=\pi^2/6$."},
          math=[r"\frac{d}{dz}\mathrm{Li}_2(z)=-\frac{\log(1-z)}{z},\qquad \mathrm{Li}_2(1)=\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}{6}"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Prove the reflection identity by differentiation + endpoint", requires="expert",
           prose=r"Show $\partial_z[\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)]=\partial_z[-\log z\log(1-z)]$, so the two "
                 r"sides differ by a constant; fix it at $z\to1$ as $\mathrm{Li}_2(1)=\pi^2/6$.",
           math=[r"\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)=\frac{\pi^2}{6}-\log(z)\log(1-z)"],
           references=["sub-method: dilogarithm -> {Li_2 derivative, endpoint constant, Basel value Li_2(1)=pi^2/6}"],
           decompose=[
               dict(title="Differentiate the two dilogarithms", requires="working",
                    prose=r"Use $\mathrm{Li}_2'(u)=-\log(1-u)/u$ with the chain rule on $\mathrm{Li}_2(1-z)$.",
                    math=[r"\frac{d}{dz}\mathrm{Li}_2(z)=-\frac{\log(1-z)}{z},\quad "
                          r"\frac{d}{dz}\mathrm{Li}_2(1-z)=+\frac{\log z}{1-z}"],
                    references=["sub-method: derivative of Li_2"],
                    decompose=[
                        dict(title="The slope of Li_2 from its series", requires="plain",
                             prose=r"Differentiating $\sum z^n/n^2$ termwise gives $\sum z^{n-1}/n=-\log(1-z)/z$.",
                             math=[r"\frac{d}{dz}\sum_{n\ge1}\frac{z^n}{n^2}=\sum_{n\ge1}\frac{z^{n-1}}{n}=-\frac{\log(1-z)}{z}"]),
                        dict(title="Chain rule on Li_2(1-z)", requires="plain",
                             prose=r"With $u=1-z$, $\tfrac{d}{dz}\mathrm{Li}_2(u)=\mathrm{Li}_2'(u)\cdot(-1)=\tfrac{\log z}{1-z}$.",
                             math=[r"\frac{d}{dz}\mathrm{Li}_2(1-z)=-\Big(-\frac{\log(1-(1-z))}{1-z}\Big)=\frac{\log z}{1-z}"]),
                    ]),
               dict(title="Differentiate the RHS and match", requires="working",
                    prose=r"$\tfrac{d}{dz}[-\log z\log(1-z)]=-\tfrac{\log(1-z)}{z}+\tfrac{\log z}{1-z}$ — exactly the "
                          r"sum of the two dilog derivatives. So both sides have the same slope.",
                    math=[r"\frac{d}{dz}\big[-\log z\log(1-z)\big]=-\frac{\log(1-z)}{z}+\frac{\log z}{1-z}"],
                    references=["base method -> library/product-rule.md"],
                    decompose=[
                        dict(title="Product rule on -log z log(1-z)", requires="plain",
                             prose=r"$-(\tfrac1z\log(1-z)+\log z\cdot\tfrac{-1}{1-z})$ — product rule, then tidy signs.",
                             math=[r"-\Big(\frac{\log(1-z)}{z}-\frac{\log z}{1-z}\Big)"]),
                        dict(title="Compare with the dilog derivatives", requires="plain",
                             prose=r"Term for term this equals $\mathrm{Li}_2'(z)+\tfrac{d}{dz}\mathrm{Li}_2(1-z)$, so the difference is constant.",
                             math=[r"\partial_z\big[\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)+\log z\log(1-z)\big]=0"]),
                    ]),
               dict(title="Fix the constant at z->1 (and read off z=1/2)", requires="working",
                    prose=r"A zero derivative means a constant; evaluate at $z\to1$: $\mathrm{Li}_2(1)+\mathrm{Li}_2(0)+0=\pi^2/6$. "
                          r"Setting $z=\tfrac12$ then gives $2\,\mathrm{Li}_2(\tfrac12)=\tfrac{\pi^2}{6}-\log^2 2$.",
                    math=[r"\text{const}=\mathrm{Li}_2(1)=\frac{\pi^2}{6};\qquad \mathrm{Li}_2(\tfrac12)=\frac{\pi^2}{12}-\frac12\log^2 2"],
                    references=["sub-method: Basel value Li_2(1)=pi^2/6"],
                    decompose=[
                        dict(title="Why Li_2(1)=pi^2/6", requires="plain",
                             prose=r"$\mathrm{Li}_2(1)=\sum 1/n^2$ is the Basel sum, equal to $\pi^2/6$.",
                             math=[r"\mathrm{Li}_2(1)=\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}{6}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `dilogarithm_reflection` REGENERATES $\pi^2/6-\log z\log(1-z)$ by the derivative match "
        r"(constant $\pi^2/6$ emerging from $\mathrm{Li}_2(1)$, nothing written in), matching DLMF 25.12.4; and a "
        r"numeric spot-check at $z=\tfrac12$ confirms $2\,\mathrm{Li}_2(\tfrac12)=\pi^2/6-\log^2 2$.",
        math=[r"\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)=\frac{\pi^2}{6}-\log z\log(1-z)\quad(\text{DLMF 25.12.4})",
              r"2\,\mathrm{Li}_2(\tfrac12)=\frac{\pi^2}{6}-\log^2 2"],
        references=["engine: special_methods.dilogarithm_reflection (derivative match + endpoint constant)",
                    "DLMF 25.12.4 — independent published reflection identity",
                    "arXiv:2606.24497 — Kashaev action built from Li_2"])
    d.result(
        latex=r"\mathrm{Li}_2(z)+\mathrm{Li}_2(1-z)=\frac{\pi^{2}}{6}-\log(z)\log(1-z),\qquad "
              r"\mathrm{Li}_2(\tfrac12)=\frac{\pi^2}{12}-\frac12\log^2 2",
        note="reflection derived by differentiation + endpoint (pi^2/6 from Li_2(1), nothing written in); "
             "opens the dilogarithm / special-function track used across the QFT corpus.")
    return d
