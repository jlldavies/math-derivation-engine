---
id: tricomi-u-reduction
name: Power × shifted-power × exponential → Tricomi U
domain: special-function
regime: meijer_g
status: verified
---

## Applies when (recognition signature)
A half-line integral of a **power** times a **shifted power** times an
**exponential**:  `∫_0^∞ x^{a-1} (x+c)^{-b} e^{-s x} dx`.
Tells: `x^{power} (x+const)^{power} e^{±x}` over `[0,∞)`; oscillatory variants have
`s = ±i·(freq)` (then it is a Laplace transform evaluated on the imaginary axis).

## The rule
`∫_0^∞ x^{a-1} (x+c)^{-b} e^{-s x} dx = Γ(a) · c^{a-b} · U(a, a-b+1, c s)`
where `U` is the Tricomi confluent hypergeometric function. Holds by analytic
continuation for **complex `s`** (the oscillatory case) and continues in `a`
past the convergence boundary (the divergent piece is then a finite-part /
`(e^{-sx}-1)` subtraction). Asymptotics in `s` come from the large-`z` expansion
of `U` (DLMF 13.7; integer-`b` cases carry logs).

## Worked example
The Blitz correlators reduce to this exactly:
`N = (1/i)[ Γ(-½)/8 · U(-½,0,-8iℒ) + ¼ ]`,
`Z₁ = (√π/8) ∫_0^ℒ k₀ U(½,0,-8ik₀) dk₀`.
Verified to **18 digits** (incl. the oscillatory case). Code:
`examples/subleading_closed_form.py`.

## Explain (altitudes)
- **expert** — the integral is the Laplace transform of `x^{a-1}(x+c)^{-b}`, which
  is precisely `U`'s integral representation (DLMF 13.4.4) after `x = c t`; a
  Mellin–Barnes view gives the same. The whole analytic structure (continuation,
  asymptotics) travels with the closed form.
- **working** — substitute `x = c t` to map the integral onto `U`'s standard
  integral rep, then read off the parameters `(a, a-b+1, cs)`.
- **plain** — this exact *shape* of integral has a known "name" answer, the way
  `a²+b²=c²` flags a right triangle — so you recognize it and write the function
  down instead of grinding it out.

## LaTeX
rule: \int_{0}^{\infty}x^{a-1}(x+c)^{-b}e^{-s x}\,dx=\Gamma(a)\,c^{\,a-b}\,U(a,\,a-b+1,\,c s)
example: N=\tfrac{1}{i}\Big[\tfrac{\Gamma(-1/2)}{8}\,U\!\big(-\tfrac12,0,-8i\mathcal{L}\big)+\tfrac14\Big]

## References
- DLMF 13.4.4 (integral representation of `U`); 13.7 (large-`z` asymptotics).
- Gradshteyn–Ryzhik 3.383.5.
- Library: SymPy `hyperu`, mpmath `hyperu`.
- Worked example: Blitz & Majid, arXiv:2405.18397 (the correlators).

## Links
[[meijer-g-reduction]] · [[watsons-lemma]] · [[mellin-barnes]] · [[hadamard-finite-part]]
