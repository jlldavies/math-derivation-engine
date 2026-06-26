---
id: half-angle-formulae
name: Half-angle formulae
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You need a trig function of **half an angle** in terms of the whole angle — exact
values like `sin 15°` (= half of `30°`), or you are setting up the
**Weierstrass `t = tan(θ/2)` substitution** for an integral, where `sin θ`,
`cos θ` must be rewritten through `tan(θ/2)`.

## The rule
From `cos θ = 1 − 2 sin²(θ/2) = 2 cos²(θ/2) − 1` (the double-angle formula run
backwards):

`sin(θ/2) = ±√((1 − cos θ)/2)`,   `cos(θ/2) = ±√((1 + cos θ)/2)`.

The tangent half-angle has sign-free forms:

`tan(θ/2) = (1 − cos θ)/sin θ = sin θ/(1 + cos θ)`.

The `±` on `sin`/`cos` is resolved by the quadrant of `θ/2`; the `tan` forms need
no `±` because numerator and denominator carry the sign automatically.

## Worked example
Exact `sin 15°`, taking `θ = 30°` so `θ/2 = 15°` (first quadrant, positive root):

`sin 15° = √((1 − cos 30°)/2) = √((1 − √3/2)/2) = √((2 − √3)/4) = ½√(2 − √3)`.

Numerically `½√(2 − 1.7320508) = ½√0.2679492 = ½(0.5176381) = 0.258819`, which
matches `sin 15° = 0.258819`. ✓ (The equivalent surd form is `(√6 − √2)/4`.)

## Explain (altitudes)
- **expert** — these are the double-angle identities solved for the half-angle;
  the `tan(θ/2)` form is the coordinate `t` that rationalises the circle, sending
  `(cos θ, sin θ) = ((1−t²)/(1+t²), 2t/(1+t²))` — a stereographic projection,
  hence its central role in the Weierstrass substitution.
- **working** — start from `cos θ = 1 − 2 sin²(θ/2)`; rearrange to
  `sin²(θ/2) = (1 − cos θ)/2` and take the root. For `tan(θ/2)`, multiply
  `sin θ/(1 + cos θ)` top and bottom by the conjugate, or use
  `sin θ = 2 sin(θ/2)cos(θ/2)` and `1 + cos θ = 2 cos²(θ/2)`.
- **plain** — if you know the cosine of an angle, you can get the sine and cosine
  of **half** that angle by a square-root formula. This is how exact values like
  `sin 15°` are found without a calculator.

## LaTeX
rule: \sin\frac{\theta}{2}=\pm\sqrt{\frac{1-\cos\theta}{2}},\quad \cos\frac{\theta}{2}=\pm\sqrt{\frac{1+\cos\theta}{2}},\quad \tan\frac{\theta}{2}=\frac{1-\cos\theta}{\sin\theta}
example: \sin 15^{\circ}=\sqrt{\frac{1-\cos 30^{\circ}}{2}}=\frac{1}{2}\sqrt{2-\sqrt{3}}=\frac{\sqrt{6}-\sqrt{2}}{4}

## References
- A-level / pre-calculus "Half-angle formulae"; standard trigonometric identities.
- The `tan(θ/2)` form underlies the Weierstrass (tangent half-angle) substitution.

## Links
[[double-angle-formulae]] · [[weierstrass-substitution]] · [[compound-angle-formulae]]
