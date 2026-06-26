---
id: metric-transformation-law
name: Metric / tensor transformation under a change of coordinates
domain: tensor
regime: tensor
status: verified
---

## Applies when (recognition signature)
A line element / metric is given in one set of coordinates and you transform to
new ones (a change of variables `x = x(x̄)`); you want a component of the new
metric (a coefficient of `dx̄^a dx̄^b`). Tells: "line element", "ds²", "apply these
transformations", "find the coefficient of dX²", GR / differential-geometry context.

## The rule
A metric is a rank-2 `(0,2)` tensor; each index carries a Jacobian factor:
`ḡ_{ab} = (∂xᵘ/∂x̄ᵃ)(∂xᵛ/∂x̄ᵇ) g_{μν}`  (pullback `ḡ = Jᵀ g J`). For a **diagonal**
metric, the diagonal coefficient is just `ḡ_{āā} = Σ_μ g_{μμ} (∂xᵘ/∂x̄ᵃ)²` — no
cross terms. The names of the coordinates are irrelevant; only the map matters.

## Worked example
Schwarzschild (Hobson 14.47), letters permuted, with `t=t̄²r̄, r=r̄cosθ̄+2m,
θ=sin⁻¹(r̄θ̄), φ=cos(φ̄t̄)`. The coefficient of `dr̄²` is
`(1−2m/cos(φ̄t̄))·θ̄²/(1−r̄²θ̄²) − t̄⁴cos²(φ̄t̄) − cos²(φ̄t̄)sin²(t̄²r̄)cos²θ̄`.
Verified with SymPy — `examples/schwarzschild_transform.py`.

## Explain (altitudes)
- **expert** — the pullback `ḡ = Jᵀ g J`, `Jᵘ_a = ∂xᵘ/∂x̄ᵃ`; coordinate-covariance
  of GR — the geometry is unchanged, only its components rotate by the Jacobian.
- **working** — write each old coordinate as a function of the new ones,
  differentiate to get the Jacobian column, and (diagonal metric) sum each
  `g_{μμ}` times that partial squared.
- **plain** — rewrite every old letter in the new ones, see how fast each changes
  as you step in the new direction, then add up those stretches — squared —
  weighted by the metric.

## LaTeX
rule: \bar g_{ab}=\frac{\partial x^\mu}{\partial\bar x^a}\frac{\partial x^\nu}{\partial\bar x^b}\,g_{\mu\nu}\ \Rightarrow\ \bar g_{\bar a\bar a}=\sum_\mu g_{\mu\mu}\Big(\frac{\partial x^\mu}{\partial\bar x^a}\Big)^2
example: \bar g_{\bar r\bar r}=\Big(1-\tfrac{2m}{\cos(\bar\phi\bar t)}\Big)\tfrac{\bar\theta^{2}}{1-\bar r^{2}\bar\theta^{2}}-\bar t^{4}\cos^{2}(\bar\phi\bar t)-\cos^{2}(\bar\phi\bar t)\sin^{2}(\bar t^{2}\bar r)\cos^{2}\bar\theta

## References
- Hobson, Efstathiou & Lasenby, *General Relativity: An Introduction for Physicists*,
  §14 (Schwarzschild), eq. 14.47.
- Any GR / differential-geometry text — the tensor transformation law.
- Library: SymPy (Jacobian + substitution).

## Links
[[sym-antisym-contraction]] · [[laplacian-from-div-grad]] · [[epsilon-delta-identity]]
