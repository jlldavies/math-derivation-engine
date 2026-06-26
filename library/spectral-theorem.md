---
id: spectral-theorem
name: Spectral theorem — symmetric ⇒ orthogonal eigenbasis
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
A **symmetric** (real, `A = Aᵀ`) or Hermitian matrix — covariance matrices, Hessians,
quadratic forms, Gram matrices, inertia tensors. Tells: "symmetric matrix",
"orthogonally diagonalise", `A = QΛQᵀ`, "real eigenvalues", "orthonormal
eigenvectors", principal-axis theorem, sign of a quadratic form.

## The rule
If `A = Aᵀ` (real), then all eigenvalues `λ_i` are **real** and eigenvectors for
distinct eigenvalues are **orthogonal**; one can choose an orthonormal eigenbasis,
giving `A = QΛQᵀ` with `Q` orthogonal (`QᵀQ = I`) and `Λ = diag(λ_i)`. So
`A = Σ_i λ_i q_i q_iᵀ` (spectral resolution). The quadratic form `xᵀAx` is positive
definite iff every `λ_i > 0`.

## Worked example
`A = [[2,1],[1,2]]` (symmetric). `λ = 1, 3` with eigenvectors `(1,−1)` and `(1,1)`,
which are **orthogonal**; normalise to `q₁=(1,−1)/√2`, `q₂=(1,1)/√2`. Then
`Q = [[1,1],[−1,1]]/√2` is orthogonal and `A = Q diag(1,3) Qᵀ`.
(SymPy: `Matrix([[2,1],[1,2]]).is_symmetric()` → `True`; eigenvectors orthogonal.)

## Explain (altitudes)
- **expert** — a real symmetric operator is self-adjoint, hence normal; the finite
  spectral theorem gives an orthonormal eigenbasis and the resolution `A = Σ λ_i P_i`
  into orthogonal projectors. It is the principal-axis theorem for quadratic forms
  and underlies PCA and the inertia tensor.
- **working** — for a symmetric matrix the eigenvectors automatically come out
  perpendicular and the eigenvalues real, so the diagonalising `Q` is a pure
  rotation/reflection and `Q⁻¹ = Qᵀ` (no messy inverse).
- **plain** — a symmetric matrix only stretches along a set of mutually
  perpendicular axes (never twisting). Line up with those axes and it just scales —
  and the axes stay at right angles.

## LaTeX
rule: A=A^{\mathsf T}\ \Rightarrow\ A=Q\Lambda Q^{\mathsf T},\quad Q^{\mathsf T}Q=I,\ \ \lambda_i\in\mathbb R,\ \ A=\sum_i\lambda_i\,\mathbf q_i\mathbf q_i^{\mathsf T}
example: \left[\begin{matrix}2&1\\1&2\end{matrix}\right]=\tfrac12\left[\begin{matrix}1&1\\-1&1\end{matrix}\right]\left[\begin{matrix}1&0\\0&3\end{matrix}\right]\left[\begin{matrix}1&-1\\1&1\end{matrix}\right]

## References
- Strang, *Linear Algebra and Its Applications*, §5.5 (symmetric matrices).
- Horn & Johnson, *Matrix Analysis*, §4.1 (spectral theorem for Hermitian matrices).
- Library: NumPy `numpy.linalg.eigh` (symmetric/Hermitian); SymPy `Matrix.diagonalize`.
- Worked example: `[[2,1],[1,2]]`, orthogonal eigenvectors (standard exercise).

## Links
[[eigendecomposition]] · [[singular-value-decomposition]] · [[gram-schmidt]]
