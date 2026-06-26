---
id: u-substitution
name: u-substitution (reverse chain rule)
domain: calculus
regime: elementary
status: verified
---

## Applies when (recognition signature)
The integrand contains an **inner function and (a multiple of) its derivative** —
a composite `f(g(x))·g'(x)`. Tell: you can see "something" and its own slope
multiplied together.

## The rule
`∫ f(g(x)) g'(x) dx = ∫ f(u) du`, with `u = g(x)`, `du = g'(x) dx`. The composite
collapses to a plain integral in `u`.

## Worked example
`∫ 2x cos(x²) dx = sin(x²)`  (u = x², du = 2x dx). SymPy confirms.

## Explain (altitudes)
- **expert** — the chain rule run backwards; a 1-D change of variables, i.e. the
  pullback of the 1-form `f(u)du` along `u=g(x)`.
- **working** — spot the inner function `g` and its derivative `g'` in the
  integrand; rename `u=g`, and the integral becomes elementary in `u`.
- **plain** — undo the chain rule: if you see something and its slope multiplied,
  call the something `u` and the problem gets simple.

## LaTeX
rule: \int f\!\big(g(x)\big)\,g'(x)\,dx=\int f(u)\,du
example: \int 2x\cos(x^{2})\,dx=\sin(x^{2})

## References
- Any calculus text; SymPy `integrate`.
- Registry: `u_sub`.

## Links
[[integration-by-parts]] · [[gaussian-integral]]
