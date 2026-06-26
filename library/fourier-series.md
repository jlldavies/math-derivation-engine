---
id: fourier-series
name: Fourier series — expand a periodic function in sines and cosines
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
A periodic function (period `2π` or `2L`), or boundary/initial data to be expanded
in modes. Tells: "periodic", "expand in harmonics", "Fourier coefficients",
square/sawtooth/triangle waves, the coefficients of a separated PDE solution,
mode amplitudes.

## The rule
A periodic `f` (period `2π`) expands as
`f(x) = a₀/2 + Σ_{n≥1}(a_n cos nx + b_n sin nx)`, with coefficients from
orthogonality of the trig system: `a_n = (1/π)∫_{−π}^{π} f(x)cos nx dx`,
`b_n = (1/π)∫_{−π}^{π} f(x)sin nx dx`. The series converges in `L²`, and pointwise
to `½[f(x⁺)+f(x⁻)]` at jumps (Dirichlet).

## Worked example
Odd square wave `f(x) = +1` on `(0,π)`, `−1` on `(−π,0)`. All `a_n=0` (odd); 
`b_n = (1/π)∫_{−π}^{π} f sin nx dx = (2/π)∫_0^π sin nx dx = (2/nπ)(1−cos nπ)`,
which is `4/(nπ)` for odd `n` and `0` for even `n`. Hence
`f(x) = (4/π) Σ_{k odd} sin(kx)/k`. Standard result (Tolstov, *Fourier Series*, §1).

## Explain (altitudes)
- **expert** — `{1, cos nx, sin nx}` is a complete orthogonal basis for `L²(−π,π)`;
  the coefficients are projections, Parseval gives the energy, and convergence is
  governed by the function's smoothness (Gibbs at jumps).
- **working** — multiply `f` by `cos nx` (or `sin nx`) and integrate; orthogonality
  kills every term but one, isolating that coefficient. Reassemble the weighted
  harmonics.
- **plain** — any repeating wiggle is a stack of pure tones. To find how much of
  each tone is present, "tune in" by multiplying and averaging, and add the tones
  back up.

## LaTeX
rule: f(x)=\frac{a_{0}}{2}+\sum_{n=1}^{\infty}\!\left(a_{n}\cos nx+b_{n}\sin nx\right),\quad a_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}\!f(x)\cos nx\,dx
example: f(x)=\frac{4}{\pi}\sum_{k\ \mathrm{odd}}\frac{\sin(kx)}{k}

## References
- Tolstov, *Fourier Series*, §1 (coefficients, square wave).
- Stein & Shakarchi, *Fourier Analysis*, ch. 2.
- Library: SymPy `fourier_series`; SciPy `scipy.fft` (discrete spectrum).
- Worked example: Tolstov §1 (the square wave).

## Links
[[separation-of-variables]] · [[fourier-transform]] · [[sturm-liouville]]
