---
id: meijer-g-reduction
name: Products of powers/exponentials → Meijer-G
domain: special-function
regime: meijer_g
status: verified
---

## Applies when (recognition signature)
A half-line integral of **products** of algebraic powers, exponentials, and/or
trig factors — convolution-type integrals — where a closed form exists but is a
*named* special function rather than an elementary one.

## The rule
Represent each factor by its Mellin–Barnes contour integral (see [[mellin-barnes]]);
the whole integral collapses into a single **Meijer-G** function
`G^{m,n}_{p,q}(z | …)`. SymPy's `meijerg` algorithm does exactly this; almost every
classical special function is a special case of `G`.

## Worked example
`∫_0^∞ x^{-1/2}(x+8)^{-3/2} e^{-x} dx = G((½,),();(0,1),(); 8) / (4√π)`
(SymPy, the Blitz-shaped integrand). The harder oscillatory siblings reduce to
Tricomi `U` — see [[tricomi-u-reduction]].

## Explain (altitudes)
- **expert** — `G` is the universal closed form for Mellin–Barnes integrals; the
  integral table reduces to bookkeeping of the `G` parameter lists. Its asymptotics
  come from closing the Barnes contour (residues vs the saddle).
- **working** — each factor has a Mellin–Barnes representation; multiply them and
  collect the result into one `G`-function by reading off its `(a)` and `(b)`
  parameter rows.
- **plain** — a giant "master function" that most textbook integrals turn out to
  be a special case of — recognize the shape and write `G` with the right numbers.

## LaTeX
rule: \int_{0}^{\infty}\big(\text{powers}\times\text{exp/trig}\big)\,dx=G^{m,n}_{p,q}\!\big(z\big)
example: \int_{0}^{\infty}x^{-1/2}(x+8)^{-3/2}e^{-x}\,dx=\tfrac{1}{4\sqrt{\pi}}\,G^{2,1}_{1,2}\!\big(8\big)

## References
- Beals & Szmigielski, *Meijer G-Functions: A Gentle Introduction*; DLMF 16.17.
- Library: SymPy `integrate(..., meijerg=True)`.

## Links
[[tricomi-u-reduction]] · [[mellin-barnes]] · [[watsons-lemma]] · [[gamma-function]]
