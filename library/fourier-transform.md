---
id: fourier-transform
name: Fourier transform
domain: transform
regime: integral-transform
status: verified
---

## Applies when (recognition signature)
A function on the whole line where frequency content, convolution, or a
constant-coefficient PDE/ODE matters. Tell: `∫_{-∞}^{∞} e^{−ikx}(…) dx`,
diffraction/spectra, or convolution you want to turn into a product.

## The rule
`f̂(k) = ∫_{-∞}^{∞} e^{−ikx} f(x) dx`. Linear; maps `d/dx → ik`, convolution →
product, and translation → modulation. Inversion:
`f(x) = (1/2π) ∫_{-∞}^{∞} e^{ikx} f̂(k) dk`.

## Worked example
The Gaussian is self-dual: `FT[e^{−x²/2}](k) = √(2π) e^{−k²/2}`. Complete the
square `−x²/2 − ikx = −(x+ik)²/2 − k²/2` and use `∫_{-∞}^{∞} e^{−(x+ik)²/2} dx =
√(2π)` (contour shift). (Known result.)

## Explain (altitudes)
- **expert** — the transform diagonalizes translation: plane waves `e^{ikx}` are
  the simultaneous eigenfunctions of `d/dx`, so differential operators become
  polynomials in `k`; the Gaussian is a fixed point because it minimizes the
  uncertainty product.
- **working** — decompose `f` into pure waves; differentiation becomes
  multiply-by-`ik` and convolution becomes ordinary multiplication, so PDEs turn
  algebraic. Completing the square handles the Gaussian.
- **plain** — break a shape into pure sine waves and record how much of each.
  A bell curve is special: its recipe of waves is another bell curve.

## LaTeX
rule: \hat{f}(k)=\int_{-\infty}^{\infty}e^{-ikx}f(x)\,dx
example: \int_{-\infty}^{\infty}e^{-x^{2}/2}\,e^{-ikx}\,dx=\sqrt{2\pi}\,e^{-k^{2}/2}

## References
- Standard transform; Stein & Shakarchi, *Fourier Analysis*; Bracewell.
- Library: SymPy `fourier_transform`.

## Links
[[gaussian-integral]] · [[fresnel-integral]] · [[mellin-barnes]] · [[convolution-theorem]]
