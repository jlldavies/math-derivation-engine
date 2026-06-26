---
id: qr-decomposition
name: QR decomposition — A = QR
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
A matrix you want to factor into orthonormal columns times an upper-triangular
matrix: least squares, the QR eigenvalue algorithm, orthogonal projection. Tells:
"QR", `A = QR`, "orthonormal columns", least-squares normal-equation avoidance,
Householder/Givens, Gram–Schmidt applied to columns.

## The rule
Orthonormalise the columns of `A` (Gram–Schmidt, or Householder/Givens reflections):
`Q` has those orthonormal columns (`QᵀQ = I`) and `R` is upper-triangular with
`r_{jk} = ⟨a_k, q_j⟩` (`j<k`) and `r_{kk} = ‖u_k‖` (the residual norm at step `k`).
Then `A = QR`. Least squares `Ax≈b` becomes `Rx = Qᵀb` (well-conditioned).

## Worked example
`A = [[1,1],[0,1]]` (columns `a₁=(1,0)`, `a₂=(1,1)`). `a₁` is already unit:
`q₁=(1,0)`, `r₁₁=1`. `r₁₂=⟨a₂,q₁⟩=1`; `u₂=a₂−1·q₁=(0,1)`, `r₂₂=1`, `q₂=(0,1)`.
So `Q = I`, `R = [[1,1],[0,1]] = A` (here `A` was already upper-triangular with
orthonormal columns). (NumPy: `numpy.linalg.qr([[1,1],[0,1]])` → `Q=I, R=A`.)

## Explain (altitudes)
- **expert** — QR is Gram–Schmidt recorded as a factorisation: the orthonormal
  basis is `Q`, the change-of-coordinates from the original columns is the
  upper-triangular `R`. Householder QR computes the same `Q,R` backward-stably as a
  product of reflections, the workhorse of the QR eigenvalue iteration.
- **working** — run Gram–Schmidt on the columns to get orthonormal `Q`; the inner
  products you used and the lengths you divided by assemble, in upper-triangular
  order, into `R`.
- **plain** — split the matrix into a "pure rotation/reflection" part (`Q`, axes at
  right angles, length one) and an "upper-triangular stretch" part (`R`); together
  they rebuild the original.

## LaTeX
rule: A=QR,\quad Q^{\mathsf T}Q=I,\ R\ \text{upper-}\triangle,\qquad r_{jk}=\langle \mathbf a_k,\mathbf q_j\rangle,\ \ r_{kk}=\left\lVert \mathbf u_k\right\rVert
example: \left[\begin{matrix}1&1\\0&1\end{matrix}\right]=\underbrace{\left[\begin{matrix}1&0\\0&1\end{matrix}\right]}_{Q}\underbrace{\left[\begin{matrix}1&1\\0&1\end{matrix}\right]}_{R}

## References
- Trefethen & Bau, *Numerical Linear Algebra*, lectures 7–10 (Gram–Schmidt, Householder).
- Golub & Van Loan, *Matrix Computations*, §5.2.
- Library: NumPy `numpy.linalg.qr`; SciPy `scipy.linalg.qr`; SymPy `Matrix.QRdecomposition`.
- Worked example: `[[1,1],[0,1]]` (upper-triangular with orthonormal columns).

## Links
[[gram-schmidt]] · [[lu-decomposition]] · [[eigendecomposition]]
