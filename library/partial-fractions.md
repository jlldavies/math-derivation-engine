---
id: partial-fractions
name: Partial fractions (split a rational function)
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A rational integrand `P(x)/Q(x)` whose denominator **factorises**, and you want to
integrate it. Tell: a single fraction with a factorable bottom you can't integrate
directly, but each separate factor would be a standard log or arctan.

## The rule
If `deg P < deg Q` (else divide first — see `polynomial-division`), split over the
factors of `Q`. For distinct linear factors:

`P(x) / [(x−r₁)(x−r₂)…] = A₁/(x−r₁) + A₂/(x−r₂) + …`,

with each `Aᵢ` found by the cover-up rule (multiply through, set `x = rᵢ`).
Repeated and irreducible-quadratic factors get `A/(x−r)² ` and `(Bx+C)/(x²+…)`
terms. Each piece then integrates to a `ln` or `arctan`.

## Worked example
`1/(x²−1) = 1/[(x−1)(x+1)] = ½·1/(x−1) − ½·1/(x+1)`, so
`∫ dx/(x²−1) = ½ ln|x−1| − ½ ln|x+1| + C`.
(SymPy: `apart(1/(x**2-1)) → 1/(2*(x-1)) - 1/(2*(x+1))`.)

## Explain (altitudes)
- **expert** — a partial-fraction decomposition is the basis expansion of `P/Q`
  in the space of proper rationals spanned by `{(x−rᵢ)^{−k}}` and quadratic
  counterparts; the residue `Aᵢ` is literally `P(rᵢ)/Q'(rᵢ)`, the same residue that
  drives `contour-residues`.
- **working** — factor the denominator, write one unknown over each factor, clear
  denominators and match coefficients (or cover-up each root). The hard fraction
  becomes a sum of easy ones, each a standard integral.
- **plain** — a complicated fraction can be broken into a few simple fractions
  added together. Find the simple pieces, integrate each one (they're just logs),
  and add the results.

## LaTeX
rule: \frac{P(x)}{(x-r_{1})(x-r_{2})\cdots}=\frac{A_{1}}{x-r_{1}}+\frac{A_{2}}{x-r_{2}}+\cdots
example: \frac{1}{x^{2}-1}=\frac{1}{2}\left(\frac{1}{x-1}-\frac{1}{x+1}\right)

## References
- A-level Maths / Further Maths (Edexcel C4 partial fractions); Stewart,
  *Calculus*, §7.4.
- Library: SymPy `apart`.

## Links
[[polynomial-division]] · [[standard-integrals]] · [[integration-by-parts]]
