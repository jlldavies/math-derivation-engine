---
id: wave-equation
name: Wave equation — d'Alembert's travelling-wave solution
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
A hyperbolic PDE `u_tt = c² u_xx` (vibrations, acoustics, EM in 1-D). Tells:
"wave", "vibrating string", second time-derivative against second space-
derivative, signal speed `c`; an initial-value (Cauchy) problem with displacement
`f` and velocity `g`.

## The rule
The operator factors as `(∂_t − c∂_x)(∂_t + c∂_x)`, so the general solution is a
sum of a right- and a left-mover: `u = F(x−ct) + G(x+ct)`. With initial data
`u(x,0)=f(x)`, `u_t(x,0)=g(x)`, d'Alembert's formula is
`u(x,t) = ½[f(x−ct)+f(x+ct)] + (1/2c)∫_{x−ct}^{x+ct} g(s) ds`.

## Worked example
For `u_tt = c² u_xx` on the line with `u(x,0)=f(x)`, `u_t(x,0)=g(x)`, d'Alembert's
formula gives `u(x,t) = ½[f(x−ct)+f(x+ct)] + (1/2c)∫_{x−ct}^{x+ct} g(s) ds`. Check:
at `t=0` the integral vanishes so `u=f`; `∂_t u|_{t=0} = ½[−cf'+cf'] + ½[g+g] = g`.
The solution at `(x,t)` depends only on data in `[x−ct, x+ct]` (domain of
dependence). Standard result (Strauss, *PDEs*, §2.1).

## Explain (altitudes)
- **expert** — the characteristics `x ∓ ct = const` diagonalize the operator; the
  travelling-wave decomposition is exact, and the velocity term is the
  antiderivative supplied by integrating along the two characteristics from the
  data line.
- **working** — any solution splits into a shape moving right plus a shape moving
  left, both at speed `c`. Match the two unknown shapes to the initial position and
  speed, and the velocity contributes the integral term.
- **plain** — a pluck on a string sends half the bump left and half right at fixed
  speed; if the string also starts moving, that adds up over the stretch the two
  signals have swept across.

## LaTeX
rule: u_{tt}=c^{2}u_{xx}\ \Rightarrow\ u(x,t)=\tfrac12\!\left[f(x-ct)+f(x+ct)\right]+\frac{1}{2c}\int_{x-ct}^{x+ct}\!g(s)\,ds
example: u(x,0)=f(x),\ u_t(x,0)=g(x)\ \Rightarrow\ u(x,t)=\tfrac12\!\left[f(x-ct)+f(x+ct)\right]+\frac{1}{2c}\int_{x-ct}^{x+ct}\!g(s)\,ds

## References
- Strauss, *Partial Differential Equations: An Introduction*, §2.1 (d'Alembert).
- Evans, *Partial Differential Equations*, §2.4.
- Library: SymPy `pdsolve`/`dsolve` along characteristics; SciPy for numerics.
- Worked example: Strauss §2.1 (the d'Alembert formula).

## Links
[[method-of-characteristics]] · [[separation-of-variables]] · [[fourier-series]]
