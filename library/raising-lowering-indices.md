---
id: raising-lowering-indices
name: Raising and lowering indices with the metric
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
You need to convert a vector to a covector (or back), contract a covariant with a
contravariant tensor, or compute an inner product / norm. Tells: "raise/lower an
index", "V_a vs V^a", "g_ab V^b", "musical isomorphism", "inner product",
"covariant vs contravariant components", "inverse metric".

## The rule
The metric maps vectors to covectors and back: `V_a = g_ab V^b` (lower),
`V^a = g^{ab} V_b` (raise), where `g^{ab}` is the matrix inverse of `g_ab`, so
`g^{ab} g_bc = δ^a_c`. The same applies index-by-index to any tensor. The two
operations are inverse, and the norm is `g_ab V^a V^b = V_a V^a`. In flat Cartesian
space `g_ab = δ_ab`, so up and down components coincide.

## Worked example
**Schwarzschild**, `ds² = −(1−2M/r)dt² + (1−2M/r)^{−1}dr² + r²dΩ²`. For a purely
radial vector `V^a = (0, V^r, 0, 0)`, lowering gives
`V_r = g_rr V^r = (1−2M/r)^{−1} V^r` (all other `V_a = 0`). The inverse metric
component is just the reciprocal, `g^{rr} = (1−2M/r)` — `g^{ab}` is the matrix
inverse of `g_ab`, diagonal here so component-wise reciprocals.

## Explain (altitudes)
- **expert** — the musical isomorphisms `♭: TM → T*M`, `♯: T*M → TM` induced by the
  metric; `g^{ab}` is the inverse bilinear form and contraction with it realizes the
  canonical identification.
- **working** — to lower, multiply by `g_ab` and sum; to raise, multiply by the
  inverse metric `g^{ab}`; for a diagonal metric each component just picks up the
  corresponding metric factor (or its reciprocal).
- **plain** — the metric is a dictionary between two ways of writing the same arrow;
  lowering or raising an index just translates between them, and the inverse metric
  is what undoes the translation.

## LaTeX
rule: V_a=g_{ab}V^{b},\qquad V^{a}=g^{ab}V_b,\qquad g^{ab}g_{bc}=\delta^{a}{}_{c}
example: \text{Schwarzschild radial: }V_r=g_{rr}V^{r}=\left(1-\frac{2M}{r}\right)^{-1}V^{r}

## References
- D'Inverno, *Introducing Einstein's Relativity*, §5–6.
- Misner, Thorne & Wheeler, *Gravitation*, §2–3. Hartle, *Gravity*, §7.

## Links
[[metric-transformation-law]] · [[christoffel-symbols]] · [[covariant-derivative]]
