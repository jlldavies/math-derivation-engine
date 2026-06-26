---
id: pythagorean-identity
name: Pythagorean identity (sin²+cos²=1)
domain: trigonometry
regime: elementary
status: drafted
---

## Applies when (recognition signature)
You see `sin²` and `cos²` of the **same angle** added together, or a stray
`1 − sin²`/`1 − cos²`, or a `1 + tan²`/`sec²` to swap. Tell: a trig expression you
want to collapse to a single function, or a `√(1 − sin²θ)` you want simplified.

## The rule
For any angle `θ`:

`sin²θ + cos²θ = 1`.

Dividing through by `cos²θ` gives `1 + tan²θ = sec²θ`; dividing by `sin²θ` gives
`1 + cot²θ = csc²θ`. These let you rewrite any one of the three pairs in terms of
another.

## Worked example
Simplify `(1 − sin²θ)/cosθ`. Since `1 − sin²θ = cos²θ`, the expression is
`cos²θ/cosθ = cosθ`.

## Explain (altitudes)
- **expert** — the unit-circle relation `‖(cosθ, sinθ)‖² = 1`; the `SO(2)`
  orbit lies on `x²+y²=1`, so the identity is just that circle's equation in
  rotated coordinates. The `sec`/`csc` forms are the same relation projected onto
  the tangent/cotangent charts.
- **working** — a point on the unit circle has coordinates `(cosθ, sinθ)`, and
  the circle has radius 1, so its coordinates satisfy `x²+y²=1`. Divide by `cos²`
  or `sin²` to get the `sec`/`csc` versions when those functions appear.
- **plain** — draw a right triangle inside a circle of radius 1. The two short
  sides are `sinθ` and `cosθ`, and Pythagoras says the squares of the short sides
  add up to the square of the long side (which is 1). So `sin² + cos² = 1`.

## LaTeX
rule: \sin^{2}\theta+\cos^{2}\theta=1\qquad\Longrightarrow\qquad 1+\tan^{2}\theta=\sec^{2}\theta
example: \frac{1-\sin^{2}\theta}{\cos\theta}=\frac{\cos^{2}\theta}{\cos\theta}=\cos\theta

## References
- A-level Pure (Edexcel/AQA/OCR) "Trigonometric identities"; standard in any
  pre-calculus text (Stewart; CGP A-level).
- Library: SymPy `simplify`/`trigsimp` applies it automatically.

## Links
[[compound-angle-formulae]] · [[double-angle-formulae]] · [[trig-substitution]]
