---
id: hadamard-finite-part
name: Hadamard finite part — analytic continuation past a pole
domain: regularization
regime: regularization
status: drafted
---

## Applies when (recognition signature)
A half-line integral `∫_0^∞ x^{a−1} f(x) dx` that **diverges at an endpoint** (UV at
`x→0` or large-`x`) because the power `a` sits past the convergence boundary. Tell:
the integral converges as an analytic function of `a` in some strip, has a **simple
pole** at the offending integer `a`, and you want the *finite* value there. Often
flagged by a `(e^{−sx}−1)`-style subtraction making the integrand integrable.

## The rule
Define the integral by **analytic continuation in the exponent `a`** (Mellin
continuation). Where it converges it is a meromorphic function `F(a)` of `a`; the
divergence at the target `a₀` is a simple pole. The **Hadamard finite part** is the
regular (constant) term of the Laurent expansion there:

`F.p. ∫_0^∞ x^{a₀−1} f(x) dx = lim_{a→a₀} [ F(a) − (pole part) ]`.

Equivalently, subtract the divergent Taylor piece of `f` that causes the endpoint
divergence — e.g. `f(x)→f(x)−f(0)` near `0`, the `(e^{−sx}−1)` subtraction — so the
remaining integral converges and equals the same finite part.

## Worked example
The Blitz UV-divergent `α`-integral. The momentum integral leaves a parametric
integral of Tricomi/`Γ` type, `∫_0^∞ α^{a−1} g(α) dα`, that diverges at `α→0` for
the physical exponent. Continue in `a`: the integral is `Γ(a)·(analytic)`, with the
UV divergence sitting in `Γ(a)`'s pole. The finite part is the value after dropping
that pole — the `(e^{−sα}−1)` subtraction reproduces it, and it matches the Tricomi
closed form continued past its convergence boundary
(`examples/subleading_closed_form.py`, the divergent piece).

## Explain (altitudes)
- **expert** — the Mellin transform `F(a)=∫x^{a−1}f(x)dx` is meromorphic; endpoint
  divergences become poles whose residues are the Taylor coefficients of `f` at the
  endpoint. The finite part is the renormalized value — the same object as a
  minimal-subtraction counterterm, and it agrees with the analytic continuation of
  the special-function closed form.
- **working** — treat the exponent as a variable, integrate where it converges to
  get a function with a pole, then read off the constant term at the pole; or just
  subtract the piece of the integrand that misbehaves at the endpoint and integrate
  the rest.
- **plain** — the integral is infinite only because of one bad sliver near the edge.
  Slide the power slightly so it converges, get a formula, and keep the part that
  stays finite as you slide back — the infinity lives in a single pole you discard.

## LaTeX
rule: \operatorname{F.p.}\int_{0}^{\infty}x^{a_{0}-1}f(x)\,dx=\lim_{a\to a_{0}}\left[\,\int_{0}^{\infty}x^{a-1}f(x)\,dx-\frac{\operatorname{Res}}{a-a_{0}}\,\right]
example: \int_{0}^{\infty}x^{a-1}\left(e^{-sx}-1\right)dx=\Gamma(a)\,s^{-a},\qquad -1<\operatorname{Re}a<0
## References
- Hadamard, *Lectures on Cauchy's Problem* (1923) (partie finie).
- Gelfand & Shilov, *Generalized Functions*, Vol. I, §3 (`x_+^λ` continuation).
- DLMF 1.16(v) / Mellin-transform continuation.

## Links
[[tricomi-u-reduction]] · [[mellin-barnes]] · [[gamma-function]] · [[zeta-regularization]]
