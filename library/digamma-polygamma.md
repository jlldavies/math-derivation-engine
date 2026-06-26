---
id: digamma-polygamma
name: Digamma & polygamma — log-derivatives of Gamma
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
Sums `Σ [1/(k+α) − 1/(k+β)]`, harmonic-number tails, derivatives of `Γ` w.r.t. a
parameter, or `ln Γ` appearing in an expansion. Tells: telescoping `1/(k+a)` series,
`∂_a` of Beta/Gamma integrals, finite parts of `Σ 1/k`-type divergences.

## The rule
Digamma `ψ(s) = Γ'(s)/Γ(s) = d/ds ln Γ(s)`, with `ψ(1) = −γ` (Euler–Mascheroni),
recurrence `ψ(s+1) = ψ(s) + 1/s`, and series `ψ(s) = −γ + Σ_{k≥0}[1/(k+1) − 1/(k+s)]`.
Polygamma `ψ^{(m)}(s) = d^m/ds^m ψ(s) = (−1)^{m+1} m! Σ_{k≥0} 1/(k+s)^{m+1}`.

## Worked example
`Σ_{k=0}^∞ [1/(k+1) − 1/(k+a)] = ψ(a) + γ`. This is exactly the series form of `ψ`
rearranged: `ψ(a) = −γ + Σ_{k≥0}[1/(k+1) − 1/(k+a)]`, so the sum equals `ψ(a) + γ`
(mpmath `digamma`; e.g. `a=2` gives `ψ(2)+γ = 1`).

## Explain (altitudes)
- **expert** — `ψ` is the logarithmic derivative of the Weierstrass product for `Γ`,
  so the `γ` and the `Σ[1/(k+1)−1/(k+s)]` are the product's `e^{γs}` and `∏(1+s/k)`
  pieces differentiated; polygammas are its higher logarithmic derivatives ↔ Hurwitz `ζ`.
- **working** — differentiate `ln Γ(s) = −γ s − ln s + Σ_k[s/k − ln(1+s/k)]` once;
  the result is `−γ − 1/s + Σ[1/k − 1/(k+s)]`, i.e. the stated series, giving the sum.
- **plain** — `ψ` measures how fast `Γ` grows in log-terms; its building-block series
  is `Σ[1/(k+1) − 1/(k+a)]`, which therefore equals `ψ(a)+γ`.

## LaTeX
rule: \psi(s)=\frac{\Gamma'(s)}{\Gamma(s)},\quad \psi(1)=-\gamma,\qquad \psi^{(m)}(s)=(-1)^{m+1}m!\sum_{k=0}^{\infty}\frac{1}{(k+s)^{m+1}}
example: \sum_{k=0}^{\infty}\left(\frac{1}{k+1}-\frac{1}{k+a}\right)=\psi(a)+\gamma

## References
- DLMF 5.4.13 (`ψ(1)=−γ`), 5.7.6 (series), 5.15 (polygamma).
- Gradshteyn–Ryzhik 8.36. SymPy `digamma`/`polygamma`; mpmath `digamma`.

## Links
[[gamma-function]] · [[euler-maclaurin]] · [[zeta-regularization]]
