---
id: sturm-liouville
name: Sturm–Liouville theory — real eigenvalues, orthogonal eigenfunctions
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
A second-order linear eigenvalue ODE in self-adjoint form `(p u')' + (q + λw)u = 0`
with separated homogeneous BCs — typically the spatial ODE left by separation of
variables. Tells: "eigenvalues/eigenfunctions", "orthogonal modes", weight
function `w`, completeness/expansion theorems, Bessel/Legendre/trig mode families.

## The rule
For the regular Sturm–Liouville problem `(p u')' + (q + λw)u = 0` on `[a,b]` with
`p,w>0` and separated BCs, the operator is self-adjoint, so: eigenvalues `λ_n` are
**real**, simple, and `→∞`; eigenfunctions `u_n` for distinct `λ_n` are
**orthogonal under the weight** `w`, `∫_a^b u_m u_n w dx = 0` (`m≠n`); and they form
a complete basis for expanding any sufficiently smooth function.

## Worked example
`u'' + λu = 0` (so `p=w=1`, `q=0`) on `[0,π]` with `u(0)=u(π)=0`. Nontrivial
solutions need `λ_n = n²` with `u_n = sin(nx)`, `n=1,2,…`. These are orthogonal:
`∫_0^π sin(mx)sin(nx) dx = 0` for `m≠n` and `π/2` for `m=n` — the basis behind the
Fourier sine series. Standard result (Coddington & Levinson, *Theory of ODEs*, ch. 7).

## Explain (altitudes)
- **expert** — writing the operator as `L = (1/w)[(p∂)∂ + q]` makes it formally
  self-adjoint in `L²(w)`; reality and orthogonality follow from
  `⟨Lu,v⟩=⟨u,Lv⟩` plus the boundary terms vanishing, and Sturm comparison gives the
  oscillation/completeness theorems.
- **working** — put the ODE in `(pu')' + (q+λw)u = 0` form; the BCs select a
  discrete `λ_n`. Because the operator is symmetric under the `w`-weighted inner
  product, different modes are orthogonal — exactly what lets you expand data in them.
- **plain** — this kind of equation only "rings" at certain special numbers
  (eigenvalues), each with its own shape. Those shapes don't overlap (they're
  orthogonal), so you can build any signal by mixing them.

## LaTeX
rule: \left(p\,u'\right)'+\left(q+\lambda w\right)u=0\ \Rightarrow\ \int_{a}^{b}u_{m}\,u_{n}\,w\,dx=0\ (m\neq n)
example: u''+\lambda u=0,\ u(0)=u(\pi)=0\ \Rightarrow\ \lambda_{n}=n^{2},\ u_{n}=\sin(nx)

## References
- Coddington & Levinson, *Theory of Ordinary Differential Equations*, ch. 7–8.
- Al-Gwaiz, *Sturm–Liouville Theory and its Applications*, ch. 2–3.
- Library: SciPy `scipy.linalg.eigh_tridiagonal` (discretized SL problems); SymPy for closed forms.
- Worked example: Coddington & Levinson ch. 7 (`u''+λu=0` on `[0,π]`).

## Links
[[separation-of-variables]] · [[fourier-series]] · [[eigendecomposition]] · [[greens-function]]
