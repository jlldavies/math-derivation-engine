---
id: complex-trig-identities
name: Trig identities via exponentials
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You need to either **expand** `cos nθ`/`sin nθ` as polynomials in `cosθ, sinθ`, or
**linearise** a power `sinⁿθ`/`cosⁿθ` into a sum of single multiple-angle terms
(the form you must reach before integrating `∫ sinⁿθ dθ`). Tell: a high power of a
single sinusoid, or a multiple-angle target.

## The rule
Write `cosθ = (z + z⁻¹)/2`, `sinθ = (z − z⁻¹)/(2i)` with `z = e^{iθ}` (so
`zⁿ = e^{inθ}` gives `cos nθ + i sin nθ`). Then:
- **powers → multiple angles:** expand `((z ± z⁻¹)/…)ⁿ` by the binomial theorem and
  pair terms `zᵏ + z⁻ᵏ = 2cos kθ` (or `zᵏ − z⁻ᵏ = 2i sin kθ`);
- **multiple angles → powers:** equate real/imag parts of `zⁿ` (de Moivre).
Both directions are pure algebra in `z`.

## Worked example
Linearise `sin³θ`. With `sinθ = (z − z⁻¹)/(2i)`:
`sin³θ = ((z − z⁻¹)/(2i))³ = (z³ − 3z + 3z⁻¹ − z⁻³)/(2i)³`.
Now `(2i)³ = −8i`, and group conjugate powers:
`z³ − z⁻³ = 2i sin 3θ`, `z − z⁻¹ = 2i sinθ`, so the numerator is
`(2i sin 3θ) − 3(2i sinθ) = 2i(sin 3θ − 3 sinθ)`. Divide by `−8i`:
`sin³θ = (sin 3θ − 3 sinθ)/(−4) = (3 sinθ − sin 3θ)/4`. ✓

## Explain (altitudes)
- **expert** — this is harmonic analysis on `S¹`: `{e^{ikθ}}` is the orthogonal
  Fourier basis, and "linearising `sinⁿθ`" is just reading off its finite Fourier
  coefficients; the cos-power expansions are the Chebyshev `Tₙ` (see
  chebyshev-polynomials).
- **working** — substitute `z = e^{iθ}`, binomial-expand, and re-pair powers using
  `zᵏ ± z⁻ᵏ = 2cos kθ` or `2i sin kθ`. Watch the `(2i)ⁿ` factor — it carries the sign.
- **plain** — every `sin`/`cos` is a combination of `z = e^{iθ}` and `1/z`. Once it
  is all powers of `z`, you just multiply out like ordinary algebra and translate
  back, no trig identities to memorise.

## LaTeX
rule: \cos\theta=\frac{z+z^{-1}}{2},\quad \sin\theta=\frac{z-z^{-1}}{2i},\qquad z^{k}\pm z^{-k}=\begin{cases}2\cos k\theta\\ 2i\sin k\theta\end{cases}
example: \sin^{3}\theta=\left(\frac{z-z^{-1}}{2i}\right)^{3}=\frac{2i\left(\sin 3\theta-3\sin\theta\right)}{-8i}=\frac{3\sin\theta-\sin 3\theta}{4}

## References
- Standard "powers and multiples" technique; e.g. Riley, Hobson & Bence
  *Mathematical Methods*, ch. on complex numbers.
- Library: SymPy `expand_trig`, `fourier_series`.

## Links
[[euler-formula]] · [[de-moivre-theorem]] · [[product-to-sum]] · [[chebyshev-polynomials]]
