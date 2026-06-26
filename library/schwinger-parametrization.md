---
id: schwinger-parametrization
name: Schwinger parametrization — exponentiate the denominator
domain: regularization
regime: regularization
status: verified
---

## Applies when (recognition signature)
A denominator raised to a power, `1/A^n` (with `Re A>0`), that you want to turn into
a **Gaussian-friendly exponential** before doing a momentum integral. Tell:
Euclidean propagators `1/(k²+m²)^n`; you would rather integrate `e^{−s(k²+m²)}`
(which factorizes and is Gaussian in `k`) than the rational form directly.

## The rule
`1/A^n = 1/Γ(n) ∫_0^∞ s^{n−1} e^{−sA} ds`, valid for `Re A>0`, `Re n>0`.

This is just the Gamma-function integral after the rescaling `t=sA`. Each
denominator gets its own Schwinger time `s`; the loop momentum then appears only in
exponentials `e^{−s k²}`, so the `k`-integral is a pure **Gaussian** and is done by
completing the square. The leftover `s`-integral(s) reproduce the parametric
representation (and, after rescaling, the Feynman-parameter form).

## Worked example
A Euclidean propagator integral `I = ∫ d^d k/(2π)^d · 1/(k²+m²)`. Exponentiate
(`n=1`): `1/(k²+m²)=∫_0^∞ ds · e^{−s(k²+m²)}`. Swap orders and do the Gaussian
`k`-integral, `∫ d^d k/(2π)^d e^{−s k²}=(4π s)^{−d/2}`:

`I = ∫_0^∞ ds · e^{−s m²} (4π s)^{−d/2} = (4π)^{−d/2} ∫_0^∞ s^{−d/2} e^{−s m²} ds`.

The remaining `s`-integral is a Gamma function: `= (4π)^{−d/2} Γ(1−d/2) (m²)^{d/2−1}`,
matching the `n=1` `d`-dimensional master integral.

## Explain (altitudes)
- **expert** — the trick is the Mellin (Gamma) representation of a power; it trades
  a rational denominator for a heat-kernel proper-time integral. Gaussian
  `k`-integration is exact in any `d`, so the whole loop reduces to a `Γ`-function
  in the Schwinger time — the proper-time form underlying zeta/heat-kernel
  regularization.
- **working** — replace `1/A` by an integral of `e^{−sA}` over a time `s`; the
  momentum now sits in a Gaussian, which you integrate by completing the square; the
  remaining `s`-integral is a Gamma function.
- **plain** — a fraction is hard to integrate, but `e^{−s·stuff}` is easy. This rule
  rewrites the fraction as a sum (integral) of such exponentials, you knock out the
  Gaussian momentum part, and finish with a single tidy `s`-integral.

## LaTeX
rule: \frac{1}{A^{n}}=\frac{1}{\Gamma(n)}\int_{0}^{\infty}s^{\,n-1}\,e^{-sA}\,ds,\qquad \operatorname{Re}A>0
example: \int\frac{d^{d}k}{(2\pi)^{d}}\,\frac{1}{k^{2}+m^{2}}=\frac{1}{(4\pi)^{d/2}}\,\Gamma\!\left(1-\frac{d}{2}\right)\left(m^{2}\right)^{d/2-1}
## References
- Schwinger, Phys. Rev. 82 (1951) 664 (proper-time representation).
- Peskin & Schroeder, *An Introduction to QFT*, §A.4.
- Itzykson & Zuber, *Quantum Field Theory*.

## Links
[[gamma-function]] · [[dimensional-regularization]] · [[gaussian-integral]]
