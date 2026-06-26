---
id: trig-reduction-formulae
name: Trig reduction formulae
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
An integral of an **integer power** `∫ sinⁿx dx`, `∫ cosⁿx dx`, or a product
`∫ sinᵐx cosⁿx dx`, where you want a recursion that lowers the exponent by 2 each
step. Tell: a single high power of sine/cosine, especially over `[0, π/2]` (Wallis).

## The rule
Integration by parts (split off one factor, differentiate the rest) gives
`∫ sinⁿx dx = −(1/n) sinⁿ⁻¹x cos x + ((n−1)/n) ∫ sinⁿ⁻²x dx`,
and symmetrically `∫ cosⁿx dx = (1/n) cosⁿ⁻¹x sin x + ((n−1)/n) ∫ cosⁿ⁻²x dx`.
Iterate down to `∫ dx` (`n` even) or `∫ sin x dx` (`n` odd). Over `[0, π/2]` the
boundary term vanishes, leaving the **Wallis recursion** `Iₙ = ((n−1)/n) Iₙ₋₂`.

## Worked example
`∫₀^{π/2} sin⁴x dx`. Boundary term `−(1/4) sin³x cos x` is `0` at both ends, so
`I₄ = (3/4) I₂`. Again `I₂ = (1/2) I₀` with `I₀ = ∫₀^{π/2} dx = π/2`.
Therefore `I₄ = (3/4)·(1/2)·(π/2) = 3π/16`. ✓
(Numeric check: `3π/16 ≈ 0.5890`.)

## Explain (altitudes)
- **expert** — the recursion is the `n ↦ n−2` contiguous relation for the Beta
  integral `∫₀^{π/2} sinᵐx cosⁿx dx = ½ B((m+1)/2, (n+1)/2)`; the Wallis case
  `Iₙ = ((n−1)/n)Iₙ₋₂` is the `Γ`-function's functional equation in disguise, and its
  `n→∞` ratio gives the Wallis product for `π`.
- **working** — write `sinⁿx = sinⁿ⁻¹x · sin x`, integrate by parts with
  `dv = sin x dx`, and use `cos²x = 1 − sin²x` to fold the new integral back, which
  produces the `((n−1)/n)` recursion. Apply limits to kill the boundary term.
- **plain** — each step trades `sinⁿ` for `sinⁿ⁻²` plus an easy piece, so you walk the
  power down two at a time until nothing is left but a trivial integral.

## LaTeX
rule: \int\sin^{n}x\,dx=-\frac{1}{n}\sin^{n-1}x\cos x+\frac{n-1}{n}\int\sin^{n-2}x\,dx
example: \int_{0}^{\pi/2}\sin^{4}x\,dx=\frac{3}{4}\cdot\frac{1}{2}\cdot\frac{\pi}{2}=\frac{3\pi}{16}

## References
- Wallis, *Arithmetica Infinitorum* (1656); standard reduction-formula derivation.
- Gradshteyn–Ryzhik 2.510–2.513; Abramowitz & Stegun §4.3.
- Library: SymPy `integrate`, `Integral.doit`.

## Links
[[integration-by-parts]] · [[product-to-sum]] · [[standard-integrals]]
