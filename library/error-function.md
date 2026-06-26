---
id: error-function
name: Error function — the partial Gaussian
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
A **partial** Gaussian integral `∫ e^{-t²} dt` (not the whole line, so the
square-and-polar trick of [[gaussian-integral]] fails); a Gaussian tail; the
cumulative normal probability.

## The rule
`∫ e^{-t²} dt = (√π/2) erf(t)`, where `erf(x) = (2/√π) ∫_0^x e^{-t²} dt`,
`erf(∞)=1`, `erf(-x)=-erf(x)`. The antiderivative is **non-elementary** — so it is
*named*.

## Worked example
`∫ e^{-t²} dt = (√π/2) erf(t)`;  `∫_{-∞}^{∞} e^{-t²} dt = √π` (SymPy — consistent
with the Gaussian page).

## Explain (altitudes)
- **expert** — the non-elementary antiderivative of the Gaussian; the normal CDF
  up to scaling; an incomplete gamma `γ(½, x²)`; entire, with asymptotics
  `erf(x) ~ 1 − e^{-x²}/(x√π)`.
- **working** — the *whole-line* Gaussian is `√π` by symmetry, but a *partial* one
  has no elementary antiderivative — so we name the partial area `erf`.
- **plain** — the running total of the bell curve out from the centre; there's no
  simple formula, so it was given a name.

## LaTeX
rule: \int e^{-t^{2}}\,dt=\tfrac{\sqrt{\pi}}{2}\,\operatorname{erf}(t)
example: \operatorname{erf}(x)=\tfrac{2}{\sqrt{\pi}}\int_{0}^{x}e^{-t^{2}}\,dt

## References
- DLMF 7.2; SymPy / mpmath `erf`.

## Links
[[gaussian-integral]] · [[gamma-function]] · [[fresnel-integral]]
