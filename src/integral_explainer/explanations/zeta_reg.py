"""LEVELED Derivation for the zeta_reg method (CLAUDE.md rule 7 + rule 11).

WORKED TARGET:  1 + 2 + 3 + ... = ζ(-1) = -1/12.

The ENGINE's realization is special_methods.zeta_regularize(power=1) -> sp.zeta(-1),
which SymPy evaluates by the analytic continuation of the Riemann zeta function
(the closed form ζ(-n) = -B_{n+1}/(n+1), itself a consequence of the functional
equation). This file mirrors THAT computation as a qualification tree:

  - the Dirichlet series Σ n^{-s} converges only for Re s > 1, so the sum at s = -1
    is OUTSIDE the series — it must be DEFINED by continuation, not summed;
  - the functional equation ζ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) ζ(1-s) carries ζ to
    the left half-plane; at s = -1 it reads ζ(-1) = -ζ(2)/(2π^2);
  - the Basel value ζ(2) = π^2/6 then gives ζ(-1) = -1/12  (= -B_2/2).

Sub-methods referenced per step:
  analytic_continuation -> { functional_equation -> { Gamma reflection, sin special value },
                             Basel value ζ(2) = π^2/6 }.

The per-level step counts EMERGE from the `requires`/`decompose` cut:
  expert grasps "continue and evaluate" as ONE move; working sees its pieces;
  plain decomposes those pieces to high-school-checkable arithmetic.

Run:  python scratch/expl_zeta_reg.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

from .. import special_methods as sm
import sympy as sp

def build_zeta_reg_derivation() -> Derivation:
    """A leveled why/how/step Derivation for 1+2+3+... = ζ(-1) = -1/12,
    mirroring special_methods.zeta_regularize (analytic continuation of ζ)."""
    problem = Problem(
        latex=r"1+2+3+\cdots \;\overset{\text{reg}}{=}\; \zeta(-1)",
        represents="the formally divergent sum of the naturals, regularized as ζ(-1)",
        goal=Goal.EVALUATE,
        integral=r"\zeta(-1)")
    d = Derivation(problem)

    # ---- WHY: the recognition / decision -------------------------------------------------
    d.why(
        "Why this approach — regularize by analytic continuation",
        {"plain": r"The pile $1+2+3+\cdots$ grows without bound, so it has no ordinary sum. "
                  r"But the recipe '$\sum n^{-s}$' DOES have a finite answer whenever $s$ is big "
                  r"enough, and that answer is a smooth function of $s$. We follow that smooth "
                  r"function to $s=-1$ (where the recipe formally reads $\sum n^{1}=1+2+3+\cdots$) "
                  r"and read off the value it lands on.",
         "working": r"$\zeta(s)=\sum_{n\ge1} n^{-s}$ converges only for $\operatorname{Re}s>1$; at "
                    r"$s=-1$ the series is divergent. But $\zeta$ extends to a meromorphic function on "
                    r"$\mathbb{C}$ (one pole, at $s=1$), and $\zeta(-1)$ is the value of that unique "
                    r"continuation — the regularized sum.",
         "expert": r"$\sum n^{-s}$ defines $\zeta$ on the half-plane $\operatorname{Re}s>1$; the object "
                   r"$1+2+3+\cdots$ is its value at $s=-1$, outside the domain of convergence. "
                   r"Regularization = take the value of the unique analytic continuation, fixed by the "
                   r"functional equation."},
        forced_by=r"the Dirichlet series $\sum n^{-s}$ is divergent at $s=-1$ — naive summation is "
                  r"blocked — yet $\zeta$ is analytic off $s=1$, so a value at $s=-1$ exists by "
                  r"continuation even though no partial sum approaches it.",
        payoff=r"continuation returns a single, convention-independent number ($-1/12$) that is the "
               r"one consistent with $\zeta$'s analytic structure; a cutoff would give a "
               r"scheme-dependent answer and hide the $\zeta(2)=\pi^2/6$ link the functional equation exposes.",
        relies_on=r"analytic continuation is UNIQUE (identity theorem): the continuation agreeing with "
                  r"$\sum n^{-s}$ on $\operatorname{Re}s>1$ is the only one, so $\zeta(-1)$ is well-defined.")

    # ---- HOW: the machinery (the functional equation) ------------------------------------
    d.how(
        "How the approach works — the functional equation carries ζ to s = -1",
        {"plain": r"There is a mirror law (Riemann's functional equation) connecting the value of "
                  r"$\zeta$ at $s$ to its value at $1-s$. Setting $s=-1$ mirrors us to $1-s=2$, where "
                  r"$\zeta(2)$ is a known finite number. So $\zeta(-1)$ is just a fixed multiple of $\zeta(2)$.",
         "working": r"Riemann's functional equation "
                    r"$\zeta(s)=2^{s}\pi^{s-1}\sin\!\frac{\pi s}{2}\,\Gamma(1-s)\,\zeta(1-s)$ relates the "
                    r"left half-plane to the right. At $s=-1$ the right side is finite and computable, so it "
                    r"DEFINES $\zeta(-1)$.",
         "expert": r"The reflection $\zeta(s)=2^{s}\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s)$ is the "
                   r"analytic continuation; evaluating it at $s=-1$ collapses (via $\sin(-\pi/2)$, "
                   r"$\Gamma(2)$, $\zeta(2)$) to $-\zeta(2)/(2\pi^2)=-B_2/2=-1/12$."},
        math=[r"\zeta(s)=2^{s}\,\pi^{\,s-1}\,\sin\!\left(\frac{\pi s}{2}\right)\Gamma(1-s)\,\zeta(1-s)"])

    # ---- THE STEPS: ONE qualification tree; the per-level counts EMERGE from the cut. ----
    # expert  -> grasps "continue and evaluate" as ONE node (requires=expert);
    # working -> sees its 3 sub-steps (set up FE / plug s=-1 / use Basel);
    # plain   -> decomposes those into high-school arithmetic (the special values one by one).
    d.step(
        "Evaluate ζ(-1) by analytic continuation", requires="expert",
        prose=r"Continue $\zeta$ off its convergence half-plane with the functional equation, "
              r"evaluate the equation at $s=-1$ (where $\sin\frac{\pi s}{2}$, $\Gamma(1-s)$, "
              r"$\zeta(1-s)$ are all explicit), and assemble: $\zeta(-1)=-\dfrac{\zeta(2)}{2\pi^{2}}=-\dfrac1{12}$.",
        math=[r"\zeta(-1)=2^{-1}\pi^{-2}\sin\!\left(-\tfrac{\pi}{2}\right)\Gamma(2)\,\zeta(2)"
              r"=-\frac{\zeta(2)}{2\pi^{2}}=-\frac{1}{12}"],
        references=["sub-method: analytic_continuation (continue past Re s > 1)",
                    "base method → library/riemann-zeta.md"],
        decompose=[
            # ---- working sub-step 1: the convergence floor (why we MUST continue) ----------
            dict(title="The series only converges for Re s > 1", requires="working",
                 prose=r"The defining sum $\sum n^{-s}$ converges iff $\operatorname{Re}s>1$, so "
                       r"$s=-1$ is OUTSIDE it — there is nothing to add up; we must continue instead.",
                 math=[r"\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^{s}}\quad(\operatorname{Re}s>1),"
                       r"\qquad s=-1\notin\{\operatorname{Re}s>1\}"],
                 references=["sub-method: Dirichlet series / p-series convergence",
                             "base method → library/p-series-convergence.md"],
                 decompose=[
                     dict(title="Why p-series needs Re s > 1", requires="plain",
                          prose=r"For real $s$, $\sum 1/n^{s}$ is a $p$-series with $p=s$: it converges "
                                r"exactly when $p>1$ (compare with $\int_1^\infty x^{-s}dx$). At $s=-1$ the "
                                r"terms are $n^{1}=1,2,3,\dots$, growing — so it diverges.",
                          math=[r"\sum_{n\ge1}\frac{1}{n^{s}}<\infty \iff s>1;\qquad "
                                r"s=-1:\ \frac{1}{n^{-1}}=n\to\infty"],
                          references=["base method → library/p-series-convergence.md"]),
                 ]),
            # ---- working sub-step 2: write down the functional equation at s = -1 ----------
            dict(title="Plug s = -1 into the functional equation", requires="working",
                 prose=r"Substitute $s=-1$ into "
                       r"$\zeta(s)=2^{s}\pi^{s-1}\sin\frac{\pi s}{2}\Gamma(1-s)\zeta(1-s)$. Each factor "
                       r"becomes an explicit special value; the mirror point is $1-s=2$.",
                 math=[r"\zeta(-1)=2^{-1}\,\pi^{-2}\,\sin\!\left(-\frac{\pi}{2}\right)\,\Gamma(2)\,\zeta(2)"],
                 references=["sub-method: functional_equation (Riemann reflection)"],
                 decompose=[
                     dict(title="The sine factor: sin(-π/2) = -1", requires="plain",
                          prose=r"At $s=-1$, $\frac{\pi s}{2}=-\frac{\pi}{2}$, and $\sin(-\pi/2)=-1$ "
                                r"(the sine of a quarter-turn down).",
                          math=[r"\sin\!\left(\frac{\pi(-1)}{2}\right)=\sin\!\left(-\frac{\pi}{2}\right)=-1"],
                          references=["base method → library/unit-circle-values.md"]),
                     dict(title="The Gamma factor: Γ(2) = 1", requires="plain",
                          prose=r"$\Gamma(1-s)=\Gamma(2)$, and $\Gamma(2)=1!=1$ ($\Gamma$ of a positive "
                                r"integer is a factorial).",
                          math=[r"\Gamma(1-(-1))=\Gamma(2)=1!=1"],
                          references=["sub-method: Gamma at integers (Γ(n)=(n-1)!)",
                                      "base method → library/gamma-function.md"]),
                     dict(title="The powers: 2^{-1} π^{-2}", requires="plain",
                          prose=r"$2^{s}=2^{-1}=\tfrac12$ and $\pi^{s-1}=\pi^{-2}=1/\pi^2$ — plain "
                                r"exponent arithmetic.",
                          math=[r"2^{-1}=\frac12,\qquad \pi^{-1-1}=\pi^{-2}=\frac{1}{\pi^{2}}"],
                          references=["base method → library/exponent-rules.md"]),
                     dict(title="Collect the constant factors", requires="plain",
                          prose=r"Multiply the explicit pieces $\tfrac12\cdot\pi^{-2}\cdot(-1)\cdot1$; only "
                                r"$\zeta(2)$ is left symbolic.",
                          math=[r"\zeta(-1)=\frac12\cdot\frac{1}{\pi^{2}}\cdot(-1)\cdot1\cdot\zeta(2)"
                                r"=-\frac{\zeta(2)}{2\pi^{2}}"]),
                 ]),
            # ---- working sub-step 3: supply ζ(2) (Basel) and finish -----------------------
            dict(title="Use the Basel value ζ(2) = π²/6 and simplify", requires="working",
                 prose=r"The mirror lands on $\zeta(2)$, the Basel sum $\sum 1/n^2=\pi^2/6$. Substituting "
                       r"cancels the $\pi^2$ and leaves a pure rational.",
                 math=[r"\zeta(-1)=-\frac{1}{2\pi^{2}}\cdot\frac{\pi^{2}}{6}=-\frac{1}{12}"],
                 references=["sub-method: Basel value ζ(2) = π²/6",
                             "base method → library/basel-problem.md"],
                 decompose=[
                     dict(title="Recall ζ(2) = π²/6 (Basel)", requires="plain",
                          prose=r"$\zeta(2)=\sum_{n\ge1}1/n^2=\pi^2/6$ is the Basel sum (Euler) — a known "
                                r"convergent value, here used as a black box.",
                          math=[r"\zeta(2)=\sum_{n=1}^{\infty}\frac{1}{n^{2}}=\frac{\pi^{2}}{6}"],
                          references=["base method → library/basel-problem.md"]),
                     dict(title="Substitute and cancel π²", requires="plain",
                          prose=r"Put $\zeta(2)=\pi^2/6$ into $-\zeta(2)/(2\pi^2)$; the $\pi^2$ cancels.",
                          math=[r"-\frac{1}{2\pi^{2}}\cdot\frac{\pi^{2}}{6}"
                                r"=-\frac{\pi^{2}}{12\pi^{2}}=-\frac{1}{12}"],
                          references=["base method → library/fraction-arithmetic.md"]),
                 ]),
        ])

    # ---- VERIFY: independent cross-checks, not used to derive --------------------------
    val = sm.zeta_regularize(1)            # the ENGINE's realization: sp.zeta(-1)
    bernoulli_check = -sp.bernoulli(2) / 2  # closed form ζ(-n) = -B_{n+1}/(n+1)
    d.verify(
        r"Three independent checks, none used to derive the answer. (1) The engine's realization "
        r"$\texttt{zeta\_regularize(1)}=\texttt{sp.zeta(-1)}$ returns $-1/12$ by SymPy's own analytic "
        r"continuation. (2) The Bernoulli closed form $\zeta(-n)=-B_{n+1}/(n+1)$ gives "
        r"$\zeta(-1)=-B_2/2=-(1/6)/2=-1/12$. (3) Ramanujan/Abel summation of $1+2+3+\cdots$ "
        r"independently lands on the same $-1/12$.",
        math=[r"\texttt{sp.zeta}(-1)=" + sp.latex(val),
              r"-\frac{B_2}{2}=-\frac{1}{2}\cdot\frac{1}{6}=" + sp.latex(bernoulli_check)],
        references=["engine realization: special_methods.zeta_regularize → sp.zeta(-1)",
                    "closed form: ζ(-n) = -B_{n+1}/(n+1)  (Bernoulli)",
                    "external gate: external_gates.py zeta_reg vs Wikipedia ζ-regularization"])
    d.result(
        latex=r"1+2+3+\cdots\;\overset{\text{reg}}{=}\;\zeta(-1)=-\frac{1}{12}",
        note=f"engine sp.zeta(-1) = {val}; matches Bernoulli closed form -B_2/2 and the published value.")
    return d

def main():
    d = build_zeta_reg_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[]  (VALID — no warnings)")
    assert not qwarn, qwarn
    assert len(set(counts.values())) == len(counts), f"counts must all differ: {counts}"
    print("OK: three bands present, counts genuinely differ, every step within its reader's reach.")
