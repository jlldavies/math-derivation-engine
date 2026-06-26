# Physics-paper test corpus

Cutting-edge papers to derive/check the maths against — gauging engine utility AND surfacing
missing techniques. Rule: the **engine** does the maths; we only verify and gate (rule 10 — the
paper is the published source). Work slowly, section by section, full Definition of Done for any
new capability.

| # | arXiv / file | title | status |
|---|---|---|---|
| 1 | [2606.24859v1](https://arxiv.org/html/2606.24859v1) | — | to examine |
| 2 | [2606.24713v1](https://arxiv.org/html/2606.24713v1) | — | to examine |
| 3 | [2606.24577v2](https://arxiv.org/html/2606.24577v2) | — | to examine |
| 4 | [2606.24497v1](https://arxiv.org/html/2606.24497v1) | — | to examine |
| 5 | [2606.24490v1](https://arxiv.org/html/2606.24490v1) | — | to examine |
| 6 | [2606.24442v1](https://arxiv.org/html/2606.24442v1) | — | to examine |
| 7 | [2606.24382v1](https://arxiv.org/html/2606.24382v1) | — | to examine |
| 8 | [2606.24328v2](https://arxiv.org/html/2606.24328v2) | — | to examine |
| 9 | [2606.24285v1](https://arxiv.org/html/2606.24285v1) | — | to examine |
| 10 | [2606.24272v1](https://arxiv.org/html/2606.24272v1) | — | to examine |
| 11 | [2606.24018v1](https://arxiv.org/html/2606.24018v1) | — | to examine |
| 12 | [2606.23893v1](https://arxiv.org/html/2606.23893v1) | — | to examine |
| 13 | [2606.23779v1](https://arxiv.org/html/2606.23779v1) | — | to examine |
| 14 | [2606.23776v1](https://arxiv.org/html/2606.23776v1) | — | to examine |
| 15 | [2606.24886v1](https://arxiv.org/html/2606.24886v1) | — | to examine |
| 16 | [2602.06905v2](https://arxiv.org/html/2602.06905v2) | — | to examine |
| L1 | `local/arXiv-2606.23785v1/` | **Controlled Chaos in 4D SCFTs** (RMT / spin chains) | **complete — hole closed** |
| L2 | `local/arXiv-2606.24008v1/` | **Lagrangian formulations for mixed-antisymmetric HS fields** (BRST) | **complete — core derived, gaps rounded up** |

## CORPUS GAP MAP / BUILD QUEUE (ultracode scan of 13 papers, 2026-06-25)
Ranked by how many papers need each missing capability. (#1 tensor-bootstrap 2606.24859 not scanned —
agent rate-limited; from triage it needs tensor-contraction + path-integral/Schwinger-Dyson; melon
√(1+8gn)/(4gn) algebraic.) **No remaining paper is FULLY green** — each has load-bearing pieces in gaps.

1. **[5 papers] Special-function / integral-transform & asymptotics engine** — Bessel-product &
   Hankel/Weber-Schafheitlin integrals, double-sine / quantum-dilog, infinite q-Pochhammer products,
   Airy resummation, Euler-Maclaurin summation, Fredholm/Tracy-Widom determinants. Papers: 23779,
   23893, 24018, 24490, 24285. **BUILD FIRST — IN PROGRESS:** ✅ `q_pochhammer` (log(a;q)_∞ Lambert
   series, DLMF 17.2 + numeric oracle — the q-series kernel), ✅ `bessel_hankel` (Gaussian Hankel
   transform e^{-a²/4p}/2p, DLMF 10.22), and ✅ `airy` (WKB on y''=xy → e^{-2/3 x^{3/2}}/(2√π x^{1/4}),
   DLMF 9.7.5 + numeric oracle — large-N ABJM/Airy #12), and ✅ `euler_maclaurin` PROMOTED
   recognition-only → EXECUTABLE (H_n ~ ln n+γ+1/(2n)−1/(12n²)+1/(120n⁴) via integral+endpoint+
   Bernoulli-derivative corrections, DLMF 2.10 + numeric oracle) built. **25 executable / 3 recognition-
   only.** Remaining #1: double-sine / quantum-dilog, Fredholm/Tracy-Widom determinants (both exotic).
   ALSO: every method now GROUNDED in a published step-by-step guide (`methods.STEP_GUIDES`, enforced by
   `tests/test_step_guides.py`; map in `METHOD_STEP_SOURCES.md`).
2. **[3] Conformal Casimir Δ(Δ−d) + conformal-block hypergeometric ODE + shadow/partial-wave (SL(2,C))**
   — CFT/representation theory. Papers: 24382, 24285, 24328. **IN PROGRESS:** ✅ `conformal_casimir`
   C₂=Δ(Δ−d) built (full DoD, 29th method) — embedding null-cone Laplacian, genuine differentiation,
   d emerges from the (d+2)-dim sum; Simmons-Duffin TASI gated; non-compact analogue of su(2) J²=j(j+1).
   Also ✅ `conformal_block` (SL(2) block k_h=z^h 2F1(h,h;2h;z) solves the Casimir ODE, eigenvalue
   h(h-1); Dolan-Osborn/Simmons-Duffin) — built via ultracode workflow. Remaining #2: conformal-block
   hypergeometric ODE closed forms, shadow/partial-wave transforms.
3. **[2] Symmetric-function / Jack-polynomial + S_n character algebra** — 24272, 24490. **STARTED:**
   ✅ `jacobi_trudi` (Schur s_λ=det(h_{λ_i-i+j}); s_(2,1) gated vs Wikipedia; Macdonald I.3) — the
   determinantal backbone under Jack/Macdonald. Remaining: Jack P_λ^{(α)}, S_n characters.
4. **[2] GR conserved-charge engines** — 2602.06905, 24577. **STARTED:** ✅ `komar_mass` (Schwarzschild
   Komar mass = M via the curvature engine + Killing-vector surface integral; Wald ch.11 / Poisson 4.3.3).
   Remaining: Wald entropy (∂L/∂R_abcd → A/4), Komar angular momentum, BMS charges.

**ULTRACODE WORKFLOW (2026-06-26):** built #2/#3/#4 in parallel — 3 agents each researched sources,
built a genuine sympy computation + complete leveled Derivation in standalone scripts (no git worktree
since local-only repo), self-tested; I integrated + re-verified (coverage NONE, all DoD+validate). 32
methods, 29 executable.
5. **[1 each] bespoke single-paper** — bosonization/Luttinger-RG (24713), Berezin-Toeplitz/index theory
   +characteristic classes (24577), Berends-Giele recursion (23776), Tomita-Takesaki modular (23779),
   BES integrability kernel (24018), GKZ/KZ systems (24285), SL-perturbation/RT surfaces (24328),
   K-matrix lattice/Smith-normal-form (24713), harmonic analysis on quotients+Bayesian (24886).
   **De-prioritise** (low return until the recurring modules exist).

**CROSS-CUTTING SUBSTRATE (the "knot theory" analogue, James asked to surface):** **q-series /
Pochhammer-product machinery** recurs under #1 AND #3 (23893, 24272, 24490) — it underlies localization
partition functions, Jack-polynomial structure constants, Jacobi dressing factors AND knot invariants.
Build a shared **q-series / orthogonal-polynomial kernel** as a foundational dependency, not per-paper.
Knot theory *itself* (A-polynomials/Jones/HOMFLY) is only Kashaev #4 → a single-paper, low-priority full
domain; its derivable slice was the dilogarithm volume, already done.

**OUT OF SCOPE (numerics-dominated):** 24886 cosmic-topology (Bayesian), 24713 SMG (DMRG/tensor-network).

## Triage (2026-06-25) — domain routing for the 16 web papers
The engine is **broad-domain** (James: NOT just integrals — GR/tensors, operator algebra, special
functions, RMT all count). Routing by maths domain + engine fit:
- **GREEN (derives most now):** 2606.24497 Kashaev (dilog/stationary-phase), 2606.24442 canonical-quant
  (operator algebra/eigenvalues), 2606.24018 large-charge (zeta/log/cosh asymptotics), 2606.24490
  Multi-dim-Chaos-II (RMT β-ensemble), 2602.06905 rotating-BH (GR/curvature).
- **PARTIAL (one new method):** 2606.24382 de-Sitter (Casimir+₀F₁), 2606.24285 celestial (Mellin/Beta/
  Casimir), 2606.23893 OSV (Airy/double-sine), 2606.24328 p-wave (curvature✓+Sturm-Liouville PDE),
  2606.24859 tensor-bootstrap, 2606.24713 SMG-bosonization, 2606.23779 excitability, 2606.23776 gluon-AdS.
- **GAP (new domain track):** 2606.24577 IIB (vielbein→char-classes), 2606.24272 equivariant (Jack
  polynomials), 2606.24886 cosmic-topology (Bayesian stats).
- **BUILDS this session (full DoD):** `dilogarithm` (Euler reflection, DLMF 25.12.4) → special-fn track;
  `wigner_surmise` (GOE/GUE/GSE constants by moment-matching, Wikipedia/2606.23785) → RMT/probability;
  `casimir` (su(2) J²=j(j+1) by highest-weight/ladder via sympy spin, Wikipedia) → representation-theory
  (same arg → conformal Δ(Δ-d) for #7/#9); `confluent_0F1` (₀F₁=Bessel J_ν via hyperexpand, DLMF
  10.16.9) → confluent-hypergeometric (#7); `sturm_liouville` (-y''=λy on [0,L] → λ_n=(nπ/L)² via
  dsolve+BCs+sine-zeros, Wikipedia) → **PDE track** (p-wave #8). **25 methods, 9 domain tracks.** Next:
  conformal Casimir Δ(Δ-d), Airy/double-sine (#12); then derive the GREEN papers in full.

### #4 — Kashaev limits of quantum A-polynomials (2606.24497) — DERIVED (2026-06-25)
GREEN, exercises the dilogarithm/special-fn track → 5 gates in `tests/test_paper_kashaev.py`:
- **(19) Li₂ special values** π²/6, −π²/12, π²/12−½ln²2; **(21) Rogers L-function reflection**
  L(x)+L(1/x)=π²/3 (real part, branch-robust); **(27) figure-eight saddle polynomial** g²+(2+t²+t⁻²
  −t⁴−t⁻⁴)g+1=0 solved, roots a reciprocal pair (Vieta product=1).
- **HEADLINE (28/29): the engine computes the figure-eight knot's HYPERBOLIC VOLUME = 1.0149416064096537**
  (13-digit match to the known value) from the dilogarithm action ½[Li₂(1/z*)−Li₂(z*)] at z*=e^{iπ/3} —
  a real topological invariant out of the dilog track.
- **RULE-8 FLAG / GAPS:** saddle condition (24) NOT reproduced — ∂_z of the AI-transcribed action (23)
  gives z=−1, not (24); likely the HTML-scraped action is imprecise (needs the paper PDF), flagged not
  claimed. q-series/Pochhammer (18), A-polynomials + HOMFLY/Jones knot invariants — out of engine scope.

### #6 — Canonical Quantization, higher-derivative (2606.24442) — DERIVED (2026-06-25)
First GREEN web paper derived end-to-end (proving the widening on real maths). The ENGINE derives the
spectral + operator-algebra core → 7 gates in `tests/test_paper_canonical_quant.py`:
- **(3.31) characteristic eq** λ²f⁴−(1+2λω)f²+ω²=0 — substitute x=e^{ift} into the 4th-order EOM.
- **(3.32-33) frequencies** f₁,₂=(√(1+4λω)∓1)/(2λ) — algebraic solve of the quadratic in f².
- **(3.47-48) perturbative** f₁→ω(1−λω+2λ²ω²) and **(3.49)** prefactor 1/√(1+4λω)→1−2λω+6λ²ω² —
  series-expansion track.
- **(3.22/3.43) unequal-time commutators** [x(t₁),x(t₂)]=−i sin(ω Δt) (1-mode) and the 2-mode
  −i/√(1+4λω)[sin f₁Δt+sin f₂Δt] — **oscillator_commutator** (the new operator-algebra track), via
  rewrite(sin). Real cross-track demonstration: algebra + series + operator commutators in one paper.
- **GAPS (test_ROUNDUP_remaining_gaps):** Dirac-bracket constrained quantization (3.5-3.8) — needs a
  Poisson-bracket + constraint-matrix-inverse method; Legendre transform L→H — sympy-doable, no
  dedicated method. Both next-build candidates if we want the constrained-Hamiltonian track.

## Findings log

### L1 — Controlled Chaos in 4D SCFTs (2606.23785)
- **§2 Wigner surmise** (eq. 338–343), β = 1,2,4. Engine reproduced all 6 defining integrals:
  ∫₀^∞ ρ_β ds = 1 (normalized) and ∫₀^∞ s ρ_β ds = 1 (unit mean). **Utility: verifies the RMT
  level-spacing normalization constants.** No new technique needed (Gaussian moments). → persisted
  as a paper gate in `tests/test_paper_gates.py`.
- **§2 GE r-statistics** (eq. 346) normalization N_β = ∫₀^∞ (1+x)^β/(1+x+x²)^(1+3β/2) dx:
  - **β=2, β=4: engine reproduces** (16√3π/243; −2/45+112√3π/2187), matched to numeric ground truth.
  - **β=1: GENUINE GAP** — ∫₀^∞ (1+x)/(1+x+x²)^(5/2) (half-integer-power rational over [0,∞));
    numeric = 14/27. Missing technique: **Euler / trig substitution** (complete the square →
    (u²+a²)^(5/2)). → next build target via full Definition of Done.
- **BUG FOUND + FIXED (the real payoff):** `_by_parts` mishandled the boundary term of a
  *definite* integral — returned `u·v − ∫v du` with `u·v` un-evaluated instead of `[u·v]ₐᵇ`,
  giving a WRONG −∞ for the β=2 r-statistics. Fixed (boundary term via limit, skip if divergent);
  this also unblocked β=2/β=4. Regression-gated in `tests/test_paper_gates.py`.
- Gated: `tests/test_paper_gates.py` (now `-m slow`). Engine did all maths; no compensating.
- **NEW METHOD built (full DoD): `complete_square_sub`** — completes the square (Euler sub
  u=x+b/2a) for a definite ∫ of P(x)/(irreducible quadratic)^(p/2); closes the β=1 gap (→ 14/27).
  Wired + externally gated (the paper integral) + validated leveled explanation (4/6/9). **18/18
  methods complete.** Also: a 2nd by_parts fix (`_easy_dv` guard — don't misfire expensively on
  radical-power quadratics) + the heavy gates marked `slow` to keep the default suite ~10s.
- **Search-cost FIXED:** the ~38s was DIRECT (default sp.integrate) GRINDING on the complete-square
  domain (meijer_g fails it in 0.0s). A tier-split escalation broke 4 table gates (uglier meijer_g
  forms); the clean fix = a targeted `_direct` guard skipping that domain (defer to the rewrite) +
  simplify the rewrite's output. csquare gate 38s→2s, paper gates 179s→11s, zero coverage lost.
  Perf regression test `tests/test_perf.py`.

### L1 — WHOLE-PAPER audit complete (2026-06-25)
Inventoried all 65 maths objects; the **engine reproduces essentially every closed form in the
paper** — 17 new gates in `tests/test_paper_distributions.py`:
- **§2 normalizations:** Poisson ρ & r-stat, Wigner semicircle — all = 1 (engine search).
- **App. B chi / generalized-gamma:** chi PDF norm + moment formula μ_n=2^{n/2}Γ((k+n)/2)/Γ(k/2)
  (symbolic k,n), χ_3 mean/2nd-moment, power-of-chi PDF norm + mean + variance + reciprocal
  (k>p), generalized-gamma norm (symbolic a,d,c), and the **χ_k^p ↔ GenGamma(2^{p/2},k/p,2/p)
  PDF identity** — all exact. **Utility: verifies every distribution constant the paper relies on.**
- **App. C spectral rigidity:** the engine REPRODUCES the Dyson–Mehta least-squares derivation
  (minimize ∫(N−A−Bx)² → A*=J₀/E, B*=12J₁/E³ → Δ₃ = K/E − J₀²/E² − 12J₁²/E⁴, exact), and the
  universal GOE/GUE/GSE asymptotic constants (−0.0687, 1.1651, 3.0919). Real derivational utility,
  not just an integral.
- **THE ONE HOLE — NOW CLOSED (full DoD, 2026-06-25):** large-k **asymptotic SERIES of a ratio of
  Gamma functions** (μ=k^{p/2}+…, σ²=½p²k^{p−1}+…, ⟨1/Z⟩=k^{−p/2}+…). sympy's `gamma.aseries` raises
  PoleError, but **`loggamma.aseries` (the Stirling series) works** — so the new method
  **`gamma_ratio_asymptotic`** (special_methods) takes logs, expands each loggamma, subtracts,
  exponentiates, re-expands in 1/z. Reproduces **DLMF 5.11.13** (`Γ(z+a)/Γ(z+b) ~ z^{a−b}[1+(a−b)
  (a+b−1)/(2z)]`) — externally gated — and now DERIVES the paper's μ ~ k^{p/2}, σ² ~ ½p²k^{p−1} (the
  cancellation the limit couldn't do — verified p=2,3,5), ⟨1/Z⟩ ~ k^{−p/2}. CAPABILITY method, wired
  + gated + leveled Derivation (expert 4 / working 7 / plain 12). **19 methods, all complete.**

**FRAMING (James, 2026-06-25):** the point is NOT accuracy-checking the papers — it's whether our
tool could have **DERIVED** each result in the same format, **laying out enough steps that a person
gains confidence** (accuracy only matters where our derivation diverges). So every new method's
payload is the leveled, step-by-step Derivation, not the pass/fail.

### L2 — Lagrangian formulations for mixed-antisymmetric HS fields (2606.24008)
**A DIFFERENT DOMAIN — operator superalgebra, not integrals.** Inventoried 39 objects: ~all are
(super)commutator/structure-constant relations (Cat A), BRST nilpotency Q²=0 (Cat B), oscillator/
Verma realizations (Cat C), counting formulas (Cat D); essentially NO integrals/special functions.
The engine had **no entry point** for operator algebra — so it could derive ~none of it at first.
- **Scoped the gap → BUILDABLE:** sympy's `quantum.boson` + `normal_ordered_form` does canonical
  commutator algebra. **Built `oscillator_commutator` (full DoD):** computes [A,B] from [a,a†]=1 by
  normal ordering (nothing written in). Externally gated on the **su(1,1)** bosonic realization
  (closes: [K0,K±]=±K±, [K+,K-]=-2K0) and **DERIVES the paper's A.5 Jordan-Schwinger gl(k)** relation
  [t_i^j,t_p^q]=δ_p^j t_i^q − δ_i^q t_p^j (k=2,3 verified). Leveled Derivation (4/6/9). **20 methods.**
  A real bug surfaced en route: cross-mode brackets [a_1†,a_3] need `independent=True` to vanish.
- **GAPS ROUNDED UP (test_paper_hs_algebra.py::test_ROUNDUP_remaining_gaps)** — next operator-algebra
  build targets, the bulk of the paper: (1) **BRST nilpotency** Q²=2ΣB^iσ^i(G) — needs ghost
  oscillators + assembling Q from structure constants + Jacobi bookkeeping; (2) **Verma-module
  realizations** (l',t',g'_0 in b/d oscillators) — many-mode, very long; (3) **general-k so(k,k)
  with the Lorentz-index trace** (a_{iμ}a^{jμ} → d-dependent t_i^i terms); (4) **Lagrangian actions**
  ⟨χ|KQ|χ⟩ — formal, not a closed-form eval. **Verdict: engine opened the verifiable CORE (Cat A
  commutators + Cat D counts); the BRST/Verma machinery is a sizable operator-algebra sub-engine
  still to build.** Good signal for batching: integrals/special-fn/asymptotics papers fit now;
  pure BRST/representation-theory papers need the operator-algebra track first.
