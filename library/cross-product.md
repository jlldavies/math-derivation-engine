---
id: cross-product
name: Cross (vector) product
domain: tensor
regime: elementary
status: drafted
---

## Applies when (recognition signature)
You need a vector **perpendicular to two given vectors** in 3-D, or an oriented
area/volume: a normal to a plane, the area of a parallelogram or triangle, a
torque `r × F`, or a moment. Tell: two 3-D vectors and a question about a normal
direction, area, or "perpendicular to both".

## The rule
For `a`, `b` in ℝ³, the cross product is the vector with components

`(a × b)_i = ε_{ijk} a_j b_k`  (sum over `j, k`),

i.e. `a × b = (a₂b₃ − a₃b₂, a₃b₁ − a₁b₃, a₁b₂ − a₂b₁)`. Its magnitude is
`|a × b| = |a| |b| sin θ` (the area of the parallelogram spanned by `a`, `b`), it
is perpendicular to both, and its direction follows the right-hand rule. It is
antisymmetric: `b × a = − a × b`.

## Worked example
`a = (1, 0, 0)`, `b = (0, 1, 0)`: `a × b = (0·0 − 0·1, 0·0 − 1·0, 1·1 − 0·0)
= (0, 0, 1)`. So `î × ĵ = k̂`, a unit normal to the `xy`-plane, and the
parallelogram they span has area `|a × b| = 1`.

## Explain (altitudes)
- **expert** — in index form `(a×b)_i = ε_{ijk}a^j b^k`, the Hodge dual of the
  wedge `a ∧ b`; antisymmetry of `ε` forces antisymmetry of the product, and the
  ε–δ identity links `(a×b)·(c×d)` back to dot products. It is special to three
  dimensions (where 2-forms and 1-forms have equal rank).
- **working** — the Levi-Civita symbol `ε_{ijk}` (which is `+1`/`−1` for
  even/odd permutations of `123`, `0` if any index repeats) packages the
  determinant rule. Read off each component as a `2×2` determinant; the result is
  perpendicular to both inputs with length `|a||b|sinθ`.
- **plain** — given two arrows in space, the cross product is a new arrow at right
  angles to both, with length equal to the area of the parallelogram they make.
  Point your right hand's fingers from the first arrow to the second and your
  thumb shows which way it points.

## LaTeX
rule: \left(\mathbf{a}\times\mathbf{b}\right)_{i}=\varepsilon_{ijk}\,a_{j}\,b_{k},\qquad \left|\mathbf{a}\times\mathbf{b}\right|=\left|\mathbf{a}\right|\left|\mathbf{b}\right|\sin\theta
example: \left(1,0,0\right)\times\left(0,1,0\right)=\left(0,0,1\right)

## References
- A-level Further Maths / first-year "Vector product"; standard in vector calculus
  texts (Anton; Griffiths, *Introduction to Electrodynamics*).
- Library: SymPy `Matrix.cross`.

## Links
[[dot-product]] · [[epsilon-delta-identity]] · [[sym-antisym-contraction]]
