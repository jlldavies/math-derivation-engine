---
id: chain-rule
name: Chain rule (differentiation)
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A **function inside another function** — a composite `f(g(x))`. Tell: `sin(x²)`,
`e^{3x}`, `(2x+1)^7`, `√(1+x²)`; "a function of a function", brackets raised to a
power, anything where you'd substitute an inner expression.

## The rule
Differentiate the outer function (leaving the inner one alone), then multiply by the
derivative of the inner function:

`d/dx f(g(x)) = f'(g(x)) · g'(x)`.

In Leibniz form, with `u = g(x)`: `dy/dx = (dy/du)(du/dx)`.

## Worked example
`d/dx sin(x²) = 2x cos(x²)`  (outer `sin` gives `cos(x²)`; inner `x²` gives `2x`).
SymPy confirms.

## Explain (altitudes)
- **expert** — the derivative of a composition as the product of linearizations:
  `D(f∘g) = (Df∘g)·Dg`, the 1-D shadow of the multivariable chain rule where the
  Jacobians compose. Differentiation forward; u-substitution is the same identity run
  backwards under the integral.
- **working** — peel the layers from the outside in: differentiate the outer
  function keeping the inside intact, then multiply by the inside's derivative. Chain
  more factors for more nesting.
- **plain** — for a function inside a function, differentiate the outside (leave the
  inside as it is), then times the slope of the inside. `sin(x²)` gives
  `cos(x²)·2x`.

## LaTeX
rule: \frac{d}{dx}\,f\!\left(g(x)\right)=f'\!\left(g(x)\right)\,g'(x)
example: \frac{d}{dx}\,\sin\!\left(x^{2}\right)=2x\cos\!\left(x^{2}\right)

## References
- Edexcel/OCR A-level Mathematics, chain rule / differentiating composite functions;
  standard in any calculus text (Stewart; Spivak).
- Library: SymPy `diff`.

## Links
[[power-rule]] · [[product-rule]] · [[u-substitution]] · [[implicit-differentiation]]
