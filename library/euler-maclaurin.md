---
id: euler-maclaurin
name: Euler–Maclaurin summation formula
domain: asymptotics
regime: asymptotic_expansion
status: verified
---

## Applies when (recognition signature)
You need to **convert a sum into an integral plus corrections**, or get the
**asymptotics of a partial sum** `Σ_{n=a}^b f(n)` for smooth `f`. Tells: a sum that
looks like a Riemann sum of an integral, "approximate this sum for large `N`",
harmonic-number / `Σ 1/n` asymptotics, Stirling-type expansions, trapezoid-rule
error terms, "connect a discrete sum to a continuous integral". `f` should be
smooth enough to differentiate several times.

## The rule
For `f ∈ C^{2m}` on `[a,b]` (integer endpoints):
`Σ_{n=a}^{b} f(n) = ∫_a^b f(x) dx + (f(a)+f(b))/2 + Σ_{k=1}^{m} B_{2k}/(2k)! [f^{(2k−1)}(b) − f^{(2k−1)}(a)] + R_m`,
where `B_{2k}` are Bernoulli numbers and `R_m` is the remainder (an integral against
a periodic Bernoulli polynomial). Truncating gives an asymptotic expansion; the
`(f(a)+f(b))/2` is the trapezoidal correction.

## Worked example
The harmonic numbers: take `f(x)=1/x`, `a=1`, `b=N`. Then `∫_1^N dx/x = ln N`,
the endpoint term `(1 + 1/N)/2`, and `f'(x) = −1/x²` give
`Σ_{n=1}^N 1/n = ln N + γ + 1/(2N) − 1/(12N²) + ⋯`,
which both defines the Euler–Mascheroni constant `γ` and yields its asymptotic tail.
Matched to mpmath `harmonic(N)` and `euler` (`γ`).

## Explain (altitudes)
- **expert** — repeated integration by parts against Bernoulli polynomials interpolates
  the sum by `∫ f`; the `B_{2k}` corrections are the obstruction terms, and the formula
  is the bridge from the trapezoid rule to `ζ`-values and Stirling's series.
- **working** — a sum is roughly the integral of `f`; the formula makes that exact by
  adding the trapezoid endpoint average and a series of derivative corrections weighted
  by Bernoulli numbers, giving an asymptotic expansion you truncate.
- **plain** — adding up `f` at whole numbers is almost the same as the area under `f`;
  this gives the area plus small, shrinking fix-up terms so the two agree.

## LaTeX
rule: \sum_{n=a}^{b}f(n)=\int_{a}^{b}f(x)\,dx+\frac{f(a)+f(b)}{2}+\sum_{k=1}^{m}\frac{B_{2k}}{(2k)!}\left[f^{(2k-1)}(b)-f^{(2k-1)}(a)\right]+R_m
example: \sum_{n=1}^{N}\frac{1}{n}=\ln N+\gamma+\frac{1}{2N}-\frac{1}{12N^{2}}+\cdots
## References
- DLMF 2.10(i) (Euler–Maclaurin formula and remainder); Bender & Orszag, *Advanced Mathematical Methods*, §6.6.
- Gradshteyn–Ryzhik 0.121; Abramowitz & Stegun 23.1.30.
- Library: mpmath `sumem` (Euler–Maclaurin summation), `harmonic`, `euler` (`γ`).
- Worked example: harmonic-number asymptotics, standard (DLMF 2.10.8).

## Links
[[zeta-regularization]] · [[abel-plana]] · [[gamma-function]]
