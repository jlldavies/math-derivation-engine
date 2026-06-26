---
id: heat-equation
name: Heat equation — diffusion and the Gaussian heat kernel
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
A parabolic PDE `u_t = D u_xx` (diffusion/heat). Tells: "diffusion", "heat
conduction", "smoothing", a first time-derivative against a second space-
derivative; spreading of an initial concentration, the fundamental solution on the
whole line, `e^{−x²/4Dt}` shapes.

## The rule
On the whole line the fundamental solution (heat kernel) is a spreading Gaussian:
`u(x,t) = (1/√(4πDt)) e^{−x²/4Dt}`, solving `u_t = D u_xx` with `u(·,0)=δ`. Its
total mass is conserved, `∫_{−∞}^{∞} u dx = 1` for all `t>0`, and the general
solution is the convolution of this kernel with the initial data.

## Worked example
The kernel `Φ(x,t) = (4πDt)^{−1/2} e^{−x²/4Dt}` satisfies `Φ_t = D Φ_xx`, and by
the Gaussian integral `∫_{−∞}^{∞} (4πDt)^{−1/2} e^{−x²/4Dt} dx = 1` (substitute
`y = x/√(4Dt)`, leaving `(1/√π)∫ e^{−y²}dy = 1`). So heat diffuses while total
heat is conserved. Standard result (Evans, *PDEs*, §2.3).

## Explain (altitudes)
- **expert** — `Φ` is the Green's function of the heat operator `∂_t − D∂_x²`; it
  is the transition density of Brownian motion with variance `2Dt`, and unit mass
  is the conservation law `d/dt ∫u = D[u_x] = 0`.
- **working** — a point of heat spreads into a Gaussian whose width grows like
  `√t`; checking it solves the PDE is two derivatives, and its area is the standard
  Gaussian integral, which stays 1 as it spreads.
- **plain** — drop a spot of heat and it blurs out into a bell shape that gets
  wider and flatter over time, but the total amount of heat never changes.

## LaTeX
rule: u_t=D\,u_{xx}\ \Rightarrow\ u(x,t)=\frac{1}{\sqrt{4\pi D t}}\,e^{-x^{2}/4Dt}
example: \int_{-\infty}^{\infty}\frac{1}{\sqrt{4\pi D t}}\,e^{-x^{2}/4Dt}\,dx=1

## References
- Evans, *Partial Differential Equations*, §2.3 (heat equation, fundamental sol.).
- Crank, *The Mathematics of Diffusion*, ch. 2.
- Library: SymPy verifies the kernel; SciPy `scipy.ndimage.gaussian_filter` (numeric diffusion).
- Worked example: Evans §2.3 (the heat kernel and its unit mass).

## Links
[[separation-of-variables]] · [[gaussian-integral]] · [[fourier-transform]]
