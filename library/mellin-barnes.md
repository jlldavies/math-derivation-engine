---
id: mellin-barnes
name: Mellin transform & Barnes contour integrals
domain: special-function
regime: mellin
status: drafted
---

## Applies when (recognition signature)
Products of powers you want to separate; resolving an integral or sum into a
contour integral in a complex parameter `s`. The substrate beneath Meijer-G and
much of asymptotics.

## The rule
Mellin transform `M[f](s) = ∫_0^∞ x^{s-1} f(x) dx`, inverse a **Barnes** contour
integral `f(x) = (1/2πi) ∫ M[f](s) x^{-s} ds`. A product in `x` becomes a
convolution in `s`; **which way you close the contour** gives either the
convergent series (one side) or the asymptotic series (the other) — residues sum
to each.

## Worked example
`M[e^{-x}](s) = Γ(s)` (SymPy). Inverting, `e^{-x} = (1/2πi)∫ Γ(s) x^{-s} ds`; the
residues of `Γ` at `s = -n` give the Taylor series `Σ (-1)^n x^n / n!`.

## Explain (altitudes)
- **expert** — the Mellin transform diagonalizes scaling; Barnes integrals encode
  *both* the convergent and asymptotic expansions through the contour choice — the
  engine of the experimental-math / special-function toolkit (and of [[meijer-g-reduction]]).
- **working** — transform each factor, multiply, then invert by a contour integral
  and sum residues — picking the residues on the side where the contour closes.
- **plain** — a change of viewpoint where "stretching" becomes simple, so a hard
  product turns into a tidy list of residue terms you add up.

## LaTeX
rule: M[f](s)=\int_{0}^{\infty}x^{s-1}f(x)\,dx,\qquad f(x)=\tfrac{1}{2\pi i}\int M[f](s)\,x^{-s}\,ds
example: M[e^{-x}](s)=\Gamma(s)

## References
- Paris & Kaminski, *Asymptotics and Mellin–Barnes Integrals*; DLMF 1.14.
- Library: SymPy `mellin_transform`.

## Links
[[meijer-g-reduction]] · [[tricomi-u-reduction]] · [[gamma-function]] · [[watsons-lemma]]
