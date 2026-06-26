---
id: trig-graph-transformations
name: Trig graph transformations (amplitude, period, phase, shift)
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You meet a sinusoid in the form `y = A sin(Bx + C) + D` (or with `cos`) and must
read off — or impose — its **amplitude, period, phase and vertical shift**: graph
sketching, fitting a wave to data, or describing how a base curve `y = sin x` is
stretched and translated.

## The rule
For `y = A sin(Bx + C) + D` (with `B > 0`):

- **amplitude** `= |A|` (vertical half-height; `A < 0` also reflects in the midline);
- **period** `= 2π/B` (horizontal stretch by `1/B`);
- **phase shift** `= −C/B` (horizontal translation; `> 0` = right, `< 0` = left);
- **vertical shift** `= D` (the midline `y = D`).

So the graph oscillates between `D − |A|` and `D + |A|`, completing one cycle every
`2π/B`, displaced `−C/B` horizontally.

## Worked example
`y = 3 sin(2x − π/3) + 1`. Read off `A = 3`, `B = 2`, `C = −π/3`, `D = 1`:

- amplitude `= |3| = 3`;
- period `= 2π/2 = π`;
- phase shift `= −C/B = −(−π/3)/2 = π/6` (i.e. `π/6` to the **right**);
- vertical shift `= 1`, so the midline is `y = 1` and the curve runs from
  `1 − 3 = −2` up to `1 + 3 = 4`.

Check: factor the argument as `2(x − π/6)`, confirming the rightward shift of `π/6`
and period `π`. At `x = π/6`: `y = 3 sin 0 + 1 = 1` (on the midline, rising). ✓

## Explain (altitudes)
- **expert** — `A sin(Bx + C) + D` is the orbit of the base function under the
  affine group acting on the `(x, y)` plane: `B` and `A` are the horizontal and
  vertical scalings, `−C/B` and `D` the translations. `B` is the angular frequency
  `ω`; `C` the initial phase; `(A, D)` set the range `[D−|A|, D+|A|]`.
- **working** — build the curve from `y = sin x` by four steps in order:
  horizontal stretch by `1/B` (period `2π/B`), shift left by `C/B`, vertical
  stretch by `A`, raise by `D`. Factor `Bx + C = B(x + C/B)` to see the shift
  cleanly.
- **plain** — `A` controls how **tall** the wave is, `B` how **squashed** (more
  wiggles), `−C/B` slides it **left/right**, and `D` lifts it **up/down**. Read
  those four numbers and you can sketch or describe any sine/cosine wave.

## LaTeX
rule: y=A\sin\!\left(Bx+C\right)+D:\quad \text{amp}=|A|,\ \ \text{period}=\frac{2\pi}{B},\ \ \text{phase}=-\frac{C}{B},\ \ \text{shift}=D
example: y=3\sin\!\left(2x-\frac{\pi}{3}\right)+1:\quad |A|=3,\ \ \frac{2\pi}{2}=\pi,\ \ -\frac{-\pi/3}{2}=\frac{\pi}{6},\ \ D=1

## References
- A-level / pre-calculus "Transformations of trigonometric graphs".
- Standard sinusoid parametrisation in signals and oscillation theory.

## Links
[[harmonic-form]] · [[radians-arc-sector]]
