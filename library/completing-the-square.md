---
id: completing-the-square
name: Completing the square
domain: algebra
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A quadratic `ax² + bx + c` you want to rewrite with the variable appearing **once**
— to find a vertex, solve, or prepare a surd for `trig-substitution`. Tell: a
quadratic with a linear term you'd rather see as "(something)² plus a constant".

## The rule
Force a perfect square by halving the linear coefficient:

`ax² + bx + c = a(x + b/2a)² + (c − b²/4a)`.

The bracket is the perfect square `a(x + b/2a)²`; the leftover constant
`c − b²/4a` is what's needed to keep equality. The turning point sits at
`x = −b/2a`, value `c − b²/4a`.

## Worked example
`x² + 6x + 5`: here `b/2 = 3`, and `(x+3)² = x² + 6x + 9`, which overshoots by `4`,
so `x² + 6x + 5 = (x+3)² − 4`. Minimum `−4` at `x = −3`.
(SymPy: `factor((x+3)**2 - 4) → (x+1)*(x+5)`, matching the roots.)

## Explain (altitudes)
- **expert** — completing the square is the affine shift `x ↦ x + b/2a` that
  removes the linear term, exhibiting the quadratic in vertex (canonical) form; it
  is the algebraic step that derives the `quadratic-formula` and rationalises
  quadratic denominators for integration.
- **working** — take half the `x`-coefficient, square it, add and subtract it; the
  first three terms fold into `(x + b/2a)²` and you carry the correction outside.
  This isolates `x` in one place, so solving or shifting is immediate.
- **plain** — rearrange `x² + 6x + 5` so the `x` only shows up once. Half of 6 is
  3, and `(x+3)²` is almost right — it's `4` too big — so the answer is `(x+3)² − 4`.
  Now you can read off the lowest point at a glance.

## LaTeX
rule: ax^{2}+bx+c=a\left(x+\frac{b}{2a}\right)^{2}+\left(c-\frac{b^{2}}{4a}\right)
example: x^{2}+6x+5=\left(x+3\right)^{2}-4

## References
- A-level Maths (GCSE/AS algebra: completing the square); any standard algebra text.
- Library: SymPy `factor` / `solve` confirm the roots.

## Links
[[quadratic-formula]] · [[trig-substitution]]
