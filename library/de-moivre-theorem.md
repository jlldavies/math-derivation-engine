---
id: de-moivre-theorem
name: De Moivre's theorem
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You need `cos nθ` or `sin nθ` as a polynomial in `cosθ, sinθ` (multiple-angle
expansion), a power of a complex number in modulus–argument form, or the `n`-th
roots of a complex number. Tell: an integer power of `(cosθ + i sinθ)`, or a demand
to "expand `cos 3θ`".

## The rule
For integer `n`,
`(cosθ + i sinθ)ⁿ = cos nθ + i sin nθ`.
Equivalently `(e^{iθ})ⁿ = e^{inθ}` (see euler-formula). Expanding the left side by
the binomial theorem and equating real and imaginary parts gives `cos nθ` and
`sin nθ` as polynomials in `cosθ` and `sinθ`. For fractional `n = 1/m` it gives the
`m` distinct roots (one per added `2πk`).

## Worked example
Get `cos 3θ`. Take `n = 3`:
`(cosθ + i sinθ)³ = cos³θ + 3 cos²θ (i sinθ) + 3 cosθ (i sinθ)² + (i sinθ)³`
`= (cos³θ − 3 cosθ sin²θ) + i(3 cos²θ sinθ − sin³θ)`.
The real part is `cos 3θ = cos³θ − 3 cosθ sin²θ`. Replace `sin²θ = 1 − cos²θ`:
`cos 3θ = cos³θ − 3 cosθ(1 − cos²θ) = 4cos³θ − 3 cosθ`. ✓

## Explain (altitudes)
- **expert** — de Moivre is the statement that `θ ↦ e^{iθ}` is a group homomorphism
  `(ℝ,+) → (S¹,·)`; the multiple-angle polynomials are the Chebyshev polynomials,
  `cos nθ = Tₙ(cosθ)`, and the fractional case enumerates the cosets giving roots of
  unity / roots of any complex number.
- **working** — to expand `cos nθ`, raise `(cosθ + i sinθ)` to the `n`-th power with
  the binomial theorem and read off the real (cos) or imaginary (sin) part, then use
  `sin² = 1 − cos²` to tidy.
- **plain** — multiplying complex numbers **adds their angles**, so taking the
  `n`-th power multiplies the angle by `n`. That single fact turns "angle `nθ`" into
  algebra you can expand.

## LaTeX
rule: \left(\cos\theta+i\sin\theta\right)^{n}=\cos n\theta+i\sin n\theta
example: \cos 3\theta=\operatorname{Re}\left(\cos\theta+i\sin\theta\right)^{3}=\cos^{3}\theta-3\cos\theta\sin^{2}\theta=4\cos^{3}\theta-3\cos\theta

## References
- A-level Further Maths "De Moivre's theorem".
- Abramowitz & Stegun §4.3.20; any complex-analysis text.
- Library: SymPy `expand_trig`, `re`, `im`.

## Links
[[euler-formula]] · [[complex-trig-identities]] · [[roots-of-unity]]
