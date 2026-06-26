---
id: standard-integrals
name: Standard integrals (the table you memorise)
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
The integrand is already one of the textbook forms — a power `x^n`, `1/x`, an
exponential `e^x`, a basic trig function, or `1/(1+x²)` — with no composition to
unwind. Tell: you recognise the integrand on sight as the derivative of something
standard, so you can write the answer down without any manoeuvre.

## The rule
Reverse the standard derivatives. The core table (add `+C` for indefinite forms):

`∫ xⁿ dx = x^{n+1}/(n+1)` for `n ≠ −1`,  `∫ (1/x) dx = ln|x|`,
`∫ eˣ dx = eˣ`,  `∫ cos x dx = sin x`,  `∫ sin x dx = −cos x`,
`∫ 1/(1+x²) dx = arctan x`,  `∫ 1/√(1−x²) dx = arcsin x`.

Everything harder is a manoeuvre (substitution, parts, partial fractions) that
ends by hitting one of these.

## Worked example
`∫_0^1 x² dx = [x³/3]_0^1 = 1/3`. (SymPy: `integrate(x**2,(x,0,1)) → 1/3`.)

## Explain (altitudes)
- **expert** — these are the antiderivative representatives of the elementary
  function classes closed under differentiation; the `n = −1` exception is exactly
  where the power family hands off to the logarithm, and the inverse-trig entries
  are the seeds that `trig-substitution` rationalises into.
- **working** — each line is just a derivative read backwards: since `d/dx(x^{n+1})
  = (n+1)xⁿ`, dividing by `n+1` inverts it; the `1/x → ln|x|` case patches the hole
  the power rule leaves at `n = −1`.
- **plain** — integration is differentiation in reverse, so learn the short list of
  "what differentiates to this" and you can do the easy ones instantly. The odd one
  out is `1/x`, whose integral is `ln|x|`, not a power.

## LaTeX
rule: \int x^{n}\,dx=\frac{x^{n+1}}{n+1}\;(n\neq-1),\qquad \int\frac{1}{x}\,dx=\ln\left|x\right|
example: \int_{0}^{1}x^{2}\,dx=\left[\frac{x^{3}}{3}\right]_{0}^{1}=\frac{1}{3}

## References
- A-level Maths / Further Maths (Edexcel C2–C4 integration tables); Stewart,
  *Calculus*, table of basic integrals.
- Library: SymPy `integrate`.

## Links
[[power-rule]] · [[u-substitution]] · [[integration-by-parts]] · [[trig-substitution]]
