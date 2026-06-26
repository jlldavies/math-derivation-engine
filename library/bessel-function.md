---
id: bessel-function
name: Bessel J — the oscillatory cylinder function
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
Integrals `∫_0^π cos(nθ − x sinθ) dθ`, or the ODE `x²y'' + xy' + (x²−n²)y = 0`
(cylindrical / radial separation), or Laplace/Hankel transforms of oscillatory
radial data. Tells: cylindrical symmetry, wave equation in polar coordinates,
`J_n(x)` appearing in diffraction / FM-spectrum / drum-mode problems.

## The rule
`J_n(x) = (1/π) ∫_0^π cos(nθ − x sinθ) dθ` (integer `n`) solves
`x²y'' + xy' + (x²−n²)y = 0`. Laplace transform:
`∫_0^∞ e^{-px} J_0(ax) dx = 1/√(a²+p²)` for `Re p > |Im a|`.

## Worked example
`∫_0^∞ e^{-px} J_0(ax) dx = 1/√(a²+p²)`. Expand `J_0(ax) = Σ_k (−1)^k (ax/2)^{2k}/(k!)²`,
integrate termwise with `∫_0^∞ e^{-px}x^{2k}dx = (2k)!/p^{2k+1}`, and the series sums
to `p^{-1}(1+a²/p²)^{-1/2} = 1/√(a²+p²)` (mpmath `besselj`).

## Explain (altitudes)
- **expert** — `J_n` is the entire solution of Bessel's equation regular at the
  origin; the integral form is the `n`-th Fourier coefficient of the plane wave
  `e^{ix sinθ}` (Jacobi–Anger), and the Laplace transform is the `s`-plane image of
  the generating-function / Hankel structure.
- **working** — `J_0`'s power series integrates term-by-term against `e^{-px}`
  (each term a Gamma integral); the resulting binomial series is `(a²+p²)^{-1/2}`.
- **plain** — `J_n` is the "sine and cosine" for round drums; its Laplace transform
  is the neat closed form `1/√(a²+p²)`.

## LaTeX
rule: J_n(x)=\frac{1}{\pi}\int_{0}^{\pi}\cos\!\left(n\theta-x\sin\theta\right)d\theta,\qquad x^2y''+xy'+(x^2-n^2)y=0
example: \int_{0}^{\infty}e^{-px}J_0(ax)\,dx=\frac{1}{\sqrt{a^2+p^2}}

## References
- DLMF 10.9.1 (integral rep), 10.2.1 (ODE), 10.22.43 (Laplace transform).
- Gradshteyn–Ryzhik 6.611.1. SymPy/mpmath `besselj`.

## Links
[[gamma-function]] · [[hypergeometric-2f1]] · [[laplace-transform]]
