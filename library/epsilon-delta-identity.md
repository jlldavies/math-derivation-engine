---
id: epsilon-delta-identity
name: Levi-Civita ε–δ contraction identity
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
A product of two Levi-Civita symbols sharing one index, `ε_{ijk} ε_{ilm}`; or its
disguises — a double cross product `a×(b×c)`, or curl-of-curl `∇×(∇×F)`.

## The rule
`ε_{ijk} ε_{ilm} = δ_{jl} δ_{km} − δ_{jm} δ_{kl}`  ("first–first minus first–second").
Everything cross-product collapses to dot products via this.

## Worked example
- `a×(b×c) = b(a·c) − c(a·b)`  (the BAC–CAB rule).
- `∇×(∇×F) = ∇(∇·F) − ∇²F`  — SymPy verifies the x-component identity.

## Explain (altitudes)
- **expert** — it is the contraction that encodes the `\mathfrak{so}(3)` structure
  constants; the alternating tensor squared resolves into the metric (δ) tensors,
  which is why cross products reduce to dot products.
- **working** — the right side is the only δ-combination with the correct index
  symmetry; pattern-match `ε ε` → `δδ − δδ` and read indices off in order.
- **plain** — turns a messy "cross then cross again" into two clean
  "multiply-and-add" (dot) terms: BAC minus CAB.

## LaTeX
rule: \varepsilon_{ijk}\,\varepsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}
example: \mathbf{a}\times(\mathbf{b}\times\mathbf{c})=\mathbf{b}\,(\mathbf{a}\cdot\mathbf{c})-\mathbf{c}\,(\mathbf{a}\cdot\mathbf{b})

## References
- Goldstein, *Classical Mechanics*; any vector-calculus text.
- Library: SymPy tensor / component check.

## Links
[[div-of-curl]] · [[sym-antisym-contraction]] · [[laplacian-from-div-grad]]
