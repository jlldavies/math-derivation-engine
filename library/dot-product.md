---
id: dot-product
name: Dot (scalar) product
domain: tensor
regime: elementary
status: drafted
---

## Applies when (recognition signature)
You need a **single number** measuring how much two vectors point the same way:
testing perpendicularity, projecting one vector onto another, finding the angle
between them, or computing work `F·d`. Tell: two vectors and a question about
angle, length, or "are these at right angles?".

## The rule
For vectors `a`, `b` in ℝⁿ:

`a · b = Σ_i a_i b_i = a₁b₁ + a₂b₂ + … = |a| |b| cos θ`,

where `θ` is the angle between them. Consequences: `a · a = |a|²`;
`a ⊥ b ⇔ a · b = 0`; and the scalar projection of `a` onto `b` is
`a · b / |b|`.

## Worked example
`a = (1, 2, 2)`, `b = (2, −1, 0)`: `a · b = 1·2 + 2·(−1) + 2·0 = 0`, so they are
**orthogonal**. The scalar projection of `a` onto `c = (3, 4, 0)` is
`a · c / |c| = (3 + 8 + 0)/5 = 11/5`.

## Explain (altitudes)
- **expert** — the Euclidean metric contracted on two vectors, `g_{ij} a^i b^j`;
  on an orthonormal basis `g_{ij} = δ_{ij}` and it reduces to the coordinate sum.
  It is the symmetric, positive-definite bilinear form that defines lengths and
  angles.
- **working** — multiply matching components and add. The result equals
  `|a||b|cosθ`, so dividing by the lengths gives `cosθ`; a zero result means the
  vectors are perpendicular, and `a·b/|b|` is how far `a` reaches along `b`.
- **plain** — multiply the matching numbers of two vectors and add them up. If you
  get zero the arrows are at right angles. The bigger the answer (for fixed
  lengths) the more the two arrows point the same way.

## LaTeX
rule: \mathbf{a}\cdot\mathbf{b}=\sum_{i}a_{i}b_{i}=\left|\mathbf{a}\right|\left|\mathbf{b}\right|\cos\theta
example: \left(1,2,2\right)\cdot\left(2,-1,0\right)=2-2+0=0\ \Rightarrow\ \mathbf{a}\perp\mathbf{b}

## References
- A-level "Vectors" (scalar product); first-year linear algebra (Anton; Strang).
- Library: SymPy `Matrix.dot`.

## Links
[[cross-product]] · [[epsilon-delta-identity]]
