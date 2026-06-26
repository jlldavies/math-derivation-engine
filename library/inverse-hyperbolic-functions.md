---
id: inverse-hyperbolic-functions
name: Inverse hyperbolic functions (arsinh, arcosh, artanh)
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
An integral with `√(x²+1)`, `√(x²−1)`, or `1/(1−x²)` (the `+`/hyperbolic
cousins of the arcsin/arctan forms), or you want a closed form for the inverse of
`sinh/cosh/tanh`. Tell: `1/√(x²+1)` integrates to a log, not an arcsin — reach for
arsinh.

## The rule
Because the hyperbolic functions are built from `exp`, their inverses are **logs**:
`arsinh x = ln(x + √(x²+1))` (all `x`),
`arcosh x = ln(x + √(x²−1))` (`x ≥ 1`),
`artanh x = ½ ln((1+x)/(1−x))` (`|x| < 1`).
Their derivatives give three standard integrals:
`d/dx arsinh x = 1/√(x²+1)`, `d/dx arcosh x = 1/√(x²−1)`, `d/dx artanh x = 1/(1−x²)`.

## Worked example
Derive the log form of `arsinh`. Let `y = arsinh x`, so `x = sinh y = (eʸ−e⁻ʸ)/2`.
Write `u = eʸ`: then `2x = u − 1/u`, i.e. `u² − 2x u − 1 = 0`, so
`u = x + √(x²+1)` (take `+` since `u = eʸ > 0`). Hence `y = ln(x + √(x²+1))`.
Differentiating: `y' = (1 + x/√(x²+1))/(x + √(x²+1)) = 1/√(x²+1)`. ✓

## Explain (altitudes)
- **expert** — these are the real restrictions of the multivalued
  `arcsin, arctan` continued to imaginary argument: `arsinh x = −i·arcsin(ix)`.
  The branch points sit at `x = ±i` (arsinh) and `x = ±1` (arcosh/artanh),
  which is exactly where the radical / denominator vanishes.
- **working** — to invert `sinh`, set `u = eʸ` and solve the resulting quadratic;
  the positive root is forced by `eʸ > 0`. Differentiate the log to get the
  standard integral `∫ dx/√(x²+1) = arsinh x + C`.
- **plain** — undoing a hyperbolic function means undoing an `eˣ`, and the inverse
  of `eˣ` is `ln`. That is why every answer here is a logarithm.

## LaTeX
rule: \operatorname{arsinh}x=\ln\!\left(x+\sqrt{x^{2}+1}\right),\qquad \frac{d}{dx}\operatorname{arsinh}x=\frac{1}{\sqrt{x^{2}+1}}
example: x=\frac{u-1/u}{2}\;\Rightarrow\; u^{2}-2xu-1=0\;\Rightarrow\; u=x+\sqrt{x^{2}+1}

## References
- Abramowitz & Stegun §4.6; DLMF §4.37 (inverse hyperbolic functions).
- Gradshteyn–Ryzhik 2.261–2.275 (the `√(x²±1)` standard integrals).
- Library: SymPy `asinh`, `acosh`, `atanh`.

## Links
[[hyperbolic-functions]] · [[trig-substitution]] · [[standard-integrals]]
