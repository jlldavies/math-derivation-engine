---
id: polynomial-division
name: Polynomial (long) division
domain: algebra
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A ratio of polynomials where the top has degree **≥** the bottom — an improper
rational — that you need to simplify before factoring, integrating, or finding
partial fractions. Tell: `deg P ≥ deg Q`, or a "show that `(x−r)` is a factor"
question.

## The rule
Divide `P(x)` by `D(x)` (degree of `D` no larger) to get a quotient and remainder:

`P(x) = Q(x) D(x) + R(x)`,  with `deg R < deg D`.

Long division (or synthetic division for a linear `D`) produces `Q` and `R` term by
term, matching the leading power at each step. If `R = 0`, `D` is a factor of `P`;
the **remainder theorem** says dividing by `(x − r)` leaves remainder `P(r)`.

## Worked example
`(x³ − 1)/(x − 1)`: long division gives `x³ − 1 = (x − 1)(x² + x + 1) + 0`, so
`(x³ − 1)/(x − 1) = x² + x + 1`. (SymPy: `div(x**3-1, x-1) → (x**2 + x + 1, 0)`.)

## Explain (altitudes)
- **expert** — this is the Euclidean division in the polynomial ring `k[x]`, which
  is a Euclidean domain; quotient and remainder are unique, and `R(r) = P(r)` (the
  remainder theorem) makes division the engine behind factor-finding and
  `partial-fractions`.
- **working** — divide the leading term of what's left by the leading term of `D`,
  multiply back, subtract, and repeat until the remainder's degree drops below `D`.
  You get `P = QD + R` exactly, just like integer long division.
- **plain** — split a top-heavy fraction the way you'd do long division with
  numbers: see how many times the bottom goes into the top, subtract, bring down
  the next bit. For `(x³−1)/(x−1)` it goes in exactly, giving `x² + x + 1`.

## LaTeX
rule: P(x)=Q(x)\,D(x)+R(x),\qquad \deg R<\deg D
example: \frac{x^{3}-1}{x-1}=x^{2}+x+1

## References
- A-level Maths / Further Maths (algebraic division, remainder/factor theorem);
  standard algebra texts.
- Library: SymPy `div` / `quo` / `rem`.

## Links
[[partial-fractions]] · [[quadratic-formula]]
