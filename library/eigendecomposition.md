---
id: eigendecomposition
name: Eigendecomposition — diagonalise via eigenvectors
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
A square matrix you want to **diagonalise**, raise to a power, or whose dynamics
you want to decouple. Tells: "eigenvalues", "eigenvectors", "diagonalise `A`",
`A = QΛQ⁻¹`, `Aⁿ`, modal/normal-mode analysis, "find vectors `v` with `Av` parallel
to `v`". Requires `A` (n×n) to have `n` linearly independent eigenvectors.

## The rule
Solve `Av = λv`, i.e. `det(A − λI) = 0` for the eigenvalues `λ_i`, then
`(A − λ_iI)v_i = 0` for the eigenvectors. If the `n` eigenvectors are independent,
stack them as columns of `Q` and the eigenvalues on the diagonal of `Λ`:
`A = QΛQ⁻¹`. Then `Aⁿ = QΛⁿQ⁻¹` (powers act on the diagonal). Symmetric `A` gives
an orthogonal `Q` (the spectral theorem); a non-diagonalisable `A` needs Jordan form.

## Worked example
`A = [[2,1],[1,2]]`. Characteristic polynomial `(2−λ)² − 1 = λ² − 4λ + 3 = 0`
⇒ `λ = 1, 3`. For `λ=1`: `(A−I)v=0` ⇒ `v=(1,−1)`; for `λ=3`: `v=(1,1)`.
So `Q = [[1,1],[−1,1]]`, `Λ = diag(1,3)`, and `A = QΛQ⁻¹`.
(SymPy: `Matrix([[2,1],[1,2]]).eigenvects()` → `[(1,1,[(1,−1)]), (3,1,[(1,1)])]`.)

## Explain (altitudes)
- **expert** — `A` is similar to a diagonal operator iff its eigenvectors span the
  space; the similarity `Q` is the change of basis to the eigenbasis, in which `A`
  acts coordinate-wise as `Λ`. Defect (geometric < algebraic multiplicity) obstructs
  this and forces Jordan blocks.
- **working** — find the scalars `λ` for which `A−λI` is singular, get a null vector
  for each, and use those vectors as a new basis; in that basis `A` just scales each
  axis by its `λ`, so it is diagonal.
- **plain** — some special directions only get stretched (not turned) by the matrix.
  Line the matrix up with those directions and all it does is stretch — which makes
  everything (like repeated multiplication) easy.

## LaTeX
rule: A\,\mathbf v=\lambda\,\mathbf v\ \Rightarrow\ A=Q\Lambda Q^{-1},\quad \Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\ \ A^{n}=Q\Lambda^{n}Q^{-1}
example: A=\left[\begin{matrix}2&1\\1&2\end{matrix}\right],\ \ \lambda=1,3,\ \ \mathbf v_1=\left[\begin{matrix}1\\-1\end{matrix}\right],\ \mathbf v_2=\left[\begin{matrix}1\\1\end{matrix}\right]

## References
- Strang, *Linear Algebra and Its Applications*, ch. 5 (eigenvalues/eigenvectors).
- Horn & Johnson, *Matrix Analysis*, §1.1–1.3.
- Library: NumPy `numpy.linalg.eig`; SymPy `Matrix.eigenvects`.
- Worked example: standard `[[2,1],[1,2]]` text exercise (Strang §5.1).

## Links
[[spectral-theorem]] · [[singular-value-decomposition]] · [[cayley-hamilton]] · [[determinant-expansion]]
