---
id: christoffel-symbols
name: Christoffel symbols of the Levi-Civita connection
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
You have a metric `g_{ab}` (a line element `ds²`) and need the connection
coefficients — for a covariant derivative, a geodesic equation, or curvature.
Tells: "Christoffel symbols", "connection", "Γ^a_bc", "compute the geodesics of
this metric", "is this spacetime flat?", any GR problem that starts from `ds²`.

## The rule
For the unique torsion-free, metric-compatible (Levi-Civita) connection,
`Γ^a_bc = ½ g^{ad}(∂_b g_dc + ∂_c g_db − ∂_d g_bc)`. It is symmetric in the lower
pair, `Γ^a_bc = Γ^a_cb` (torsion-free), and it is the *only* connection with both
`∇_a g_bc = 0` and zero torsion. The `g^{ad}` is the inverse metric; the bracket
is built purely from first derivatives of the metric, so flat (constant-component)
metrics give `Γ = 0`.

## Worked example
The **Bondi radiating metric** (D'Inverno §21, ex. 21.5). Its 20 independent
non-zero Christoffel components were computed from the rule above and matched
component-for-component to D'Inverno's printed answer — every one agreed.
Code: `examples/bondi_christoffel.py` (SymPy builds `g^{ad}`, differentiates,
contracts; verified against metric compatibility `∇_a g_bc = 0`).

## Explain (altitudes)
- **expert** — the fundamental theorem of (pseudo-)Riemannian geometry: torsion-free
  + metric-compatible fixes the connection uniquely, and solving those two conditions
  for `Γ` gives exactly the Koszul half-sum of metric derivatives.
- **working** — invert the metric, take the three first-derivative terms
  `∂_b g_dc + ∂_c g_db − ∂_d g_bc`, contract with `½ g^{ad}`; exploit symmetry in
  `b,c` so you only do each pair once.
- **plain** — the Christoffel symbols are the "correction terms" that tell you how
  the coordinate grid itself bends, so that straight lines and rates of change still
  make sense on a curved surface; they are read off from how the metric changes.

## LaTeX
rule: \Gamma^{a}{}_{bc}=\frac{1}{2}\,g^{ad}\left(\partial_b g_{dc}+\partial_c g_{db}-\partial_d g_{bc}\right)
example: \Gamma^{a}{}_{bc}=\Gamma^{a}{}_{cb},\qquad \nabla_a g_{bc}=0\ \Longrightarrow\ \text{20 non-zero components (Bondi metric)}

## References
- D'Inverno, *Introducing Einstein's Relativity*, §10 and exercise 21.5 (Bondi metric).
- Misner, Thorne & Wheeler, *Gravitation*, §8 (the connection).
- Wald, *General Relativity*, §3.1. Library: SymPy (`examples/bondi_christoffel.py`).

## Links
[[metric-transformation-law]] · [[covariant-derivative]] · [[riemann-curvature]] · [[raising-lowering-indices]] · [[geodesic-equation]]
