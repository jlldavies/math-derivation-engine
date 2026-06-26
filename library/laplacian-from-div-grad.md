---
id: laplacian-from-div-grad
name: Laplacian = divergence of gradient
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
The divergence of a gradient, `∇·(∇φ)`; or wherever "how a point differs from its
neighbourhood average" appears (heat, diffusion, potentials, harmonic functions).

## The rule
`∇·∇φ = ∇²φ = ∂²φ/∂x² + ∂²φ/∂y² + ∂²φ/∂z²` — the **trace of the Hessian**
`tr(∂_i∂_j φ)`. (Contrast curl-of-grad, which is the *antisymmetric* part and
vanishes — see [[sym-antisym-contraction]].)

## Worked example
`∇·∇φ = φ_xx + φ_yy + φ_zz` (SymPy confirms `div(grad φ)` equals the sum of pure
second derivatives).

## Explain (altitudes)
- **expert** — the Laplace–Beltrami operator; the symbol of diffusion (heat
  kernel) and, with a sign, the wave operator; `ker Δ` = harmonic functions
  (mean-value property). It is the *trace* (symmetric contraction) of the Hessian,
  the complement of the curl's antisymmetric part.
- **working** — divergence of gradient = sum of the pure second derivatives = the
  trace of the matrix of second partials.
- **plain** — how much a point sits above or below the average of its immediate
  neighbours — curvature added up over all directions.

## LaTeX
rule: \nabla\cdot\nabla\phi=\nabla^{2}\phi=\partial_x^{2}\phi+\partial_y^{2}\phi+\partial_z^{2}\phi
example: \nabla^{2}\phi=\operatorname{tr}\!\big(\partial_i\partial_j\phi\big)

## References
- DLMF / any PDE text; SymPy `divergence(gradient(φ))`.

## Links
[[sym-antisym-contraction]] · [[div-of-curl]] · [[gaussian-integral]]
