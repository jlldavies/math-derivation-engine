---
id: integration-by-parts
name: Integration by parts (LIATE)
domain: calculus
regime: elementary
status: verified
---

## Applies when (recognition signature)
A product where one factor *simplifies when differentiated* and the other is
easily integrated: polynomial×exp, polynomial×trig, log, inverse-trig. Tell:
`∫ (polynomial / log / arctan) × (easy-to-integrate)`.

## The rule
`∫ u dv = u v − ∫ v du`. Choose `u` by **LIATE** (Log, Inverse-trig, Algebraic,
Trig, Exp) — earliest in the list is `u`, so it differentiates toward something
simpler.

## Worked example
`∫ x e^x dx = (x−1) e^x`  (u=x, dv=e^x dx). SymPy confirms.

## Explain (altitudes)
- **expert** — it is the adjoint of `d/dx`; the boundary term is the integrated
  total derivative from the product rule, and it generalizes to Green's identities
  / integration by parts in `n` dimensions (the divergence theorem in disguise).
- **working** — run the product rule backwards: move the derivative off the hard
  factor onto the easy one, paying a `uv` boundary term.
- **plain** — swap which piece you differentiate so the leftover integral is
  easier — trade a hard multiply-then-integrate for a simple one.

## LaTeX
rule: \int u\,dv=uv-\int v\,du
example: \int x\,e^{x}\,dx=(x-1)\,e^{x}

## References
- Any calculus text; SymPy `manualintegrate` (rule-tree exposition).
- Registry: `parts`.

## Links
[[u-substitution]] · [[gamma-function]] · [[differentiation-under-integral]]
