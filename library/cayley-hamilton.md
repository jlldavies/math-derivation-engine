---
id: cayley-hamilton
name: Cayley–Hamilton — a matrix satisfies its own characteristic polynomial
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
You want to reduce high matrix powers, express `A⁻¹` as a polynomial in `A`, or
compute `f(A)`. Tells: "characteristic polynomial", `p(A) = 0`, "Cayley–Hamilton",
"reduce `Aⁿ` to lower powers", `A² = tr(A)A − det(A)I`, matrix exponential via
polynomial reduction.

## The rule
For an n×n matrix `A` with characteristic polynomial `p(λ) = det(λI − A)`, the
matrix satisfies its own polynomial: `p(A) = 0`. For 2×2 this is
`A² − tr(A)·A + det(A)·I = 0`. Consequences: every power `Aⁿ` (n ≥ size) reduces to
a polynomial of degree < n in `A`; and `A⁻¹ = (1/det A)(tr(A)I − A)` for an
invertible 2×2.

## Worked example
Any 2×2 `A = [[a,b],[c,d]]`: `tr(A) = a+d`, `det(A) = ad−bc`, and
`A² − (a+d)A + (ad−bc)I = 0`. Concretely `A = [[1,2],[3,4]]`: `tr=5`, `det=−2`,
`A² = [[7,10],[15,22]]`, and `A² − 5A − 2I = [[7−5−2, 10−10],[15−15, 22−20−2]] = 0`.
(SymPy: `A.charpoly()` then substitute `A` → zero matrix.)

## Explain (altitudes)
- **expert** — over the eigenbasis `p(A)` acts as `p(λ_i) = 0` on each eigenvector;
  the identity holds without diagonalisability by the adjugate identity
  `(λI−A)adj(λI−A) = p(λ)I` and a degree-matching argument, so `p(A) = 0` as an
  operator. It makes `ℂ[A]` a quotient of `ℂ[λ]` by the minimal polynomial.
- **working** — plug the matrix into the very polynomial whose roots are its
  eigenvalues and you get the zero matrix; that lets you rewrite `A²` (and higher) in
  terms of `A` and `I`, collapsing big powers.
- **plain** — a matrix obeys its own "fingerprint" equation. For a 2×2 that says
  `A² = (a+d)A − (ad−bc)I`, so you never need a power higher than `A¹` — everything
  folds back down.

## LaTeX
rule: p(\lambda)=\det(\lambda I-A)\ \Rightarrow\ p(A)=0,\qquad (n=2)\ \ A^{2}-\operatorname{tr}(A)\,A+\det(A)\,I=0
example: A=\left[\begin{matrix}1&2\\3&4\end{matrix}\right]:\ \ A^{2}-5A-2I=\left[\begin{matrix}0&0\\0&0\end{matrix}\right]

## References
- Horn & Johnson, *Matrix Analysis*, §2.4 (Cayley–Hamilton, minimal polynomial).
- Strang, *Linear Algebra and Its Applications*, §5.2 (characteristic polynomial).
- Library: SymPy `Matrix.charpoly`; verify by substitution.
- Worked example: `[[1,2],[3,4]]`, `A² − 5A − 2I = 0` (standard exercise).

## Links
[[eigendecomposition]] · [[determinant-expansion]]
