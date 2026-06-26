---
id: inverse-laplace-bromwich
name: Inverse Laplace — Bromwich contour by residues
domain: transform
regime: transform
status: drafted
---

## Applies when (recognition signature)
You have a Laplace-domain function `F(s)` and need the time-domain `f(t)`, and
`F(s)` is a **rational** (or otherwise meromorphic) function with isolated poles.
Tells: "inverse Laplace", `F(s)` with a denominator that factors, partial
fractions, a transfer function, "find f(t)", `1/(s−a)`, `1/(s²+ω²)`, control /
circuits / ODE-solution context.

## The rule
The inverse Laplace transform is the **Bromwich (Mellin) integral** up a vertical
line to the right of all singularities:
`f(t) = (1/2πi) ∫_{c−i∞}^{c+i∞} F(s) e^{st} ds`, `c > Re(all poles)`. Close the
contour to the left (for `t>0`) and apply the residue theorem: `f(t)` is the **sum
of residues** of `F(s)e^{st}` at the poles of `F`. For simple poles, each
contributes `Res_{s=sₖ} F(s)e^{st}`.

## Worked example
`F(s) = 1/(s−a)` has a single simple pole at `s=a`. Its residue:
`Res_{s=a} e^{st}/(s−a) = e^{at}`. So `f(t) = e^{at}` for `t>0`. (Abramowitz &
Stegun / standard Laplace table — `1/(s−a) ↔ e^{at}`; SymPy:
`inverse_laplace_transform(1/(s-a), s, t) → exp(a*t)·Heaviside(t)`.)

## Explain (altitudes)
- **expert** — the Bromwich line lives in the strip of convergence; closing left
  and invoking Jordan's lemma (the `e^{st}` factor decays for `t>0` as `Re s→−∞`)
  reduces the inversion to `Σ Res`. The pole locations are the system's natural
  frequencies; residues are the modal amplitudes.
- **working** — write `f(t)` as the contour integral, then use the residue theorem:
  the integral equals `2πi` times the sum of residues, the `2πi` cancels the
  prefactor, and each simple pole `sₖ` gives `(numerator/denominator′)e^{sₖt}`.
- **plain** — to undo a Laplace transform you read off where the formula blows up
  (its poles); each blow-up point `a` hands you a piece `e^{at}`, and you add the
  pieces to get the time function. Here there's one pole, so `f(t)=e^{at}`.

## LaTeX
rule: f(t)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}F(s)\,e^{st}\,ds=\sum_{k}\operatorname*{Res}_{s=s_k}\left[F(s)\,e^{st}\right]
example: \operatorname*{Res}_{s=a}\frac{e^{st}}{s-a}=e^{at}\ \Rightarrow\ f(t)=e^{at}

## References
- Arfken & Weber, *Mathematical Methods for Physicists*, §7 (Bromwich integral / residues).
- Abramowitz & Stegun, *Handbook of Mathematical Functions*, §29 (Laplace transform pairs).
- Library: SymPy `inverse_laplace_transform`; mpmath `invertlaplace`.
- Worked example: `1/(s−a) ↔ e^{at}` (standard Laplace table).

## Links
[[laplace-transform]] · [[contour-residues]] · [[gamma-reflection]]
