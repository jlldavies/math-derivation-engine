---
id: mellin-transform
name: Mellin transform — the defining integral
domain: transform
regime: integral-transform
status: verified
---

## Applies when (recognition signature)
An integral of the form `∫_0^∞ x^{s-1} f(x) dx` — a function tested against a pure
power `x^{s-1}` over the half-line — or any time you want to turn multiplicative /
scaling structure into an algebraic parameter `s`. This is the base *definition* page;
the contour/residue machinery on top of it lives in [[mellin-barnes]].

## The rule
`M[f](s) = ∫_0^∞ x^{s-1} f(x) dx`, defined on a **fundamental strip** `a < Re(s) < b`
where the integral converges (the bounds are fixed by how `f` behaves at `0` and at
`∞`). Linear; a rescaling `f(λx)` multiplies the transform by `λ^{−s}`. The inverse is
the Mellin–Bromwich (Barnes) contour integral
`f(x) = (1/2πi) ∫_{c−i∞}^{c+i∞} M[f](s) x^{−s} ds` with `c` inside the strip.

## Worked example
`M[e^{-x}](s) = ∫_0^∞ x^{s-1} e^{-x} dx = Γ(s)` on `Re(s) > 0` — Euler's integral of the
second kind. SymPy: `mellin_transform(exp(-x), x, s) = (gamma(s), (0, ∞), True)`.

## Explain (altitudes)
- **expert** — the multiplicative analogue of the Fourier/Laplace transform: it
  diagonalizes the dilation operator `x d/dx`, so `M[f](s)` is the spectrum of `f` under
  scaling. It is holomorphic on its fundamental strip, and its poles encode the
  asymptotics of `f` at `0` and `∞` — the Mellin–Barnes correspondence.
- **working** — multiply `f` by the kernel `x^{s-1}` and integrate over `(0,∞)`; the
  result is a function of `s`, valid on the strip where both endpoints converge. Reading
  off its poles gives series / asymptotics; the inverse is a contour integral.
- **plain** — a recipe that turns a function into a function of a new variable `s` by
  integrating it against a power of `x`. For nice functions you just look the answer up —
  e.g. `e^{-x}` gives the Gamma function.

## LaTeX
rule: M[f](s)=\int_{0}^{\infty}x^{s-1}f(x)\,dx
example: M[e^{-x}](s)=\Gamma(s)\quad(\Re(s)>0)

## References
- DLMF 1.14(iv); Paris & Kaminski, *Asymptotics and Mellin–Barnes Integrals*.
- Library: SymPy `mellin_transform`.

## Links
[[mellin-barnes]] · [[gamma-function]] · [[laplace-transform]] · [[improper-integrals]] · [[meijer-g-reduction]] · [[watsons-lemma]]
