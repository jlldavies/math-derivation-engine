---
id: double-angle-formulae
name: Double-angle formulae (sin2t, cos2t)
domain: trigonometry
regime: elementary
status: drafted
---

## Applies when (recognition signature)
You see a function of `2θ` you want in terms of `θ` (or the reverse), or a stray
`sinθ cosθ` or `cos²θ`/`sin²θ` you want to fold into a single angle. Tell:
`2 sinθ cosθ` to collapse, or `cos²θ` to linearise before integrating.

## The rule
Set `A = B = θ` in the compound-angle formulae:

`sin 2θ = 2 sinθ cosθ`
`cos 2θ = cos²θ − sin²θ = 1 − 2sin²θ = 2cos²θ − 1`

The last two forms come from substituting `sin²θ + cos²θ = 1`, and give the
power-reduction identities `sin²θ = (1 − cos2θ)/2`, `cos²θ = (1 + cos2θ)/2`.

## Worked example
Derive `cos 2θ` from the compound angle:
`cos(θ + θ) = cosθ cosθ − sinθ sinθ = cos²θ − sin²θ`. Then with
`cos²θ = 1 − sin²θ` this is `1 − 2sin²θ`.

## Explain (altitudes)
- **expert** — the `n = 2` case of de Moivre, `(cosθ + i sinθ)² = cos2θ + i sin2θ`;
  the power-reduction forms are the projection onto the `cos2θ` harmonic, the key
  step in linearising quadratics of sinusoids for Fourier work.
- **working** — square the unit complex number `e^{iθ}` to double its angle, then
  read off real and imaginary parts. Use `sin²+cos²=1` to trade between the three
  equivalent `cos2θ` forms depending on which one cancels best.
- **plain** — these are just the addition formulae with both angles equal. They
  let you turn `2 sinθ cosθ` into one clean `sin2θ`, and turn an awkward `cos²θ`
  into something with no square — which is exactly what you need to integrate it.

## LaTeX
rule: \sin 2\theta=2\sin\theta\cos\theta,\qquad \cos 2\theta=\cos^{2}\theta-\sin^{2}\theta=1-2\sin^{2}\theta
example: \cos\!\left(\theta+\theta\right)=\cos^{2}\theta-\sin^{2}\theta=1-2\sin^{2}\theta

## References
- A-level Pure "Double-angle formulae"; standard in any trigonometry text.
- Library: SymPy `expand_trig` / `trigsimp`.

## Links
[[compound-angle-formulae]] · [[pythagorean-identity]]
