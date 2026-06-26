---
id: sine-rule
name: Sine rule (law of sines)
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
A **non-right** triangle where you know an angle and its **opposite side**, plus
one more angle or side. Tells: "solve the triangle", AAS/ASA (two angles + a side),
or SSA (two sides + a non-included angle, the ambiguous case). Keyword: a
side paired with the angle *facing* it.

## The rule
In any triangle with sides `a, b, c` opposite angles `A, B, C`:

`a/sinA = b/sinB = c/sinC = 2R`,

where `R` is the circumradius. Pick the ratio you know fully and use it to unlock
the others. (For finding an unknown **angle**, flip it: `sinA/a = sinB/b = …`.)

## Worked example
Solve the triangle with `A = 30°`, `B = 45°`, `a = 10`.
Angles sum to 180°, so `C = 180° − 30° − 45° = 105°`.
Then `b = a·sinB/sinA = 10·sin45°/sin30° = 10·(√2/2)/(1/2) = 10√2 ≈ 14.14`, and
`c = a·sinC/sinA = 10·sin105°/sin30° = 20·sin105° ≈ 19.32`.

## Explain (altitudes)
- **expert** — each ratio equals `2R` because the inscribed-angle theorem gives a
  chord of length `2R·sinθ` for the angle `θ` it subtends at the circumference;
  the common value is an invariant of the triangle's circumcircle.
- **working** — drop the altitude `h` from one vertex: it equals `b·sinC` and also
  `c·sinB`, so `b/sinB = c/sinC`. Repeat from another vertex to chain in the third
  ratio. The shared altitude is what links the pairs.
- **plain** — in a triangle, the bigger a side, the bigger the angle opposite it,
  and the rule says side-over-(sine-of-its-opposite-angle) is the *same* for all
  three. Know one such pair and you can find any missing side or angle.

## LaTeX
rule: \frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R
example: b=\frac{a\,\sin B}{\sin A}=\frac{10\,\sin 45^{\circ}}{\sin 30^{\circ}}=10\sqrt{2}\approx 14.14

## References
- A-level Pure (Edexcel/AQA/OCR) "Triangles — sine and cosine rules"; any
  trigonometry/pre-calculus text (Stewart; CGP A-level).
- Library: SymPy `solve` on `sin`-ratio equations; `sympy.geometry` triangle objects.

## Links
[[cosine-rule]] · [[compound-angle-formulae]] · [[law-of-tangents]]
