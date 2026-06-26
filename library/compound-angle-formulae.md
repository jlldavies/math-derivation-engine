---
id: compound-angle-formulae
name: Compound-angle formulae (sin/cos of A±B)
domain: trigonometry
regime: elementary
status: drafted
---

## Applies when (recognition signature)
You meet `sin(A+B)`, `cos(A−B)`, or any trig function of a **sum or difference of
two angles**, and want to break it into functions of the single angles. Tell:
evaluating an awkward angle like `75°` as `45°+30°`, or expanding `sin(x+h)` to
differentiate `sin` from first principles.

## The rule
For any angles `A`, `B`:

`sin(A ± B) = sin A cos B ± cos A sin B`
`cos(A ± B) = cos A cos B ∓ sin A sin B`

(The `cos` formula flips sign: `+` inside gives `−` between the terms.)
The tangent form follows: `tan(A ± B) = (tan A ± tan B)/(1 ∓ tan A tan B)`.

## Worked example
`sin 75° = sin(45° + 30°) = sin45 cos30 + cos45 sin30
= (√2/2)(√3/2) + (√2/2)(1/2) = (√6 + √2)/4`.

## Explain (altitudes)
- **expert** — these are the real and imaginary parts of
  `e^{i(A+B)} = e^{iA}e^{iB}`; equivalently the matrix product of two planar
  rotations `R(A)R(B) = R(A+B)`, so the formulae just record how rotation angles
  add.
- **working** — multiply two unit complex numbers `e^{iA}` and `e^{iB}`: their
  angles add, and matching real and imaginary parts gives the `cos` and `sin`
  expansions directly.
- **plain** — there is no shortcut like `sin(A+B) = sinA + sinB` (that is false).
  Instead each of `sin` and `cos` of a combined angle is a specific mix of the
  separate sines and cosines. Memorise the two lines and you can find exact values
  for angles like `75°` by splitting them into `45°` and `30°`.

## LaTeX
rule: \sin\!\left(A\pm B\right)=\sin A\cos B\pm\cos A\sin B,\qquad \cos\!\left(A\pm B\right)=\cos A\cos B\mp\sin A\sin B
example: \sin 75^{\circ}=\sin\!\left(45^{\circ}+30^{\circ}\right)=\frac{\sqrt{6}+\sqrt{2}}{4}

## References
- A-level Pure "Addition formulae"; standard in any trigonometry/pre-calculus text.
- Library: SymPy `expand_trig` produces these expansions.

## Links
[[double-angle-formulae]] · [[pythagorean-identity]]
