---
id: separation-of-variables
name: Separation of variables — split a PDE into ODEs
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
A linear, homogeneous PDE on a product domain with homogeneous boundary
conditions, and you want a series/product solution. Tells: `u_t = u_xx`,
`u_tt = c²u_xx`, `∇²u = 0` with `u(0,t)=u(L,t)=0`; "separable", "product
solution", "expand in modes", a rectangular/disk geometry with BCs on each edge.

## The rule
Seek `u(x,t) = X(x)T(t)`. Substituting and dividing by `XT` forces each side to
depend on a different variable, so both equal a constant `−λ`:
`X''/X = T'/T = −λ`. This splits the PDE into two ODEs,
`X'' + λX = 0` and `T' + λT = 0` (heat) or `T'' + c²λT = 0` (wave). The
homogeneous BCs make `X` a Sturm–Liouville eigenproblem with a discrete spectrum
`λ_n`; superpose the modes and fix coefficients from the initial data.

## Worked example
Heat equation `u_t = u_xx` on `[0,π]`, `u(0,t)=u(π,t)=0`. Then `X''+λX=0` with
`X(0)=X(π)=0` gives `λ_n = n²`, `X_n = sin(nx)`, and `T_n = e^{−n²t}`, so
`u(x,t) = Σ_{n≥1} b_n e^{−n²t} sin(nx)`, with `b_n` the Fourier sine coefficients
of `u(x,0)`. Standard result (Haberman, *Applied PDEs*, §2.3).

## Explain (altitudes)
- **expert** — the spatial operator `−d²/dx²` with the BCs is self-adjoint
  (Sturm–Liouville); its eigenfunctions are a complete orthogonal basis, so the
  product ansatz is exact and the series converges in `L²`.
- **working** — assume the solution is a product, divide through by it; a function
  of `x` equal to a function of `t` must be constant. Solve the two ODEs, pick the
  constant so the boundary conditions hold, and sum the allowed modes.
- **plain** — guess the answer is "a shape in space" times "a fade in time". The
  equation then breaks into two easy one-variable equations, and you add up the
  allowed shapes to match the start.

## LaTeX
rule: u(x,t)=X(x)T(t)\ \Rightarrow\ \frac{X''}{X}=\frac{T'}{T}=-\lambda
example: u(x,t)=\sum_{n=1}^{\infty}b_{n}\,e^{-n^{2}t}\sin(nx)

## References
- Haberman, *Applied Partial Differential Equations*, §2.3–2.4 (heat equation).
- Strauss, *Partial Differential Equations: An Introduction*, §4.1.
- Library: SymPy `pde_separate`; SciPy for the resulting eigenmodes.
- Worked example: Haberman §2.3 (heat on a finite interval).

## Links
[[heat-equation]] · [[fourier-series]] · [[sturm-liouville]] · [[wave-equation]]
