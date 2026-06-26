---
id: abel-plana
name: Abel–Plana formula (sum-to-integral with complex correction)
domain: asymptotics
regime: resummation
status: drafted
---

## Applies when (recognition signature)
You want to turn an **infinite sum `Σ_{n≥0} f(n)`** into an integral plus an exact
correction, especially to **extract a finite part of a divergent sum** (Casimir-type
subtractions). Tells: subtracting `Σ f(n) − ∫ f dx` to isolate a vacuum energy,
`f` analytic in the right half-plane with controlled growth, "regularize this sum
exactly", Casimir-energy mode sums, "express a sum as an integral over the imaginary
axis". Best when `f` extends analytically and decays in the strip.

## The rule
For `f` analytic in `Re z ≥ 0` with suitable decay:
`Σ_{n=0}^{∞} f(n) = ∫_0^∞ f(x) dx + f(0)/2 + i ∫_0^∞ [f(ix) − f(−ix)] / (e^{2πx} − 1) dx`.
The last term is the exact correction beyond the integral and endpoint half-value;
the `1/(e^{2πx}−1)` kernel suppresses the high end, so the correction is often a
small, finite, convergent integral even when the original sum diverges.

## Worked example
Regularizing `Σ_{n=0}^∞ n` as a consistency check on `ζ(−1) = −1/12`. With the
convergence factor `f(n) = n e^{−εn}`, the integral `∫_0^∞ x e^{−εx} dx = 1/ε²`
and endpoint pieces carry the `1/ε²` divergence, while the Abel–Plana correction
contributes the finite `−1/12` (here `i∫_0^∞ [ix − (−ix)]/(e^{2πx}−1) dx
= −2∫_0^∞ x/(e^{2πx}−1) dx = −1/12`). This matches the `ζ`-regularized value.

## Explain (altitudes)
- **expert** — apply the residue theorem to `f(z)·cot(πz)` (or a contour wrapping the
  integers); the integer poles reproduce the sum, the real-axis pieces give `∫f` and
  the half-endpoint, and the imaginary-axis integral with the Bose kernel is the exact
  remainder — a scheme-independent route to Casimir finite parts.
- **working** — write the sum as a contour integral around the integers, deform onto
  the real and imaginary axes; you get the plain integral, half the boundary term, and
  a small correction integral weighted by `1/(e^{2πx}−1)`.
- **plain** — a sum equals the area under the curve plus a tidy leftover; this formula
  writes that leftover exactly as one extra integral, so even "infinite" sums hand back
  a finite number.

## LaTeX
rule: \sum_{n=0}^{\infty}f(n)=\int_{0}^{\infty}f(x)\,dx+\frac{f(0)}{2}+i\int_{0}^{\infty}\frac{f(ix)-f(-ix)}{e^{2\pi x}-1}\,dx
example: -2\int_{0}^{\infty}\frac{x}{e^{2\pi x}-1}\,dx=-\frac{1}{12}=\zeta(-1)
## References
- Whittaker & Watson, *A Course of Modern Analysis*, §7.2; DLMF 1.10(vi) (Abel–Plana sum).
- Elizalde, *Ten Physical Applications of Spectral Zeta Functions*, ch. 2 (Casimir).
- Library: mpmath `quad` (the correction integral), `zeta` (cross-check).
- Worked example: Casimir consistency `−1/12`, standard (Elizalde §2).

## Links
[[euler-maclaurin]] · [[zeta-regularization]]
