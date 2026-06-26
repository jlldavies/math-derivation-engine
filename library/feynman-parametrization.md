---
id: feynman-parametrization
name: Feynman parametrization — combine denominators
domain: regularization
regime: regularization
status: verified
---

## Applies when (recognition signature)
A loop integrand is a **product of distinct propagator denominators**
`1/(A₁ A₂ ··· Aₙ)` (each `Aᵢ` a quadratic in the loop momentum). Tell: two or more
factors like `1/(k²−m²)` and `1/((k+p)²−m²)` multiplying each other, blocking a
direct momentum shift. You want them fused into one denominator so the `k`-integral
becomes a single spherically-symmetric quadratic.

## The rule
`1/(AB) = ∫_0^1 dx / [xA + (1−x)B]²`, and in general

`1/(A₁···Aₙ) = (n−1)! ∫_0^1 dⁿx · δ(1−Σxᵢ) / (x₁A₁+···+xₙAₙ)ⁿ`.

The `xᵢ` (Feynman parameters) live on the simplex `Σxᵢ=1`. After combining,
complete the square in the loop momentum to shift `k→ℓ` so the denominator is
`(ℓ²−Δ)ⁿ` with `Δ` depending only on the parameters and external invariants — then
the momentum integral is a standard `d`-dimensional master integral.

## Worked example
Combine `1/[(k²−m²)((k+p)²−m²)]`. With `A=(k+p)²−m²`, `B=k²−m²`:

`1/(AB)=∫_0^1 dx /[xA+(1−x)B]²`. The bracket is
`k²+2x k·p + x p² − m² = (k+xp)² − Δ`, with `Δ = m² − x(1−x)p²`.

Shifting `ℓ=k+xp` gives `1/(AB)=∫_0^1 dx/(ℓ²−Δ)²` — one quadratic denominator,
ready for the `∫d^dℓ` master formula.

## Explain (altitudes)
- **expert** — the identity is the Schwinger trick projected onto the simplex; the
  Jacobian `(n−1)!` and the `δ(1−Σxᵢ)` come from rescaling the Schwinger times to a
  total and an angle. The shift `ℓ=k+xp` is legitimate in dim-reg because the
  measure is translation-invariant, and `Δ(x)` carries all the kinematics.
- **working** — write the product of denominators as one integral over an auxiliary
  variable `x`, complete the square in `k`, and shift the loop variable so the
  denominator depends only on `ℓ²`. Now the angular symmetry is manifest.
- **plain** — multiplying two "distance" denominators is awkward; this rule rewrites
  the product as an average over a slider `x` of a single denominator, so you only
  ever integrate one clean quadratic.

## LaTeX
rule: \frac{1}{A_{1}\cdots A_{n}}=(n-1)!\int_{0}^{1}\!d^{n}x\,\frac{\delta\!\left(1-\sum_i x_i\right)}{\left(\sum_i x_i A_i\right)^{n}}
example: \frac{1}{AB}=\int_{0}^{1}\frac{dx}{\left[\,(k+xp)^{2}-\Delta\,\right]^{2}},\qquad \Delta=m^{2}-x(1-x)p^{2}
## References
- Feynman, Phys. Rev. 76 (1949) 769 (original parametrization).
- Peskin & Schroeder, *An Introduction to QFT*, §6.3 & §A.4.
- Weinberg, *The Quantum Theory of Fields*, Vol. I.

## Links
[[dimensional-regularization]] · [[schwinger-parametrization]] · [[gamma-function]]
