---
id: solving-trig-equations
name: Solving trig equations over an interval
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
An equation like `sinx = k`, `tan2x = 1`, or a **quadratic in a trig function**
(`2sin²x − sinx − 1 = 0`) to be solved over a stated interval such as `[0, 2π)` or
`0° ≤ x < 360°`. Tells: "find all solutions in…", "how many roots", a trig function
appearing squared, or a doubled/shifted argument.

## The rule
1. Reduce to one trig function (use `sin² + cos² = 1`, double-angle, or factor a
   quadratic-in-trig). 2. Solve the base equation: `sinx = k` has principal value
   `x₀ = arcsin k`, and the **full** solution set comes from the function's period
   and symmetry — for sine, `x = x₀ + 2πn` and `x = π − x₀ + 2πn`. 3. Keep only the
   values inside the given interval. Watch a scaled argument (`x → 2x` doubles the
   number of roots).

## Worked example
Solve `2sin²x − sinx − 1 = 0` on `[0, 2π)`.
Let `s = sinx`: `2s² − s − 1 = (2s + 1)(s − 1) = 0`, so `s = 1` or `s = −1/2`.
`sinx = 1` ⇒ `x = π/2`. `sinx = −1/2` ⇒ `x = π + π/6 = 7π/6` and
`x = 2π − π/6 = 11π/6` (third and fourth quadrants).
Solutions: `x ∈ {π/2, 7π/6, 11π/6}`.

## Explain (altitudes)
- **expert** — solving over an interval is choosing the representatives of the
  solution coset modulo the period that land in a fundamental domain; the
  symmetries (`sin(π − x) = sinx`, even/odd) generate the full preimage of `k` under
  the (non-injective) trig map. Quadratic-in-trig is just composing that with a
  polynomial root-finding.
- **working** — treat the trig function as the unknown, factor or use the quadratic
  formula, then back out each value. For each base value get *all* angles via the
  CAST/quadrant rule and add `2πn`, then filter to the interval. A `2x` inside means
  solve over `[0, 4π)` first, then halve.
- **plain** — substitute `s = sinx` so the equation becomes ordinary algebra; solve
  for `s`. Then for each answer find every angle in the range with that sine,
  remembering sine takes each value twice per turn (except at the peaks).

## LaTeX
rule: 2\sin^{2}x-\sin x-1=0\ \Longrightarrow\ \left(2\sin x+1\right)\left(\sin x-1\right)=0
example: \sin x=1\ \text{or}\ \sin x=-\tfrac{1}{2}\ \Longrightarrow\ x\in\left\{\tfrac{\pi}{2},\,\tfrac{7\pi}{6},\,\tfrac{11\pi}{6}\right\}

## References
- A-level Pure (Edexcel/AQA/OCR) "Solving trigonometric equations"; any
  trigonometry/pre-calculus text (Stewart; CGP A-level).
- Library: SymPy `solveset(eq, x, domain=Interval(0, 2*pi))`.

## Links
[[reciprocal-trig-functions]] · [[double-angle-formulae]] · [[harmonic-form]]
