---
id: reciprocal-trig-functions
name: Reciprocal trig functions (sec, cosec, cot)
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
An expression carrying `sec`, `cosec` (csc), or `cot`, or an identity you want to
prove by rewriting everything in `sin` and `cos`. Tells: a `1 + tan²` you want to
collapse to `sec²`, a `1 + cot²` to `cosec²`, or a messy quotient of trig functions
to simplify. Keyword: "prove the identity" / "simplify".

## The rule
The three reciprocal functions are

`secθ = 1/cosθ`,  `cosecθ = 1/sinθ`,  `cotθ = cosθ/sinθ = 1/tanθ`.

Dividing the Pythagorean identity `sin²θ + cos²θ = 1` by `cos²θ` and by `sin²θ`
gives the companion identities

`1 + tan²θ = sec²θ`,  `1 + cot²θ = cosec²θ`.

## Worked example
Prove `sec²θ + cosec²θ = sec²θ·cosec²θ`.
LHS `= 1/cos²θ + 1/sin²θ = (sin²θ + cos²θ)/(sin²θ·cos²θ) = 1/(sin²θ·cos²θ)`
using `sin²θ + cos²θ = 1`. That last expression is `sec²θ·cosec²θ`, the RHS. ∎

## Explain (altitudes)
- **expert** — `sec`, `cosec`, `cot` are the reciprocals dual to `cos`, `sin`,
  `tan`; the identities `1 + tan² = sec²` and `1 + cot² = cosec²` are the
  Pythagorean relation pushed onto the tangent and cotangent charts of the circle,
  i.e. the same `x²+y²=1` read in projected coordinates.
- **working** — never memorize the reciprocal identities separately: get them by
  dividing `sin² + cos² = 1` through by `cos²` (for `sec`) or `sin²` (for `cosec`).
  For proofs, convert everything to `sin`/`cos`, combine over a common denominator,
  then apply `sin² + cos² = 1`.
- **plain** — `sec`, `cosec`, `cot` are just "one over" `cos`, `sin`, `tan`. To
  prove a trig identity, rewrite each in terms of `sin` and `cos`, tidy the
  fractions, and use `sin² + cos² = 1` to finish.

## LaTeX
rule: \sec\theta=\frac{1}{\cos\theta},\quad \operatorname{cosec}\theta=\frac{1}{\sin\theta},\quad \cot\theta=\frac{\cos\theta}{\sin\theta};\qquad 1+\tan^{2}\theta=\sec^{2}\theta
example: \sec^{2}\theta+\operatorname{cosec}^{2}\theta=\frac{\sin^{2}\theta+\cos^{2}\theta}{\sin^{2}\theta\cos^{2}\theta}=\frac{1}{\sin^{2}\theta\cos^{2}\theta}=\sec^{2}\theta\,\operatorname{cosec}^{2}\theta

## References
- A-level Pure (Edexcel/AQA/OCR) "Reciprocal trig functions and identities"; any
  pre-calculus text (Stewart; CGP A-level).
- Library: SymPy `sec`, `csc`, `cot`; `simplify`/`trigsimp` apply these identities.

## Links
[[pythagorean-identity]] · [[solving-trig-equations]] · [[double-angle-formulae]]
