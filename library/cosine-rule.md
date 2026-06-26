---
id: cosine-rule
name: Cosine rule (law of cosines)
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
A **non-right** triangle where the sine rule stalls: you know **two sides and the
included angle** (SAS → find the third side), or **all three sides** (SSS → find an
angle). Tell: no complete side/opposite-angle pair to start the sine rule. It is
Pythagoras with a correction term for the non-right angle.

## The rule
In any triangle with sides `a, b, c` opposite angles `A, B, C`:

`c² = a² + b² − 2ab·cosC`,

with the cyclic variants for `a²` and `b²`. Rearranged for an angle:
`cosC = (a² + b² − c²)/(2ab)`. When `C = 90°`, `cosC = 0` and it reduces to
`c² = a² + b²` (Pythagoras).

## Worked example
Find the third side with `a = 5`, `b = 7`, included angle `C = 60°`.
`c² = 5² + 7² − 2·5·7·cos60° = 25 + 49 − 70·(1/2) = 74 − 35 = 39`,
so `c = √39 ≈ 6.245`.

## Explain (altitudes)
- **expert** — it is the law of cosines as the polarization identity
  `|a − b|² = |a|² + |b|² − 2⟨a,b⟩`: writing the third side as the vector
  difference of the other two, the inner product `⟨a,b⟩ = ab·cosC` is exactly the
  cross term. Pythagoras is the orthogonal (`cosC = 0`) special case.
- **working** — place `C` at the origin; the side `c` is the vector difference of
  the sides `a` and `b`. Expand `|a − b|²` and the dot product `a·b = ab·cosC`
  supplies the `−2ab·cosC` correction to `a² + b²`.
- **plain** — Pythagoras only works for right angles. If the corner isn't 90°, you
  add a fix-up term `−2ab·cosC`: when the corner is sharp (`cosC > 0`) the opposite
  side is shorter; when it's blunt (`cosC < 0`) it's longer.

## LaTeX
rule: c^{2}=a^{2}+b^{2}-2ab\cos C\qquad\Longrightarrow\qquad \cos C=\frac{a^{2}+b^{2}-c^{2}}{2ab}
example: c^{2}=5^{2}+7^{2}-2\cdot 5\cdot 7\cos 60^{\circ}=39,\qquad c=\sqrt{39}\approx 6.245

## References
- A-level Pure (Edexcel/AQA/OCR) "Triangles — sine and cosine rules"; standard in
  any trigonometry text (Stewart; CGP A-level).
- Library: SymPy `solve`/`acos`; verify against `sympy.geometry` triangles.

## Links
[[sine-rule]] · [[pythagorean-identity]] · [[dot-product]]
