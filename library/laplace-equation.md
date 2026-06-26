---
id: laplace-equation
name: Laplace's equation — harmonic functions and the Poisson integral
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
An elliptic PDE `∇²u = 0` (steady-state, potential, equilibrium). Tells:
"harmonic", "potential", "steady state", "no sources", a Dirichlet problem
(boundary values prescribed); electrostatics, steady heat, ideal flow, the
mean-value property.

## The rule
Harmonic functions obey the **mean-value property**: `u` at a point equals its
average over any surrounding circle/sphere (hence the maximum principle). On the
unit disk, separation in polar coordinates gives
`u(r,θ) = a₀ + Σ_{n≥1} r^n (a_n cos nθ + b_n sin nθ)`, whose coefficients are the
Fourier coefficients of the boundary data — equivalently the Poisson integral
`u(r,θ) = (1/2π)∫_{−π}^{π} (1−r²)/(1−2r cos(θ−φ)+r²) g(φ) dφ`.

## Worked example
Dirichlet problem on the unit disk: `∇²u=0`, `u(1,θ)=g(θ)`. Expand
`g(θ) = a₀ + Σ(a_n cos nθ + b_n sin nθ)`; the bounded harmonic extension multiplies
the `n`-th mode by `r^n`, giving `u(r,θ) = a₀ + Σ r^n(a_n cos nθ + b_n sin nθ)`,
which resums to the Poisson kernel above. At `r=0` this returns `u(0)=a₀`, the mean
of `g` — the mean-value property. Standard result (Churchill & Brown, *Complex
Variables and Applications*, ch. 10).

## Explain (altitudes)
- **expert** — the disk Green's function yields the Poisson kernel as its normal
  derivative; harmonicity is the real part of analyticity, so the `r^n e^{inθ}`
  modes are exactly the boundary-bounded solutions and the maximum principle is
  automatic.
- **working** — separate `∇²` in polar coordinates: the angular part forces
  integer `n` and `cos nθ, sin nθ`; the radial part forces `r^n` (the `r^{−n}` piece
  blows up at 0). Match coefficients to the boundary Fourier series.
- **plain** — at steady state, each point's value is just the average of its
  neighbours. Expand the boundary into waves, shrink each wave's amplitude toward
  the centre by `r^n`, and the centre is the plain average of the edge.

## LaTeX
rule: \nabla^{2}u=0\ \Rightarrow\ u(r,\theta)=a_{0}+\sum_{n=1}^{\infty}r^{n}\!\left(a_{n}\cos n\theta+b_{n}\sin n\theta\right)
example: u(r,\theta)=\frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{1-r^{2}}{1-2r\cos(\theta-\varphi)+r^{2}}\,g(\varphi)\,d\varphi

## References
- Churchill & Brown, *Complex Variables and Applications*, ch. 10 (Poisson integral).
- Evans, *Partial Differential Equations*, §2.2 (Laplace's equation).
- Library: SymPy (polar separation + Fourier match); SciPy for numerics.
- Worked example: Churchill & Brown ch. 10 (Dirichlet problem on the disk).

## Links
[[greens-function]] · [[fourier-series]] · [[separation-of-variables]]
