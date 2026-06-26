---
id: div-of-curl
name: Divergence of a curl vanishes
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
The divergence of a curl: `∇·(∇×F)`, i.e. `ε_{ijk} ∂_i ∂_j F_k`. Sibling of
curl-of-grad — both are the symmetric×antisymmetric pattern, both are `d²=0`.

## The rule
`ε_{ijk} ∂_i ∂_j F_k = 0`: `∂_i ∂_j` is symmetric in `(i,j)`, `ε_{ijk}` is
antisymmetric in `(i,j)` ⇒ the contraction is identically zero. See
[[sym-antisym-contraction]].

## Worked example
`∇·(∇×F) = 0` for every smooth `F`. SymPy verifies it for a generic vector field
(`P,Q,R`)(x,y,z) → 0.

## Explain (altitudes)
- **expert** — `d²=0` for the 1-form `F♭`: `∇×F` is (the dual of) `dF♭`, an exact
  2-form, hence closed and divergence-free.
- **working** — `ε_{ijk}∂_i∂_j` is a symmetric pair contracted with an
  antisymmetric symbol ⇒ 0.
- **plain** — a curl field is made of closed loops: whatever flows in flows out,
  so there are no sources or sinks — zero divergence.

## LaTeX
rule: \varepsilon_{ijk}\,\partial_i\partial_j F_k=0
example: \nabla\cdot(\nabla\times\mathbf{F})=0

## References
- do Carmo, *Differential Forms and Applications* (`d²=0`).
- Library: SymPy `divergence(curl(F))` → 0.

## Links
[[sym-antisym-contraction]] · [[epsilon-delta-identity]] · [[laplacian-from-div-grad]]
