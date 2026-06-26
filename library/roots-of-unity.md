---
id: roots-of-unity
name: Roots of unity
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
Solving `zⁿ = 1` (or any `zⁿ = w`), summing equally-spaced points on the unit
circle, factoring `zⁿ − 1`, or anywhere a discrete cyclic symmetry of order `n`
appears (DFT, regular `n`-gon, periodic sums). Tell: an `n`-th power set equal to a
constant, or "the `n`-th roots of …".

## The rule
The `n` solutions of `zⁿ = 1` are
`z_k = e^{2πik/n} = cos(2πk/n) + i sin(2πk/n)`, `k = 0, 1, …, n−1`,
equally spaced on the unit circle. They are the powers `1, ω, ω², …, ωⁿ⁻¹` of the
primitive root `ω = e^{2πi/n}`, and (for `n ≥ 2`) they **sum to zero**:
`Σ_{k=0}^{n−1} z_k = 0`, since `zⁿ − 1 = (z − 1)(zⁿ⁻¹ + … + 1)` and the bracket's
roots are the non-trivial ones.

## Worked example
Cube roots of unity (`n = 3`). With `ω = e^{2πi/3}`:
`1`, `ω = cos120° + i sin120° = −½ + i√3/2`, `ω² = cos240° + i sin240° = −½ − i√3/2`.
Their sum: `1 + (−½ + i√3/2) + (−½ − i√3/2) = 1 − 1 = 0`, so `1 + ω + ω² = 0`. ✓
(Check: `ω³ = e^{2πi} = 1`, and `ω² = ω̄`.)

## Explain (altitudes)
- **expert** — the `n`-th roots of unity are the cyclic group `μₙ ≅ ℤ/nℤ` inside
  `ℂ*`; their vanishing sum is the value at `z = 1` of `(zⁿ−1)/(z−1) = Φ`-product, and
  they are the eigenvalues of the cyclic shift — the backbone of the DFT.
- **working** — write `1 = e^{2πik}` for every integer `k`, take the `n`-th root to
  get `e^{2πik/n}`, and keep `k = 0..n−1` (further `k` repeat). They sit at the
  vertices of a regular `n`-gon, so by symmetry their centroid — the sum over `n` — is
  the origin.
- **plain** — the solutions of `zⁿ = 1` are `n` equally spaced points around a circle
  of radius 1, starting at `1`. Because they are symmetric about the centre, the
  arrows to them cancel out and add to nothing.

## LaTeX
rule: z^{n}=1\;\Longrightarrow\; z_{k}=e^{2\pi i k/n},\quad k=0,1,\dots,n-1,\qquad \sum_{k=0}^{n-1}z_{k}=0
example: 1+\omega+\omega^{2}=1+\left(-\tfrac12+\tfrac{\sqrt3}{2}i\right)+\left(-\tfrac12-\tfrac{\sqrt3}{2}i\right)=0

## References
- A-level Further Maths "Roots of unity"; Gauss, *Disquisitiones* (cyclotomy).
- Abramowitz & Stegun §3.7; any algebra text on cyclic groups.
- Library: SymPy `solve(z**n - 1, z)`, `roots`.

## Links
[[de-moivre-theorem]] · [[euler-formula]]
