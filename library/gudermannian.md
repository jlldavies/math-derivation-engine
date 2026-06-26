---
id: gudermannian
name: Gudermannian function — circular ↔ hyperbolic without complex numbers
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You need to link a hyperbolic angle to a circular one over the reals — Mercator-map
latitude, the integral `∫ sech x dx`, or converting between `tanh`/`sech` and
`tan`/`sec` without invoking `i`. Tells: "Gudermannian", "Mercator projection
latitude", `gd(x)`, `arctan(sinh x)`, a real identity tying hyperbolic and circular
trig together.

## The rule
The Gudermannian `gd` maps the real line onto `(−π/2, π/2)` and matches the circular
and hyperbolic functions of related angles with **no complex numbers**:
`gd(x) = 2 arctan(tanh(x/2)) = arctan(sinh x) = 2 arctan(eˣ) − π/2`.
Its companion identities are `sin(gd x) = tanh x`, `cos(gd x) = sech x`,
`tan(gd x) = sinh x`. Its derivative is the clean
`gd′(x) = sech x = 1/cosh x`,
so `gd(x) = ∫₀ˣ sech t dt` — the Gudermannian is the antiderivative of `sech`.

## Worked example
Verify the two defining facts from `gd(x) = arctan(sinh x)`. **Value at 0:**
`gd(0) = arctan(sinh 0) = arctan(0) = 0`. **Derivative:** by the chain rule with
`(d/dx) arctan u = u′/(1+u²)` and `u = sinh x`, `u′ = cosh x`,
`gd′(x) = cosh x/(1 + sinh²x)`. Using the hyperbolic Pythagorean identity
`1 + sinh²x = cosh²x`, this collapses to `cosh x/cosh²x = 1/cosh x = sech x`. So
`gd′(x) = sech x` and `gd(0) = 0`, as claimed — and integrating back gives the
standard `∫ sech x dx = gd(x) + C` (Abramowitz & Stegun, §4.3.117).

## Explain (altitudes)
- **expert** — `gd` is the real diffeomorphism `ℝ → (−π/2,π/2)` conjugating the
  one-parameter hyperbolic "rotation" to the circular one; it realises the
  circular–hyperbolic link entirely over ℝ (the complex route `tan θ = tanh(ix)/i`
  is avoided), with `sech` as the pushforward of the flat measure — hence its role as
  the Mercator latitude scale factor.
- **working** — set `θ = gd(x)`; then `tan θ = sinh x` and differentiating gives the
  Mercator relation `dθ/dx = sech x`. It lets you swap a hyperbolic-angle problem for a
  circular-angle one and integrate `sech` in closed form.
- **plain** — there's a single function that turns a "hyperbolic angle" into an
  ordinary angle between −90° and +90°, no imaginary numbers needed. Its slope is
  `sech x`, which is why it's the area under the `sech` curve.

## LaTeX
rule: \mathrm{gd}(x)=2\arctan\!\left(\tanh\frac{x}{2}\right)=\arctan(\sinh x),\qquad \mathrm{gd}'(x)=\operatorname{sech} x
example: \mathrm{gd}'(x)=\frac{\cosh x}{1+\sinh^{2}x}=\frac{\cosh x}{\cosh^{2}x}=\operatorname{sech} x,\quad \mathrm{gd}(0)=0

## References
- Abramowitz & Stegun, *Handbook of Mathematical Functions*, §4.3.117 and §4.3.115.
- Gradshteyn & Ryzhik, *Tables of Integrals*, §1.49 (Gudermannian).
- Library: SymPy `gudermannian` (`mpmath.gudermannian`); verify `diff(atan(sinh(x)), x)`.
- Worked example: A&S §4.3.117 (`gd′ = sech`, `∫ sech = gd`).

## Links
[[hyperbolic-functions]] · [[inverse-trig-functions]] · [[inverse-hyperbolic-functions]] · [[pythagorean-identity]]
