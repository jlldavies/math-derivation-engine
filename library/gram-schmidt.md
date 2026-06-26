---
id: gram-schmidt
name: Gram–Schmidt orthonormalisation
domain: linear-algebra
regime: linear_algebra
status: drafted
---

## Applies when (recognition signature)
You have a set of linearly independent vectors (or a spanning set) and want an
**orthonormal** basis for the same span. Tells: "orthonormalise", "orthogonal
basis", "Gram–Schmidt", building `Q` for a QR factorisation, projecting onto a
subspace, orthogonal polynomials.

## The rule
Process the `v_k` in order, subtracting off their components along the already-built
orthonormal vectors `e_j` (`j<k`), then normalise:
`u_k = v_k − Σ_{j<k} ⟨v_k, e_j⟩ e_j`, `e_k = u_k / ‖u_k‖`.
Each `u_k` is the part of `v_k` orthogonal to `span(v_1,…,v_{k−1})`; the `{e_k}`
are orthonormal and span the same space step by step. (Modified Gram–Schmidt
reorders the subtractions for numerical stability.)

## Worked example
In ℝ²: `v₁=(1,1)`, `v₂=(1,0)`. `e₁ = v₁/√2 = (1,1)/√2`.
`u₂ = v₂ − ⟨v₂,e₁⟩e₁ = (1,0) − (1/√2)(1,1)/√2 = (1,0) − (½,½) = (½,−½)`,
so `e₂ = (1,−1)/√2`. The pair `{(1,1)/√2, (1,−1)/√2}` is orthonormal.
(Verify `⟨e₁,e₂⟩ = 0`, `‖e₁‖=‖e₂‖=1`.)

## Explain (altitudes)
- **expert** — Gram–Schmidt is the orthogonal projection `u_k = (I − P_{k−1})v_k`
  onto the orthogonal complement of the running subspace; collecting the steps gives
  `A = QR` with `R` upper-triangular holding the coefficients `⟨v_k,e_j⟩` and `‖u_k‖`.
- **working** — take each new vector, subtract its shadow on every direction you've
  already fixed (so what's left is perpendicular to them), then scale to unit length.
- **plain** — straighten a tilted set of arrows into perpendicular ones: for each
  arrow, remove the parts that point along arrows you've already straightened, keep
  the leftover, and shrink it to length one.

## LaTeX
rule: \mathbf u_k=\mathbf v_k-\sum_{j<k}\langle \mathbf v_k,\mathbf e_j\rangle\,\mathbf e_j,\qquad \mathbf e_k=\frac{\mathbf u_k}{\left\lVert \mathbf u_k\right\rVert}
example: \mathbf e_1=\frac{1}{\sqrt2}\left[\begin{matrix}1\\1\end{matrix}\right],\quad \mathbf e_2=\frac{1}{\sqrt2}\left[\begin{matrix}1\\-1\end{matrix}\right]

## References
- Strang, *Linear Algebra and Its Applications*, §3.4 (orthogonalisation, QR).
- Trefethen & Bau, *Numerical Linear Algebra*, lectures 7–8 (classical vs modified).
- Library: NumPy via `numpy.linalg.qr`; SymPy `GramSchmidt`.
- Worked example: `(1,1),(1,0)` in ℝ² (standard text exercise).

## Links
[[qr-decomposition]] · [[singular-value-decomposition]]
