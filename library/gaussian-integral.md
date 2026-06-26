---
id: gaussian-integral
name: Gaussian integral — square it and go to polar
domain: calculus
regime: special-function
status: verified
---

## Applies when (recognition signature)
A Gaussian `e^{-a x²}` (or `e^{-(quadratic)}`) integrated over the whole line (or
half-line), where no elementary antiderivative exists. Tell: `∫ e^{-x²}`-shaped
integrand with infinite limits; normalization of a normal distribution.

## The rule
The 1-D integral has no elementary antiderivative, but its **square** is a 2-D
integral with **rotational symmetry** — go to polar coordinates:

`I = ∫_{-∞}^{∞} e^{-x²} dx`,  `I² = ∫∫ e^{-(x²+y²)} dx dy
   = ∫_0^{2π}∫_0^{∞} e^{-r²} r dr dθ = 2π · ½ = π`  ⇒  `I = √π`.

General: `∫_{-∞}^{∞} e^{-a x²} dx = √(π/a)`.

## Worked example
`∫_{-∞}^{∞} e^{-x²} dx = √π`.  (SymPy: `integrate(exp(-x**2), (x,-oo,oo)) → sqrt(pi)`.)

## Explain (altitudes)
- **expert** — the trick exploits the `SO(2)` rotational symmetry of `e^{-r²}`;
  the radial measure `r dr` is the Jacobian that makes it elementary. Generalizes
  to `n` dimensions and underlies the normal-distribution normalization and the
  heat kernel.
- **working** — you can't integrate it in 1-D, but two copies multiply to
  `e^{-(x²+y²)}`, which depends only on `r`; in polar the stray `r dr` cancels the
  difficulty and the integral collapses to `2π · ½`.
- **plain** — one bell curve is hard, but two of them make a round hill. Measure
  the hill's volume in thin rings out from the centre and it's easy — then take
  the square root to get back the single curve.

## LaTeX
rule: \int_{-\infty}^{\infty}e^{-a x^{2}}\,dx=\sqrt{\tfrac{\pi}{a}}
example: \int_{-\infty}^{\infty}e^{-x^{2}}\,dx=\sqrt{\pi}

## References
- Poisson's trick — standard in any calculus text (e.g. Stewart; Spivak).
- Library: SymPy `integrate` does this directly.

## Links
[[error-function]] · [[fresnel-integral]] · [[gamma-function]]
