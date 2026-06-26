---
id: ricci-tensor-scalar
name: Ricci tensor and Ricci scalar by contraction
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
You have the Riemann tensor (or a metric) and need its contractions — for the
Einstein equations, to classify a spacetime, or to get a single curvature number.
Tells: "Ricci tensor", "Ricci scalar", "scalar curvature", "R_ab", "trace of the
curvature", "Einstein tensor", "curvature of this metric".

## The rule
Contract Riemann on its first and third indices for the Ricci tensor,
`R_bd = R^a_bad`, which is symmetric (`R_bd = R_db`). Contract again with the
inverse metric for the Ricci scalar, `R = g^{bd} R_bd`. For a maximally symmetric
`n`-space of radius `a`, `R_bd = ((n−1)/a²) g_bd` and `R = n(n−1)/a²`.

## Worked example
The **unit 2-sphere** (`a = 1`, `n = 2`): from `R_θφθφ = sin²θ` the Ricci tensor is
`R_bd = g_bd` and the scalar is `R = 2`. For a sphere of radius `a`, `R = 2/a²`
(positive, constant — the Gaussian curvature is `1/a²` and `R = 2K`). De Sitter
space in `n = 4` likewise has constant positive `R = 12/a²`.

## Explain (altitudes)
- **expert** — `R_bd` is the trace of the curvature endomorphism on each tangent
  direction; for an Einstein space `R_bd ∝ g_bd`, and `R` is the full double trace,
  the scalar driving the Einstein–Hilbert action.
- **working** — sum `R^a_bad` over the repeated index `a` to get `R_bd`, then raise
  and contract with `g^{bd}` to get the single number `R`.
- **plain** — the Ricci scalar boils all the curvature down to one number: how much
  the surface bends on average at a point — `2` for a unit sphere, `0` for a flat
  plane.

## LaTeX
rule: R_{bd}=R^{a}{}_{bad},\qquad R=g^{bd}R_{bd}
example: \text{unit }S^2:\ R_{bd}=g_{bd},\ R=2\quad\Longrightarrow\quad \text{radius }a:\ R=\frac{2}{a^{2}}

## References
- D'Inverno, *Introducing Einstein's Relativity*, §6 and §22 (de Sitter).
- Misner, Thorne & Wheeler, *Gravitation*, §13. Hartle, *Gravity*, §21.

## Links
[[riemann-curvature]] · [[christoffel-symbols]] · [[metric-transformation-law]]
