---
id: exponential-function
name: The exponential function e^x
domain: calculus
regime: elementary
status: verified
---

## Applies when (recognition signature)
Anything built on `e^x` or `e^{-x}` — growth/decay, the function that is its own
derivative, the series for `e^x`, or substituting `f(x)=e^{-x}` into an integral or
transform. The decaying factor `e^{-x}` is the canonical weight under the Gamma, Laplace
and Mellin integrals.

## The rule
`d/dx e^x = e^x`, `e^0 = 1`, `e^x e^y = e^{x+y}`, and `e^x = Σ_{n≥0} x^n/n!`. The decaying
branch `e^{-x} = 1/e^x → 0` as `x→∞`, and it shrinks **faster than any power** of `x`
grows. Basic integrals: `∫ e^x dx = e^x + C`, `∫_0^∞ e^{-x} dx = 1`.

## Worked example
`∫_0^∞ e^{-x} dx = [−e^{-x}]_0^∞ = 0 − (−1) = 1` (which is `Γ(1) = 0! = 1`).

## Explain (altitudes)
- **expert** — the unique solution of `y'=y` with `y(0)=1`; `exp` is the group
  isomorphism `(ℝ,+) → (ℝ_{>0},×)`, entire with no zeros, and `e^{-x}` is the
  rapidly-decaying weight that makes the Euler/Laplace/Mellin integrals converge.
- **working** — the function equal to its own derivative; because `e^{-x}` decays faster
  than any polynomial grows, integrals like `∫_0^∞ (power)·e^{-x} dx` converge at `∞`.
- **plain** — repeated multiplication extended to *any* power, with the special base
  `e ≈ 2.718`. `e^{-x}` is a curve that starts at `1` (when `x=0`) and shrinks toward `0`
  as `x` grows.

## LaTeX
rule: \frac{d}{dx}e^{x}=e^{x},\qquad e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!},\qquad e^{-x}\xrightarrow[x\to\infty]{}0
example: \int_{0}^{\infty}e^{-x}\,dx=\big[-e^{-x}\big]_{0}^{\infty}=1

## References
- Any calculus text; DLMF 4.2; SymPy / mpmath `exp`.

## Links
[[gamma-function]] · [[taylor-series]] · [[hyperbolic-functions]] · [[euler-formula]] · [[improper-integrals]] · [[standard-integrals]]
