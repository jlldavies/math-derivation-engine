---
id: product-rule
name: Product rule (differentiation)
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
Two functions of `x` **multiplied together**, each one you can differentiate on its
own — `x² sin x`, `e^x ln x`, `(x+1)(x²-3)`. Tell: a product where neither factor is
just a constant.

## The rule
Differentiate each factor in turn and add the two results:

`d/dx (u v) = u' v + u v'`,  where `u = u(x)`, `v = v(x)`.

(For three factors: `(uvw)' = u'vw + uv'w + uvw'`.)

## Worked example
`d/dx (x² sin x) = 2x sin x + x² cos x`  (`u = x²`, `u' = 2x`; `v = sin x`,
`v' = cos x`). SymPy confirms.

## Explain (altitudes)
- **expert** — the Leibniz rule, the derivation of `d(uv)=u\,dv+v\,du`; the `n=1`
  case of the general Leibniz formula and the first-order term in the variation of a
  product. Follows from the difference quotient of `uv` once you add and subtract
  `u(x)v(x+h)`.
- **working** — differentiate the first factor times the second as-is, plus the
  first as-is times the derivative of the second. Two terms, one per factor.
- **plain** — when two things are multiplied, differentiate one at a time and add:
  (slope of first)×(second) plus (first)×(slope of second).

## LaTeX
rule: \frac{d}{dx}\left(uv\right)=u'v+uv'
example: \frac{d}{dx}\left(x^{2}\sin x\right)=2x\sin x+x^{2}\cos x

## References
- Edexcel/OCR A-level Mathematics, product rule for differentiation; standard in any
  calculus text (Stewart; Spivak).
- Library: SymPy `diff`.

## Links
[[power-rule]] · [[quotient-rule]] · [[chain-rule]]
