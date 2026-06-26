---
id: arithmetic-geometric-series
name: Arithmetic and geometric series
domain: calculus
regime: elementary
status: drafted
---

## Applies when (recognition signature)
A sum whose terms change by a **constant difference** (arithmetic) or a
**constant ratio** (geometric). Tell: `a, a+d, a+2d, …` or `a, ar, ar², …`;
"sum the first `n` terms", "sum to infinity", recurring decimals, or a
`Σ r^n` you want in closed form.

## The rule
Arithmetic progression (common difference `d`):
`S_n = n/2 · (2a + (n−1)d) = n/2 · (first + last)`.

Geometric progression (common ratio `r`):
`S_n = a(1 − r^n)/(1 − r)` for `r ≠ 1`; and if `|r| < 1`, as `n → ∞`,
`S_∞ = a/(1 − r)`.

## Worked example
`Σ_{n≥1} (1/2)^n`: a GP with first term `a = 1/2` and ratio `r = 1/2`, so
`S_∞ = (1/2)/(1 − 1/2) = 1`.

## Explain (altitudes)
- **expert** — the geometric sum is the partial-fraction/telescoping identity
  `(1−r)Σ_{0}^{n-1} r^k = 1 − r^n`; convergence for `|r|<1` is the `r`-disc of the
  generating function `1/(1−r)`, the prototype for every power series' radius.
- **working** — for the AP, pair the first and last terms (each pair sums to
  `2a+(n−1)d`). For the GP, multiply `S` by `r`, subtract, and everything in the
  middle cancels, leaving `S(1−r) = a(1−r^n)`.
- **plain** — adding a list that grows by a fixed step: average the first and last
  and multiply by how many there are. Adding one that's multiplied by a fixed
  fraction each time: if the fraction is less than 1 the terms shrink to nothing
  and the whole endless sum lands on a finite number — like `½+¼+⅛+… = 1`.

## LaTeX
rule: S_{n}=\frac{n}{2}\left(2a+(n-1)d\right),\qquad \sum_{k=0}^{\infty}ar^{k}=\frac{a}{1-r}\ \ (|r|<1)
example: \sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^{n}=\frac{\tfrac{1}{2}}{1-\tfrac{1}{2}}=1

## References
- A-level Pure "Sequences and series" (arithmetic & geometric); standard in any
  algebra/pre-calculus text.
- Library: SymPy `summation` / `Sum(...).doit()`.

## Links
[[binomial-theorem]] · [[taylor-series]]
