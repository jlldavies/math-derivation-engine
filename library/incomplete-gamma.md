---
id: incomplete-gamma
name: Incomplete Gamma — the split exponential moment
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
`∫_x^∞ t^{a-1} e^{-t} dt` or `∫_0^x t^{a-1} e^{-t} dt` — the Gamma integrand cut at
a finite limit `x`. Tells: a power times `e^{-t}` over a *partial* range; tail/CDF
probabilities; truncated exponential moments; large-`x` asymptotics of such tails.

## The rule
Upper `Γ(a,x) = ∫_x^∞ t^{a-1} e^{-t} dt` and lower `γ(a,x) = ∫_0^x t^{a-1} e^{-t} dt`
satisfy `γ(a,x) + Γ(a,x) = Γ(a)`. Recurrence `Γ(a+1,x) = a Γ(a,x) + x^a e^{-x}`.
Large-`x` asymptotic: `Γ(a,x) ~ x^{a-1} e^{-x}` (leading term).

## Worked example
As `x → ∞`, `Γ(a,x) ~ x^{a-1} e^{-x}` — integrate `∫_x^∞ t^{a-1}e^{-t}dt` by parts
once: `= x^{a-1}e^{-x} + (a−1)∫_x^∞ t^{a-2}e^{-t}dt`, and the remainder is smaller
by a factor `~(a−1)/x`, so the first term dominates (matches mpmath `gammainc`).

## Explain (altitudes)
- **expert** — `Γ(a,x)` is the entire-in-`a` continuation of the Gamma tail; its
  asymptotic series `x^{a-1}e^{-x}Σ (a-1)(a-2)…/x^k` is a Watson's-lemma expansion of
  the shifted integrand, divergent but asymptotic, with the exponential setting scale.
- **working** — one integration by parts peels off `x^{a-1}e^{-x}` and leaves an
  integral of the same shape with `a → a−1`; iterating gives the asymptotic series,
  and the first term is the leading behaviour for large `x`.
- **plain** — split the factorial-integral at a point `x`: the upper piece is almost
  all "out near `x`", so for large `x` it is just `x^{a-1}e^{-x}`.

## LaTeX
rule: \Gamma(a,x)=\int_{x}^{\infty}t^{a-1}e^{-t}\,dt,\qquad \gamma(a,x)=\int_{0}^{x}t^{a-1}e^{-t}\,dt,\qquad \gamma(a,x)+\Gamma(a,x)=\Gamma(a)
example: \Gamma(a,x)\;\sim\;x^{a-1}e^{-x}\qquad(x\to\infty)

## References
- DLMF 8.2 (definitions), 8.11.2 (asymptotics); Gradshteyn–Ryzhik 8.350.
- SymPy `uppergamma`/`lowergamma`; mpmath `gammainc`.

## Links
[[gamma-function]] · [[watsons-lemma]] · [[error-function]]
