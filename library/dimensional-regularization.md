---
id: dimensional-regularization
name: Dimensional regularization — d-dimensional loop integral
domain: regularization
regime: regularization
status: verified
---

## Applies when (recognition signature)
A Euclidean (or Wick-rotated) **loop momentum integral** over `d` dimensions whose
integrand is a power of `1/(k²+Δ)` — i.e. a single quadratic denominator raised to
power `n` after Feynman-combining propagators. Tells: `∫ d^d k/(2π)^d` with
`(k²+Δ)^{-n}`; the integral is UV-divergent in `d=4` and you want the divergence
isolated as a pole in `ε = 4−d` rather than a hard cutoff.

## The rule
With `Δ>0` and the integral defined by analytic continuation in `d`:

`∫ d^d k/(2π)^d · 1/(k²+Δ)^n = Δ^{d/2−n}/(4π)^{d/2} · Γ(n−d/2)/Γ(n)`.

The UV divergence appears as a **pole of `Γ(n−d/2)`** when `n−d/2` hits a
non-positive integer. Rotational symmetry reduces the angular part to the surface
of the unit `(d−1)`-sphere, `Ω_{d−1}=2π^{d/2}/Γ(d/2)`; the radial part is a Beta
integral. The formula continues to non-integer `d`, so `ε=4−d` is a free regulator.

## Worked example
Take `n=2`, `d=4−ε`. Then `n−d/2 = ε/2` and `Δ^{d/2−n}=Δ^{−ε/2}`:

`∫ d^d k/(2π)^d · 1/(k²+Δ)² = 1/(4π)^{2−ε/2} · Γ(ε/2)/Γ(2) · Δ^{−ε/2}`.

Expanding with `Γ(ε/2)=2/ε − γ + O(ε)` and `(4π)^{ε/2}Δ^{−ε/2}=1+(ε/2)ln(4π/Δ)`:

`= 1/(4π)² · [ 2/ε − γ + ln 4π − ln Δ + O(ε) ]` — the standard `1/ε` UV pole.

## Explain (altitudes)
- **expert** — continuing the integral in `d` trades a dimensionful cutoff for a
  meromorphic function of `d`; gauge/Lorentz invariance is preserved because the
  measure `d^d k` is rotationally invariant, and the only singularities are the
  `Γ`-poles at the logarithmically/quadratically divergent dimensions. The
  `Δ^{d/2−n}` scaling fixes the renormalization-group running.
- **working** — do the angular integral (sphere surface area in `d` dims), then
  the radial integral is a Beta function; the answer is one Gamma ratio. Set
  `d=4−ε`, expand the Gamma near its pole, and the divergence is the `1/ε` term.
- **plain** — the integral blows up in 4 dimensions, so pretend the dimension is a
  slightly-less-than-4 dial. The answer becomes a clean formula whose infinity is
  trapped in a single `1/ε` term you can see and subtract.

## LaTeX
rule: \int\frac{d^{d}k}{(2\pi)^{d}}\,\frac{1}{\left(k^{2}+\Delta\right)^{n}}=\frac{1}{(4\pi)^{d/2}}\,\frac{\Gamma\!\left(n-\frac{d}{2}\right)}{\Gamma(n)}\,\Delta^{\,d/2-n}
example: \int\frac{d^{d}k}{(2\pi)^{d}}\,\frac{1}{\left(k^{2}+\Delta\right)^{2}}=\frac{1}{(4\pi)^{2}}\left[\frac{2}{\varepsilon}-\gamma+\ln 4\pi-\ln\Delta+O(\varepsilon)\right]
## References
- 't Hooft & Veltman, Nucl. Phys. B44 (1972) 189 (regularization & renormalization).
- Peskin & Schroeder, *An Introduction to QFT*, §A.4 (the master formula).
- Srednicki, *Quantum Field Theory*, §14.

## Links
[[gamma-function]] · [[feynman-parametrization]] · [[schwinger-parametrization]] · [[gaussian-integral]]
