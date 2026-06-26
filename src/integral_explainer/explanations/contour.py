"""Leveled Derivation for the CONTOUR method (rule 7 + rule 11 Definition of Done),
WORKED TARGET:  ∫_{-∞}^{∞} 1/(x^2+1) dx = π.

This mirrors the ACTUAL engine computation
  special_methods.contour_real_line(1/(x**2+1), x):
    1. substitute x->z, write f = num/den            (sp.together / sp.fraction)
    2. check deg(den) >= deg(num)+2  (the arc -> 0)   (sp.degree)
    3. poles with Im>0:  roots of den, keep upper-half (sp.roots, sp.im)
    4. residue at each upper pole                      (sp.residue)
    5. value = 2*pi*i * sum(residues)                  (sp.simplify)

The qualification tree is cut so the per-level step COUNTS EMERGE and DIFFER:
  - EXPERT chunks the whole evaluation into ONE node ("close in the UHP, sum residues").
  - WORKING sees that node's machinery sub-steps (arc vanishes / locate pole / residue /
    assemble 2*pi*i*Sum).
  - PLAIN decomposes those further into high-school-grokkable pieces, each bottoming out
    to a base library page (partial fractions, limits, geometric reasoning, arithmetic).

Sub-methods referenced: contour -> { residue theorem, Jordan/arc-vanishing lemma,
pole-finding (roots), residue-at-a-simple-pole formula }.

Run:  python scratch/expl_contour.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

import sympy as sp

HDR = r"\int_{-\infty}^{\infty}\frac{1}{x^{2}+1}\,dx"

def build_contour_derivation() -> Derivation:
    """A genuine why/how/step qualification tree for ∫ 1/(x^2+1) dx = π by residues."""
    problem = Problem(
        latex=HDR,
        represents="a rational integral over the whole real line (a Lorentzian / Cauchy density shape)",
        goal=Goal.EVALUATE,
        integral="real-line value of 1/(x^2+1)")
    d = Derivation(problem)

    # ---- WHY this approach (the recognition / decision) ----------------------
    d.why("Why this approach — close the contour and read off a residue",
          {"plain": r"The graph of $1/(x^{2}+1)$ is a smooth bump that dies away on both "
                    r"sides, so the area under it is a finite number. Instead of hunting an "
                    r"antiderivative, we lift the problem into the complex plane: the function "
                    r"blows up only at the special point where $x^{2}+1=0$, and a theorem says "
                    r"the whole integral is fixed by what happens right at that one point.",
           "working": r"$1/(x^{2}+1)$ is rational with the denominator's degree two above the "
                      r"numerator's, so the real integral converges and a big semicircular arc "
                      r"in the upper half-plane contributes nothing. The closed contour then "
                      r"equals $2\pi i$ times the residue at the single enclosed pole.",
           "expert": r"Rational integrand, $\deg(\text{den})=\deg(\text{num})+2$: the UHP arc "
                     r"vanishes, so $\int_{-\infty}^{\infty}=2\pi i\sum_{\operatorname{Im}>0}\operatorname{Res}$. "
                     r"The simple pole at $z=i$ carries the whole answer."},
          forced_by=r"the integrand is rational with no elementary real antiderivative worth "
                    r"chasing, yet it is meromorphic with a single pole in the upper half-plane "
                    r"and decays like $1/|z|^{2}$ — exactly the data the residue theorem consumes.",
          payoff=r"residues turn a global area into a single local computation at $z=i$; the "
                 r"$\pi$ falls out of $2\pi i\cdot(-i/2)$ as STRUCTURE (a half-residue of a "
                 r"Lorentzian), not a quadrature number that hides where it came from.",
          relies_on=r"$\deg(\text{den})\ge\deg(\text{num})+2$ so the arc integral $\to0$ "
                    r"(Jordan/ML estimate), and the pole at $z=i$ is simple — both hold here.")

    # ---- HOW the machinery works (the residue theorem) -----------------------
    d.how("How the approach works — the residue theorem on a closed semicircle",
          {"plain": r"Bend the real line up into a big half-circle in the complex plane so it "
                    r"forms a closed loop. A loop integral equals $2\pi i$ times the 'residue' "
                    r"(a local strength) at each blow-up point caught inside. The half-circle "
                    r"part adds nothing, so the real line alone equals that residue sum.",
           "working": r"Close $[-R,R]$ with the upper semicircle $C_R$. By Cauchy's residue "
                      r"theorem $\oint=2\pi i\sum\operatorname{Res}$ over enclosed poles. As "
                      r"$R\to\infty$ the arc $\int_{C_R}\to0$, leaving the real integral "
                      r"$=2\pi i\sum_{\operatorname{Im}>0}\operatorname{Res}$.",
           "expert": r"$\oint_{[-R,R]\cup C_R}f=2\pi i\sum_{\operatorname{Im}>0}\operatorname{Res}f$; "
                     r"$|f|=O(R^{-2})$ on $C_R$ gives arc $\to0$, so the principal value over "
                     r"$\mathbb{R}$ equals the enclosed residue sum."},
          math=[r"\oint_{[-R,R]\cup C_R}\frac{dz}{z^{2}+1}"
                r"=2\pi i\!\!\sum_{\operatorname{Im}(z_k)>0}\!\!\operatorname{Res}_{z=z_k}\frac{1}{z^{2}+1}"],
          references=["base method -> library/residue-theorem.md"])

    # ---- THE STEP: one expert node, decomposed for working, then plain -------
    # EXPERT grasps the whole evaluation as ONE move (requires="expert").
    d.step("Evaluate by closing in the upper half-plane and summing residues",
           requires="expert",
           prose=r"View $f(z)=1/(z^{2}+1)$; its only upper-half pole is the simple pole "
                 r"$z=i$ with residue $-i/2$, and the arc vanishes, so the real integral is "
                 r"$2\pi i\cdot(-\tfrac{i}{2})=\pi$.",
           math=[r"\int_{-\infty}^{\infty}\frac{dx}{x^{2}+1}"
                 r"=2\pi i\,\operatorname{Res}_{z=i}\frac{1}{z^{2}+1}"
                 r"=2\pi i\!\left(-\frac{i}{2}\right)=\pi"],
           references=["sub-method: residue theorem", "sub-method: arc-vanishing (ML/Jordan) lemma"],
           decompose=[
               # --- WORKING sub-step 1: the arc vanishes (the convergence licence) ---
               dict(title="The big semicircular arc contributes nothing", requires="working",
                    prose=r"On $C_R$ the integrand is $O(R^{-2})$ while the arc length is $\pi R$, "
                          r"so the arc integral is $O(R^{-1})\to0$ — this is what lets us close the contour.",
                    math=[r"\left|\int_{C_R}\frac{dz}{z^{2}+1}\right|\le\frac{\pi R}{R^{2}-1}"
                          r"\xrightarrow[R\to\infty]{}0"],
                    references=["sub-method: arc-vanishing (ML/Jordan) lemma"],
                    decompose=[
                        dict(title="Bound the size of the integrand on the arc", requires="plain",
                             prose=r"On the circle $|z|=R$, $|z^{2}+1|\ge|z|^{2}-1=R^{2}-1$, so "
                                   r"the integrand is at most $1/(R^{2}-1)$.",
                             math=[r"|z|=R\ \Rightarrow\ |z^{2}+1|\ge R^{2}-1\ \Rightarrow\ "
                                   r"\left|\frac{1}{z^{2}+1}\right|\le\frac{1}{R^{2}-1}"],
                             references=["base method -> library/triangle-inequality.md"]),
                        dict(title="Multiply by the arc length and take the limit", requires="plain",
                             prose=r"Size times length: $\dfrac{1}{R^{2}-1}\cdot\pi R\to0$ as $R$ grows, "
                                   r"because the bottom grows faster than the top.",
                             math=[r"\frac{1}{R^{2}-1}\cdot \pi R=\frac{\pi R}{R^{2}-1}\to0"],
                             references=["base method -> library/limits-at-infinity.md"]),
                    ]),
               # --- WORKING sub-step 2: locate the enclosed pole ---
               dict(title="Find the pole inside the contour", requires="working",
                    prose=r"The poles are the roots of $z^{2}+1=0$, namely $z=\pm i$; only "
                          r"$z=i$ has positive imaginary part, so only it is enclosed by the "
                          r"upper-half contour.",
                    math=[r"z^{2}+1=0\ \Rightarrow\ z=\pm i,\qquad \operatorname{Im}(i)=+1>0"],
                    references=["sub-method: pole-finding (roots of the denominator)"],
                    decompose=[
                        dict(title="Solve the denominator equal to zero", requires="plain",
                             prose=r"Set the bottom to zero. $z^{2}=-1$ has the two square roots "
                                   r"of $-1$, which are $i$ and $-i$.",
                             math=[r"z^{2}+1=0\ \Rightarrow\ z^{2}=-1\ \Rightarrow\ z=i\ \text{or}\ z=-i"],
                             references=["base method -> library/imaginary-unit.md"]),
                        dict(title="Keep only the upper-half root", requires="plain",
                             prose=r"The contour sits in the upper half-plane (imaginary part $>0$). "
                                   r"$i$ is up there; $-i$ is below, so we discard it.",
                             math=[r"\operatorname{Im}(i)=1>0,\quad \operatorname{Im}(-i)=-1<0"]),
                    ]),
               # --- WORKING sub-step 3: residue at the simple pole z = i ---
               dict(title="Compute the residue at z = i", requires="working",
                    prose=r"$z=i$ is a simple pole, so the residue is "
                          r"$\lim_{z\to i}(z-i)f(z)$; factoring $z^{2}+1=(z-i)(z+i)$ cancels "
                          r"the $(z-i)$ and leaves $1/(2i)=-i/2$.",
                    math=[r"\operatorname{Res}_{z=i}\frac{1}{z^{2}+1}"
                          r"=\lim_{z\to i}\frac{z-i}{(z-i)(z+i)}=\frac{1}{2i}=-\frac{i}{2}"],
                    references=["sub-method: residue-at-a-simple-pole formula"],
                    decompose=[
                        dict(title="Factor the denominator", requires="plain",
                             prose=r"A difference/sum of the roots: $z^{2}+1=(z-i)(z+i)$ — check by "
                                   r"expanding, $(z-i)(z+i)=z^{2}-i^{2}=z^{2}+1$.",
                             math=[r"z^{2}+1=(z-i)(z+i)"],
                             references=["base method -> library/factoring-quadratics.md"]),
                        dict(title="Cancel the (z - i) factor", requires="plain",
                             prose=r"The simple-pole residue multiplies by $(z-i)$ and lets $z\to i$; "
                                   r"the $(z-i)$ on top cancels the one on the bottom.",
                             math=[r"(z-i)\cdot\frac{1}{(z-i)(z+i)}=\frac{1}{z+i}"]),
                        dict(title="Substitute z = i and simplify 1/(2i)", requires="plain",
                             prose=r"Put $z=i$: the leftover is $1/(i+i)=1/(2i)$. Multiply top and "
                                   r"bottom by $i$ to clear the imaginary unit: $1/(2i)=-i/2$.",
                             math=[r"\frac{1}{z+i}\Big|_{z=i}=\frac{1}{2i}=\frac{1}{2i}\cdot\frac{i}{i}"
                                   r"=\frac{i}{2i^{2}}=-\frac{i}{2}"],
                             references=["base method -> library/dividing-by-i.md"]),
                    ]),
               # --- WORKING sub-step 4: assemble 2*pi*i * sum(residues) ---
               dict(title="Assemble:  2*pi*i times the residue sum", requires="working",
                    prose=r"The residue theorem multiplies the residue sum by $2\pi i$. With the "
                          r"single residue $-i/2$, the $i\cdot i=-1$ turns the imaginary factor "
                          r"real and gives $\pi$.",
                    math=[r"2\pi i\sum\operatorname{Res}=2\pi i\!\left(-\frac{i}{2}\right)"
                          r"=-\pi i^{2}=\pi"],
                    references=["sub-method: residue theorem"],
                    decompose=[
                        dict(title="Multiply the residue by 2*pi*i", requires="plain",
                             prose=r"There is just one residue, $-i/2$. Multiply it by $2\pi i$.",
                             math=[r"2\pi i\cdot\left(-\frac{i}{2}\right)=-\pi i\cdot i=-\pi i^{2}"]),
                        dict(title="Use i squared = -1", requires="plain",
                             prose=r"Since $i^{2}=-1$, the two minus signs cancel and the answer is "
                                   r"the real number $\pi$.",
                             math=[r"-\pi i^{2}=-\pi(-1)=\pi"],
                             references=["base method -> library/imaginary-unit.md"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) ---------------------
    d.verify(
        r"Two independent checks. The symbolic engine routine "
        r"`special_methods.contour_real_line(1/(x**2+1), x)` returns $\pi$ by exactly this "
        r"residue computation; and elementary calculus agrees, since "
        r"$\int 1/(x^{2}+1)\,dx=\arctan x$ and $\arctan(\infty)-\arctan(-\infty)=\pi$.",
        math=[r"\texttt{contour\_real\_line}(1/(x^{2}+1),x)=\pi",
              r"\big[\arctan x\big]_{-\infty}^{\infty}=\frac{\pi}{2}-\left(-\frac{\pi}{2}\right)=\pi"],
        references=["engine: special_methods.contour_real_line (sp.residue, upper-half-plane)",
                    "base method -> library/arctangent-integral.md",
                    "external gate: phys.libretexts.org Complex Methods (Chong) ch.09 Contour Integration"])
    d.result(latex=r"\int_{-\infty}^{\infty}\frac{dx}{x^{2}+1}=2\pi i\,\operatorname{Res}_{z=i}\frac{1}{z^{2}+1}=\pi",
             note="value DERIVED as 2*pi*i*(-i/2); cross-checked by the engine routine and by arctan.")
    return d
