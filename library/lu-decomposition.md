---
id: lu-decomposition
name: LU decomposition — A = LU via elimination
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
A square system you want to solve (especially for many right-hand sides), a
determinant to compute cheaply, or a factorisation into triangular pieces. Tells:
"LU", "Gaussian elimination", `A = LU`, `Ax = b` for several `b`, "forward/back
substitution", pivoting (`PA = LU`).

## The rule
Gaussian elimination without row swaps factors `A = LU`: `U` is the upper-triangular
result of elimination, and `L` is **unit lower-triangular** holding the multipliers
`ℓ_{ij} = (entry eliminated)/(pivot)` used to zero each subdiagonal entry. Then
`Ax = b` solves as `Ly = b` (forward) then `Ux = y` (back). `det A = ∏ u_{ii}`.
If a zero pivot appears, swap rows: `PA = LU`.

## Worked example
`A = [[4,3],[6,3]]`. Multiplier `ℓ₂₁ = 6/4 = 3/2`; subtract `3/2 ×` row 1 from row 2:
row 2 → `[0, 3 − 3/2·3] = [0, −3/2]`. So
`L = [[1,0],[3/2,1]]`, `U = [[4,3],[0,−3/2]]`, and `LU = A`.
Check `det A = 4·(−3/2) = −6 = 4·3 − 3·6`. (SciPy: `scipy.linalg.lu(A)`.)

## Explain (altitudes)
- **expert** — elimination is left-multiplication by unit lower-triangular
  elementary matrices `E_k`; `L = (E_{n−1}⋯E_1)⁻¹` is again unit lower-triangular,
  so `A = LU` records the whole elimination as one triangular factor pair. Partial
  pivoting introduces a permutation `P` for stability and existence.
- **working** — do ordinary row reduction to reach upper-triangular `U`, and write
  down the multiples you subtracted; those multiples, placed below the diagonal of
  an identity, are `L`.
- **plain** — clearing a system to a staircase shape *is* a factorisation: `U` is
  the cleared matrix, `L` is the bookkeeping of what you subtracted, and the two
  multiply back to the original.

## LaTeX
rule: A=LU,\quad L\ \text{unit lower-}\triangle,\ U\ \text{upper-}\triangle,\qquad \ell_{ij}=\frac{a_{ij}^{(j)}}{u_{jj}},\ \ \det A=\prod_i u_{ii}
example: \left[\begin{matrix}4&3\\6&3\end{matrix}\right]=\left[\begin{matrix}1&0\\\tfrac32&1\end{matrix}\right]\left[\begin{matrix}4&3\\0&-\tfrac32\end{matrix}\right]

## References
- Golub & Van Loan, *Matrix Computations*, §3.2 (LU, pivoting).
- Strang, *Linear Algebra and Its Applications*, §1.5.
- Library: SciPy `scipy.linalg.lu`, `lu_factor`/`lu_solve`; SymPy `Matrix.LUdecomposition`.
- Worked example: `[[4,3],[6,3]]` 2×2 elimination (standard text exercise).

## Links
[[determinant-expansion]] · [[matrix-inverse]] · [[qr-decomposition]]
