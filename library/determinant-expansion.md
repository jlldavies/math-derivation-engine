---
id: determinant-expansion
name: Determinant by cofactor (Laplace) expansion
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
You need a determinant of a small or structured matrix (a row/column with zeros),
or the symbolic form of `det A`. Tells: "determinant", "expand along a row/column",
"cofactor", "minor", `det A`, "Laplace expansion", invertibility test (`det ≠ 0`).

## The rule
Pick any row `i` (or column `j`) and expand:
`det A = Σ_j (−1)^{i+j} a_{ij} M_{ij}`, where the **minor** `M_{ij}` is the
determinant of `A` with row `i` and column `j` deleted, and `(−1)^{i+j} M_{ij}` is
the **cofactor** `C_{ij}`. Choose the row/column with the most zeros to minimise
work. (For numerics, prefer LU: cofactor expansion is `O(n!)`.)

## Worked example
`A = [[1,2,3],[4,5,6],[7,8,10]]`, expand along row 1:
`det = 1·(5·10−6·8) − 2·(4·10−6·7) + 3·(4·8−5·7)`
`    = 1·(50−48) − 2·(40−42) + 3·(32−35) = 2 + 4 − 9 = −3`.
(SymPy: `Matrix([[1,2,3],[4,5,6],[7,8,10]]).det()` → `−3`.)

## Explain (altitudes)
- **expert** — Laplace expansion is the alternating-multilinear `n`-form evaluated
  by linearity in one slot; each cofactor is the induced `(n−1)`-form on the
  complementary block, with the sign the parity of the transposition pattern. It is
  the row-of-`adj A` identity `A·adj A = (det A)I` read one entry at a time.
- **working** — sweep across one row; each entry times the (signed) determinant of
  the smaller matrix you get by crossing out its row and column, alternating + − +.
- **plain** — break a big determinant into smaller ones: go along a row, and for
  each number multiply it by the determinant of what's left after you hide its row
  and column, flipping the sign as you step across.

## LaTeX
rule: \det A=\sum_{j=1}^{n}(-1)^{i+j}\,a_{ij}\,M_{ij},\qquad M_{ij}=\det\!\big(A\ \text{minus row }i,\ \text{col }j\big)
example: \det\left[\begin{matrix}1&2&3\\4&5&6\\7&8&10\end{matrix}\right]=1(2)-2(-2)+3(-3)=-3

## References
- Strang, *Linear Algebra and Its Applications*, §4.2 (cofactors).
- Axler, *Linear Algebra Done Right*, ch. on determinants.
- Library: SymPy `Matrix.det()`; NumPy `numpy.linalg.det` (via LU).
- Worked example: `[[1,2,3],[4,5,6],[7,8,10]]`, `det = −3` (standard exercise).

## Links
[[matrix-inverse]] · [[eigendecomposition]] · [[lu-decomposition]]
