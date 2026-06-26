---
id: method-of-characteristics
name: Method of characteristics — ride the curves a first-order PDE is constant on
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
A first-order PDE, `a u_x + b u_t = c` (linear or quasilinear), with data given on
a curve. Tells: transport/advection `u_t + c u_x = 0`, traffic-flow / conservation
laws, "propagation", "signal speed"; the solution is constant (or evolves by an
ODE) along moving curves.

## The rule
Along curves defined by `dx/a = dt/b = du/c` (the characteristic ODEs), the PDE
reduces to an ODE for `u`. For `a u_x + b u_t = 0`, `u` is constant along
characteristics `dx/dt = a/b`, so `u` is an arbitrary function of the
characteristic invariant. Trace each curve back to the data curve to read off the
value.

## Worked example
Transport `u_t + c u_x = 0` with `u(x,0)=f(x)`. Characteristics solve
`dx/dt = c`, i.e. `x − ct = const`, and `du/dt = 0` along them, so `u` is constant
on each. Hence `u(x,t) = f(x − ct)` — the initial profile rigidly translates at
speed `c`. Standard result (Strauss, *PDEs*, §1.2).

## Explain (altitudes)
- **expert** — the PDE says `∇u · (a,b) = c`; the integral curves of the vector
  field `(a,b)` foliate the domain, reducing the PDE to ODEs along the leaves and
  exposing where characteristics cross (shock formation, in the quasilinear case).
- **working** — set `dx/a = dt/b = du/c`, integrate the first pair to get the
  curves the solution lives on, integrate `du` along them, and apply the data.
- **plain** — the equation describes something drifting. Follow along with the
  drift and the value barely changes, so the starting picture just slides over —
  `f(x−ct)` is the picture shifted by how far it has travelled.

## LaTeX
rule: a\,u_x+b\,u_t=c\ \Rightarrow\ \frac{dx}{a}=\frac{dt}{b}=\frac{du}{c}
example: u_t+c\,u_x=0,\ u(x,0)=f(x)\ \Rightarrow\ u(x,t)=f\!\left(x-ct\right)

## References
- Strauss, *Partial Differential Equations: An Introduction*, §1.2.
- Evans, *Partial Differential Equations*, §3.2.
- Library: SymPy `pdsolve` (linear first-order); method-of-lines in SciPy.
- Worked example: Strauss §1.2 (the transport equation).

## Links
[[wave-equation]] · [[heat-equation]]
