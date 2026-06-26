"""Leveled Derivation for the sym_antisym identity  S_ij A_ij = 0  (CLAUDE.md rule 7 + 11).

REALIZATION mirrored: special_methods.SYM_ANTISYM — the IDENTITY search edge
`_contract_to_zero` builds a symmetric S (S_ij=S_ji) and an antisymmetric A (A_ij=-A_ji)
on n indices, forms the double sum  sum_{i,j} S_ij A_ij, and `sp.expand` collapses it to 0;
the is_zero goal then settles the state. The MATHEMATICAL engine of that collapse is index
relabelling:  X = S_ij A_ij = S_ji A_ji  (rename dummies i<->j)  = S_ij(-A_ij) = -X, so 2X=0.

This file is local scratch only (rule 1: no src edits, no sync). Run:
    python scratch/expl_sym_antisym.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

from .. import special_methods as sm
import sympy as sp

HDR = r"S_{ij}\,A_{ij}\;=\;\sum_{i,j} S_{ij}A_{ij}\;=\;0"

def build_sym_antisym_derivation() -> "Derivation":
    """A genuine why/how/step qualification tree for  S_ij A_ij = 0.

    The cut (`requires` + nested `decompose`) makes the per-level step counts EMERGE and
    DIFFER:  expert sees ONE move ("relabel and it folds to 0"); working sees its 3 sub-moves
    (rename the dummies, push antisymmetry through, solve 2X=0); plain decomposes those into
    high-school pieces (what a dummy sum is, what sym/antisym mean on the n=3 grid, the chain
    rename -> sign -> the equation 2X=0 -> divide by 2).
    """
    problem = Problem(
        latex=HDR,
        represents=r"double contraction of a symmetric tensor $S_{ij}=S_{ji}$ with an "
                   r"antisymmetric tensor $A_{ij}=-A_{ji}$ (e.g. a stress tensor against a "
                   r"rotation/curl tensor); summation over repeated $i,j$",
        goal=Goal.PROVE,
        integral="S_ij A_ij = 0  (sym x antisym contraction vanishes)")
    d = Derivation(problem)

    # ---- WHY: the recognition / decision (not a 'step') ------------------------------------
    d.why("Why this approach — exploit the clashing symmetries, do not expand",
          {"plain": r"$S$ is symmetric (swapping the two labels changes nothing) and $A$ is "
                    r"antisymmetric (swapping the two labels flips the sign). The sum "
                    r"$\sum_{i,j} S_{ij}A_{ij}$ runs over every pair. The smart move is NOT to "
                    r"add up all the terms, but to notice that renaming the summation labels "
                    r"must give the same total — yet the symmetries force that 'same total' to "
                    r"equal its own negative, so it can only be $0$.",
           "working": r"The contraction $S_{ij}A_{ij}$ is a scalar (all indices summed). Rather "
                      r"than evaluate $n^2$ products, relabel the dummy indices $i\leftrightarrow j$: "
                      r"the value is unchanged, but $S$'s symmetry and $A$'s antisymmetry turn the "
                      r"relabelled sum into the negative of the original. A quantity equal to minus "
                      r"itself is zero — independent of $n$ and of the entries.",
           "expert": r"$S_{(ij)}A_{[ij]}$: a full symmetric/antisymmetric index contraction "
                     r"vanishes identically. The symmetric part of $A$ and the antisymmetric part "
                     r"of $S$ are both zero, so $S_{ij}A_{ij}=S_{(ij)}A_{[ij]}=0$; the one-line "
                     r"realization is the dummy swap $i\leftrightarrow j$."},
          forced_by=r"the two tensors carry OPPOSITE symmetry under the same index swap "
                    r"($S_{ij}=S_{ji}$, $A_{ij}=-A_{ji}$) — the structural clash, not the numeric "
                    r"entries, is what kills the sum. Expanding the $n^2$ terms would hide that.",
          payoff=r"the relabelling proof is one line and holds for EVERY $n$ and every such "
                 r"$S,A$ (the engine's $n{=}3$ `sp.expand`$\to 0$ is just a witness, not the "
                 r"reason); the entry-by-entry cancellation is a number that destroys the structure.",
          relies_on=r"the index $i,j$ are DUMMY (summed) so renaming them cannot change the value; "
                    r"and the two defining symmetries $S_{ij}=S_{ji}$, $A_{ij}=-A_{ji}$ hold for "
                    r"all $i,j$.")

    # ---- HOW: the machinery (the identity itself) ------------------------------------------
    d.how("How the approach works — relabel the dummy indices",
          {"plain": r"Call the total $X=\sum_{i,j}S_{ij}A_{ij}$. Swap the names of the two "
                    r"summation labels (allowed — they are just bookkeeping). Using "
                    r"$S_{ji}=S_{ij}$ and $A_{ji}=-A_{ij}$, the swapped sum equals $-X$. So "
                    r"$X=-X$, which forces $X=0$.",
           "working": r"$X=S_{ij}A_{ij}\overset{i\leftrightarrow j}{=}S_{ji}A_{ji}"
                      r"=S_{ij}(-A_{ij})=-S_{ij}A_{ij}=-X\ \Rightarrow\ 2X=0\ \Rightarrow\ X=0$.",
           "expert": r"Relabelling the contracted pair gives $X=-X$; the identity is the "
                     r"vanishing of a symmetric$\times$antisymmetric contraction."},
          math=[r"X=\sum_{i,j} S_{ij}A_{ij}\ \overset{i\leftrightarrow j}{=}\ "
                r"\sum_{i,j} S_{ji}A_{ji}=\sum_{i,j} S_{ij}(-A_{ij})=-X"])

    # ---- THE STEP TREE -----------------------------------------------------------------------
    # ONE expert node. Working sees its 3 children. Plain decomposes 2 of those 3 further.
    #   expert : 1 step
    #   working: 3 steps
    #   plain  : (2) + (2) + 1 = 5 steps      <- counts EMERGE and strictly differ 1<3<5
    d.step("Prove S_ij A_ij = 0 by relabelling the dummy indices", requires="expert",
           prose=r"Rename $i\leftrightarrow j$ in the dummy sum; $S_{ji}=S_{ij}$ and "
                 r"$A_{ji}=-A_{ij}$ turn it into the negative of itself, so it is $0$. "
                 r"(The engine's $n{=}3$ `sp.expand` $\to 0$ is the numeric witness.)",
           math=[r"S_{ij}A_{ij}=S_{ji}A_{ji}=-S_{ij}A_{ij}\ \Rightarrow\ S_{ij}A_{ij}=0"],
           references=["sub-method: index relabelling (dummy rename)",
                       "sub-method: symmetry substitution (S_ji=S_ij, A_ji=-A_ij)",
                       "realization: special_methods.SYM_ANTISYM  (_contract_to_zero -> sp.expand -> 0)"],
           decompose=[
               # -- working step 1: relabel the dummies (decomposes for plain) -------------
               dict(title="Relabel the summation indices i <-> j", requires="working",
                    prose=r"The indices $i,j$ are dummy (summed over the same range), so renaming "
                          r"them leaves the value unchanged: $\sum_{i,j}S_{ij}A_{ij}=\sum_{i,j}S_{ji}A_{ji}$.",
                    math=[r"X:=\sum_{i,j} S_{ij}A_{ij}=\sum_{i,j} S_{ji}A_{ji}"],
                    references=["sub-method: index relabelling (dummy rename)"],
                    decompose=[
                        dict(title="A summed (dummy) index is just a placeholder name",
                             requires="plain",
                             prose=r"$\sum_{i,j}$ adds the same recipe over every pair, e.g. for "
                                   r"$n=3$ over $i,j\in\{0,1,2\}$. The LETTERS are bookkeeping: "
                                   r"$\sum_k c_k=\sum_m c_m$. So calling the first label $j$ and the "
                                   r"second $i$ adds the EXACT same nine products in a different order.",
                             math=[r"\sum_{i,j} f(i,j)=\sum_{i,j} f(j,i)\quad(\text{just a renaming})"],
                             references=["base method -> library/summation-dummy-index.md"]),
                        dict(title="Apply the rename to our sum", requires="plain",
                             prose=r"Replace $i$ by $j$ and $j$ by $i$ everywhere inside: every "
                                   r"$S_{ij}A_{ij}$ becomes $S_{ji}A_{ji}$, and the total $X$ is unchanged.",
                             math=[r"X=\sum_{i,j} S_{ij}A_{ij}=\sum_{i,j} S_{ji}A_{ji}"]),
                    ]),
               # -- working step 2: push the two symmetries through (decomposes for plain) -
               dict(title="Use the symmetries: S_ji = S_ij and A_ji = -A_ij", requires="working",
                    prose=r"Symmetry of $S$ leaves $S_{ji}=S_{ij}$; antisymmetry of $A$ gives "
                          r"$A_{ji}=-A_{ij}$. The relabelled sum is therefore $-X$.",
                    math=[r"\sum_{i,j} S_{ji}A_{ji}=\sum_{i,j} S_{ij}(-A_{ij})=-\sum_{i,j}S_{ij}A_{ij}=-X"],
                    references=["sub-method: symmetry substitution (S_ji=S_ij, A_ji=-A_ij)"],
                    decompose=[
                        dict(title="What symmetric / antisymmetric mean on the entries",
                             requires="plain",
                             prose=r"Symmetric means the grid is unchanged when reflected across the "
                                   r"diagonal: $S_{ji}=S_{ij}$ (e.g. $S_{10}=S_{01}$). Antisymmetric "
                                   r"means reflecting flips the sign: $A_{ji}=-A_{ij}$ (e.g. "
                                   r"$A_{10}=-A_{01}$), and the diagonal must be $0$ since $A_{ii}=-A_{ii}$.",
                             math=[r"S_{ji}=S_{ij},\qquad A_{ji}=-A_{ij},\qquad A_{ii}=0"],
                             references=["base method -> library/symmetric-antisymmetric-matrix.md"]),
                        dict(title="Substitute and pull the minus sign out", requires="plain",
                             prose=r"Put $S_{ji}=S_{ij}$ and $A_{ji}=-A_{ij}$ into each term; the "
                                   r"common factor $-1$ comes outside the whole sum, giving $-X$.",
                             math=[r"\sum_{i,j} S_{ji}A_{ji}=\sum_{i,j} S_{ij}\,(-A_{ij})"
                                   r"=-\sum_{i,j} S_{ij}A_{ij}=-X"]),
                    ]),
               # -- working step 3: solve X = -X (high-school grokkable; NOT decomposed,
               #    so it shows AS-IS at plain too -> requires=plain, an honest leaf) ------
               dict(title="X = -X forces X = 0", requires="plain",
                    prose=r"Steps 1 and 2 say the SAME total equals both $X$ and $-X$. Adding $X$ to "
                          r"both sides gives $2X=0$, so $X=0$: the contraction vanishes for every $n$ "
                          r"and every such $S,A$ (the engine's $n=3$ `sp.expand`$\to 0$ confirms it).",
                    math=[r"X=-X\ \Rightarrow\ 2X=0\ \Rightarrow\ X=\sum_{i,j}S_{ij}A_{ij}=0"],
                    references=["base method -> library/linear-equation-one-unknown.md"]),
           ])

    # ---- VERIFY: the engine's own witness (n=3) --------------------------------------------
    S3, A3 = sm._symmetric(3), sm._antisymmetric(3)
    witness = sm._contract_to_zero((S3, A3))[0]   # = sp.expand(sum S_ij A_ij) -> 0, EMERGES
    route = sm.prove_sym_antisym(3)["best"]        # (cost, state, route) from the real search
    d.verify(
        r"Independent witness, NOT used to derive the result: the engine's IDENTITY search edge "
        r"builds the explicit symmetric $S$ and antisymmetric $A$ for $n=3$, forms "
        r"$\sum_{i,j}S_{ij}A_{ij}$, and `sp.expand` collapses it to $0$ (never written in); the "
        r"is_zero goal then settles the state. The relabelling proof above is the REASON; this is "
        r"the check.",
        math=[r"n=3:\quad \sum_{i,j} S_{ij}A_{ij}\ \xrightarrow{\ \mathtt{sp.expand}\ }\ " + sp.latex(witness),
              r"\text{search route: }\ " + r"\to ".join(route[2]) + r"\ \Rightarrow\ \text{state}=" + sp.latex(route[1])],
        references=["realization: special_methods.SYM_ANTISYM / _contract_to_zero",
                    "engine: strategies.prove_identity (IDENTITY goal = curvature.is_zero)",
                    "method: library/symmetric-antisymmetric-contraction.md"])
    d.result(latex=r"S_{ij}A_{ij}=\sum_{i,j} S_{ij}A_{ij}=0\qquad(S_{ij}=S_{ji},\ A_{ij}=-A_{ji})",
             note="proved by the dummy-index swap X = -X => X = 0; "
                  "engine n=3 witness sp.expand -> 0 agrees.")
    return d

def main():
    d = build_sym_antisym_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}   # EMERGENT from the tree cut
    qwarn = validate_qualification(tracks)
    print("level step counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[]  (VALID — no warnings)")
    print("counts differ:", len(set(counts.values())) == len(counts),
          "| ordering plain>=working>=expert:",
          counts["plain"] >= counts["working"] >= counts["expert"])
    assert not qwarn, qwarn
    out = os.path.join(os.path.dirname(__file__), "expl_sym_antisym.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render_leveled(tracks))
    print("rendered ->", out)
