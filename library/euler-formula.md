---
id: euler-formula
name: Euler's formula
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
Any time `sin`/`cos` would be easier as exponentials: linearising products of
sinusoids, deriving trig identities by exponent algebra, phasors in AC/oscillation
problems, or connecting circular and hyperbolic functions. Tell: `e^{iθ}`, or a trig
manipulation that begs to be "done with exponents instead".

## The rule
`e^{iθ} = cosθ + i sinθ`.
Taking `θ → −θ` and combining gives the inversion (the exponential forms):
`cosθ = (e^{iθ} + e^{−iθ})/2`,  `sinθ = (e^{iθ} − e^{−iθ})/(2i)`.
These are the workhorse for turning trig into algebra; with `θ → ix` they also give
`cosh x = cos(ix)`, `sinh x = −i sin(ix)` (the hyperbolic link).

## Worked example
Derive `cos 2θ` from `e^{2iθ} = (e^{iθ})²`. The right side is
`(cosθ + i sinθ)² = (cos²θ − sin²θ) + i(2 sinθ cosθ)`. The left side is
`cos 2θ + i sin 2θ`. Equating real parts: `cos 2θ = cos²θ − sin²θ`
(and imaginary parts give `sin 2θ = 2 sinθ cosθ`). ✓

## Explain (altitudes)
- **expert** — both sides solve `f' = i f`, `f(0) = 1`, so they agree by uniqueness;
  equivalently the Taylor series of `e^{iθ}` splits into the even (cos) and odd
  (i·sin) series (see taylor-series). `θ ↦ e^{iθ}` wraps ℝ onto the unit circle, the
  universal cover of `S¹`.
- **working** — replace every `cos` and `sin` by its exponential form, do ordinary
  index algebra on the exponents, then collect back into `cos`/`sin`. Multiplying
  exponentials adds angles, which is where the addition formulae come from.
- **plain** — `e^{iθ}` is the point on the unit circle at angle `θ`: its horizontal
  part is `cosθ`, its vertical part is `sinθ`. So one tidy exponential carries both
  trig functions at once.

## LaTeX
rule: e^{i\theta}=\cos\theta+i\sin\theta,\qquad \cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},\quad \sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}
example: e^{2i\theta}=\left(e^{i\theta}\right)^{2}=\left(\cos\theta+i\sin\theta\right)^{2}\;\Rightarrow\;\cos 2\theta=\cos^{2}\theta-\sin^{2}\theta

## References
- Euler, *Introductio in analysin infinitorum* (1748).
- Abramowitz & Stegun §4.3.16; DLMF §4.14.
- Library: SymPy `exp`, `rewrite(exp)` / `rewrite(cos)`.

## Links
[[de-moivre-theorem]] · [[hyperbolic-functions]] · [[taylor-series]] · [[complex-trig-identities]] · [[gudermannian]]
