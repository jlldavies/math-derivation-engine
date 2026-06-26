---
id: watsons-lemma
name: Watson's lemma — endpoint asymptotics of Laplace integrals
domain: special-function
regime: asymptotic_expansion
status: verified
---

## Applies when (recognition signature)
You want the **large-parameter asymptotics** of a Laplace-type integral
`∫_0^∞ f(t) e^{-x t} dt` as `x → ∞` (or, via `x → ±i·(freq)`, an oscillatory /
Fourier integral). The value is dominated by the endpoint `t = 0`.

## The rule
Expand `f` near `t=0`, `f(t) ~ Σ a_k t^{k+λ}`, and integrate term by term using
`∫_0^∞ t^{σ-1} e^{-x t} dt = Γ(σ)/x^σ`:
`∫_0^∞ f(t) e^{-x t} dt ~ Σ a_k Γ(k+λ+1) / x^{k+λ+1}`  (`x → ∞`).
Only the behaviour of `f` at the endpoint matters.

## Worked example
`∫_0^∞ e^{-x t}/(1+t) dt ~ Σ_k (−1)^k k! / x^{k+1}`  (from `1/(1+t)=Σ(−1)^k t^k`).
This is the engine behind the Blitz ℒ-asymptotics (`examples/subleading_*`).

## Explain (altitudes)
- **expert** — the asymptotic contribution localizes at the endpoint; rigorous via
  the Γ-moments; the oscillatory analogue is stationary phase / the Erdélyi
  extension, and it underlies the large-`z` expansion of `U` and Meijer-G.
- **working** — for large damping `x`, only `f` near `t=0` survives; Taylor-expand
  there and integrate each power against `e^{-x t}` (giving a Γ over a power of `x`).
- **plain** — with strong damping the integral only "feels" the very start
  `t ≈ 0`; describe `f` there and add up the pieces.

## LaTeX
rule: \int_{0}^{\infty}f(t)\,e^{-x t}\,dt\sim\sum_{k}a_k\,\frac{\Gamma(k+\lambda+1)}{x^{\,k+\lambda+1}}
example: \int_{0}^{\infty}\frac{e^{-x t}}{1+t}\,dt\sim\sum_{k}\frac{(-1)^{k}\,k!}{x^{\,k+1}}

## References
- Bender & Orszag, *Advanced Mathematical Methods*, ch. 6; DLMF 2.3.
- Registry: `asymptotic_expansion`.

## Links
[[gamma-function]] · [[tricomi-u-reduction]] · [[gaussian-integral]] · [[borel-summation]]
