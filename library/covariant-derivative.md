---
id: covariant-derivative
name: Covariant derivative of tensors
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
You need to differentiate a vector / covector / tensor field on a curved space so
the result is still a tensor. Tells: "covariant derivative", "∇_b", "nabla",
"parallel transport", "divergence/curl in curved space", "is `∂_a T` a tensor?",
"metric compatibility".

## The rule
For a vector, `∇_b V^a = ∂_b V^a + Γ^a_bc V^c`; for a covector,
`∇_b ω_a = ∂_b ω_a − Γ^c_ba ω_c`. Each upper index adds a `+Γ` term, each lower
index subtracts a `Γ` term, and `∇_b f = ∂_b f` on scalars. The Christoffel terms
cancel the non-tensorial part of `∂_b`, so `∇` maps tensors to tensors. The
Levi-Civita connection is **metric-compatible**: `∇_a g_bc = 0`.

## Worked example
**Metric compatibility** `∇_a g_bc = 0`. Expanding,
`∂_a g_bc − Γ^d_ab g_dc − Γ^d_ac g_bd = 0`, which is exactly the symmetrized
Christoffel definition rearranged — so it holds identically for the Levi-Civita
`Γ`. This identity was used to **confirm the Bondi Christoffels**: every computed
component satisfies `∇_a g_bc = 0` (`examples/bondi_christoffel.py`).

## Explain (altitudes)
- **expert** — the unique connection `∇` with `∇g = 0` and zero torsion; the `Γ`
  terms are the connection coefficients in a coordinate basis, restoring tensoriality
  lost by the partial derivative.
- **working** — write `∂_b` of the component, then add `+Γ^a_bc(·)` for each upper
  index and subtract `−Γ^c_ba(·)` for each lower index; check your `Γ`s by verifying
  `∇_a g_bc = 0`.
- **plain** — on a curved surface the coordinate grid bends, so a plain derivative
  mixes in fake changes from the grid; the covariant derivative subtracts that grid
  bending and keeps only the real change in the field.

## LaTeX
rule: \nabla_b V^{a}=\partial_b V^{a}+\Gamma^{a}{}_{bc}V^{c},\qquad \nabla_b \omega_a=\partial_b\omega_a-\Gamma^{c}{}_{ba}\,\omega_c
example: \nabla_a g_{bc}=\partial_a g_{bc}-\Gamma^{d}{}_{ab}g_{dc}-\Gamma^{d}{}_{ac}g_{bd}=0

## References
- D'Inverno, *Introducing Einstein's Relativity*, §6 (covariant differentiation).
- Wald, *General Relativity*, §3.1. Misner, Thorne & Wheeler, *Gravitation*, §10.
- Library: SymPy (`examples/bondi_christoffel.py`, metric-compatibility check).

## Links
[[christoffel-symbols]] · [[raising-lowering-indices]] · [[riemann-curvature]]
