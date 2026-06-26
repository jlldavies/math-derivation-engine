---
id: beta-function
name: Beta function — the Gamma-ratio integral
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
`∫_0^1 t^{a-1} (1−t)^{b-1} dt` — a power of `t` times a power of `(1−t)` over the
unit interval. Tells: two powers summing the endpoints `0` and `1`; trigonometric
moments `∫_0^{π/2} sin^m θ cos^n θ dθ` after `t = sin²θ`; ratios of factorials in
normalizations.

## The rule
`B(a,b) = ∫_0^1 t^{a-1} (1−t)^{b-1} dt = Γ(a)Γ(b)/Γ(a+b)` for `Re a, Re b > 0`.
Symmetric in `a,b`; continues meromorphically via the Gamma ratio. Trig form:
`∫_0^{π/2} sin^{2a-1}θ cos^{2b-1}θ dθ = ½ B(a,b)`.

## Worked example
`B(½,½) = Γ(½)²/Γ(1) = (√π)²/1 = π`. Equivalently
`∫_0^1 dt/√(t(1−t)) = π` (SymPy / mpmath).

## Explain (altitudes)
- **expert** — the Euler integral of the first kind; the Gamma-ratio identity
  follows from the 2D integral `Γ(a)Γ(b) = ∫∫ x^{a-1}y^{b-1}e^{-(x+y)}` in polar-like
  coordinates `x = u t, y = u(1−t)`, which factorizes into `Γ(a+b)·B(a,b)`.
- **working** — substitute `x = u t`, `y = u(1−t)` in the product `Γ(a)Γ(b)`; the
  Jacobian gives `u`, the `u`-integral is `Γ(a+b)`, and the `t`-integral is `B(a,b)`.
- **plain** — a tidy "name" answer for the integral of `t^{a-1}(1−t)^{b-1}` on
  `[0,1]`: it is just a ratio of factorials (Gammas), so `B(½,½)=π`.

## LaTeX
rule: B(a,b)=\int_{0}^{1}t^{a-1}(1-t)^{b-1}\,dt=\frac{\Gamma(a)\,\Gamma(b)}{\Gamma(a+b)}
example: B\!\left(\tfrac12,\tfrac12\right)=\frac{\Gamma(1/2)^2}{\Gamma(1)}=\frac{\left(\sqrt{\pi}\right)^2}{1}=\pi

## References
- DLMF 5.12 (beta integral); Gradshteyn–Ryzhik 3.191, 8.380.
- SymPy / mpmath `beta`.

## Links
[[gamma-function]] · [[gaussian-integral]] · [[hypergeometric-2f1]]
