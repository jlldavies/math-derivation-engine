---
id: sum-to-product
name: Sum-to-product formulae
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You have a **sum or difference of two trig functions** — `sin P ± sin Q`,
`cos P ± cos Q` — and want a product. Tell: factorising to find common zeros,
simplifying `sin P + sin Q` before cancelling, or recognising beats (two close
frequencies multiplying a slow envelope).

## The rule
Setting `A = (P+Q)/2`, `B = (P−Q)/2` in the product-to-sum identities and
inverting:

`sin P + sin Q = 2 sin((P+Q)/2) cos((P−Q)/2)`
`sin P − sin Q = 2 cos((P+Q)/2) sin((P−Q)/2)`
`cos P + cos Q = 2 cos((P+Q)/2) cos((P−Q)/2)`
`cos P − cos Q = −2 sin((P+Q)/2) sin((P−Q)/2)`

## Worked example
Simplify `sin 5x + sin 3x`. Take `P = 5x`, `Q = 3x`, so `(P+Q)/2 = 4x`,
`(P−Q)/2 = x`:

`sin 5x + sin 3x = 2 sin 4x cos x`.

Check at `x = π/4`: LHS `= sin(5π/4) + sin(3π/4) = −0.70711 + 0.70711 = 0`; RHS
`= 2 sin π cos(π/4) = 2(0)(0.70711) = 0`. ✓ The product form exposes the zeros
(`sin 4x = 0` or `cos x = 0`) at a glance.

## Explain (altitudes)
- **expert** — these are the product-to-sum relations read right-to-left, i.e. the
  inverse linear change `(A,B) ↔ (P,Q)` with `P = A+B`, `Q = A−B`. In exponential
  form, `e^{iP} + e^{iQ} = e^{i(P+Q)/2}(e^{i(P−Q)/2} + e^{−i(P−Q)/2})`, and the
  bracket is `2 cos((P−Q)/2)` — the factorisation made visible.
- **working** — substitute `P = A+B` and `Q = A−B` into
  `sin(A+B) + sin(A−B) = 2 sin A cos B`; then `A = (P+Q)/2`, `B = (P−Q)/2` give the
  stated form. The other three come from the matching product-to-sum lines.
- **plain** — adding two waves equals **one** wave at the average frequency
  multiplied by a slowly varying factor at the half-difference frequency. That is
  why two slightly different tones produce "beats", and why the sum factorises
  neatly.

## LaTeX
rule: \sin P+\sin Q=2\sin\!\left(\frac{P+Q}{2}\right)\cos\!\left(\frac{P-Q}{2}\right),\qquad \cos P+\cos Q=2\cos\!\left(\frac{P+Q}{2}\right)\cos\!\left(\frac{P-Q}{2}\right)
example: \sin 5x+\sin 3x=2\sin\!\left(\frac{5x+3x}{2}\right)\cos\!\left(\frac{5x-3x}{2}\right)=2\sin 4x\cos x

## References
- A-level / pre-calculus "Sum-to-product identities"; standard trigonometric tables.
- Underlies the beat phenomenon in acoustics and amplitude modulation.

## Links
[[product-to-sum]] · [[compound-angle-formulae]]
