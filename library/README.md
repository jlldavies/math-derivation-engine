# Pattern library — the recognizer wiki

The "massive world of mathematical knowledge", captured as a navigable wiki: one
page per recognizable **pattern**. The proposer matches a problem against these to
recognize *which pattern applies and why* (see [PLAN.md](../PLAN.md)). Each page
is also a **golden test** — its worked example has a known result.

**Karpathy-style (GO4 K12):** curated, cross-linked pages — not opaque vector
chunks — because *choosing the right pattern is the hard part*. The retrieval
architecture (straight lookup vs RAG vs GraphRAG — GO4 K1–K13) is **deliberately
not chosen yet**: we capture enough pages to see the corpus shape first (GO4 K13),
then decide. The in-code `src/integral_explainer/methods.py` registry is the
engine-facing *subset*; these pages are the richer source.

## Page schema

```
---
id: <kebab-id>
name: <short name>
domain: tensor | calculus | special-function | pde | linear-algebra
regime: <methods.py regime>          # links to the in-code registry
status: seed | drafted | verified
---
## Applies when (recognition signature)   — the surface tells that trigger it
## The rule                                — the transform/identity, stated precisely
## Worked example                          — a concrete instance, known result (a golden test)
## Explain (altitudes)                     — expert / working / plain
## References                              — authoritative + library + worked-example sources
## Links                                   — [[other-pattern]] cross-links
```

## Index

**110 pages across 10 domains** — base (A-level) → advanced. A problem is one query from its method; the qualification trees bottom out on the foundational pages.


### algebra (4)
[[binomial-theorem]] · [[completing-the-square]] · [[polynomial-division]] · [[quadratic-formula]]

### trigonometry (29)
[[chebyshev-polynomials]] · [[complex-trig-identities]] · [[compound-angle-formulae]] · [[cosine-rule]] · [[de-moivre-theorem]] · [[double-angle-formulae]] · [[euler-formula]] · [[gudermannian]] · [[half-angle-formulae]] · [[harmonic-form]] · [[hyperbolic-functions]] · [[inverse-hyperbolic-functions]] · [[inverse-trig-functions]] · [[law-of-tangents]] · [[product-to-sum]] · [[pythagorean-identity]] · [[radians-arc-sector]] · [[reciprocal-trig-functions]] · [[roots-of-unity]] · [[sine-rule]] · [[small-angle-approximation]] · [[solving-trig-equations]] · [[spherical-trigonometry]] · [[sum-to-product]] · [[trig-graph-transformations]] · [[trig-orthogonality]] · [[trig-power-series]] · [[trig-reduction-formulae]] · [[weierstrass-substitution]]

### calculus (17)
[[arithmetic-geometric-series]] · [[chain-rule]] · [[contour-residues]] · [[differentiation-under-integral]] · [[exponential-function]] · [[gaussian-integral]] · [[implicit-differentiation]] · [[improper-integrals]] · [[integration-by-parts]] · [[partial-fractions]] · [[power-rule]] · [[product-rule]] · [[quotient-rule]] · [[standard-integrals]] · [[taylor-series]] · [[trig-substitution]] · [[u-substitution]]

### tensor (13)
[[christoffel-symbols]] · [[covariant-derivative]] · [[cross-product]] · [[div-of-curl]] · [[dot-product]] · [[epsilon-delta-identity]] · [[geodesic-equation]] · [[laplacian-from-div-grad]] · [[metric-transformation-law]] · [[raising-lowering-indices]] · [[ricci-tensor-scalar]] · [[riemann-curvature]] · [[sym-antisym-contraction]]

### special-function (14)
[[bessel-function]] · [[beta-function]] · [[digamma-polygamma]] · [[error-function]] · [[fresnel-integral]] · [[gamma-function]] · [[gamma-reflection]] · [[hypergeometric-2f1]] · [[incomplete-gamma]] · [[meijer-g-reduction]] · [[mellin-barnes]] · [[polylogarithm]] · [[tricomi-u-reduction]] · [[watsons-lemma]]

### asymptotics (6)
[[abel-plana]] · [[borel-summation]] · [[euler-maclaurin]] · [[method-of-stationary-phase]] · [[saddle-point-method]] · [[zeta-regularization]]

### regularization (4)
[[dimensional-regularization]] · [[feynman-parametrization]] · [[hadamard-finite-part]] · [[schwinger-parametrization]]

### transform (6)
[[convolution-theorem]] · [[fourier-transform]] · [[inverse-laplace-bromwich]] · [[laplace-transform]] · [[mellin-transform]] · [[z-transform]]

### pde (8)
[[fourier-series]] · [[greens-function]] · [[heat-equation]] · [[laplace-equation]] · [[method-of-characteristics]] · [[separation-of-variables]] · [[sturm-liouville]] · [[wave-equation]]

### linear-algebra (9)
[[cayley-hamilton]] · [[determinant-expansion]] · [[eigendecomposition]] · [[gram-schmidt]] · [[lu-decomposition]] · [[matrix-inverse]] · [[qr-decomposition]] · [[singular-value-decomposition]] · [[spectral-theorem]]

## Sourcing channels
- **Authoritative** — DLMF, Gradshteyn–Ryzhik, textbook identity tables (citable).
- **Library** — SymPy/SciPy reductions we wrap and explain (code-grounded).
- **Worked examples** — arXiv papers / problem sets shown in real use (e.g. Blitz).
