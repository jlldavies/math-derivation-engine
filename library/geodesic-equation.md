---
id: geodesic-equation
name: Geodesic equation — straightest / extremal path
domain: tensor
regime: tensor
status: drafted
---

## Applies when (recognition signature)
You want the path a free particle / light ray follows, or the "straight lines" of a
curved space, given a metric and its connection. Tells: "geodesic", "equation of
motion", "free-fall path", "extremal proper time", "great circle", "straightest
path", "shortest path on a surface".

## The rule
`d²x^a/dτ² + Γ^a_bc (dx^b/dτ)(dx^c/dτ) = 0`, where `τ` is an affine parameter
(proper time for a timelike path). It is the Euler–Lagrange equation for extremal
arc length / proper time, and equivalently `u^b ∇_b u^a = 0` — the tangent vector
is parallel-transported along itself. The `Γ` term is the only correction to
`d²x^a/dτ² = 0`; where the connection vanishes the path is a straight coordinate
line.

## Worked example
**Flat space**, Cartesian coordinates: all `Γ^a_bc = 0`, so `d²x^a/dτ² = 0` gives
`x^a(τ) = p^a + τ q^a` — ordinary straight lines. **Unit 2-sphere**,
`ds² = dθ² + sin²θ dφ²`: the geodesic equations
`θ̈ − sinθ cosθ φ̇² = 0`, `φ̈ + 2cotθ θ̇ φ̇ = 0` are solved by **great circles**
(e.g. `θ = π/2`, `φ = ωτ` is the equator).

## Explain (altitudes)
- **expert** — autoparallels of the Levi-Civita connection, `u^b∇_b u^a = 0`; the
  Euler–Lagrange equations of `∫√(g_{ab}ẋ^aẋ^b)` with affine parametrization
  removing the reparametrization freedom.
- **working** — plug the metric's Christoffels into the equation, get one ODE per
  coordinate, and solve; with `Γ = 0` they collapse to constant-velocity lines.
- **plain** — a geodesic is the straightest possible path you can walk without
  turning the wheel: a straight line on a flat floor, a great circle on a globe —
  it is also the shortest route between two points.

## LaTeX
rule: \frac{d^2x^{a}}{d\tau^2}+\Gamma^{a}{}_{bc}\,\frac{dx^{b}}{d\tau}\frac{dx^{c}}{d\tau}=0
example: \text{flat: }x^{a}(\tau)=p^{a}+\tau\,q^{a};\qquad S^2:\ \theta=\tfrac{\pi}{2},\ \phi=\omega\tau\ (\text{great circle})

## References
- Hartle, *Gravity: An Introduction to Einstein's General Relativity*, §8.
- D'Inverno, *Introducing Einstein's Relativity*, §7. Wald, *General Relativity*, §3.3.

## Links
[[christoffel-symbols]] · [[covariant-derivative]] · [[metric-transformation-law]]
