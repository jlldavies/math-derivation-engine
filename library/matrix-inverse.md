---
id: matrix-inverse
name: Matrix inverse — adjugate / Gauss–Jordan
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
You need `A⁻¹` explicitly (small matrix, symbolic entries) or to solve `Ax = b` by
inversion. Tells: "inverse", `A⁻¹`, "adjugate/adjoint", "Gauss–Jordan", `[A | I] →
[I | A⁻¹]`, the 2×2 swap-and-negate formula, invertibility (`det A ≠ 0`).

## The rule
`A⁻¹ = adj(A) / det(A)`, where `adj(A)` is the transpose of the cofactor matrix
(`adj(A)_{ij} = C_{ji}`), valid iff `det A ≠ 0`. Equivalently, row-reduce the
augmented `[A | I]` to `[I | A⁻¹]` (Gauss–Jordan). For 2×2 this collapses to the
familiar `swap the diagonal, negate the off-diagonal, divide by the determinant`.

## Worked example
`[[a,b],[c,d]]⁻¹ = (1/(ad−bc)) [[d,−b],[−c,a]]`, provided `ad−bc ≠ 0`.
Concretely `[[2,1],[1,1]]⁻¹ = (1/1)[[1,−1],[−1,2]] = [[1,−1],[−1,2]]`; check
`[[2,1],[1,1]]·[[1,−1],[−1,2]] = [[1,0],[0,1]]`.
(SymPy: `Matrix([[2,1],[1,1]]).inv()` → `[[1,−1],[−1,2]]`.)

## Explain (altitudes)
- **expert** — `A·adj(A) = (det A)I` is the Cramer identity; dividing by `det A`
  inverts `A` when it is a unit. Gauss–Jordan realises `A⁻¹` as the product of the
  elementary matrices that reduce `A` to `I`, the practical `O(n³)` route versus the
  `O(n!)` adjugate.
- **working** — either build the cofactor matrix, transpose it, and divide by the
  determinant; or stick the identity beside `A` and row-reduce until `A` becomes the
  identity — whatever the identity turns into is the inverse.
- **plain** — the inverse undoes the matrix. For a 2×2: swap the two diagonal
  numbers, flip the sign of the other two, and divide everything by `ad−bc`.

## LaTeX
rule: A^{-1}=\frac{\operatorname{adj}(A)}{\det A},\qquad \left[\begin{matrix}a&b\\c&d\end{matrix}\right]^{-1}=\frac{1}{ad-bc}\left[\begin{matrix}d&-b\\-c&a\end{matrix}\right]
example: \left[\begin{matrix}2&1\\1&1\end{matrix}\right]^{-1}=\left[\begin{matrix}1&-1\\-1&2\end{matrix}\right]

## References
- Strang, *Linear Algebra and Its Applications*, §1.6, §4.4 (Gauss–Jordan, Cramer).
- Horn & Johnson, *Matrix Analysis*, §0.8 (adjugate identity).
- Library: SymPy `Matrix.inv()`; NumPy `numpy.linalg.inv` / `solve`.
- Worked example: 2×2 closed form; `[[2,1],[1,1]]` (standard exercise).

## Links
[[determinant-expansion]] · [[lu-decomposition]]
