---
id: quotient-rule
name: Quotient rule (differentiation)
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
One function **divided by** another, both depending on `x` — `sin x / x`,
`(x²+1)/(x-2)`, `e^x / x³`. Tell: a fraction with `x` in the denominator that you
can't trivially split into separate powers.

## The rule
`d/dx (u/v) = (u' v − u v') / v²`,  where `u = u(x)`, `v = v(x)`, and `v ≠ 0`.

Note the order in the numerator: derivative of top times bottom **minus** top times
derivative of bottom.

## Worked example
`d/dx (sin x / x) = (x cos x − sin x) / x²`  (`u = sin x`, `u' = cos x`; `v = x`,
`v' = 1`). SymPy confirms.

## Explain (altitudes)
- **expert** — the product rule applied to `u·v^{-1}` with the chain rule on
  `v^{-1}` (giving `−v'v^{-2}`), then put over the common denominator `v²`; the
  derivative of a ratio of smooth functions wherever `v ≠ 0`.
- **working** — write it as (bottom × derivative of top − top × derivative of
  bottom) all over the bottom squared. Mind the minus sign and the order.
- **plain** — for a fraction, do (slope of top)×(bottom) minus (top)×(slope of
  bottom), then divide the whole thing by the bottom squared.

## LaTeX
rule: \frac{d}{dx}\left(\frac{u}{v}\right)=\frac{u'v-uv'}{v^{2}}
example: \frac{d}{dx}\left(\frac{\sin x}{x}\right)=\frac{x\cos x-\sin x}{x^{2}}

## References
- Edexcel/OCR A-level Mathematics, quotient rule for differentiation; standard in any
  calculus text (Stewart; Spivak).
- Library: SymPy `diff`.

## Links
[[product-rule]] · [[chain-rule]]
