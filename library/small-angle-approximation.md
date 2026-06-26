---
id: small-angle-approximation
name: Small-angle approximation
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
An angle `θ` (in **radians**) is close to zero and you want a quick algebraic
stand-in for a trig function — limits like `sin θ/θ`, the period of a pendulum,
linearising a nonlinear oscillator, or the leading term of an error analysis.

## The rule
For small `θ` measured in **radians**:

`sin θ ≈ θ`,   `tan θ ≈ θ`,   `cos θ ≈ 1 − θ²/2`.

These are the truncated Maclaurin series: `sin θ = θ − θ³/6 + …`,
`cos θ = 1 − θ²/2 + θ⁴/24 − …`, `tan θ = θ + θ³/3 + …`. The error in `sin θ ≈ θ`
is `O(θ³)`; in `cos θ ≈ 1 − θ²/2` it is `O(θ⁴)`. (Radians are essential — in
degrees `sin θ ≈ θ·π/180`.)

## Worked example
**The standard limit.** Since `sin θ = θ − θ³/6 + …`,

`sin θ/θ = 1 − θ²/6 + … → 1`  as  `θ → 0`,  so  `lim_{θ→0} sin θ/θ = 1`.

**The cosine companion.** Using `cos θ ≈ 1 − θ²/2`,
`1 − cos θ ≈ θ²/2`, hence

`lim_{θ→0} (1 − cos θ)/θ² = ½`.

Numerical check at `θ = 0.01` rad: `sin θ/θ = 0.00999983/0.01 = 0.9999983` (≈ 1),
and `1 − cos θ = 0.00005000` ≈ `θ²/2 = 0.00005`. ✓

## Explain (altitudes)
- **expert** — these are the order-1 and order-2 jets of `sin`, `cos`, `tan` at
  `0`; the approximations are the truncated Taylor polynomials, with remainder
  controlled by Taylor's theorem (`|sin θ − θ| ≤ |θ|³/6`). Geometrically, near the
  identity the rotation group is approximated by its Lie algebra: arc ≈ chord to
  first order.
- **working** — on the unit circle the arc length is `θ`, the opposite side is
  `sin θ`, the tangent segment is `tan θ`; squeezing gives `cos θ ≤ sin θ/θ ≤ 1`,
  so the ratio → 1. Keeping one more term gives the quadratic `cos` correction.
- **plain** — for a tiny angle (in radians) the sine and the angle are almost
  equal because the arc and its straight chord nearly coincide; the cosine is just
  under 1 by `½θ²`. This is why `sin θ/θ` heads to exactly 1 as `θ` shrinks.

## LaTeX
rule: \sin\theta\approx\theta,\qquad \tan\theta\approx\theta,\qquad \cos\theta\approx 1-\frac{\theta^{2}}{2}\quad(\theta\to 0,\ \text{radians})
example: \lim_{\theta\to 0}\frac{\sin\theta}{\theta}=1,\qquad 1-\cos\theta\approx\frac{\theta^{2}}{2}

## References
- A-level / first-year calculus "Small-angle approximations" and the fundamental
  trigonometric limit.
- Truncations of the Maclaurin series for `sin`, `cos`, `tan`.

## Links
[[taylor-series]] · [[radians-arc-sector]] · [[trig-power-series]]
