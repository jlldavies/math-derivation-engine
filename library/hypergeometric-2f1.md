---
id: hypergeometric-2f1
name: Gauss ₂F₁ — the master hypergeometric
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
A series `Σ (a)_k (b)_k / ((c)_k k!) z^k` (ratio of consecutive terms a rational
function of `k`), or the Euler-type integral `∫_0^1 t^{b-1}(1−t)^{c-b-1}(1−zt)^{-a}dt`,
or the ODE `z(1−z)y'' + [c−(a+b+1)z]y' − ab y = 0`. Tells: most named special
functions are special cases (elementary, Legendre, Jacobi, complete elliptic).

## The rule
`₂F₁(a,b;c;z) = Σ_{k≥0} (a)_k (b)_k / ((c)_k k!) z^k`, `|z|<1`, with Pochhammer
`(q)_k = q(q+1)…(q+k−1)`. Euler integral (`Re c > Re b > 0`):
`₂F₁(a,b;c;z) = Γ(c)/(Γ(b)Γ(c−b)) ∫_0^1 t^{b-1}(1−t)^{c-b-1}(1−zt)^{-a} dt`.

## Worked example
`₂F₁(a,b;b;z) = (1−z)^{-a}`. With `c = b` the `k`-th coefficient is
`(a)_k (b)_k / ((b)_k k!) = (a)_k/k!`, so the series is `Σ (a)_k z^k/k!`, the binomial
series for `(1−z)^{-a}` (SymPy `hyper`).

## Explain (altitudes)
- **expert** — `₂F₁` is the canonical Fuchsian function with regular singular points
  at `0,1,∞`; the Euler integral is its Riemann–Liouville / Mellin–Barnes
  representation, and `c=b` collapses the contour to the binomial theorem.
- **working** — setting `c = b` cancels `(b)_k` against `(c)_k`, leaving the
  Maclaurin series of `(1−z)^{-a}`; the Euler integral is then just the Beta integral
  with the `(1−zt)^{-a}` factor expanded.
- **plain** — one super-formula that contains lots of familiar functions; with two
  parameters equal it reduces to the ordinary `(1−z)^{-a}`.

## LaTeX
rule: {}_2F_1(a,b;c;z)=\sum_{k=0}^{\infty}\frac{(a)_k (b)_k}{(c)_k\,k!}\,z^k=\frac{\Gamma(c)}{\Gamma(b)\Gamma(c-b)}\int_{0}^{1}t^{b-1}(1-t)^{c-b-1}(1-zt)^{-a}\,dt
example: {}_2F_1(a,b;b;z)=\left(1-z\right)^{-a}

## References
- DLMF 15.2.1 (series), 15.6.1 (Euler integral), 15.4.6 (the `(1−z)^{-a}` case).
- Gradshteyn–Ryzhik 9.111. SymPy `hyper`; mpmath `hyp2f1`.

## Links
[[beta-function]] · [[gamma-function]] · [[meijer-g-reduction]]
