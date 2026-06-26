r"""LEVELED Derivation for METHOD conformal_casimir (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.conformal_casimir. The engine DERIVES the conformal Casimir of
a scalar primary of dimension Delta in d dimensions,
    C_2 = Delta(Delta - d),
in embedding space: a primary is a degree-(-Delta) homogeneous function on the null cone X^2=0 in
R^{d+1,1}; the engine builds f=(X.C)^{-Delta} (C a fixed null vector), applies the SO(d+1,1) Laplacian
-sum_{A<B} L_{AB}^2 by genuine differentiation, and reduces on the cone -> Delta(Delta-d). The d
emerges from the (d+2)-dim index sum. The non-compact analogue of su(2)'s J^2=j(j+1).

Sub-methods referenced by the steps:
    conformal_casimir -> { embedding-space null cone, homogeneous (degree) operator,
                           SO(d+1,1) rotation generators L_{AB} }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = r"C_2=-\tfrac12 L_{AB}L^{AB}\ \text{on a primary}\ \Rightarrow\ C_2=\Delta(\Delta-d)"


def build_conformal_casimir_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the quadratic Casimir of the conformal group $SO(d+1,1)$ on a scalar primary of "
                   r"dimension $\Delta$ — the invariant that labels a conformal representation",
        goal=Goal.SIMPLIFY,
        integral="conformal Casimir Delta(Delta-d) via the embedding null cone")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — lift to the null cone, read the Casimir off the homogeneity",
          {"plain": r"The conformal group is non-compact, so there are no finite matrices to diagonalise. The "
                    r"trick: lift the $d$-dimensional theory to a cone in two extra dimensions, where a primary "
                    r"of 'dimension $\Delta$' becomes a simple scaling function $f\to t^{-\Delta}f$. The Casimir is "
                    r"then a Laplacian whose value is read straight off that scaling power.",
           "working": r"In embedding space $\mathbb R^{d+1,1}$ a primary of dimension $\Delta$ is a function on the "
                      r"null cone $X^2=0$ homogeneous of degree $-\Delta$. The Casimir $-\tfrac12 L_{AB}L^{AB}$ is the "
                      r"$SO(d+1,1)$ Laplacian, and on a homogeneous function it returns $\Delta(\Delta-d)$.",
           "expert": r"The conformal algebra is $so(d+1,1)$; its quadratic Casimir, realized as the embedding "
                     r"Laplacian on the null cone, acts on a degree-$(-\Delta)$ section as $\Delta(\Delta-d)$ — the "
                     r"non-compact analogue of $J^2=j(j+1)$."},
          forced_by=r"$SO(d+1,1)$ has no finite-dimensional unitary reps, but its action linearises on the "
                    r"embedding null cone, where 'conformal dimension' is just a homogeneity degree.",
          payoff=r"the exact label $\Delta(\Delta-d)$ — the mass-dimension relation $m^2=\Delta(\Delta-d)$ and the "
                 r"eigenvalue that powers conformal blocks; a number would lose the whole $\Delta$-dependence.",
          relies_on=r"the embedding/null-cone realization (a primary = degree-$(-\Delta)$ homogeneous function on "
                    r"$X^2=0$) and the Casimir as the $SO(d+1,1)$ Laplacian.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — homogeneous function on the null cone, hit with the Laplacian",
          {"plain": r"Build a primary as $f=(X\cdot C)^{-\Delta}$ for a fixed null direction $C$ — it scales as "
                    r"$t^{-\Delta}$. Apply the rotation-squared operator $\sum L_{AB}^2$ and set $X^2=0$; what's left "
                    r"is a number times $f$, and that number is $\Delta(\Delta-d)$.",
           "working": r"$f=(X\cdot C)^{-\Delta}$ is degree $-\Delta$. With $L_{AB}=X_A\partial_B-X_B\partial_A$, compute "
                      r"$-\sum_{A<B}L_{AB}^2 f$ and impose $X^2=0$; using $C^2=0$ the result is $\Delta(\Delta-d)f$.",
           "expert": r"$-\tfrac12 L_{AB}L^{AB}=X^2\square-(X\!\cdot\!\partial)(X\!\cdot\!\partial+d)$; on $X^2=0$ and "
                     r"degree $-\Delta$ this is $-(-\Delta)(-\Delta+d)=\Delta(\Delta-d)$."},
          math=[r"f=(X\cdot C)^{-\Delta},\quad L_{AB}=X_A\partial_B-X_B\partial_A,\quad C^2=X^2=0"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Hit the homogeneous primary with the embedding Laplacian", requires="expert",
           prose=r"Take $f=(X\cdot C)^{-\Delta}$ on the null cone, apply $-\sum_{A<B}L_{AB}^2$, and reduce with "
                 r"$X^2=C^2=0$: the eigenvalue is $\Delta(\Delta-d)$.",
           math=[r"-\sum_{A<B}L_{AB}^2\,f=\Delta(\Delta-d)\,f"],
           references=["sub-method: conformal_casimir -> {embedding null cone, homogeneity, L_{AB} generators}"],
           decompose=[
               dict(title="Build the primary on the null cone", requires="working",
                    prose=r"Embed $\mathbb R^d$ in the null cone $X^2=0$ of $\mathbb R^{d+1,1}$; a primary of dimension "
                          r"$\Delta$ is $f=(X\cdot C)^{-\Delta}$, homogeneous of degree $-\Delta$.",
                    math=[r"X^2=0,\qquad f=(X\cdot C)^{-\Delta},\qquad (X\cdot\partial)f=-\Delta f"],
                    references=["sub-method: embedding-space null cone"],
                    decompose=[
                        dict(title="Why a primary is a homogeneous function", requires="plain",
                             prose=r"Scaling $X\to tX$ multiplies $f$ by $t^{-\Delta}$ — that is exactly 'has conformal "
                                   r"dimension $\Delta$'.",
                             math=[r"f(tX)=t^{-\Delta}f(X)"]),
                    ]),
               dict(title="Apply the rotation generators twice", requires="working",
                    prose=r"$L_{AB}=X_A\partial_B-X_B\partial_A$ are the $SO(d+1,1)$ rotations; form $-\sum_{A<B}L_{AB}^2 f$ "
                          r"by differentiating $f$ twice.",
                    math=[r"-\sum_{A<B}\big(X_A\partial_B-X_B\partial_A\big)^2 f"],
                    references=["sub-method: SO(d+1,1) generators L_{AB}"],
                    decompose=[
                        dict(title="Each L_{AB} is a rotation derivative", requires="plain",
                             prose=r"$L_{AB}$ rotates the $A$-$B$ plane: $X_A\partial_B-X_B\partial_A$ — apply it, then apply it again.",
                             math=[r"L_{AB}f=(X_A\partial_B-X_B\partial_A)f"]),
                    ]),
               dict(title="Reduce on the null cone to read the eigenvalue", requires="working",
                    prose=r"Using $-\tfrac12 L_{AB}L^{AB}=X^2\square-(X\!\cdot\!\partial)(X\!\cdot\!\partial+d)$, set $X^2=0$ and "
                          r"$(X\!\cdot\!\partial)=-\Delta$: the eigenvalue is $-(-\Delta)(-\Delta+d)=\Delta(\Delta-d)$.",
                    math=[r"X^2\to0,\ (X\!\cdot\!\partial)\to-\Delta\ \Rightarrow\ -(-\Delta)(-\Delta+d)=\Delta(\Delta-d)"],
                    references=["sub-method: homogeneity (degree) operator"],
                    decompose=[
                        dict(title="The X^2 term drops on the cone", requires="plain",
                             prose=r"On the null cone $X^2=0$, so the $X^2\square$ piece vanishes, leaving only the "
                                   r"degree operator part.",
                             math=[r"X^2=0\ \Rightarrow\ X^2\square\,f=0"]),
                        dict(title="Plug in the degree -Delta", requires="plain",
                             prose=r"$(X\!\cdot\!\partial)f=-\Delta f$, so $(X\!\cdot\!\partial)(X\!\cdot\!\partial+d)f=(-\Delta)(-\Delta+d)f$; the "
                                   r"overall minus gives $\Delta(\Delta-d)$.",
                             math=[r"-(-\Delta)(-\Delta+d)=\Delta(\Delta-d)"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `conformal_casimir(d)` builds $f=(X\cdot C)^{-\Delta}$, applies $-\sum_{A<B}L_{AB}^2$ by "
        r"genuine differentiation, and reduces on the null cone — returning $\Delta(\Delta-d)$ for $d=2,3,4$ "
        r"(verified $\Delta^2-2\Delta,\ \Delta^2-3\Delta,\ \Delta^2-4\Delta$), matching the standard CFT Casimir "
        r"(Simmons-Duffin TASI). The $d$ emerges from the $(d+2)$-dimensional index sum, nothing written in.",
        math=[r"C_2=\Delta(\Delta-d)\quad(\text{Simmons-Duffin, TASI})",
              r"d=2\!:\Delta(\Delta-2),\ d=3\!:\Delta(\Delta-3),\ d=4\!:\Delta(\Delta-4)"],
        references=["engine: special_methods.conformal_casimir (embedding-space null-cone Laplacian)",
                    "Simmons-Duffin, TASI Lectures on the Conformal Bootstrap (arXiv:1602.07982)",
                    "arXiv:2606.24382 / 2606.24285 — the conformal Casimir in practice"])
    d.result(
        latex=r"C_2=\Delta(\Delta-d)\qquad(\text{scalar primary, } SO(d+1,1))",
        note="derived in embedding space by applying the SO(d+1,1) Laplacian to a degree-(-Delta) function on "
             "the null cone (d emerges from the (d+2)-dim sum); the non-compact analogue of J^2=j(j+1).")
    return d
