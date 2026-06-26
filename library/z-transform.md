---
id: z-transform
name: Z-transform — discrete Laplace transform of a sequence
domain: transform
regime: transform
status: drafted
---

## Applies when (recognition signature)
A **discrete-time sequence** `x[n]` (a signal, a difference equation, a sampled
system) where you want a single function of a complex variable `z` that encodes
the whole tail. Tells: `x[n]`, `z^{-n}`, "discrete", "difference equation",
"sampled", "sequence", `Σ_{n≥0}`, DSP / control / probability-generating-function
context. The unilateral (one-sided) transform sums `n ≥ 0`.

## The rule
The (unilateral) Z-transform maps a sequence to a power series in `z^{-1}`:
`X(z) = Σ_{n=0}^{∞} x[n] z^{-n}`, convergent on an annular **region of
convergence** `|z| > R`. It is the discrete analogue of the Laplace transform
(set `z = e^{sT}` for sample period `T`). Linearity holds; the **shift rule**
`x[n-1] ↦ z^{-1}X(z)` turns difference equations into algebra, exactly as the
Laplace transform does for differential equations.

## Worked example
The unit-step geometric sequence `x[n] = aⁿ` (n ≥ 0):
`X(z) = Σ_{n≥0} aⁿ z^{-n} = Σ_{n≥0} (a z^{-1})ⁿ = 1/(1 − a z^{-1})`,  `|z| > |a|`,
summing the geometric series. (Oppenheim & Schafer, *Discrete-Time Signal
Processing*, Table 3.1 — `aⁿ u[n] ↔ 1/(1−az⁻¹)`.) SymPy: a `geometric` series
sum reproduces it directly.

## Explain (altitudes)
- **expert** — `X(z)` is the generating function of `x[n]` evaluated on `z^{-1}`;
  the ROC `|z|>|a|` is set by the pole at `z=a`, and `z=e^{sT}` is the conformal
  map carrying the Laplace `s`-plane to the `z`-plane (imaginary axis → unit
  circle). Poles inside the unit circle ⇔ a stable causal system.
- **working** — multiply each term `x[n]` by `z^{-n}` and add up the series; for a
  geometric `aⁿ` it is a geometric series with ratio `a z^{-1}`, which sums to
  `1/(1−az⁻¹)` wherever `|a z^{-1}| < 1`.
- **plain** — pack an infinite list of numbers into one formula by tagging the
  n-th number with `z^{-n}` and adding them up; if the list is `1, a, a², …` the
  sum folds up into a tidy fraction.

## LaTeX
rule: X(z)=\sum_{n=0}^{\infty}x[n]\,z^{-n},\qquad \left|z\right|>R
example: \sum_{n=0}^{\infty}a^{n}z^{-n}=\frac{1}{1-a z^{-1}},\qquad \left|z\right|>\left|a\right|

## References
- Oppenheim & Schafer, *Discrete-Time Signal Processing*, ch. 3 (Z-transform);
  Table 3.1 for the geometric pair.
- Jury, *Theory and Application of the z-Transform Method*.
- Library: SymPy series/`summation`; SciPy `scipy.signal` (z-domain tools).
- Worked example: Oppenheim & Schafer Table 3.1, `aⁿu[n] ↔ 1/(1−az⁻¹)`.

## Links
[[laplace-transform]] · [[fourier-transform]] · [[contour-residues]]
