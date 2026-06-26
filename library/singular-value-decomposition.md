---
id: singular-value-decomposition
name: Singular value decomposition — A = UΣVᵀ
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
Any matrix (rectangular allowed, possibly singular) you want to factor into
orthogonal × diagonal × orthogonal: low-rank approximation, pseudoinverse,
PCA, condition number, "principal directions". Tells: "SVD", "singular values",
`A = UΣVᵀ`, `σ_i`, "best rank-k approximation", non-square `A`.

## The rule
For `A` (m×n), the `σ_i = √λ_i` where `λ_i` are the eigenvalues of the symmetric
PSD matrix `AᵀA`; the columns of `V` are the orthonormal eigenvectors of `AᵀA`
(right singular vectors), and the columns of `U` are `u_i = A v_i / σ_i` (left
singular vectors, for `σ_i > 0`). Then `A = U Σ Vᵀ` with `Σ` carrying the `σ_i`
(descending) on its diagonal. `U`, `V` orthogonal; rank = number of nonzero `σ_i`.

## Worked example
`A = [[1,1],[0,1]]`. `AᵀA = [[1,1],[1,2]]`, eigenvalues `λ = (3±√5)/2`, so
singular values `σ = √λ = (1+√5)/2 ≈ 1.618` and `(√5−1)/2 ≈ 0.618` (the golden
ratio and its reciprocal); note `σ₁σ₂ = 1 = |det A|`.
(SymPy: `Matrix([[1,1],[0,1]]).singular_values()` → `[(1+√5)/2, (√5−1)/2]`.)

## Explain (altitudes)
- **expert** — SVD diagonalises `A` between two orthonormal bases: `A v_i = σ_i u_i`.
  It is the eigendecomposition of `AᵀA` (and `AAᵀ`) pushed through `A`; `Σ` is the
  invariant spectrum of `A` under orthogonal equivalence, giving the Eckart–Young
  optimal low-rank truncation.
- **working** — diagonalise `AᵀA` (symmetric, so clean eigenvectors): its
  eigenvectors are the input directions `V`, the square-rooted eigenvalues are the
  stretch factors `σ`, and `A` maps each input direction to an output direction `u`.
- **plain** — every matrix, even a stretchy skewed one, is really: rotate, stretch
  each axis by a fixed amount, rotate again. SVD reads off those stretch amounts and
  the two rotations.

## LaTeX
rule: A=U\Sigma V^{\mathsf T},\quad \sigma_i=\sqrt{\lambda_i(A^{\mathsf T}A)},\ \ V=\text{eigvecs}(A^{\mathsf T}A),\ \ \mathbf u_i=\tfrac{1}{\sigma_i}A\mathbf v_i
example: A=\left[\begin{matrix}1&1\\0&1\end{matrix}\right],\ \ \sigma_{1,2}=\frac{\sqrt5\pm1}{2},\quad \sigma_1\sigma_2=|\det A|=1

## References
- Golub & Van Loan, *Matrix Computations*, §2.4, §8.6.
- Trefethen & Bau, *Numerical Linear Algebra*, lectures 4–5.
- Library: NumPy `numpy.linalg.svd`; SymPy `Matrix.singular_values`.
- Worked example: `[[1,1],[0,1]]`, golden-ratio singular values (standard exercise).

## Links
[[eigendecomposition]] · [[spectral-theorem]] · [[gram-schmidt]]
