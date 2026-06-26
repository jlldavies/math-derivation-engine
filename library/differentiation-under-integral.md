---
id: differentiation-under-integral
name: Differentiation under the integral sign (Feynman's trick)
domain: calculus
regime: parameter-integral
status: verified
---

## Applies when (recognition signature)
An integral that is hard as-is but sits inside a family `I(α)` indexed by a
parameter, where differentiating in `α` simplifies the integrand (kills a factor,
linearizes an exponential). Tell: a parameter you can introduce or already have,
and `∂f/∂α` cleaner than `f`.

## The rule
**Leibniz rule** (fixed limits): differentiate through the integral,

`d/dα ∫_a^b f(x,α) dx = ∫_a^b ∂f/∂α dx`,

valid when `f` and `∂f/∂α` are continuous on `[a,b]×` (parameter range). Build an
ODE for `I(α)`, solve it, and fix the constant from a known value `I(α_0)`.

## Worked example
`I(α) = ∫_0^∞ e^{−x²} cos(αx) dx`. Differentiating and integrating the `∂/∂α`
integrand by parts gives `I'(α) = −(α/2) I(α)`, so `I(α) = I(0) e^{−α²/4}` with
`I(0) = √π/2`. Hence `I(α) = (√π/2) e^{−α²/4}`. (Known result.)

## Explain (altitudes)
- **expert** — interchange of `d/dα` and `∫` is justified by dominated
  convergence / uniform continuity of `∂_α f`; the trick converts a quadrature
  into an ODE whose solution is pinned by one boundary value.
- **working** — slip a parameter into the integral, differentiate inside the
  integral sign to get a simpler integrand, solve the resulting differential
  equation for `I(α)`, then anchor it with an easy known case.
- **plain** — add a dial to the problem. Watch how the answer changes as you turn
  the dial — that rate is easy to compute — then add it all back up from a starting
  point you already know.

## LaTeX
rule: \frac{d}{d\alpha}\int_{a}^{b}f(x,\alpha)\,dx=\int_{a}^{b}\frac{\partial f}{\partial\alpha}\,dx
example: I(\alpha)=\int_{0}^{\infty}e^{-x^{2}}\cos(\alpha x)\,dx=\frac{\sqrt{\pi}}{2}\,e^{-\alpha^{2}/4}

## References
- Leibniz integral rule; popularized as "Feynman's trick" (Feynman, *Surely You're Joking*).
- Library: SymPy `diff` under `Integral`; verify with `integrate`.

## Links
[[gaussian-integral]] · [[integration-by-parts]] · [[laplace-transform]]
