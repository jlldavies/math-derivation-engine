---
id: harmonic-form
name: Harmonic form (a cosθ + b sinθ = R cos(θ−α))
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You meet a **linear combination of `sinθ` and `cosθ` at the same angle** —
`a cosθ + b sinθ` — and want a single sinusoid. Tell: solving
`a cosθ + b sinθ = c`, or reading off the **maximum/minimum** of such an
expression, or finding its amplitude and phase.

## The rule
For constants `a`, `b` (not both zero):

`a cosθ + b sinθ = R cos(θ − α)`,  with  `R = √(a² + b²)`  and  `tan α = b/a`.

`R` (taken positive) is the **amplitude**; `α` is the **phase shift**, with the
quadrant of `α` fixed by the signs of `a` and `b` (here `a = R cos α`,
`b = R sin α`). The expression therefore oscillates between `−R` and `+R`. An
equivalent sine form is `a cosθ + b sinθ = R sin(θ + β)` with `tan β = a/b`.

## Worked example
`3 cosθ + 4 sinθ`. Here `R = √(3² + 4²) = √25 = 5` and `tan α = 4/3`, so
`α = arctan(4/3) ≈ 53.13°`. Thus

`3 cosθ + 4 sinθ = 5 cos(θ − α)`,  `α = arctan(4/3)`.

The **maximum value is 5** (attained when `θ = α`), the minimum is `−5`. Check at
`θ = α`: `5 cos 0 = 5`, and indeed `3 cos53.13° + 4 sin53.13° = 3(0.6) + 4(0.8) = 5`. ✓

## Explain (altitudes)
- **expert** — `(a, b)` is a vector; writing it as `R(cos α, sin α)` is its polar
  form, and `a cosθ + b sinθ = (a,b)·(cosθ, sinθ)` is an inner product equal to
  `R cos(θ − α)` by the cosine of the angle between the two unit-scaled vectors.
  The whole family `{a cosθ + b sinθ}` is the 2-D space spanned by `cosθ, sinθ`;
  `R, α` are just polar coordinates on it.
- **working** — expand the target `R cos(θ − α) = R cosα cosθ + R sinα sinθ` with
  the compound-angle formula and match coefficients: `R cosα = a`, `R sinα = b`.
  Squaring and adding gives `R² = a² + b²`; dividing gives `tan α = b/a`.
- **plain** — two waves of the same frequency, one a cosine and one a sine, always
  add up to a **single** shifted cosine wave. Its height `R` comes from Pythagoras
  on `a` and `b`, and the shift `α` comes from `tan α = b/a`. The biggest the sum
  can ever be is `R`.

## LaTeX
rule: a\cos\theta+b\sin\theta=R\cos\!\left(\theta-\alpha\right),\qquad R=\sqrt{a^{2}+b^{2}},\quad \tan\alpha=\frac{b}{a}
example: 3\cos\theta+4\sin\theta=5\cos\!\left(\theta-\alpha\right),\qquad \alpha=\arctan\!\left(\frac{4}{3}\right),\quad \max=5

## References
- A-level Pure "R cos(θ − α) / harmonic form"; standard in trigonometry texts.
- Equivalent to the phasor addition of two sinusoids (engineering).

## Links
[[compound-angle-formulae]] · [[solving-trig-equations]] · [[trig-graph-transformations]]
