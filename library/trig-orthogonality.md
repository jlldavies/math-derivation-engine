---
id: trig-orthogonality
name: Orthogonality of the trigonometric system
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
You need to isolate a single Fourier coefficient, prove modes don't interfere, or
justify why `{sin nx, cos nx}` is a basis. Tells: "integral of a product of sines/
cosines over a full period", "Fourier coefficient extraction", "orthogonal modes",
Kronecker delta `δ_{mn}`, the projection step in a Fourier or Sturm–Liouville expansion.

## The rule
Over a full period `[−π, π]`, the trigonometric system is mutually orthogonal. For
integers `m, n ≥ 1`:
`∫_{−π}^{π} sin mx · sin nx dx = π δ_{mn}`,
`∫_{−π}^{π} cos mx · cos nx dx = π δ_{mn}`,
`∫_{−π}^{π} sin mx · cos nx dx = 0` (all `m, n`).
Each integral is evaluated by a product-to-sum identity:
`sin mx sin nx = ½[cos(m−n)x − cos(m+n)x]`, and `∫_{−π}^{π} cos kx dx = 0` for any
nonzero integer `k`, `= 2π` for `k = 0`. This orthogonality is exactly what lets the
Fourier coefficients be read off one at a time.

## Worked example
First a vanishing case: `∫_{−π}^{π} sin 2x sin 3x dx`. Product-to-sum gives
`sin 2x sin 3x = ½[cos x − cos 5x]`, and `∫_{−π}^{π} cos x dx = ∫_{−π}^{π} cos 5x dx = 0`,
so the integral is `0` (`m ≠ n`). Now the diagonal: `∫_{−π}^{π} sin²2x dx`. Here
`sin²2x = ½(1 − cos 4x)`, so the integral is `½[∫_{−π}^{π}1\,dx − ∫_{−π}^{π}cos 4x\,dx]
= ½[2π − 0] = π`. Both match `π δ_{mn}`. Standard result (Tolstov, *Fourier Series*, §1).

## Explain (altitudes)
- **expert** — `{1, cos nx, sin nx}_{n≥1}` is a complete orthogonal system in
  `L²(−π,π)`; it is the eigenbasis of `−d²/dx²` with periodic BCs (a regular
  Sturm–Liouville problem), so orthogonality is automatic from self-adjointness and
  the coefficients are honest inner-product projections.
- **working** — convert each product of two sinusoids into a sum of single cosines;
  every cosine of nonzero integer frequency integrates to zero over a whole period, so
  only the matched pair (`m = n`) survives, contributing `π`.
- **plain** — multiply two different pure waves and average over a full cycle and you
  get nothing; multiply a wave by itself and you get a fixed positive number. That
  "different waves cancel" is what makes them independent building blocks.

## LaTeX
rule: \int_{-\pi}^{\pi}\sin mx\,\sin nx\,dx=\pi\,\delta_{mn},\qquad \int_{-\pi}^{\pi}\sin mx\,\cos nx\,dx=0
example: \int_{-\pi}^{\pi}\sin 2x\,\sin 3x\,dx=0,\qquad \int_{-\pi}^{\pi}\sin^{2}2x\,dx=\pi

## References
- Tolstov, *Fourier Series*, §1 (orthogonality relations).
- Stein & Shakarchi, *Fourier Analysis*, ch. 2.
- Library: SymPy `integrate(sin(2*x)*sin(3*x), (x, -pi, pi))`.
- Worked example: Tolstov §1 (product-to-sum evaluation of the basis integrals).

## Links
[[fourier-series]] · [[product-to-sum]] · [[sturm-liouville]] · [[chebyshev-polynomials]]
