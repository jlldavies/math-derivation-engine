---
id: law-of-tangents
name: Law of tangents
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
A triangle given by two sides and the included angle (SAS), where you want the other
two angles without first finding the third side. Tells: "solve the triangle", two sides
plus the angle between them, a numerically stable alternative to the cosine rule that
avoids small-angle loss, classical pre-calculator triangle solving (logarithms).

## The rule
In any triangle with sides `a, b, c` opposite angles `A, B, C`,
`(a − b)/(a + b) = tan[(A − B)/2] / tan[(A + B)/2]`,
and cyclically for the other side/angle pairs. It follows directly from the sine rule
`a/sin A = b/sin B` together with the sum-to-product identities for
`sin A ± sin B`. In an SAS problem the included angle gives `A + B = 180° − C`
immediately (so `(A+B)/2` is known), and the law of tangents then delivers
`(A − B)/2` from the two known sides — fixing `A` and `B` separately.

## Worked example
Solve the triangle with `a = 7`, `b = 3`, included angle `C = 40°` (so side `c` is
opposite the known angle). First `A + B = 180° − 40° = 140°`, hence `(A+B)/2 = 70°`.
The law of tangents gives
`tan[(A−B)/2] = [(a−b)/(a+b)] tan[(A+B)/2] = (4/10) tan 70° = 0.4 × 2.7475 = 1.0990`,
so `(A−B)/2 = arctan(1.0990) ≈ 47.70°`. Then
`A = 70° + 47.70° = 117.70°`, `B = 70° − 47.70° = 22.30°`. (Check with the cosine
rule: `c = √(49 + 9 − 2·7·3·cos40°) ≈ 5.20`, and `sin A / a = sin117.70°/7 ≈ 0.1265
= sin40°/5.20` — consistent.) Standard SAS solution (Hobson, *Plane Trigonometry*, §80).

## Explain (altitudes)
- **expert** — the identity is the projective/Napier-style symmetrisation of the sine
  rule: writing `a ∝ sin A`, `b ∝ sin B`, the ratio `(a−b)/(a+b)` becomes
  `(sin A − sin B)/(sin A + sin B)`, which sum-to-product factors into the tangent
  quotient — a form chosen historically because it is additive under logarithms.
- **working** — from `a/sin A = b/sin B`, replace `a, b` by `sin A, sin B`, apply
  `sin A − sin B = 2 cos[(A+B)/2] sin[(A−B)/2]` and `sin A + sin B =
  2 sin[(A+B)/2] cos[(A−B)/2]`; the common factors cancel into `tan[(A−B)/2]/tan[(A+B)/2]`.
- **plain** — if you know two sides and the angle between them, you already know what
  the other two angles add up to. This rule converts the difference of the sides into
  the difference of those angles, so you can split the total and get each angle.

## LaTeX
rule: \frac{a-b}{a+b}=\frac{\tan\!\left(\frac{A-B}{2}\right)}{\tan\!\left(\frac{A+B}{2}\right)}
example: \tan\!\left(\frac{A-B}{2}\right)=\frac{a-b}{a+b}\tan\!\left(\frac{A+B}{2}\right)=0.4\,\tan 70^{\circ}\ \Rightarrow\ A\approx117.7^{\circ},\ B\approx22.3^{\circ}

## References
- Hobson, *A Treatise on Plane Trigonometry*, §80 (law of tangents, SAS solution).
- Abramowitz & Stegun, *Handbook of Mathematical Functions*, §4.3.149.
- Library: SymPy/`math` for the arithmetic; verify against `numpy` cosine-rule solution.
- Worked example: Hobson §80 (two sides and the included angle).

## Links
[[sine-rule]] · [[cosine-rule]] · [[half-angle-formulae]] · [[sum-to-product]] · [[spherical-trigonometry]]
