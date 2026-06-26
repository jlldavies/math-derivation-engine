---
id: radians-arc-sector
name: Radians — arc length and sector area
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
A circle problem mentioning **arc length**, **sector area**, or a **central angle
in radians** (`θ` written as a multiple of `π`, not degrees). Tells: "minor sector",
"length of arc", "area swept", or a fraction-of-the-circle question. The angle
**must** be in radians for these formulae to hold.

## The rule
For a circle of radius `r` and central angle `θ` **measured in radians**:

arc length `s = rθ`,  sector area `A = ½r²θ`.

These are the whole-circle results `2πr` and `πr²` scaled by the fraction `θ/2π` of
a full turn. (In degrees they carry an extra `π/180` factor, which is why radians
are the natural unit.)

## Worked example
Take `r = 6` and `θ = π/3`.
Arc length `s = rθ = 6·(π/3) = 2π ≈ 6.283`.
Sector area `A = ½r²θ = ½·6²·(π/3) = 18·(π/3) = 6π ≈ 18.850`.

## Explain (altitudes)
- **expert** — a radian is defined so that arc length equals `r·θ`; with that
  definition the sector area is the integral `∫₀^θ ½r² dφ = ½r²θ`, the area swept
  by the radius. Radian measure makes `d/dθ sinθ = cosθ` hold without stray
  constants, which is the deeper reason it is the canonical angular unit.
- **working** — a full turn is `2π` radians with arc `2πr` and area `πr²`. A sector
  is the fraction `θ/2π` of the circle, so its arc is `(θ/2π)·2πr = rθ` and its area
  is `(θ/2π)·πr² = ½r²θ`.
- **plain** — one radian is the angle that wraps an arc as long as the radius. So an
  angle of `θ` radians gives an arc `θ` radii long, i.e. `s = rθ`; the wedge of pie
  has area `½r²θ`.

## LaTeX
rule: s=r\theta,\qquad A=\frac{1}{2}r^{2}\theta\quad(\theta\text{ in radians})
example: s=6\cdot\frac{\pi}{3}=2\pi,\qquad A=\frac{1}{2}\cdot 6^{2}\cdot\frac{\pi}{3}=6\pi

## References
- A-level Pure (Edexcel/AQA/OCR) "Radian measure — arcs and sectors"; any
  trigonometry/pre-calculus text (Stewart; CGP A-level).
- Library: SymPy with `pi` and exact rationals; `mpmath` for numeric checks.

## Links
[[trig-graph-transformations]] · [[small-angle-approximation]] · [[solving-trig-equations]]
