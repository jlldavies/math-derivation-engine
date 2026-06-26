---
id: improper-integrals
name: Improper integrals — convergence at 0 and ∞
domain: calculus
regime: elementary
status: verified
---

## Applies when (recognition signature)
An integral with an infinite limit (`∫^∞ …`) or an integrand that blows up at an
endpoint (`∫_0 x^{p}` with `p<0`); deciding **whether such an integral converges** before
trusting a closed form. This is what fixes the *fundamental strip* of the Gamma, Laplace
and Mellin integrals.

## The rule
An improper integral is a **limit of proper ones**, taken at each bad endpoint. Two
standard power-law tests:
- **endpoint at 0 (p-test):** `∫_0^1 x^{p} dx` converges ⟺ `p > −1`.
- **tail at ∞:** `∫_1^∞ x^{p} dx` converges ⟺ `p < −1`; any integrand killed by `e^{-x}`
  (which decays faster than every power) converges at `∞` regardless of the power.

## Worked example
`∫_0^∞ x^{s-1} e^{-x} dx` converges for `Re(s) > 0`: near `0` the integrand `≈ x^{s-1}`,
finite ⟺ `s−1 > −1 ⟺ s > 0`; for large `x`, `e^{-x}` beats every power, so the tail
converges. (That `Re(s)>0` is exactly the fundamental strip of `Γ(s)`.)

## Explain (altitudes)
- **expert** — convergence is set by the *local order* of the integrand at each singular
  endpoint: a power law `x^{α}` is integrable at `0` iff `α > −1` and at `∞` iff `α < −1`;
  exponential decay dominates every power, securing the `∞`-end unconditionally. This
  pins the fundamental strips of the Gamma, Laplace and Mellin integrals.
- **working** — split the integral at its bad points and take a limit at each. At `0`
  compare with `x^{p}` (need `p > −1`); at `∞` compare with `x^{p}` (need `p < −1`), or use
  that `e^{-x}` decays faster than any power.
- **plain** — an integral over an infinite range, or one where the curve shoots to
  infinity, only encloses a finite area if the function shrinks fast enough. `∫_1^∞ 1/x`
  is infinite; `∫_1^∞ 1/x²` is finite.

## LaTeX
rule: \int_{0}^{1}x^{p}\,dx<\infty\iff p>-1,\qquad \int_{1}^{\infty}x^{p}\,dx<\infty\iff p<-1
example: \int_{0}^{\infty}x^{\,s-1}e^{-x}\,dx\ \text{converges}\iff \Re(s)>0

## References
- Any calculus text (comparison test / p-test); DLMF 1.4(iv).

## Links
[[gamma-function]] · [[exponential-function]] · [[gaussian-integral]] · [[standard-integrals]] · [[watsons-lemma]]
