---
id: polylogarithm
name: Polylogarithm — the iterated log integral
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
A series `Σ_{k≥1} z^k / k^s`, or the integral `−∫_0^z ln(1−t)/t dt` (dilogarithm), or
nested integrals of `ln(1−t)/t`. Tells: Feynman-integral finite parts, entropy /
Fermi–Dirac sums, `ζ(s)` at `z = 1`, log-weighted unit-interval integrals.

## The rule
`Li_s(z) = Σ_{k≥1} z^k / k^s` for `|z| ≤ 1` (`s>1` at `z=1`). Dilogarithm
`Li_2(z) = −∫_0^z ln(1−t)/t dt`, and `Li_s(z) = ∫_0^z Li_{s-1}(t)/t dt` (raise the
order by one log-integration). Special value `Li_s(1) = ζ(s)` (`Re s > 1`).

## Worked example
`Li_2(1) = ζ(2) = π²/6`. From the series `Σ_{k≥1} 1/k² = π²/6` (Basel); equivalently
`−∫_0^1 ln(1−t)/t dt = Σ_{k≥1} (1/k)∫_0^1 t^{k-1}dt = Σ 1/k² = π²/6` (mpmath `polylog`).

## Explain (altitudes)
- **expert** — `Li_s` is the iterated Coleman integral / generating function whose
  monodromy encodes `ζ`-values; the order-`s` ladder `Li_s = ∫ Li_{s-1} dt/t` is the
  Mellin-image statement `Li_s(1)=ζ(s)`, the boundary of its Mellin–Barnes strip.
- **working** — expand `−ln(1−t) = Σ t^k/k` inside `∫_0^1 (·)/t dt`; each term gives
  `1/k²`, so `Li_2(1) = Σ 1/k² = π²/6` (the Basel sum).
- **plain** — like `ζ(s)` but keeping a variable `z`; at `z=1` it *is* `ζ(s)`, so
  `Li_2(1) = 1 + 1/4 + 1/9 + … = π²/6`.

## LaTeX
rule: \mathrm{Li}_s(z)=\sum_{k=1}^{\infty}\frac{z^k}{k^s},\qquad \mathrm{Li}_2(z)=-\int_{0}^{z}\frac{\ln(1-t)}{t}\,dt,\qquad \mathrm{Li}_s(1)=\zeta(s)
example: \mathrm{Li}_2(1)=\sum_{k=1}^{\infty}\frac{1}{k^2}=\zeta(2)=\frac{\pi^2}{6}

## References
- DLMF 25.12.10 (series/integral), 25.12.11 (`Li_s(1)=ζ(s)`).
- Gradshteyn–Ryzhik 9.553. SymPy `polylog`; mpmath `polylog`.

## Links
[[zeta-regularization]] · [[gamma-function]] · [[mellin-barnes]]
