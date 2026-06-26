---
id: trig-substitution
name: Trigonometric substitution
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
The integrand contains a surd of the form `√(a²−x²)`, `√(a²+x²)` or `√(x²−a²)` and
no inner-derivative is visible to make a plain `u`-sub work. Tell: a square root of
a quadratic with no linear term, begging to be turned into a perfect square by a
Pythagorean identity.

## The rule
Substitute so the Pythagorean identity collapses the surd:

`√(a²−x²)` → `x = a sin θ`, using `1 − sin²θ = cos²θ`;
`√(a²+x²)` → `x = a tan θ`, using `1 + tan²θ = sec²θ`;
`√(x²−a²)` → `x = a sec θ`, using `sec²θ − 1 = tan²θ`.

Then `dx` and the surd both rewrite in `θ`, the root disappears, and you integrate
in `θ` before substituting back. (A linear term inside? First `completing-the-square`.)

## Worked example
`∫ dx/√(1−x²)`: put `x = sin θ`, `dx = cos θ dθ`, `√(1−x²) = cos θ`, so the integral
is `∫ dθ = θ = arcsin x + C`.
(SymPy: `integrate(1/sqrt(1-x**2), x) → asin(x)`.)

## Explain (altitudes)
- **expert** — this is a change of variables that uniformises the conic
  `y² = a²−x²` by its rational/trigonometric parametrisation; the substitution maps
  the surd to a single trig factor, the geometric reason the inverse-trig functions
  are the antiderivatives that appear.
- **working** — pick the trig substitution matching the surd's sign pattern; the
  identity turns `a²−x²` into `a²cos²θ`, the square root becomes `a cos θ`, and the
  whole integrand becomes elementary trig in `θ`.
- **plain** — a square root like `√(1−x²)` is awkward, but if you let `x = sin θ`
  it becomes `cos θ` and the root vanishes. Solve the easy trig integral, then swap
  back to `x` at the end.

## LaTeX
rule: \sqrt{a^{2}-x^{2}}\ \xrightarrow{\,x=a\sin\theta\,}\ a\cos\theta,\qquad dx=a\cos\theta\,d\theta
example: \int\frac{dx}{\sqrt{1-x^{2}}}=\int d\theta=\arcsin x+C

## References
- A-level Further Maths / first-year calculus (trig substitution); Stewart,
  *Calculus*, §7.3.
- Library: SymPy `integrate`.

## Links
[[u-substitution]] · [[standard-integrals]] · [[pythagorean-identity]]
