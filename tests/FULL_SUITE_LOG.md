# Full test-suite run log

Every run of the WHOLE suite (all markers, incl. slow) is recorded here. Iteration may
use targeted subsets, but the full suite is run + logged at each milestone so coverage
is never silently reduced. Most recent run is the bottom row.

| when | status | pytest summary | note |
|---|---|---|---|
| 2026-06-25 12:17 | PASS | 418 passed in 351.21s (0:05:51) | baseline: complete_square_sub + by_parts fixes; coverage=default, speed=explicit opt-in |
| 2026-06-25 12:41 | PASS | 420 passed in 188.75s (0:03:08) | perf: DIRECT guard skips complete-square domain (no 38s grind) + complete_square_sub simplify fix; paper gates 179s->11s, no coverage lost |
| 2026-06-25 13:14 | PASS | 437 passed, 1 xfailed in 175.22s (0:02:55) | whole-paper audit (2606.23785): +17 distribution/rigidity gates + 1 documented hole (Gamma-ratio asymptotic, xfail) |
| 2026-06-25 13:24 | PASS | 444 passed in 178.38s (0:02:58) | built gamma_ratio_asymptotic (full DoD) — closes the Gamma-ratio asymptotic hole via loggamma Stirling route; 19 methods, DLMF-5.11.13 gated, paper mean/variance/reciprocal now derived |
| 2026-06-25 15:55 | PASS | 452 passed in 168.31s (0:02:48) | paper L2 (2606.24008, BRST higher-spin): built oscillator_commutator (full DoD) — opens operator-algebra core, derives Jordan-Schwinger gl(k) + su(1,1); 20 methods; BRST/Verma gaps rounded up |
| 2026-06-25 16:18 | PASS | 454 passed in 173.30s (0:02:53) | triage of 16 arXiv papers + built dilogarithm method (full DoD, DLMF 25.12.4 gated) — opens special-function dilog track for the batch; 21 methods, broad-domain |
| 2026-06-25 16:25 | PASS | 456 passed in 184.59s (0:03:04) | built wigner_surmise method (full DoD) — formalizes RMT level-statistics, derives GOE/GUE/GSE constants by moment-matching; opens probability/RMT track (unlocks 2606.24490); 22 methods |
| 2026-06-25 16:41 | PASS | 458 passed in 172.46s (0:02:52) | built casimir method (full DoD) — su(2) J²=j(j+1) by highest-weight/ladder via sympy spin; opens representation-theory track (same arg -> conformal Δ(Δ-d) for 2606.24382/24285); 23 methods |
| 2026-06-25 16:49 | PASS | 460 passed in 177.34s (0:02:57) | built confluent_0F1 method (full DoD) — recognizes 0F1(;nu+1;-z^2/4)=Bessel J_nu via hyperexpand, DLMF 10.16.9 gated (de-Sitter #7); 24 methods, 9 domain tracks |
| 2026-06-25 17:12 | PASS | 462 passed in 179.91s (0:02:59) | built sturm_liouville method (full DoD) — Dirichlet boundary eigenproblem -y''=λy on [0,L] -> λ_n=(nπ/L)² via dsolve+BCs+sine-zeros; opens PDE track (#8); 25 methods, 9 domains |
| 2026-06-25 18:09 | PASS | 469 passed in 186.33s (0:03:06) | DERIVED paper #6 (2606.24442 canonical-quant): characteristic eq, frequencies, perturbative series ω(1-λω+2λ²ω²), unequal-time commutators (1+2 mode) via oscillator_commutator; gaps rounded up (Dirac brackets, Legendre) |
| 2026-06-25 18:19 | PASS | 474 passed in 183.37s (0:03:03) | DERIVED paper #4 (2606.24497 Kashaev): Li2 special values, Rogers L-reflection π²/3, saddle polynomial solve, figure-eight HYPERBOLIC VOLUME 1.0149416 from dilog action; saddle-cond(24) flagged (transcription, rule 8), q-series/A-poly out of scope |
| 2026-06-26 09:36 | PASS | 478 passed in 179.74s (0:02:59) | q-series engine: built q_pochhammer (log(a;q)_inf Lambert series via geometric resummation, DLMF 17.2 + numeric oracle) + bessel_hankel (Gaussian Hankel transform e^{-a²/4p}/2p, DLMF 10.22); 27 methods, opens q-series + Bessel/Hankel |
| 2026-06-26 09:53 | PASS | 483 passed in 188.17s (0:03:08) | (1) wired step-by-step guides into all methods (STEP_GUIDES + enforced test) + METHOD_STEP_SOURCES.md; (2) built airy_asymptotic (WKB on Airy ODE -> e^{-2/3 x^3/2}/(2sqrt(pi)x^1/4), DLMF 9.7.5, numeric oracle); 28 methods |
| 2026-06-26 10:11 | PASS | 484 passed in 183.51s (0:03:03) | promoted euler_maclaurin recognition-only -> EXECUTABLE: harmonic number H_n ~ ln n+gamma+1/(2n)-1/(12n^2)+1/(120n^4) via integral+endpoint+Bernoulli-derivative corrections (sympy), DLMF 2.10 + numeric oracle; 25 executable / 3 recognition-only |
| 2026-06-26 10:19 | PASS | 486 passed in 180.86s (0:03:00) | build #2: conformal_casimir C2=Delta(Delta-d) via embedding null-cone Laplacian (genuine differentiation, d from (d+2)-dim sum), Simmons-Duffin TASI gated; non-compact analogue of su(2) J^2; serves de-Sitter #7 + celestial #9; 29 methods |
| 2026-06-26 10:52 | PASS | 492 passed in 173.82s (0:02:53) | ultracode: built #2/#3/#4 in parallel (worktree-free, agents self-tested, I re-verified) — conformal_block (SL(2) Casimir eigenvalue h(h-1), Dolan-Osborn), jacobi_trudi (Schur s_lambda=det(h_{l_i-i+j}), Macdonald), komar_mass (Schwarzschild Komar mass=M via curvature engine, Wald/Poisson); 32 methods, all DoD+step-guides |
