---
id: sym-antisym-contraction
name: Symmetric × antisymmetric contraction vanishes
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
A tensor **symmetric** in an index pair is contracted with one **antisymmetric**
in the *same* pair:  `T = A_{..jk..} S_{..jk..}` with `S_{jk}=S_{kj}`,
`A_{jk}=-A_{kj}`.

Surface tells: `curl(grad …)`, `div(curl …)`, anything `ε_{ijk} ∂_j ∂_k`, a
Levi-Civita symbol contracted with a Hessian / a symmetric stress tensor, or
`d(dω)` (the exterior-derivative form).

## The rule
`A_{jk} S_{jk} = 0`. Relabel the contracted dummies `j ↔ k`: `S` is unchanged,
`A` flips sign, so the sum equals **minus itself** ⇒ it is identically zero.

## Worked example
`(∇×∇φ)_i = ε_{ijk} ∂_j ∂_k φ = 0`  — the curl of any gradient vanishes.
Code: `examples/tensor_curl_grad.py` (SymPy verifies `curl(grad φ) = (0,0,0)`).

## Explain (altitudes)
- **expert** — `d² = 0`: `φ` is a 0-form, `dφ` its gradient (an exact 1-form),
  `d(dφ)=0` — exact ⇒ closed; the curl identity is the 3-D shadow of the exterior
  derivative squaring to zero (trivial de Rham class).
- **working** — sum over `j,k` of (antisymmetric)(symmetric); relabel `j↔k` ⇒
  the sum equals minus itself ⇒ zero.
- **plain** — a gradient is pure downhill; "curl" is swirl; pure downhill can't
  swirl, so curl of a gradient is always zero.

## LaTeX
rule: \varepsilon_{ijk}\,S_{jk}=0\quad(S_{jk}=S_{kj},\ \varepsilon_{ijk}=-\varepsilon_{ikj})
example: (\nabla\times\nabla\phi)_i=\varepsilon_{ijk}\,\partial_j\partial_k\phi=0

## References
- Clairaut / Schwarz — mixed partials commute (gives the symmetry of `∂_j∂_k`).
- do Carmo, *Differential Forms and Applications* — `d²=0`.
- Library: SymPy `curl(grad …)` reduces to the zero vector.

## Links
[[laplacian-from-div-grad]] · [[epsilon-delta-identity]] · [[div-of-curl]]
