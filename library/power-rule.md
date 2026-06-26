---
id: power-rule
name: Power rule (differentiation)
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A single power of `x` to differentiate — anything of the shape `x^n` (or `c·x^n`),
including roots `x^{1/2}` and reciprocals `x^{-3}`. Tell: "differentiate `x` to the
something", a polynomial term, `√x`, `1/x^k`.

## The rule
Bring the exponent down as a multiplier and reduce it by one:

`d/dx (x^n) = n x^{n-1}`,  valid for any constant real `n`.

With a constant factor, `d/dx (c x^n) = c n x^{n-1}`; differentiate a polynomial
term by term.

## Worked example
`d/dx (x^5) = 5 x^4`.  (SymPy: `diff(x**5, x) → 5*x**4`.)

## Explain (altitudes)
- **expert** — the monomial derivative; the `n=1` case of the binomial expansion of
  `(x+h)^n` in the difference quotient, every higher-order term carrying a spare `h`
  that dies in the limit. Holds for all real `n` (via `x^n = e^{n ln x}` and the
  chain rule), making it the building block for Taylor coefficients.
- **working** — multiply by the old power, then knock the power down by one. Linear,
  so a constant out front just rides along and a sum differentiates term by term.
- **plain** — to differentiate `x` to a power, copy the power out to the front and
  take one off the power. So `x^5` becomes `5x^4`.

## LaTeX
rule: \frac{d}{dx}\left(x^{n}\right)=n\,x^{n-1}
example: \frac{d}{dx}\left(x^{5}\right)=5x^{4}

## References
- Edexcel/OCR A-level Mathematics, differentiation from first principles and the
  power rule; standard in any calculus text (Stewart; Spivak).
- Library: SymPy `diff`.

## Links
[[product-rule]] · [[chain-rule]] · [[standard-integrals]]
