---
id: implicit-differentiation
name: Implicit differentiation
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A relation tying `x` and `y` together that you **can't (or don't want to) solve for
`y`** — `x² + y² = 1`, `x³ + y³ = 6xy`, `sin(xy) = x`. Tell: `y` appears mixed in with
`x` and you still need `dy/dx`.

## The rule
Differentiate **both sides** with respect to `x`, treating `y` as a function of `x`
(so every `y`-term picks up a `dy/dx` via the chain rule). Then solve the resulting
linear equation for `dy/dx`.

For `F(x,y) = 0` this gives `dy/dx = −F_x / F_y` (where `F_x`, `F_y` are the partial
derivatives), valid where `F_y ≠ 0`.

## Worked example
`x² + y² = 1`  ⇒  `2x + 2y (dy/dx) = 0`  ⇒  `dy/dx = −x/y`.
(SymPy: `idiff(x**2 + y**2 - 1, y, x) → -x/y`.)

## Explain (altitudes)
- **expert** — apply `d/dx` to the level-set equation `F(x,y(x))=0`; the chain rule
  gives `F_x + F_y\,y' = 0`, so `y' = −F_x/F_y` by the implicit function theorem
  wherever `F_y ≠ 0`. The curve's tangent read off without an explicit parametrization.
- **working** — differentiate term by term; whenever you differentiate a `y` you tack
  on `dy/dx` (chain rule), use the product rule on mixed `xy`-terms, then collect the
  `dy/dx` factors and divide them out.
- **plain** — you can't always rearrange to `y = …`, so differentiate the whole
  equation as it stands, remembering `y` secretly depends on `x` (so its derivative
  carries a `dy/dx`). Then make `dy/dx` the subject. For the unit circle that gives
  `dy/dx = −x/y`.

## LaTeX
rule: \frac{dy}{dx}=-\frac{F_{x}}{F_{y}}\qquad\text{from }\frac{d}{dx}\,F\!\left(x,y(x)\right)=0
example: x^{2}+y^{2}=1\;\Rightarrow\;2x+2y\,\frac{dy}{dx}=0\;\Rightarrow\;\frac{dy}{dx}=-\frac{x}{y}

## References
- Edexcel/OCR A-level Mathematics, implicit differentiation; standard in any calculus
  text (Stewart; Spivak), implicit function theorem for the general form.
- Library: SymPy `idiff`.

## Links
[[chain-rule]] · [[product-rule]]
