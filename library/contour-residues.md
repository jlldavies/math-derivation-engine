---
id: contour-residues
name: Contour integration by residues
domain: calculus
regime: complex-analysis
status: verified
---

## Applies when (recognition signature)
A real integral over the whole line (or with `sin/cos`, `e^{ikx}`) where the
integrand extends to a meromorphic function with isolated poles and decays on a
large semicircle. Tell: `∫_{-∞}^{∞} (rational)` or `(rational)·e^{ikx}` with no
elementary antiderivative but clean poles off the real axis.

## The rule
For `f` meromorphic inside a closed contour `C` (counter-clockwise) with isolated
poles `z_k`:

`∮_C f(z) dz = 2πi Σ_k Res(f, z_k)`.

Close the real line with a semicircle in the half-plane where the integrand
decays; if that arc → 0, the real integral equals `2πi` times the enclosed
residues. Simple pole: `Res(f, z_0) = lim_{z→z_0} (z−z_0) f(z)`.

## Worked example
`∫_{-∞}^{∞} dx/(1+x²) = π`. Poles at `z = ±i`; close upward, enclosing `z = i`.
`Res = 1/(2i)`, so the integral `= 2πi · 1/(2i) = π`. (Known result; `arctan`
gives `π` directly.)

## Explain (altitudes)
- **expert** — the residue theorem is Cauchy's theorem plus the Laurent
  expansion: only the `1/(z−z_0)` term survives integration around a loop, and its
  coefficient is the residue. Jordan's lemma controls the arc for oscillatory
  factors.
- **working** — wrap the real axis into a big loop in the complex plane; the loop
  integral is just `2πi` times the residues at the poles you trapped, and the
  curved part vanishes because the integrand dies off out there.
- **plain** — bend the number line into a giant circle in an extra dimension. The
  whole trip around only "feels" the special blow-up points inside, and adding up
  those gives the answer.

## LaTeX
rule: \oint_{C}f(z)\,dz=2\pi i\sum_{k}\operatorname{Res}\left(f,z_{k}\right)
example: \int_{-\infty}^{\infty}\frac{dx}{1+x^{2}}=2\pi i\cdot\frac{1}{2i}=\pi

## References
- Cauchy residue theorem — any complex analysis text (Ahlfors; Whittaker & Watson).
- Library: SymPy `residue` and `integrate` over `(-oo, oo)`.

## Links
[[fresnel-integral]] · [[gamma-reflection]] · [[fourier-transform]]
