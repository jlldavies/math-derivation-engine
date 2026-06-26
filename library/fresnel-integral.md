---
id: fresnel-integral
name: Fresnel integrals — the oscillatory Gaussian
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
Oscillatory Gaussian-like integrals `∫ cos(x²) dx`, `∫ sin(x²) dx`, or chirped
oscillations like `∫ cos(x)/√x dx`; diffraction patterns. The oscillatory cousin
of the Gaussian (an *imaginary* variance).

## The rule
`∫_0^∞ cos(x²) dx = ∫_0^∞ sin(x²) dx = √(π/8) = ½√(π/2)`; the Fresnel functions
`C(x)=∫_0^x cos(πt²/2)dt`, `S(x)` similarly. These are the Gaussian integral
*continued to an imaginary exponent* — `erf` with an imaginary argument.

## Worked example
`∫_0^∞ cos(x²) dx = √(π/8) = 0.6266…` (mpmath, verified). Also
`∫_0^∞ cos(x)/√x dx = √(π/2)` — the divergent-oscillatory example in
`examples/meijerg_demo.py`.

## Explain (altitudes)
- **expert** — the Gaussian integral analytically continued to imaginary variance:
  Fresnel = `erf` on the diagonal of the complex plane; the prototype of
  stationary phase; the Cornu spiral is the plot of `(C,S)`.
- **working** — same trick as the Gaussian but with an imaginary exponent — the
  oscillation replaces the decay; rotate the contour (or substitute) and read off
  `√(π/8)`.
- **plain** — like the bell-curve integral, but the curve wiggles instead of
  decaying; the wiggles mostly cancel and leave a tidy `√(π/8)`.

## LaTeX
rule: \int_{0}^{\infty}\cos(x^{2})\,dx=\int_{0}^{\infty}\sin(x^{2})\,dx=\tfrac{1}{2}\sqrt{\tfrac{\pi}{2}}
example: \int_{0}^{\infty}\frac{\cos x}{\sqrt{x}}\,dx=\sqrt{\tfrac{\pi}{2}}

## References
- DLMF 7.2 (Fresnel integrals); SymPy `fresnelc`, `fresnels`; mpmath.

## Links
[[gaussian-integral]] · [[error-function]] · [[watsons-lemma]] · [[tricomi-u-reduction]]
