---
id: method-of-stationary-phase
name: Method of stationary phase (oscillatory integrals)
domain: asymptotics
regime: asymptotic_expansion
status: verified
---

## Applies when (recognition signature)
You want the **large-`λ` asymptotics** of an **oscillatory** integral
`∫ g(x) e^{iλ φ(x)} dx` with `φ` real. Tells: a purely imaginary exponent
`e^{i·λ·(phase)}`, rapid oscillation, a Fourier-type integral as frequency `→ ∞`,
or `cos`/`sin` of a large phase. The dominant contributions come from
**stationary points** `φ'(x₀)=0` where the oscillation momentarily stalls;
away from those points the wiggles cancel. (Real-exponent peaks ⇒ saddle point /
Laplace instead.)

## The rule
Sum over stationary points `x₀` (`φ'(x₀)=0`, `φ''(x₀)≠0`):
`∫ g(x) e^{iλ φ(x)} dx ~ Σ_{x₀} g(x₀) e^{iλ φ(x₀)} √(2π / (λ|φ''(x₀)|)) e^{± iπ/4}`
as `λ → ∞`, where the sign of the `π/4` phase is `sign(φ''(x₀))`. It is the
Gaussian/Fresnel integral of the local quadratic phase; non-stationary endpoints
contribute only at higher order (`O(1/λ)`).

## Worked example
`∫_{−∞}^∞ e^{iλ x²} dx = √(π/λ) e^{iπ/4}` (a Fresnel integral). Here `φ(x)=x²`,
the single stationary point is `x₀=0` with `φ''=2>0`, and the rule reproduces the
exact value: `g(0)=1`, `√(2π/(λ·2)) e^{iπ/4} = √(π/λ) e^{iπ/4}`. Exact, not just
asymptotic, because the phase is already quadratic.

## Explain (altitudes)
- **expert** — rotate the contour to steepest descent through each stationary point;
  the local quadratic phase gives a Fresnel kernel whose `±π/4` Maslov phase encodes
  the signature of `φ''`, and the asymptotic series follows from higher Taylor terms.
- **working** — where the phase is changing fast the contributions cancel; only near
  `φ'=0` does the integrand add coherently, so replace `φ` by its quadratic there and
  do the Fresnel integral, picking up `e^{±iπ/4}`.
- **plain** — a wildly wiggling signal averages to nothing except where the wiggling
  briefly pauses; add up just those pause points and you have the answer.

## LaTeX
rule: \int g(x)\,e^{i\lambda \varphi(x)}\,dx\;\sim\;\sum_{\varphi'(x_0)=0} g(x_0)\,e^{i\lambda \varphi(x_0)}\sqrt{\frac{2\pi}{\lambda\,|\varphi''(x_0)|}}\;e^{\pm i\pi/4}\qquad(\lambda\to\infty)
example: \int_{-\infty}^{\infty}e^{i\lambda x^{2}}\,dx=\sqrt{\frac{\pi}{\lambda}}\,e^{i\pi/4}
## References
- Bender & Orszag, *Advanced Mathematical Methods*, §6.5; DLMF 2.3(iii).
- Gradshteyn–Ryzhik 3.691 (Fresnel-type integrals).
- Library: mpmath `quadosc` (oscillatory verification), `fresnels`/`fresnelc`.
- Worked example: Fresnel integral `∫ e^{iλx²}dx`, standard (Bender & Orszag §6.5).

## Links
[[fresnel-integral]] · [[saddle-point-method]] · [[watsons-lemma]]
