---
id: trig-power-series
name: Power series for sine and cosine
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You need sin or cos as an analytic object — to differentiate term-by-term, take a
limit, justify a small-angle estimate, or define the functions without appeal to
geometry. Tells: "Maclaurin series of sin/cos", "entire function", "show sin x ≈ x",
"prove the series converges everywhere", power-series manipulation of trig.

## The rule
The sine and cosine are defined (or recovered) by their Maclaurin series, which
converge for **every** real (and complex) `x`:
`sin x = Σ_{n≥0} (−1)ⁿ x^{2n+1}/(2n+1)! = x − x³/3! + x⁵/5! − ⋯`
`cos x = Σ_{n≥0} (−1)ⁿ x^{2n}/(2n)! = 1 − x²/2! + x⁴/4! − ⋯`
Both have infinite radius of convergence (the ratio test gives `|x|²/[(2n+2)(2n+3)] → 0`),
so sin and cos are **entire**. Taken as definitions, all the standard properties —
`sin' = cos`, `cos' = −sin`, the Pythagorean identity, periodicity — follow from the
series alone.

## Worked example
Read the small-angle behaviour straight off the series: keeping terms to `x³`,
`sin x = x − x³/6 + O(x⁵)`, so `sin x ≈ x` for small `x` and the first correction is
`−x³/6`. Likewise `cos x = 1 − x²/2 + O(x⁴)`. For convergence everywhere, fix any `x`
and apply the ratio test to `sin x`: the ratio of successive nonzero terms is
`x²/[(2n+2)(2n+3)] → 0 < 1`, so the series converges absolutely for all `x` — the
defining series never "runs out". Standard result (Rudin, *Principles*, ch. 8).

## Explain (altitudes)
- **expert** — define `exp`, `sin`, `cos` by their power series on ℂ; absolute
  convergence everywhere makes them entire, term-by-term differentiation is licensed
  inside the radius, and the Cauchy product yields the addition formulae and Euler's
  identity, decoupling trigonometry from Euclidean geometry.
- **working** — sin and cos are their Taylor series about 0; because the factorials
  in the denominator outrun any power of `x`, the tail vanishes and the series equals
  the function for every `x`. Truncating gives polynomial approximations with known
  error `O(x^{2n+…})`.
- **plain** — you can build sine and cosine out of an endless alternating sum of
  powers of `x`. For small `x` only the first term matters, so `sin x ≈ x`; add a few
  more terms and you match the curve as far out as you like.

## LaTeX
rule: \sin x=\sum_{n=0}^{\infty}\frac{(-1)^{n}x^{2n+1}}{(2n+1)!},\qquad \cos x=\sum_{n=0}^{\infty}\frac{(-1)^{n}x^{2n}}{(2n)!}\quad(\text{all }x)
example: \sin x = x-\frac{x^{3}}{6}+O\!\left(x^{5}\right)\ \Rightarrow\ \sin x\approx x

## References
- Rudin, *Principles of Mathematical Analysis*, ch. 8 (exp/sin/cos by power series).
- Abramowitz & Stegun, *Handbook of Mathematical Functions*, §4.3.
- Library: SymPy `series(sin(x), x, 0, n)`; mpmath for high-precision evaluation.
- Worked example: A&S §4.3.65–66 (Maclaurin series, small-angle terms).

## Links
[[taylor-series]] · [[euler-formula]] · [[small-angle-approximation]] · [[pythagorean-identity]]
