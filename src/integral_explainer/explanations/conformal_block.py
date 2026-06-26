r"""LEVELED Derivation for METHOD conformal_block (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.conformal_block_casimir. The engine DERIVES that the 1D / SL(2)
global conformal block k_h(z) = z^h 2F1(h,h;2h;z) is the eigenfunction of the SL(2) quadratic-Casimir
differential operator D_z = z^2(1-z) d_z^2 - z^2 d_z (Dolan-Osborn / Simmons-Duffin normalisation) with
eigenvalue h(h-1): it builds the block as its hypergeometric power series, applies D_z by genuine
differentiation, extracts the eigenvalue from the leading z^h indicial balance, and confirms the residual
vanishes order by order. The 1D analogue of the conformal_casimir result Delta(Delta-d).

Sub-methods referenced by the steps:
    conformal_block -> { SL(2) Casimir operator D_z, hypergeometric block z^h 2F1(h,h;2h;z),
                         indicial balance (leading z^h coefficient), hypergeometric recursion }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = r"D_z\,k_h(z)=h(h-1)\,k_h(z),\quad k_h(z)=z^{h}\,{}_2F_1(h,h;2h;z)"


def build_conformal_block_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the 1D / $SL(2)$ global conformal block $k_h$ as the eigenfunction of the "
                   r"quadratic Casimir operator $D_z$ with eigenvalue $h(h-1)$ - the function that "
                   r"resums the contribution of a primary of weight $h$ and its descendants to a 4-point function",
        goal=Goal.SIMPLIFY,
        integral="SL(2) conformal block k_h = z^h 2F1(h,h;2h;z), Casimir eigenvalue h(h-1)")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach - diagonalise the Casimir instead of summing descendants by hand",
          {"plain": r"A conformal block packages an entire family - one 'primary' state of weight $h$ plus its "
                    r"infinitely many descendants - into a single function $k_h(z)$. Rather than add up that "
                    r"infinite tower, we use the fact that the whole family shares ONE number, the Casimir "
                    r"eigenvalue. That turns the block into the solution of a single differential equation.",
           "working": r"The exchanged conformal family is an irreducible $SL(2)$ representation, so the quadratic "
                      r"Casimir acts on it as a constant $h(h-1)$. The block $k_h(z)$ is the corresponding "
                      r"eigenfunction of the Casimir DIFFERENTIAL operator $D_z$, fixed by its boundary behaviour "
                      r"$k_h\sim z^h$.",
           "expert": r"In the OPE/shadow formalism the block is the $SL(2,\mathbb R)$ Casimir eigenfunction: "
                     r"$D_z k_h = h(h-1)k_h$ with the $z\to0$ boundary condition selecting $k_h=z^h{}_2F_1(h,h;2h;z)$ "
                     r"over its shadow $h\to1-h$. The 1D radial reduction of the Dolan-Osborn Casimir equation."},
          forced_by=r"the exchanged states form a single $SL(2)$ irrep, on which the quadratic Casimir is a scalar "
                    r"$h(h-1)$ - so the block obeys a 2nd-order ODE rather than an infinite descendant sum.",
          payoff=r"the closed form $k_h=z^h{}_2F_1(h,h;2h;z)$ and the exact label $h(h-1)$ - the eigenvalue that "
                 r"drives the conformal bootstrap; a numeric block would lose the whole $h$-dependence.",
          relies_on=r"the SL(2) Casimir operator $D_z=z^2(1-z)\partial_z^2-z^2\partial_z$ (Dolan-Osborn normalisation) "
                    r"and the leading boundary condition $k_h\sim z^h$.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works - apply the Casimir operator to the hypergeometric series and read the eigenvalue",
          {"plain": r"Write the block as its power series $k_h=z^h(1+\dots)$, apply the differential operator $D_z$, "
                    r"and look at the very first term: it comes out as $h(h-1)$ times the block. Then check every "
                    r"higher term cancels - confirming $k_h$ really is an eigenfunction.",
           "working": r"Expand $k_h=z^h\sum_n a_n z^n$ with $a_n=\frac{(h)_n^2}{(2h)_n\,n!}$. Apply "
                      r"$D_z=z^2(1-z)\partial_z^2-z^2\partial_z$ term by term; the leading $z^h$ coefficient gives the "
                      r"eigenvalue $h(h-1)$, and the residual $D_z k_h-h(h-1)k_h$ vanishes at every order.",
           "expert": r"$D_z z^h=h(h-1)z^h-h^2 z^{h+1}$ fixes the eigenvalue from the indicial term; the ${}_2F_1$ "
                     r"coefficients $a_n=(h)_n^2/((2h)_n n!)$ are exactly the recursion that annihilates the residual "
                     r"$(D_z-h(h-1))k_h$ order by order - the hypergeometric ODE in disguise."},
          math=[r"D_z=z^2(1-z)\partial_z^2-z^2\partial_z,\qquad k_h=z^h\sum_{n\ge0}\frac{(h)_n^2}{(2h)_n\,n!}z^n"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Apply the SL(2) Casimir operator to the block and read off h(h-1)", requires="expert",
           prose=r"Build $k_h=z^h{}_2F_1(h,h;2h;z)$, apply $D_z=z^2(1-z)\partial_z^2-z^2\partial_z$, extract the "
                 r"leading-term eigenvalue $h(h-1)$, and confirm the residual vanishes identically.",
           math=[r"D_z\,k_h=h(h-1)\,k_h"],
           references=["sub-method: conformal_block -> {SL(2) Casimir operator, hypergeometric block, indicial balance}",
                       "relates to conformal_casimir: this is the 1D h(h-1) vs the d-dim Delta(Delta-d)"],
           decompose=[
               dict(title="Write the block as its hypergeometric power series", requires="working",
                    prose=r"The block is $k_h=z^h\sum_n a_n z^n$ with ${}_2F_1$ coefficients "
                          r"$a_n=(h)_n^2/((2h)_n\,n!)$; the prefactor $z^h$ is the leading boundary behaviour.",
                    math=[r"k_h=z^h\sum_{n\ge0}\frac{(h)_n^2}{(2h)_n\,n!}\,z^n,\qquad a_0=1"],
                    references=["sub-method: hypergeometric block z^h 2F1(h,h;2h;z)"],
                    decompose=[
                        dict(title="Why z^h is the leading behaviour", requires="plain",
                             prose=r"Near $z=0$ the block behaves like $z^h$ - that is the contribution of the "
                                   r"primary of weight $h$ before any descendants switch on.",
                             math=[r"k_h(z)\xrightarrow{z\to0}z^h"]),
                    ]),
               dict(title="Apply the Casimir operator by differentiating term by term", requires="working",
                    prose=r"$D_z=z^2(1-z)\partial_z^2-z^2\partial_z$; differentiate the series twice and once and "
                          r"assemble - no black-box doit, each derivative is elementary.",
                    math=[r"D_z\,k_h=z^2(1-z)\,k_h''-z^2\,k_h'"],
                    references=["sub-method: SL(2) Casimir operator D_z (Dolan-Osborn normalisation)"],
                    decompose=[
                        dict(title="The two derivative pieces", requires="plain",
                             prose=r"$z^2(1-z)$ multiplies the second derivative and $-z^2$ the first; that is the "
                                   r"whole operator, applied to a power series.",
                             math=[r"k_h'=\partial_z k_h,\qquad k_h''=\partial_z^2 k_h"]),
                    ]),
               dict(title="Extract the eigenvalue from the leading term", requires="working",
                    prose=r"The lowest power in $D_z k_h$ is $z^h$; its coefficient is $h(h-1)$ - read straight off "
                          r"the indicial balance $D_z z^h=h(h-1)z^h-h^2z^{h+1}$, nothing written in.",
                    math=[r"D_z z^h=h(h-1)z^h-h^2 z^{h+1}\ \Rightarrow\ \lambda=h(h-1)"],
                    references=["sub-method: indicial balance (leading z^h coefficient)"],
                    decompose=[
                        dict(title="Differentiate the leading power z^h", requires="plain",
                             prose=r"$\partial_z z^h=h z^{h-1}$ and $\partial_z^2 z^h=h(h-1)z^{h-2}$; multiply by "
                                   r"$z^2(1-z)$ and $-z^2$ and the $z^h$ coefficient is $h(h-1)$.",
                             math=[r"z^2\cdot h(h-1)z^{h-2}=h(h-1)z^h"]),
                        dict(title="Why the leading coefficient IS the eigenvalue", requires="plain",
                             prose=r"An eigenfunction obeys $D_z k_h=\lambda k_h$; matching the leading $z^h$ on both "
                                   r"sides forces $\lambda=h(h-1)$.",
                             math=[r"\lambda\,z^h=h(h-1)z^h"]),
                    ]),
               dict(title="Confirm the residual vanishes order by order", requires="working",
                    prose=r"With $\lambda=h(h-1)$ fixed, the ${}_2F_1$ coefficients make $D_z k_h-\lambda k_h$ vanish "
                          r"at every order in $z$ - the eigenvalue equation holds identically.",
                    math=[r"\big(D_z-h(h-1)\big)k_h\equiv0"],
                    references=["sub-method: hypergeometric recursion annihilates the residual"],
                    decompose=[
                        dict(title="Each order cancels", requires="plain",
                             prose=r"Term by term in $z$, the operator's output matches $h(h-1)k_h$ exactly, so the "
                                   r"difference is zero to every order checked.",
                             math=[r"[z^{h+n}]\big(D_z k_h-h(h-1)k_h\big)=0"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's conformal_block_casimir() builds $k_h=z^h\sum_n\frac{(h)_n^2}{(2h)_n n!}z^n$, applies "
        r"$D_z=z^2(1-z)\partial_z^2-z^2\partial_z$ by genuine differentiation, EXTRACTS the leading-term eigenvalue "
        r"$h^2-h=h(h-1)$ (nothing written in), and confirms the residual $D_z k_h-h(h-1)k_h$ is identically zero "
        r"order by order. Numeric spot-check at $h=2,\ z=\tfrac15$ matches the closed-form ${}_2F_1$ block. This is "
        r"the 1D analogue of the engine's $\mathrm{conformal\_casimir}$ result $\Delta(\Delta-d)$.",
        math=[r"D_z\,k_h=h(h-1)\,k_h\quad(\text{Dolan-Osborn, Simmons-Duffin TASI})",
              r"h=2,z=\tfrac15:\ D_z k_h=0.0995\ldots=2\cdot k_h"],
        references=["engine: special_methods.conformal_block_casimir (SL(2) Casimir on z^h 2F1)",
                    "Dolan-Osborn, Conformal four point functions and the OPE (arXiv:hep-th/0011040)",
                    "Simmons-Duffin, TASI Lectures on the Conformal Bootstrap (arXiv:1602.07982)"])
    d.result(
        latex=r"D_z\,k_h(z)=h(h-1)\,k_h(z),\qquad k_h(z)=z^{h}\,{}_2F_1(h,h;2h;z)",
        note="the 1D / SL(2) global conformal block is the Casimir eigenfunction with eigenvalue h(h-1) - derived "
             "by applying D_z = z^2(1-z) d_z^2 - z^2 d_z to the hypergeometric series and reading off the leading "
             "balance; the 1D analogue of conformal_casimir's Delta(Delta-d).")
    return d