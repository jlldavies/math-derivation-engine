---
id: gamma-function
name: Gamma function — the continuous factorial
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
`∫_0^∞ x^{s-1} e^{-x} dx` — a power times a decaying exponential over the half-line;
or anywhere a "factorial of a non-integer" appears (normalizations, moments).

## The rule
`∫_0^∞ x^{s-1} e^{-x} dx = Γ(s)`, with `Γ(n) = (n−1)!`, the recursion
`Γ(s+1) = s Γ(s)`, and `Γ(½) = √π`. (More generally `∫_0^∞ x^{s-1} e^{-a x} dx =
Γ(s)/a^s`.)

## Worked example
`Γ(½) = √π`, `Γ(5) = 4! = 24` (SymPy).

## Explain (altitudes)
- **expert** — the unique log-convex extension of the factorial (Bohr–Mollerup);
  meromorphic with simple poles at `s = 0,−1,−2,…`; the Mellin transform of `e^{-x}`.
- **working** — integration by parts on the integral gives `Γ(s+1)=sΓ(s)` — exactly
  the factorial recursion — so `Γ` interpolates `(n−1)!`.
- **plain** — the factorial, extended to *any* number, not just whole ones; e.g.
  `Γ(½)=√π`.

## LaTeX
rule: \int_{0}^{\infty}x^{s-1}e^{-x}\,dx=\Gamma(s),\qquad \Gamma(s+1)=s\,\Gamma(s)
example: \Gamma\!\big(\tfrac12\big)=\sqrt{\pi},\qquad \Gamma(5)=4!=24

## References
- DLMF 5.2 (integral), 5.4 (special values); SymPy / mpmath `gamma`.

## Links
[[gaussian-integral]] · [[tricomi-u-reduction]] · [[watsons-lemma]] · [[integration-by-parts]] · [[digamma-polygamma]] · [[incomplete-gamma]] · [[bessel-function]]
