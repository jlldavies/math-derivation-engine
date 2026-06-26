---
id: quadratic-formula
name: Quadratic formula
domain: algebra
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A quadratic equation `ax² + bx + c = 0` (with `a ≠ 0`) that doesn't factor by
inspection, or whenever you want the roots and the discriminant in one shot. Tell:
"solve `ax² + bx + c = 0`", or a quadratic with awkward, non-integer roots.

## The rule
The roots are

`x = (−b ± √(b² − 4ac)) / 2a`.

The discriminant `Δ = b² − 4ac` decides their nature: `Δ > 0` two real roots,
`Δ = 0` one repeated root, `Δ < 0` a complex-conjugate pair. The formula is exactly
`completing-the-square` carried out on the general quadratic.

## Worked example
`x² − 5x + 6 = 0`: `a=1, b=−5, c=6`, `Δ = 25 − 24 = 1`, so
`x = (5 ± 1)/2 = 3` or `2`. (SymPy: `solve(x**2-5*x+6, x) → [2, 3]`.)

## Explain (altitudes)
- **expert** — completing the square on `ax² + bx + c` shifts to vertex form and
  inverts the square, yielding the closed-form roots; `Δ` is (up to a square
  factor) the resultant/discriminant whose sign and vanishing classify the root
  structure over `ℝ` and `ℂ`.
- **working** — rewrite as `a(x + b/2a)² = b²/4a − c`, take the square root and
  rearrange; the `±` is the two square roots, and `b² − 4ac` under the root is what
  tells you whether the roots are real, repeated, or complex.
- **plain** — any equation shaped like `ax² + bx + c = 0` is solved by plugging
  `a, b, c` into the formula. The bit under the square root tells you how many real
  answers there are; here it gives the two roots `2` and `3`.

## LaTeX
rule: x=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}
example: x^{2}-5x+6=0\ \Rightarrow\ x=\frac{5\pm1}{2}=2,\ 3

## References
- A-level Maths (GCSE/AS: quadratic formula and discriminant); standard algebra
  texts.
- Library: SymPy `solve`.

## Links
[[completing-the-square]] · [[polynomial-division]]
