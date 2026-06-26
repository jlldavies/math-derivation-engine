---
id: laplace-transform
name: Laplace transform
domain: transform
regime: integral-transform
status: verified
---

## Applies when (recognition signature)
A causal function `f(t)` on `[0,∞)`, an initial-value ODE, a convolution, or an
integral against `e^{−st}`. Tell: `∫_0^∞ e^{−st}(…) dt`, transient/decay problems,
or a known transform pair you can read off a table.

## The rule
`F(s) = L[f](s) = ∫_0^∞ e^{−st} f(t) dt`, defined for `Re(s)` large enough for
convergence. Linear; turns `d/dt` into multiplication by `s` (minus initial data)
and convolution into a product. Solve in `s`-space, then invert by table or by the
Bromwich contour.

## Worked example
`L[t^{a−1}] = Γ(a)/s^a` for `Re(a) > 0`. Substitute `u = st` in
`∫_0^∞ e^{−st} t^{a−1} dt` to get `s^{−a} ∫_0^∞ e^{−u} u^{a−1} du = Γ(a)/s^a`.
(Known result; `a = 1` gives `1/s`.)

## Explain (altitudes)
- **expert** — the transform is a pairing of `f` against the eigenfunctions
  `e^{−st}` of `d/dt`; analyticity of `F(s)` in a right half-plane encodes growth,
  and inversion is the Mellin–Bromwich contour integral.
- **working** — multiply by a decaying weight `e^{−st}` and integrate out `t`,
  trading the time-domain ODE for an algebra problem in `s`; solve, then look up
  the inverse.
- **plain** — re-describe a signal by how much of each decay rate it contains.
  In that picture calculus turns into ordinary algebra, so the problem gets easy.

## LaTeX
rule: F(s)=\int_{0}^{\infty}e^{-st}f(t)\,dt
example: \mathcal{L}\left[t^{a-1}\right](s)=\frac{\Gamma(a)}{s^{a}}

## References
- Standard integral transform; tables in Abramowitz & Stegun §29, Oberhettinger.
- Library: SymPy `laplace_transform`.

## Links
[[gamma-function]] · [[tricomi-u-reduction]] · [[watsons-lemma]] · [[z-transform]] · [[inverse-laplace-bromwich]]
