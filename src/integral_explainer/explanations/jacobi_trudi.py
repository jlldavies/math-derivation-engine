r"""LEVELED Derivation for METHOD jacobi_trudi (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.jacobi_trudi_schur. The engine DERIVES the Schur polynomial
s_lambda via the (first) Jacobi-Trudi identity s_lambda = det(h_{lambda_i - i + j}): it reads the
complete homogeneous symmetric polynomials h_k off the generating function prod_i 1/(1-x_i t) =
sum_k h_k t^k, assembles the Jacobi-Trudi matrix, and expands its determinant. For lambda=(2,1) this
is the 2x2 det h_1 h_2 - h_3, whose expansion carries the hallmark coefficient 2 on x1 x2 x3 (it
EMERGES from the determinant, nothing written in). The determinantal backbone of the symmetric-
function ring that the localization/character machinery rests on.

Sub-methods referenced by the steps:
    jacobi_trudi -> { complete-homogeneous generating function, Jacobi-Trudi matrix,
                      determinant expansion }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = r"s_\lambda=\det\!\big(h_{\lambda_i-i+j}\big)_{1\le i,j\le L}"


def build_jacobi_trudi_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the Jacobi-Trudi identity — the Schur polynomial $s_\lambda$ as a determinant "
                   r"of complete homogeneous symmetric polynomials $h_k$, the determinantal "
                   r"backbone of the symmetric-function ring that the localization/character "
                   r"machinery rests on",
        goal=Goal.SIMPLIFY,
        integral="Schur polynomial s_(2,1) via the Jacobi-Trudi determinant")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — express the Schur function as a determinant of h's",
          {"plain": r"A Schur polynomial $s_\lambda$ is a special symmetric polynomial. Rather than sum "
                    r"it monomial-by-monomial, we write it as a small determinant whose entries are the "
                    r"easy 'complete' symmetric polynomials $h_k$ (the sum of all degree-$k$ products of "
                    r"the variables). The determinant does the bookkeeping for us.",
           "working": r"Jacobi-Trudi expresses $s_\lambda$ as $\det(h_{\lambda_i-i+j})$. The $h_k$ are read off "
                      r"the generating function $\prod_i(1-x_i t)^{-1}=\sum_k h_k t^k$, so the whole Schur "
                      r"function reduces to one determinant of known polynomials.",
           "expert": r"In the ring $\Lambda$ of symmetric functions the $h_k$ are a polynomial basis; "
                     r"Jacobi-Trudi $s_\lambda=\det(h_{\lambda_i-i+j})$ is the change of basis to the Schur "
                     r"functions, dual under the Hall inner product to $\langle s_\lambda,s_\mu\rangle=\delta_{\lambda\mu}$."},
          forced_by=r"the Schur functions are defined as a ratio of alternants $a_{\lambda+\delta}/a_\delta$ — "
                    r"a quotient that is awkward to compute and to deform; the Jacobi-Trudi determinant "
                    r"re-expresses the SAME object purely in the $h_k$, with no division.",
          payoff=r"a finite determinant of explicit polynomials — it makes $s_\lambda$ directly computable, "
                 r"exposes the duality with the elementary basis ($s_\lambda=\det(e_{\lambda'_i-i+j})$), and "
                 r"is the scaffold the Jack/Macdonald deformations and character formulas are built on.",
          relies_on=r"the generating identity $\prod_i(1-x_i t)^{-1}=\sum_k h_k t^k$ for the complete "
                    r"homogeneous symmetric polynomials, and multilinearity of the determinant.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — read off the h_k, build the matrix, take the determinant",
          {"plain": r"Step one: get the $h_k$ from the product $\prod_i 1/(1-x_i t)$ by reading the coefficient of "
                    r"$t^k$. Step two: place $h_{\lambda_i-i+j}$ in row $i$, column $j$. Step three: take the "
                    r"determinant — that polynomial is $s_\lambda$.",
           "working": r"With $\lambda=(2,1)$, $L=2$, the matrix is $\begin{pmatrix}h_2&h_3\\ h_0&h_1\end{pmatrix}$ "
                      r"(using $\lambda_i-i+j$), so $s_{(2,1)}=h_2h_1-h_3h_0=h_1h_2-h_3$.",
           "expert": r"The entry in row $i$, column $j$ is $h_{\lambda_i-i+j}$ with $h_k=0$ for $k<0$, $h_0=1$; "
                     r"the determinant is the signed sum over $S_L$, $\sum_\sigma\operatorname{sgn}(\sigma)\prod_i h_{\lambda_i-i+\sigma(i)}$."},
          math=[r"\prod_i\frac{1}{1-x_i t}=\sum_{k\ge0}h_k t^k,\qquad s_\lambda=\det\big(h_{\lambda_i-i+j}\big)"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Assemble and evaluate the Jacobi-Trudi determinant for lambda=(2,1)", requires="expert",
           prose=r"Read the $h_k$ off the generating function, build $\det(h_{\lambda_i-i+j})$ for $\lambda=(2,1)$, "
                 r"and expand: $s_{(2,1)}=h_1h_2-h_3$.",
           math=[r"s_{(2,1)}=\det\begin{pmatrix}h_2&h_3\\ h_0&h_1\end{pmatrix}=h_1h_2-h_3"],
           references=["sub-method: jacobi_trudi -> {complete-homogeneous generating function, "
                       "Jacobi-Trudi matrix, determinant expansion}"],
           decompose=[
               dict(title="Get the complete homogeneous polynomials h_k", requires="working",
                    prose=r"Expand $\prod_i(1-x_i t)^{-1}=\sum_k h_k t^k$ and read off the coefficient of each $t^k$: "
                          r"$h_0=1$, $h_1=\sum x_i$, $h_2=\sum_{i\le j}x_ix_j$, $h_3=\sum_{i\le j\le k}x_ix_jx_k$.",
                    math=[r"\prod_i\frac{1}{1-x_i t}=\sum_{k\ge0}h_k t^k,\quad h_k=[t^k]\!\prod_i\frac1{1-x_i t}"],
                    references=["sub-method: complete-homogeneous generating function"],
                    decompose=[
                        dict(title="Why each h_k is a sum of monomials", requires="plain",
                             prose=r"Each factor $1/(1-x_i t)=1+x_i t+x_i^2t^2+\dots$ is a geometric series; multiplying "
                                   r"them and collecting $t^k$ gives every degree-$k$ product of the variables once — that "
                                   r"is exactly $h_k$.",
                             math=[r"\frac1{1-x_i t}=\sum_{m\ge0}x_i^m t^m\ \Rightarrow\ h_2=x_1^2+x_1x_2+\dots"]),
                    ]),
               dict(title="Place the entries h_{lambda_i - i + j} into the matrix", requires="working",
                    prose=r"For $\lambda=(2,1)$ ($L=2$): row $1$ has $h_{2-1+1}=h_2,\ h_{2-1+2}=h_3$; row $2$ has "
                          r"$h_{1-2+1}=h_0,\ h_{1-2+2}=h_1$.",
                    math=[r"\big(h_{\lambda_i-i+j}\big)=\begin{pmatrix}h_2&h_3\\ h_0&h_1\end{pmatrix}"],
                    references=["sub-method: Jacobi-Trudi matrix"],
                    decompose=[
                        dict(title="The shift lambda_i - i + j explained", requires="plain",
                             prose=r"In row $i$, column $j$ you write the $h$ whose index is $\lambda_i-i+j$; indices below "
                                   r"$0$ mean $h=0$ and index $0$ means $h_0=1$.",
                             math=[r"\text{row }i,\ \text{col }j:\ h_{\lambda_i-i+j},\quad h_{<0}=0,\ h_0=1"]),
                    ]),
               dict(title="Expand the determinant to get s_lambda", requires="working",
                    prose=r"The $2\times2$ determinant is $h_2h_1-h_3h_0=h_1h_2-h_3$; substituting the $h_k$ and "
                          r"expanding gives the Schur polynomial with its characteristic coefficients.",
                    math=[r"s_{(2,1)}=h_1h_2-h_3=\sum_{i\le j}x_i^2x_j+\,\dots+2x_1x_2x_3"],
                    references=["sub-method: determinant expansion"],
                    decompose=[
                        dict(title="The 2x2 determinant rule", requires="plain",
                             prose=r"$\det\begin{pmatrix}a&b\\ c&d\end{pmatrix}=ad-bc$; here $a=h_2,b=h_3,c=h_0=1,d=h_1$.",
                             math=[r"ad-bc=h_2h_1-h_3\cdot1"]),
                        dict(title="The 2 x1 x2 x3 coefficient emerges", requires="plain",
                             prose=r"After expanding $h_1h_2-h_3$, the term $x_1x_2x_3$ appears in $h_1h_2$ three times and "
                                   r"in $h_3$ once, leaving coefficient $3-1=2$ — the hallmark of $s_{(2,1)}$.",
                             math=[r"[x_1x_2x_3]\,(h_1h_2-h_3)=3-1=2"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `jacobi_trudi_schur([2,1],[x1,x2,x3])` builds the $h_k$ from the generating function "
        r"$\prod_i(1-x_it)^{-1}$, assembles $\det(h_{\lambda_i-i+j})$ and expands it, returning "
        r"$x_1^2x_2+x_1^2x_3+x_1x_2^2+x_2^2x_3+x_1x_3^2+x_2x_3^2+2x_1x_2x_3$ — exactly the published "
        r"$s_{(2,1)}(x_1,x_2,x_3)$ (Wikipedia 'Schur polynomial'; Macdonald I.3). The $2$ on $x_1x_2x_3$ "
        r"EMERGES from the determinant, nothing written in; cross-checked against the bialternant "
        r"definition $a_{\lambda+\delta}/a_\delta$ and a numeric spot-check at $(2,3,5)\mapsto280$.",
        math=[r"s_{(2,1)}=x_1^2x_2+x_1^2x_3+x_1x_2^2+x_2^2x_3+x_1x_3^2+x_2x_3^2+2x_1x_2x_3",
              r"\det(h_{\lambda_i-i+j})=a_{\lambda+\delta}/a_\delta\ \text{(Jacobi-Trudi}=\text{bialternant)}"],
        references=["engine: special_methods.jacobi_trudi_schur (determinant of complete-homogeneous h_k)",
                    "Macdonald, Symmetric Functions and Hall Polynomials, I.3 (Jacobi-Trudi)",
                    "https://en.wikipedia.org/wiki/Schur_polynomial (Jacobi-Trudi identity; s_(2,1) value)"])
    d.result(
        latex=r"s_{(2,1)}(x_1,x_2,x_3)=x_1^2x_2+x_1^2x_3+x_1x_2^2+x_2^2x_3+x_1x_3^2+x_2x_3^2+2x_1x_2x_3",
        note="derived from the Jacobi-Trudi determinant s_lambda=det(h_{lambda_i-i+j}); the h_k come from "
             "the generating function prod 1/(1-x_i t), and the 2 x1 x2 x3 coefficient emerges from the "
             "determinant expansion (nothing written in).")
    return d