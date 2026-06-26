---
id: borel-summation
name: Borel summation of divergent series
domain: asymptotics
regime: resummation
status: verified
---

## Applies when (recognition signature)
You have a **divergent** (typically asymptotic) power series `Σ a_n x^n` whose
coefficients grow **factorially**, `a_n ~ n!`, and you want a finite value or a
function it represents. Tells: "this series diverges but seems to encode an answer",
factorial-growth coefficients, perturbation series in QFT/asymptotics,
`Σ (−1)^n n! x^n` and friends, "resum / give it meaning". The series is summable
(Borel) when the Borel transform extends to the positive real axis.

## The rule
Form the **Borel transform** `B(t) = Σ_n a_n t^n / n!` (which converges in a disk
because the `n!` is divided out), analytically continue it along `[0,∞)`, then take
the **Laplace integral**
`S = ∫_0^∞ e^{−t} B(t) dt`.
When this integral exists it is the Borel sum, and it reproduces the original series
as its asymptotic expansion (via `∫_0^∞ e^{−t} t^n dt = n!`). Singularities of `B`
on the positive axis obstruct summation (ambiguity / the need for lateral contours).

## Worked example
Euler's series `Σ_{n≥0} (−1)^n n! x^n`. Its Borel transform is
`B(t) = Σ (−1)^n t^n = 1/(1+t)`, so
`S(x) = ∫_0^∞ e^{−t} / (1 + x t) dt = (1/x) e^{1/x} E_1(1/x)`,
a finite, well-defined function whose asymptotic expansion as `x → 0⁺` is exactly
the divergent series. Cross-checked numerically with mpmath `quad`.

## Explain (altitudes)
- **expert** — dividing by `n!` tames the factorial growth into a convergent germ;
  Laplace-transforming back inverts the moment relation `∫ e^{−t}t^n = n!`, and the
  analytic structure of `B(t)` on `R₊` (Borel singularities) controls summability
  and resurgent ambiguities.
- **working** — the raw series blows up, so first divide term `n` by `n!` to get a
  convergent series `B(t)`, sum that in closed form, then undo the division by
  integrating `e^{−t}B(t)`; the `e^{−t}` puts the `n!` back.
- **plain** — the sum is "too big to add up", so shrink every term by a known factor,
  add the calmed-down version, then scale it back at the end to recover a real number.

## LaTeX
rule: S=\int_{0}^{\infty}e^{-t}\,B(t)\,dt,\qquad B(t)=\sum_{n}\frac{a_n}{n!}\,t^{n}
example: \sum_{n\ge 0}(-1)^{n}n!\,x^{n}\;\longmapsto\;\int_{0}^{\infty}\frac{e^{-t}}{1+x t}\,dt
## References
- Hardy, *Divergent Series*, ch. VIII; Bender & Orszag, *Advanced Mathematical Methods*, §8.2.
- DLMF 2.3 (asymptotics) and 6.2 (exponential integral `E_1`).
- Library: mpmath `quad` / `nsum` (numerical resummation), SymPy `expint`.
- Worked example: Euler's divergent series, standard (Hardy §8.5).

## Links
[[watsons-lemma]] · [[zeta-regularization]] · [[gamma-function]]
