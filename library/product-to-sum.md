---
id: product-to-sum
name: Product-to-sum formulae
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You face a **product of two trig functions** — `sin A cos B`, `cos A cos B`,
`sin A sin B` — and want a sum, not a product. Tell: integrating a product of
sinusoids (the sum form integrates term-by-term), or proving an orthogonality
relation where cross-terms must vanish.

## The rule
From the compound-angle expansions of `sin(A±B)` and `cos(A±B)`:

`2 sin A cos B = sin(A + B) + sin(A − B)`
`2 cos A cos B = cos(A − B) + cos(A + B)`
`2 sin A sin B = cos(A − B) − cos(A + B)`

(and `2 cos A sin B = sin(A + B) − sin(A − B)`.) Each turns a product into a sum
of two single-angle terms — directly integrable.

## Worked example
`∫ sin 3x cos x dx`. Use `2 sin A cos B = sin(A+B) + sin(A−B)` with `A = 3x`,
`B = x`:

`sin 3x cos x = ½[sin 4x + sin 2x]`.

Integrate term by term:

`∫ sin 3x cos x dx = ½[ −¼cos 4x − ½cos 2x ] + C = −⅛cos 4x − ¼cos 2x + C`.

Check by differentiating: `−⅛(−4 sin 4x) − ¼(−2 sin 2x) = ½ sin 4x + ½ sin 2x
= sin 3x cos x`. ✓

## Explain (altitudes)
- **expert** — writing `sin, cos` as combinations of `e^{±iθ}`, a product of
  exponentials adds exponents: `e^{iA}e^{iB} = e^{i(A+B)}`. Multiplying out
  `(e^{iA} − e^{−iA})(e^{iB} + e^{iB})/(2i·2)` and regrouping is exactly these
  identities; they are the statement that products of characters decompose into
  characters of summed frequencies.
- **working** — add the two compound-angle lines `sin(A+B) = sinA cosB + cosA sinB`
  and `sin(A−B) = sinA cosB − cosA sinB`: the `cosA sinB` terms cancel, leaving
  `sin(A+B) + sin(A−B) = 2 sinA cosB`. The cosine pair gives the other two.
- **plain** — multiplying two waves of different frequencies is the same as
  **adding** two waves, one at the sum frequency and one at the difference
  frequency. That swap is what makes products of sines and cosines easy to
  integrate.

## LaTeX
rule: 2\sin A\cos B=\sin\!\left(A+B\right)+\sin\!\left(A-B\right),\qquad 2\cos A\cos B=\cos\!\left(A-B\right)+\cos\!\left(A+B\right)
example: \int\sin 3x\cos x\,dx=\frac{1}{2}\int\!\left(\sin 4x+\sin 2x\right)dx=-\frac{1}{8}\cos 4x-\frac{1}{4}\cos 2x+C

## References
- A-level / pre-calculus "Product-to-sum identities"; standard in integral tables.
- Basis for Fourier-coefficient and orthogonality computations.

## Links
[[compound-angle-formulae]] · [[sum-to-product]] · [[trig-orthogonality]]
