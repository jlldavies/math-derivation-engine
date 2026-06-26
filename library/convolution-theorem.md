---
id: convolution-theorem
name: Convolution theorem — a transform turns convolution into a product
domain: transform
regime: transform
status: drafted
---

## Applies when (recognition signature)
An integral (or sum) of the **convolution** form `(f*g)(t) = ∫ f(τ)g(t−τ) dτ` —
a smoothing, a filter, a moving average, the distribution of a **sum** of
independent random variables, a Green's-function response. Tells: `f*g`,
`∫ f(τ)g(t−τ)dτ`, "convolution", "filter", "impulse response", "sum of independent
variables", or a product of two transforms you want to invert.

## The rule
Under the Fourier transform (and likewise Laplace), convolution becomes
**pointwise multiplication**:
`F{f * g} = F{f} · F{g}`  (and dually `F{f·g} = F{f} * F{g} / 2π`).
So a hard convolution integral is done by transforming both factors, multiplying,
and inverting. Validity: `f, g ∈ L¹` (Fourier), or both having a common strip of
convergence (Laplace).

## Worked example
Convolve two zero-mean Gaussians of variances `σ₁²` and `σ₂²`. Each has Fourier
transform `exp(−½ σ²ω²)`; the product is `exp(−½(σ₁²+σ₂²)ω²)`, which inverts to a
Gaussian of variance `σ₁²+σ₂²`:
`N(0,σ₁²) * N(0,σ₂²) = N(0, σ₁²+σ₂²)` — **variances add**. (Standard result; the
sum of two independent normals is normal — Feller, *An Introduction to Probability
Theory*, vol. II.)

## Explain (altitudes)
- **expert** — convolution is the group operation on `L¹(ℝ)`; the Fourier
  transform is the algebra isomorphism diagonalizing translation, so it carries the
  convolution algebra to the pointwise-product algebra. Gaussians are fixed points
  up to scaling, hence closed under convolution with additive variance.
- **working** — transform `f` and `g`, multiply the two transforms, invert. For
  Gaussians the transform of a Gaussian is a Gaussian, the exponents `−½σ²ω²` add,
  so the result is a Gaussian whose variance is the sum.
- **plain** — blurring with one bell curve then another is the same as blurring
  once with a wider bell curve; the spreads (variances) just add up.

## LaTeX
rule: \mathcal{F}\!\left\{f * g\right\}=\mathcal{F}\!\left\{f\right\}\cdot\mathcal{F}\!\left\{g\right\}
example: \mathcal{N}(0,\sigma_1^{2}) * \mathcal{N}(0,\sigma_2^{2})=\mathcal{N}\!\left(0,\,\sigma_1^{2}+\sigma_2^{2}\right)

## References
- Bracewell, *The Fourier Transform and Its Applications*, ch. 3 (convolution theorem).
- Feller, *An Introduction to Probability Theory and Its Applications*, vol. II
  (sum of independent normals).
- Library: SciPy `scipy.signal.fftconvolve`; SymPy `fourier_transform`.
- Worked example: Gaussian∗Gaussian, variances add (Feller vol. II).

## Links
[[fourier-transform]] · [[laplace-transform]] · [[gaussian-integral]]
