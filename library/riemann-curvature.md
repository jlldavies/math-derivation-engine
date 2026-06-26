---
id: riemann-curvature
name: Riemann curvature tensor from the connection
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
You have the Christoffel symbols (or a metric) and need the *curvature* — to test
whether a space is flat, to compute tidal forces, or to feed the Ricci tensor /
Einstein equations. Tells: "Riemann tensor", "curvature", "R^a_bcd", "is the space
flat?", "commutator of covariant derivatives", "tidal/geodesic deviation".

## The rule
`R^a_bcd = ∂_c Γ^a_db − ∂_d Γ^a_cb + Γ^a_ce Γ^e_db − Γ^a_de Γ^e_cb`. Equivalently it
is the commutator of covariant derivatives acting on a vector,
`(∇_c ∇_d − ∇_d ∇_c) V^a = R^a_bcd V^b`. It is antisymmetric in the last pair
`(c,d)` and, with the first index lowered, antisymmetric in `(a,b)`, symmetric under
pair exchange, and obeys the first Bianchi identity. The space is flat iff
`R^a_bcd = 0` everywhere.

## Worked example
The **unit 2-sphere**, `ds² = dθ² + sin²θ dφ²`. With `Γ^θ_φφ = −sinθ cosθ` and
`Γ^φ_θφ = cotθ`, the single independent component is `R_θφθφ = sin²θ` (equivalently
`R^θ_φθφ = sin²θ`). Every other component is fixed by the symmetries; a nonzero
`R` confirms the sphere is curved.

## Explain (altitudes)
- **expert** — the curvature 2-form `R = dω + ω∧ω` of the Levi-Civita connection;
  its failure to vanish is the holonomy obstruction and the source term in the
  Einstein equations via its contractions.
- **working** — differentiate the Christoffels (`∂_c Γ − ∂_d Γ`), add the two
  quadratic `ΓΓ` terms, and use the antisymmetries to compute only the independent
  components (one for the 2-sphere).
- **plain** — curvature measures how much a vector gets twisted when you carry it
  around a tiny loop; on a flat sheet nothing changes, on a sphere it comes back
  rotated, and `R` is the size of that twist.

## LaTeX
rule: R^{a}{}_{bcd}=\partial_c\Gamma^{a}{}_{db}-\partial_d\Gamma^{a}{}_{cb}+\Gamma^{a}{}_{ce}\Gamma^{e}{}_{db}-\Gamma^{a}{}_{de}\Gamma^{e}{}_{cb}
example: ds^2=d\theta^2+\sin^2\theta\,d\phi^2\ \Longrightarrow\ R_{\theta\phi\theta\phi}=\sin^2\theta

## References
- D'Inverno, *Introducing Einstein's Relativity*, §6 (the curvature tensor).
- Misner, Thorne & Wheeler, *Gravitation*, §11. Wald, *General Relativity*, §3.2.

## Links
[[christoffel-symbols]] · [[ricci-tensor-scalar]] · [[covariant-derivative]]
