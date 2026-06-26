---
id: binomial-theorem
name: Binomial theorem
domain: algebra
regime: elementary
status: drafted
---

## Applies when (recognition signature)
You need to expand a power of a sum `(a + b)ⁿ`, or read off a single coefficient,
without multiplying the bracket out by hand. Tell: a two-term bracket raised to a
power, or a question asking for "the coefficient of `xᵏ`".

## The rule
For a non-negative integer `n`:

`(a + b)ⁿ = Σ_{k=0}^{n} C(n,k) a^{n−k} bᵏ`,  with `C(n,k) = n! / [k!(n−k)!]`.

The coefficients `C(n,k)` are the entries of Pascal's triangle. For `|x| < 1` the
series extends to **any** real exponent (the binomial series), giving an infinite
expansion that is the Taylor series of `(1+x)ⁿ`.

## Worked example
`(1 + x)³ = C(3,0) + C(3,1)x + C(3,2)x² + C(3,3)x³ = 1 + 3x + 3x² + x³`.
(SymPy: `expand((1+x)**3) → x**3 + 3*x**2 + 3*x + 1`.)

## Explain (altitudes)
- **expert** — `C(n,k)` counts the ways to choose `k` of the `n` factors to
  contribute a `b`; the theorem is the generating-function identity whose
  analytic continuation in `n` is the binomial series, a special `hypergeometric`
  and the `n`-truncation of the `taylor-series` of `(1+x)ⁿ`.
- **working** — each term picks `b` from `k` of the `n` brackets and `a` from the
  rest; there are `C(n,k)` such choices, giving `C(n,k) a^{n−k} bᵏ`. Sum over `k`
  and you've expanded the power without multiplying it out.
- **plain** — to expand `(a+b)ⁿ` you don't multiply it all out: the numbers in
  front come straight from Pascal's triangle, and the powers of `a` count down
  while the powers of `b` count up. For `(1+x)³` that's `1, 3, 3, 1`.

## LaTeX
rule: (a+b)^{n}=\sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^{k},\qquad \binom{n}{k}=\frac{n!}{k!\,(n-k)!}
example: (1+x)^{3}=1+3x+3x^{2}+x^{3}

## References
- A-level Maths / Further Maths (Edexcel C2/C4 binomial expansion); standard
  algebra texts.
- Library: SymPy `expand` / `binomial`.

## Links
[[taylor-series]] · [[arithmetic-geometric-series]]
