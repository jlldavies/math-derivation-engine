r"""LEVELED Derivation for METHOD casimir (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.su2_casimir. The engine DERIVES the su(2) quadratic Casimir
    J^2 |j,j> = j(j+1) |j,j>   (hbar=1)
by rewriting J^2 = J_- J_+ + J_z^2 + hbar J_z and acting on the highest-weight state (J_+|j,j>=0),
the eigenvalue computed by sympy's spin algebra (qapply), nothing written in. The SAME highest-weight
argument yields the conformal Casimir Delta(Delta-d) (arXiv:2606.24382 / 24285).

Sub-methods referenced by the steps:
    casimir -> { ladder operators J_pm and [J_+,J_-]=2 hbar J_z, highest-weight annihilation,
                 Casimir commutes with all generators (constant on an irrep) }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"J^{2}=J_-J_++J_z^{2}+\hbar J_z,\quad J_+\lvert j,j\rangle=0\ \Rightarrow\ "
       r"J^{2}\lvert j,j\rangle=\hbar^{2}j(j+1)\lvert j,j\rangle")


def build_casimir_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the quadratic Casimir $J^2$ of $su(2)$ (angular momentum) on the spin-$j$ irrep — "
                   r"the invariant labelling a representation",
        goal=Goal.SIMPLIFY,
        integral="su(2) quadratic Casimir eigenvalue j(j+1) by the highest-weight method")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — evaluate the invariant on the easiest state of the multiplet",
          {"plain": r"$J^2=J_x^2+J_y^2+J_z^2$ has the SAME value on every state of a spin-$j$ multiplet "
                    r"(it's the thing that labels the multiplet). So to find that value we pick the easiest "
                    r"state — the top one $\lvert j,j\rangle$ — where the raising operator gives nothing.",
           "working": r"$J^2$ commutes with $J_x,J_y,J_z$, so by Schur it is a constant on the irrep. Evaluate the "
                      r"constant on the highest weight $\lvert j,j\rangle$, using ladder operators to kill the "
                      r"awkward $J_x^2+J_y^2$ part.",
           "expert": r"$[J^2,J_i]=0\Rightarrow J^2=\lambda\,\mathbb{1}$ on the irrep; $\lambda$ is read off the "
                     r"highest weight via $J^2=J_-J_++J_z^2+\hbar J_z$ and $J_+\lvert j,j\rangle=0$."},
          forced_by=r"$J^2$ commutes with all generators, so it is a single scalar on the whole irrep — and the "
                    r"highest-weight state, annihilated by $J_+$, makes that scalar trivial to read off.",
          payoff=r"the exact label $j(j+1)$ (not a numeric eigenvalue of one matrix) — the invariant that classifies "
                 r"the representation; the IDENTICAL argument gives the conformal $\Delta(\Delta-d)$.",
          relies_on=r"the ladder algebra $[J_z,J_\pm]=\pm\hbar J_\pm$, $[J_+,J_-]=2\hbar J_z$, and the existence of a "
                    r"highest weight with $J_+\lvert j,j\rangle=0$, $J_z\lvert j,j\rangle=\hbar j\lvert j,j\rangle$.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — rewrite J^2 in ladder form, then hit the highest weight",
          {"plain": r"Swap $J_x,J_y$ for the raising/lowering combos $J_\pm=J_x\pm iJ_y$. Then "
                    r"$J^2=J_-J_++J_z^2+\hbar J_z$. On the top state $J_+$ gives $0$ and $J_z$ gives $j$, so only "
                    r"$J_z^2+\hbar J_z\to j^2+j$ survives.",
           "working": r"$J_x^2+J_y^2=\tfrac12(J_+J_-+J_-J_+)$ and $[J_+,J_-]=2\hbar J_z$ give "
                      r"$J^2=J_-J_++J_z^2+\hbar J_z$; acting on $\lvert j,j\rangle$ leaves $\hbar^2(j^2+j)$.",
           "expert": r"$J^2=J_-J_++J_z(J_z+\hbar)$; $J_+\lvert j,j\rangle=0$ and $J_z\lvert j,j\rangle=\hbar j\lvert j,j\rangle$ "
                     r"give the eigenvalue $\hbar^2 j(j+1)$."},
          math=[r"J_\pm=J_x\pm iJ_y,\quad [J_+,J_-]=2\hbar J_z,\quad J^2=J_-J_++J_z^2+\hbar J_z"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Read the Casimir off the highest weight", requires="expert",
           prose=r"Rewrite $J^2=J_-J_++J_z^2+\hbar J_z$ and act on $\lvert j,j\rangle$: $J_-J_+$ dies, "
                 r"$J_z^2+\hbar J_z\to\hbar^2(j^2+j)$, so $J^2\lvert j,j\rangle=\hbar^2 j(j+1)\lvert j,j\rangle$.",
           math=[r"J^{2}\lvert j,j\rangle=\hbar^{2}j(j+1)\lvert j,j\rangle\ \xrightarrow{\hbar=1}\ j(j+1)"],
           references=["sub-method: casimir -> {ladder operators, highest-weight annihilation, Schur (constant on irrep)}"],
           decompose=[
               dict(title="Rewrite J^2 with ladder operators", requires="working",
                    prose=r"Replace $J_x^2+J_y^2=\tfrac12(J_+J_-+J_-J_+)$ and use $[J_+,J_-]=2\hbar J_z$ to normal-order.",
                    math=[r"J^2=J_x^2+J_y^2+J_z^2=\tfrac12(J_+J_-+J_-J_+)+J_z^2=J_-J_++J_z^2+\hbar J_z"],
                    references=["sub-method: ladder operators [J_+,J_-]=2 hbar J_z"],
                    decompose=[
                        dict(title="Define the raising/lowering operators", requires="plain",
                             prose=r"$J_\pm=J_x\pm iJ_y$ invert to $J_x^2+J_y^2=\tfrac12(J_+J_-+J_-J_+)$.",
                             math=[r"J_x^2+J_y^2=\tfrac12\big(J_+J_-+J_-J_+\big)"]),
                        dict(title="Normal-order with the commutator", requires="plain",
                             prose=r"$\tfrac12(J_+J_-+J_-J_+)=J_-J_++\tfrac12[J_+,J_-]=J_-J_++\hbar J_z$.",
                             math=[r"\tfrac12(J_+J_-+J_-J_+)=J_-J_++\hbar J_z"]),
                    ]),
               dict(title="Act on the highest-weight state", requires="working",
                    prose=r"$J_+\lvert j,j\rangle=0$ (nothing above the top), so $J_-J_+\lvert j,j\rangle=0$; "
                          r"$J_z\lvert j,j\rangle=\hbar j\lvert j,j\rangle$.",
                    math=[r"J_+\lvert j,j\rangle=0,\qquad J_z\lvert j,j\rangle=\hbar j\,\lvert j,j\rangle"],
                    references=["sub-method: highest-weight annihilation"],
                    decompose=[
                        dict(title="Why J_+ annihilates the top state", requires="plain",
                             prose=r"$J_+$ raises $m$ by 1, but $m=j$ is already the maximum, so the result is 0.",
                             math=[r"J_+\lvert j,m\rangle\propto\lvert j,m+1\rangle,\quad m=j\Rightarrow 0"]),
                        dict(title="J_z eigenvalue at the top", requires="plain",
                             prose=r"The top state has $m=j$, so $J_z\lvert j,j\rangle=\hbar j\lvert j,j\rangle$.",
                             math=[r"J_z\lvert j,j\rangle=\hbar j\lvert j,j\rangle"]),
                    ]),
               dict(title="Collect j(j+1)", requires="plain",
                    prose=r"Only $J_z^2+\hbar J_z$ acts: $\hbar^2 j^2+\hbar^2 j=\hbar^2 j(j+1)$ (factor $j^2+j$). Set $\hbar=1$.",
                    math=[r"(J_z^2+\hbar J_z)\lvert j,j\rangle=\hbar^2(j^2+j)\lvert j,j\rangle=\hbar^2 j(j+1)\lvert j,j\rangle"],
                    references=["base method -> library/factoring.md"]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `su2_casimir` computes $J^2\lvert j,j\rangle$ with sympy's spin algebra (qapply) and "
        r"returns $j(j+1)$ for symbolic $j$ (and $3/4,2,15/4,\dots$ for $j=\tfrac12,1,\tfrac32$) — matching the "
        r"textbook angular-momentum Casimir; nothing is written in.",
        math=[r"J^2\lvert j,j\rangle=j(j+1)\lvert j,j\rangle\quad(\hbar=1)",
              r"j=\tfrac12\!:\tfrac34,\quad j=1\!:2,\quad j=\tfrac32\!:\tfrac{15}{4}"],
        references=["engine: special_methods.su2_casimir (sympy.physics.quantum.spin, qapply)",
                    "Wikipedia, Angular momentum operator — Casimir J^2=j(j+1) (independent)",
                    "arXiv:2606.24382/24285 — same highest-weight method for conformal Delta(Delta-d)"])
    d.result(
        latex=r"J^{2}\lvert j,j\rangle=j(j+1)\lvert j,j\rangle\qquad(\hbar=1)",
        note="eigenvalue derived by the highest-weight/ladder method (qapply-computed, nothing written in); "
             "opens the representation-theory Casimir track — the same argument gives conformal Delta(Delta-d).")
    return d
