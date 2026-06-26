---
id: hyperbolic-functions
name: Hyperbolic functions (cosh, sinh, tanh)
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You meet `(eˣ ± e⁻ˣ)/2` and want a single named function, or an identity/integral
with a `+` where the circular case has a `−`: `√(x²+1)`, `x²−1`, the catenary
`y = a cosh(x/a)`, or `1 − tanh²` in a derivative. Tell: a "trig-shaped" identity
that fails the usual sign — switch to the hyperbolic family.

## The rule
Define
`cosh x = (eˣ + e⁻ˣ)/2`,  `sinh x = (eˣ − e⁻ˣ)/2`,  `tanh x = sinh x / cosh x`.
They satisfy the Pythagorean analogue and the derivative pair
`cosh²x − sinh²x = 1`,  `d/dx sinh x = cosh x`,  `d/dx cosh x = sinh x`.
**Osborn's rule:** any circular identity becomes its hyperbolic counterpart by
`cos → cosh`, `sin → sinh`, and flipping the sign of every term containing a
*product of two sines* (since `sinh = −i sin(ix)`).

## Worked example
Verify `cosh²x − sinh²x = 1`. Square the definitions:
`cosh²x = (e²ˣ + 2 + e⁻²ˣ)/4`, `sinh²x = (e²ˣ − 2 + e⁻²ˣ)/4`. Subtract: the `e²ˣ`
and `e⁻²ˣ` cancel, leaving `(2 − (−2))/4 = 4/4 = 1`. ✓
And `d/dx sinh x = d/dx (eˣ − e⁻ˣ)/2 = (eˣ + e⁻ˣ)/2 = cosh x`. ✓

## Explain (altitudes)
- **expert** — `cosh, sinh` are the even/odd parts of `exp`, equivalently the
  parametrisation of the unit hyperbola `X² − Y² = 1` by arc-area; the sign flip
  in Osborn's rule is exactly `sinh x = −i sin(ix)`, `cosh x = cos(ix)`, so the two
  families are one analytic object rotated by `i` (see euler-formula).
- **working** — treat them as "trig with a hyperbola". The same algebra works,
  but `cosh²−sinh²=1` replaces `cos²+sin²=1`, and differentiation has no stray
  minus sign: `d/dx cosh = +sinh`.
- **plain** — `cosh` and `sinh` are just `eˣ` split into its symmetric and
  antisymmetric halves. Add them back and you recover `eˣ = cosh x + sinh x`.

## LaTeX
rule: \cosh x=\frac{e^{x}+e^{-x}}{2},\quad \sinh x=\frac{e^{x}-e^{-x}}{2},\quad \cosh^{2}x-\sinh^{2}x=1
example: \cosh^{2}x-\sinh^{2}x=\frac{e^{2x}+2+e^{-2x}}{4}-\frac{e^{2x}-2+e^{-2x}}{4}=1

## References
- Abramowitz & Stegun §4.5; DLMF §4.28 (hyperbolic functions).
- A-level Further Maths "Hyperbolic functions"; Osborn's rule.
- Library: SymPy `cosh`, `sinh`, `tanh`.

## Links
[[euler-formula]] · [[inverse-hyperbolic-functions]] · [[taylor-series]]
