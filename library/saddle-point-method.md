---
id: saddle-point-method
name: Saddle point / Laplace's method (steepest descent)
domain: asymptotics
regime: asymptotic_expansion
status: verified
---

## Applies when (recognition signature)
You want the **large-parameter `λ → ∞` asymptotics** of an integral of the form
`∫_C e^{λ φ(z)} g(z) dz` (contour or real). The integrand has a sharp peak at an
interior point where the exponent is stationary. Tells: `e^{λ·(something)}` or
`(big number)^N`, factorials / Γ at large argument, "leading behaviour as `λ → ∞`",
`∫ e^{N f(x)} dx`; the peak is NOT at an endpoint (that is Watson's lemma) and the
exponent is real-dominated (oscillatory ⇒ stationary phase).

## The rule
Locate the saddle `z₀` with `φ'(z₀) = 0`. Expand `φ(z) ≈ φ(z₀) + ½ φ''(z₀)(z−z₀)²`
and do the Gaussian integral along the steepest-descent direction:
`∫_C e^{λ φ(z)} g(z) dz ~ g(z₀) e^{λ φ(z₀)} √(2π / (λ(−φ''(z₀))))`  as `λ → ∞`.
For a real maximum (Laplace's method) `−φ''(z₀) > 0`; on a complex contour the
phase of the square root is fixed by the descent direction. Higher orders come
from carrying more terms of the Taylor expansion of `φ` and `g`.

## Worked example
Stirling's formula from `Γ(λ+1) = ∫_0^∞ t^λ e^{−t} dt = ∫_0^∞ e^{λ ln t − t} dt`.
Write `t = λ x` so the exponent is `λ(ln(λx) − x)`; the saddle in `x` is `x₀ = 1`
(i.e. `t₀ = λ`), with second derivative `−1/x₀² = −1`. The rule gives
`Γ(λ+1) ~ √(2πλ) (λ/e)^λ` as `λ → ∞`. Verified against mpmath `gamma`.

## Explain (altitudes)
- **expert** — deform `C` onto a steepest-descent path through the saddle where
  `Im φ` is constant; the integral localizes Gaussianly, `−φ''(z₀)` sets the width,
  and the full asymptotic series is the Laplace expansion of the local data.
- **working** — the integrand is dominated by a single bump where `φ'=0`; replace
  `φ` by its quadratic Taylor polynomial there and integrate the resulting Gaussian,
  giving `√(2π/(λ|φ''|))` times the peak value.
- **plain** — almost all of the area sits under one tall narrow spike; measure the
  spike's height and how fast it falls off, and that is essentially the whole answer.

## LaTeX
rule: \int_{C}e^{\lambda \varphi(z)}g(z)\,dz\;\sim\;g(z_0)\,e^{\lambda \varphi(z_0)}\sqrt{\frac{2\pi}{\lambda\left(-\varphi''(z_0)\right)}}\qquad(\lambda\to\infty,\ \varphi'(z_0)=0)
example: \Gamma(\lambda+1)=\int_{0}^{\infty}e^{\lambda\ln t-t}\,dt\;\sim\;\sqrt{2\pi\lambda}\left(\frac{\lambda}{e}\right)^{\lambda}
## References
- Bender & Orszag, *Advanced Mathematical Methods*, §6.4 (Laplace) and §6.6 (steepest descent); DLMF 2.4.
- DLMF 5.11.1 (Stirling series for `Γ`).
- Library: mpmath `gamma` (verification), SymPy `gamma`.
- Worked example: Stirling's approximation, standard (Bender & Orszag §3.3, §6.4).

## Links
[[watsons-lemma]] · [[method-of-stationary-phase]] · [[gamma-function]] · [[gaussian-integral]]
