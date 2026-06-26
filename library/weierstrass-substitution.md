---
id: weierstrass-substitution
name: Weierstrass (tan half-angle) substitution
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
A definite/indefinite integral of a **rational function of `sinθ` and `cosθ`** that
resists the usual tricks — especially `1/(a + b sinθ)`, `1/(a + b cosθ)`,
`1/(1 ± sinθ)`. Tell: `∫ R(sinθ, cosθ) dθ` with `R` rational; you want it turned into
an ordinary rational-function integral.

## The rule
Set `t = tan(θ/2)`. Then
`sinθ = 2t/(1 + t²)`,  `cosθ = (1 − t²)/(1 + t²)`,  `dθ = 2 dt/(1 + t²)`.
Substituting turns any rational `R(sinθ, cosθ) dθ` into a **rational function of `t`**,
which partial-fractions and elementary integrals finish. (Branch care near
`θ = π`, where `t → ∞`.)

## Worked example
`∫ dθ/(1 + sinθ)`. With `sinθ = 2t/(1+t²)`, `dθ = 2dt/(1+t²)`:
`1 + sinθ = (1 + t² + 2t)/(1+t²) = (1+t)²/(1+t²)`, so
`dθ/(1+sinθ) = [2dt/(1+t²)] · [(1+t²)/(1+t)²] = 2dt/(1+t)²`.
Hence `∫ dθ/(1+sinθ) = ∫ 2(1+t)⁻² dt = −2/(1+t) + C = −2/(1 + tan(θ/2)) + C`. ✓
(Check by differentiating back, or numerically: from `0` to `π/2` it gives
`−2/(1+1) + 2/(1+0) = −1 + 2 = 1`.)

## Explain (altitudes)
- **expert** — `t = tan(θ/2)` is the stereographic projection of the unit circle
  from `(−1,0)` onto the line, a birational map `S¹ → ℝ`; that is exactly why it
  rationalises `ℂ(sinθ, cosθ)`. The single missing point `θ = π` is the projection
  centre (`t = ∞`).
- **working** — replace `sinθ`, `cosθ`, `dθ` by their `t`-forms, simplify to a
  rational function of `t`, then integrate by partial fractions and back-substitute
  `t = tan(θ/2)`.
- **plain** — one clever substitution rewrites every sine and cosine as a fraction in
  the single variable `t`. The messy trig integral becomes an ordinary algebra-fraction
  integral you already know how to do.

## LaTeX
rule: t=\tan\tfrac{\theta}{2}\;\Rightarrow\;\sin\theta=\frac{2t}{1+t^{2}},\quad \cos\theta=\frac{1-t^{2}}{1+t^{2}},\quad d\theta=\frac{2\,dt}{1+t^{2}}
example: \int\frac{d\theta}{1+\sin\theta}=\int\frac{2\,dt}{\left(1+t\right)^{2}}=-\frac{2}{1+t}+C=-\frac{2}{1+\tan\frac{\theta}{2}}+C

## References
- Named after Weierstrass (Stewart, *Calculus*); standard in integral tables.
- Gradshteyn–Ryzhik 2.55 (universal trig substitution).
- Library: SymPy `integrate` (uses it internally), `manualintegrate`.

## Links
[[half-angle-formulae]] · [[trig-substitution]] · [[partial-fractions]] · [[trig-reduction-formulae]]
