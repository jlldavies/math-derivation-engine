---
id: inverse-trig-functions
name: Inverse trig functions (arcsin, arccos, arctan)
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You need the **angle** from a trig value (`sinx = k` → `x = arcsin k`), an **exact**
value like `arcsin(1/2)`, or a **derivative** of `arcsin`/`arccos`/`arctan`. Tells:
`sin⁻¹`/`cos⁻¹`/`tan⁻¹`, a `1/√(1−x²)` or `1/(1+x²)` integrand (the giveaway of an
inverse-trig antiderivative), or "principal value".

## The rule
The inverse functions invert the trig functions on **restricted** ranges so they
are single-valued:

`arcsinx ∈ [−π/2, π/2]`,  `arccosx ∈ [0, π]`,  `arctanx ∈ (−π/2, π/2)`.

Their derivatives are

`d/dx arcsinx = 1/√(1−x²)`,  `d/dx arccosx = −1/√(1−x²)`,
`d/dx arctanx = 1/(1+x²)`.

## Worked example
Evaluate `arcsin(1/2)`. We need the angle `θ ∈ [−π/2, π/2]` with `sinθ = 1/2`;
that is `θ = π/6`, since `sin(π/6) = 1/2` and `π/6` lies in the principal range.
So `arcsin(1/2) = π/6`.
(Check on the derivative: `d/dx arctanx = 1/(1+x²)`, so at `x = 1` the slope is `1/2`.)

## Explain (altitudes)
- **expert** — restricting the domain picks a single branch on which the trig
  function is a bijection, giving a smooth inverse. The derivatives follow from the
  inverse-function theorem: e.g. `(arctan)'(x) = 1/(1 + tan²(arctan x)) = 1/(1+x²)`.
  These are the antiderivatives behind `trig-substitution`.
- **working** — sine repeats, so to invert it you keep just the rising branch on
  `[−π/2, π/2]`. Differentiate `sin(arcsinx) = x` implicitly:
  `cos(arcsinx)·(arcsinx)' = 1`, and `cos = √(1−sin²) = √(1−x²)`, giving
  `1/√(1−x²)`.
- **plain** — `arcsin` answers "which angle has this sine?" There are infinitely
  many, so we agree to take the one between `−90°` and `90°`. For `sin = 1/2` that
  angle is `30° = π/6`.

## LaTeX
rule: \frac{d}{dx}\arcsin x=\frac{1}{\sqrt{1-x^{2}}},\qquad \frac{d}{dx}\arctan x=\frac{1}{1+x^{2}}
example: \arcsin\!\left(\tfrac{1}{2}\right)=\frac{\pi}{6}\quad\text{since}\quad \sin\frac{\pi}{6}=\frac{1}{2},\ \frac{\pi}{6}\in\left[-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]

## References
- A-level Pure (Edexcel/AQA/OCR) "Inverse trig functions and their derivatives";
  any calculus text (Stewart; Spivak).
- Library: SymPy `asin`, `acos`, `atan`; `diff` reproduces the derivatives.

## Links
[[trig-substitution]] · [[solving-trig-equations]] · [[chain-rule]]
