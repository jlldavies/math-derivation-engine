---
id: taylor-series
name: Taylor (Maclaurin) series
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
You want to approximate a smooth function near a point by a polynomial, or
recognise a power series as a known function. Tell: "expand to order `n`",
"small-`x` behaviour", `e^x`/`sin x`/`(1+x)^k` written as an infinite sum, or a
limit you'd attack with the first few terms.

## The rule
If `f` is infinitely differentiable near `a`, then

`f(x) = Σ_{n≥0} f^{(n)}(a)/n! · (x − a)^n
      = f(a) + f'(a)(x−a) + f''(a)/2!·(x−a)² + …`

The case `a = 0` is the Maclaurin series. Each coefficient is fixed by matching
the `n`-th derivative at `a`.

## Worked example
`e^x`: every derivative is `e^x`, equal to `1` at `0`, so
`e^x = Σ x^n/n! = 1 + x + x²/2 + x³/6 + …`.
For `sin x` the derivatives cycle `0,1,0,−1`, giving
`sin x = x − x³/3! + x⁵/5! − … = x − x³/6 + x⁵/120 − …`.

## Explain (altitudes)
- **expert** — the truncated series is the unique degree-`n` polynomial agreeing
  with `f` to `n`-th order at `a`; convergence and the remainder are controlled by
  the Lagrange/integral form `R_n`, and the radius of convergence is set by the
  nearest singularity in the complex plane.
- **working** — build a polynomial whose value, slope, curvature, … all match `f`
  at `a`. The `n!` in the denominator is exactly what's needed so the `n`-th
  derivative of the term `(x−a)^n` reproduces the coefficient `f^{(n)}(a)`.
- **plain** — copy a curvy function with a polynomial by matching it more and more
  closely at one point: same height, then same slope, then same bend, and so on.
  Each extra term sharpens the fit near that point. For `e^x` the pattern is just
  `1 + x + x²/2 + x³/6 + …`.

## LaTeX
rule: f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}\left(x-a\right)^{n}
example: e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\cdots

## References
- A-level Further Pure / first-year analysis "Taylor and Maclaurin series";
  Stewart; Spivak.
- Library: SymPy `series` / `f.series(x, a, n)`.

## Links
[[binomial-theorem]] · [[chain-rule]] · [[arithmetic-geometric-series]]
