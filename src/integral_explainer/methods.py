"""The method registry: named integration/regularization patterns.

This is the pedagogical payload. Each Method carries a human-readable
explanation, an applicability hint (what shape of integrand it suits), and
references. The proposer ranks these for a given integral; the trace records
which fired.

The elementary methods overlap SymPy's manualintegrate rule set deliberately —
the value here is (a) extending into the divergent/regularization regime that
no solver exposes, and (b) attaching explanation + applicability to each.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Method:
    key: str
    name: str
    applies_when: str       # human description of the recognizable pattern
    explanation: str        # what the method does and why it works
    regime: str = "elementary"   # "elementary" | "special-function" | "divergent"
    references: tuple[str, ...] = field(default_factory=tuple)


METHODS: dict[str, Method] = {m.key: m for m in [
    Method(
        key="parts",
        name="Integration by parts",
        applies_when="product of a polynomial/log/inverse-trig with an easily integrable factor",
        explanation="∫u dv = uv − ∫v du; choose u to simplify on differentiation (LIATE).",
        regime="elementary",
    ),
    Method(
        key="u_sub",
        name="u-substitution",
        applies_when="the integrand contains an inner function and (a multiple of) its derivative",
        explanation="Substitute u=g(x), du=g'(x)dx to collapse the composite.",
        regime="elementary",
    ),
    Method(
        key="partial_fractions",
        name="Partial fractions",
        applies_when="rational integrand; denominator factorable",
        explanation="Decompose into simple/quadratic fractions integrable term-by-term.",
        regime="elementary",
    ),
    Method(
        key="contour",
        name="Contour integration / residues",
        applies_when="rational or trig-rational over (-inf,inf) or [0,2pi]; poles off the contour",
        explanation="Close the contour and sum 2πi·residues; trig integrals via z=e^{iθ}.",
        regime="special-function",
        references=("Ahlfors, Complex Analysis",),
    ),
    Method(
        key="feynman_parameter",
        name="Differentiation under the integral sign (Feynman trick)",
        applies_when="a parameter can be introduced so that ∂/∂a gives a simpler integral",
        explanation="Introduce a parameter, differentiate, integrate the easier form, integrate back in a.",
        regime="special-function",
    ),
    Method(
        key="mellin",
        name="Mellin transform / Mellin–Barnes",
        applies_when="products/powers with multiplicative structure; convolution-type integrals",
        explanation="Represent factors by Mellin–Barnes contour integrals; resolve singularities in the parameter.",
        regime="special-function",
        references=("Paris & Kaminski, Asymptotics and Mellin-Barnes Integrals",),
    ),
    Method(
        key="abel_plana",
        name="Abel–Plana formula",
        applies_when="a lattice sum to be turned into an integral plus a controlled remainder",
        explanation="Σf(n) = ∫₀^∞ f(x)dx + boundary + i∫ (f(iy)−f(−iy))/(e^{2πy}−1) dy; isolates the divergence.",
        regime="divergent",
    ),
    Method(
        key="euler_maclaurin",
        name="Euler–Maclaurin summation",
        applies_when="sum vs integral comparison; extracting the divergent part of a lattice sum",
        explanation="Σf = ∫f + (boundary terms) + Σ Bernoulli-number derivative corrections.",
        regime="divergent",
    ),
    Method(
        key="zeta_reg",
        name="Zeta-function regularization",
        applies_when="formally divergent sum/integral expressible as an analytic continuation of a zeta-type function",
        explanation="Define the divergent object by the analytic continuation of Σ n^{-s} (or spectral ζ) to the needed s.",
        regime="divergent",
        references=("Elizalde, Zeta Regularization Techniques",),
    ),
    Method(
        key="analytic_continuation",
        name="Analytic continuation in a regulator",
        applies_when="integral convergent for some parameter range, needed outside it",
        explanation="Evaluate where convergent, continue analytically to the target parameter; keep the finite part.",
        regime="divergent",
        references=("Felder & Kazhdan, Regularization of divergent integrals, arXiv:1611.05057",),
    ),
    Method(
        key="dim_reg",
        name="Dimensional regularization",
        applies_when="rotationally-invariant momentum-space integral with power-counting divergence",
        explanation="Compute in d=D−2ε dimensions; isolate 1/ε poles; the finite part is the regularized value.",
        regime="divergent",
        references=("'t Hooft & Veltman (1972)",),
    ),
    # --- special-function / divergent-regime methods ---
    Method(
        key="meijer_g",
        name="Meijer-G / hypergeometric reduction",
        applies_when="parametric integral of products of powers and exponentials over (0,∞); "
                     "e.g. ∫ x^(s-1)(x+c)^(-t) e^(i b x) dx",
        explanation="Recognize the integral as a Mellin–Barnes / Meijer-G representation, giving an "
                    "exact named closed form. The closed form is the easy part; its series/asymptotic "
                    "expansion in the parameters is where the work is (see asymptotic_expansion).",
        regime="special-function",
        references=("Blitz & Majid, arXiv:2405.18397",
                    "Beals & Szmigielski, Meijer G-Functions: A Gentle Introduction"),
    ),
    Method(
        key="asymptotic_expansion",
        name="Asymptotic / series expansion in a regulator",
        applies_when="a special-function closed form (Meijer-G, hypergeometric, incomplete gamma) whose "
                     "leading and subleading behaviour is needed as a regulator → limit (ε→0 UV, ℒ→∞ IR)",
        explanation="Expand the special function asymptotically in the small/large parameter to isolate the "
                    "divergent leading term and the finite subleading coefficients. This is the step that "
                    "exposes the UV divergence and the renormalized finite part.",
        regime="divergent",
        references=("Paris & Kaminski, Asymptotics and Mellin-Barnes Integrals",),
    ),
    Method(
        key="sturm_liouville",
        name="Sturm-Liouville boundary eigenvalue problem (quantized spectrum)",
        applies_when="a 2nd-order eigenvalue ODE -y''+q(x)y = lambda w(x) y with boundary conditions, whose "
                     "discrete spectrum and eigenfunctions are wanted — e.g. a Schrodinger/order-parameter mode",
        explanation="Solve the ODE for its general solution, impose the boundary conditions, and read the "
                    "quantization off the resulting transcendental condition: for -y''=lambda y on [0,L] with "
                    "Dirichlet BCs, y(0)=0 kills the cosine and y(L)=0 forces sin(kL)=0, giving lambda_n=(n pi/L)^2, "
                    "y_n=sin(n pi x/L). The same procedure handles curved-background modes (arXiv:2606.24328).",
        regime="pde",
        references=("https://en.wikipedia.org/wiki/Sturm-Liouville_theory (Dirichlet spectrum)",
                    "arXiv:2606.24328 (Holographic p-wave superfluids), order-parameter eigenproblem"),
    ),
    Method(
        key="confluent_0F1",
        name="Confluent-hypergeometric limit 0F1 as a Bessel function",
        applies_when="a 0F1(;b;z) confluent-hypergeometric limit appears and should be recognized in closed "
                     "form — e.g. the lifted/bulk operators of dS/AdS written with a 0F1",
        explanation="The series 0F1(;nu+1;-z^2/4) is the Bessel series up to a power prefactor, so "
                    "J_nu(z)=(z/2)^nu/Gamma(nu+1) * 0F1(;nu+1;-z^2/4). The engine reduces it with hyperexpand "
                    "and returns J_nu — recognizing the named special function. Surfaced by arXiv:2606.24382.",
        regime="special-function",
        references=("DLMF 10.16.9 (https://dlmf.nist.gov/10.16.E9)",
                    "arXiv:2606.24382 (Exact and Finite de Sitter QFT from CFT)"),
    ),
    Method(
        key="conformal_casimir",
        name="Conformal Casimir C_2 = Delta(Delta-d) (embedding null cone)",
        applies_when="the quadratic Casimir of the conformal group SO(d+1,1) on a primary of dimension "
                     "Delta is needed — the mass-dimension relation, conformal blocks, de Sitter/CFT spectra",
        explanation="In embedding space a primary is a degree-(-Delta) homogeneous function on the null cone "
                    "X^2=0 in R^{d+1,1}; applying the SO(d+1,1) Laplacian -sum L_{AB}^2 (L_{AB}=X_A d_B-X_B d_A) "
                    "and reducing on the cone gives C_2 = Delta(Delta-d). The non-compact analogue of su(2)'s "
                    "J^2=j(j+1). Surfaced by arXiv:2606.24382 (de Sitter), 2606.24285 (celestial).",
        regime="representation-theory",
        references=("Simmons-Duffin, TASI Lectures on the Conformal Bootstrap (https://arxiv.org/abs/1602.07982)",
                    "arXiv:2606.24382 / 2606.24285 (conformal Casimir Delta(Delta-d))"),
    ),
    Method(
        key="casimir",
        name="Quadratic Casimir eigenvalue (highest-weight / ladder method)",
        applies_when="the quadratic Casimir eigenvalue of a Lie-algebra irrep is needed — e.g. su(2) "
                     "angular momentum J^2=j(j+1), or (same argument) the conformal C_2=Delta(Delta-d)",
        explanation="The Casimir commutes with every generator, so it is constant on an irrep; evaluate it "
                    "on the HIGHEST-WEIGHT state, where ladder operators annihilate. For su(2), rewrite "
                    "J^2=J_-J_+ + J_z^2 + hbar J_z and act on |j,j> (J_+|j,j>=0) to get j(j+1). The same "
                    "highest-weight argument gives the conformal Casimir Delta(Delta-d) used in 2606.24382/24285.",
        regime="representation-theory",
        references=("https://en.wikipedia.org/wiki/Angular_momentum_operator#Casimir (J^2=j(j+1))",
                    "arXiv:2606.24382, 2606.24285 (conformal Casimir C_2=Delta(Delta-d))"),
    ),
    Method(
        key="airy",
        name="Airy function large-argument asymptotic (WKB)",
        applies_when="the large-argument behaviour of the Airy function Ai(x) is needed — turning points, "
                     "large-N partition functions (ABJM/Airy), uniform asymptotics",
        explanation="Apply WKB to the Airy ODE y''=x y: with y=e^S, S''+(S')^2=x; the leading balance "
                    "(S')^2~x gives the exponent -2/3 x^{3/2}, and the next order gives the x^{-1/4} prefactor, "
                    "so Ai(x) ~ e^{-2/3 x^{3/2}}/(2 sqrt(pi) x^{1/4}). The overall constant is the connection "
                    "constant (numeric-oracle confirmed). Surfaced by arXiv:2606.23893 (large-N ABJM/Airy).",
        regime="special-function",
        references=("DLMF 9.7.5 (https://dlmf.nist.gov/9.7)",
                    "arXiv:2606.23893 (Towards OSV in AdS), large-N ABJM Airy partition function"),
    ),
    Method(
        key="bessel_hankel",
        name="Bessel-weighted radial (Hankel-type) integral",
        applies_when="a radial integral of a Bessel function over [0,inf) — Hankel transforms, AdS/"
                     "holographic radial modes, diffraction integrals — where oscillation defeats quadrature",
        explanation="Expand the Bessel function as its power series, integrate term-by-term against the "
                    "Gaussian/exponential weight (standard moments), and resum: e.g. the Hankel transform of "
                    "a Gaussian is a Gaussian, int_0^inf e^{-p t^2} J_0(a t) t dt = e^{-a^2/(4p)}/(2p); and "
                    "int_0^inf e^{-p t} J_0(a t) dt = 1/sqrt(p^2+a^2). Surfaced by arXiv:2606.23779.",
        regime="special-function",
        references=("DLMF 10.22 / Gradshteyn-Ryzhik 6.6 (Bessel integrals)",
                    "arXiv:2606.23779 (Excitability of Gaussian states), AdS radial-mode integrals"),
    ),
    Method(
        key="q_pochhammer",
        name="q-Pochhammer infinite product as a Lambert series",
        applies_when="an infinite q-product (a;q)_inf = prod(1 - a q^k) appears — q-series, localization "
                     "partition functions, Jacobi/Jack dressing factors, q-exponentials",
        explanation="Take the log of the product to turn it into a sum of logs; expand each log and resum "
                    "the geometric series sum_k q^{kn}=1/(1-q^n) to get the Lambert series "
                    "log(a;q)_inf = -sum_n a^n/(n(1-q^n)). The foundational q-series kernel underneath "
                    "knot invariants, localization and symmetric-function dressing factors. Surfaced by "
                    "arXiv:2606.24497 (Kashaev) eq.(18).",
        regime="q-series",
        references=("DLMF 17.2 / Euler (https://dlmf.nist.gov/17.2)",
                    "arXiv:2606.24497 (Kashaev limits), eq.(18)"),
    ),
    Method(
        key="wigner_surmise",
        name="Wigner surmise (RMT level-spacing law by moment-matching)",
        applies_when="the level-spacing or spacing-ratio distribution of a chaotic spectrum / random-matrix "
                     "ensemble (Dyson index beta=1,2,4) is needed in closed form",
        explanation="Take the level-repulsion ansatz rho_beta(s)=c1 s^beta e^{-c2 s^2} and FIX its constants "
                    "by the two moment conditions int rho=1 (normalization) and int s rho=1 (unit mean): the "
                    "famous GOE/GUE/GSE constants emerge from the solve. The same moment-matching fixes the "
                    "r-statistics normalization. Demonstrated on arXiv:2606.23785 / 2606.24490 (RMT chaos).",
        regime="probability",
        references=("https://en.wikipedia.org/wiki/Random_matrix#Spacing_distributions (Wigner surmise)",
                    "arXiv:2606.23785 (Controlled Chaos in 4D SCFTs), eq.(338-343)"),
    ),
    Method(
        key="dilogarithm",
        name="Dilogarithm functional equations (Euler reflection)",
        applies_when="expressions in the dilogarithm Li_2 that must be evaluated or simplified via its "
                     "functional equations — e.g. saddle-point actions / WKB phases built from Li_2",
        explanation="Li_2 has no elementary closed form, but its functional equations relate its values. "
                    "Euler's reflection Li_2(z)+Li_2(1-z)=pi^2/6-log(z)log(1-z) is DERIVED by matching "
                    "derivatives (d/dz Li_2 = -log(1-z)/z) and fixing the constant at z=1 (Li_2(1)=pi^2/6); "
                    "specialising gives values like Li_2(1/2)=pi^2/12-1/2 log^2 2. Surfaced by "
                    "arXiv:2606.24497 (Kashaev limits), whose action is built from Li_2.",
        regime="special-function",
        references=("DLMF 25.12.4 (https://dlmf.nist.gov/25.12)",
                    "arXiv:2606.24497 (Kashaev limits of quantum A-polynomials)"),
    ),
    Method(
        key="oscillator_commutator",
        name="Canonical commutator algebra of Fock/oscillator operators",
        applies_when="operators built from bosonic creation/annihilation oscillators whose "
                     "(super)commutators must be computed or whose Lie-algebra realization must be "
                     "shown to close — e.g. Jordan-Schwinger gl(k), su(1,1), so(k,k) generators",
        explanation="Compute [A,B] from the canonical relation [a,a†]=1 and normal-order the result "
                    "(all a† left of all a) into a unique canonical form, so a claimed structure "
                    "[o_I,o_J]=f^K_{IJ}o_K can be verified to close. Surfaced by arXiv:2606.24008 "
                    "(BRST higher-spin), whose constraint superalgebra is an oscillator realization.",
        regime="tensor",
        references=("Jordan-Schwinger map (https://en.wikipedia.org/wiki/Jordan-Schwinger_transformation)",
                    "arXiv:2606.24008 (Lagrangian formulations for mixed-antisymmetric HS fields), Table 1 / so(k,k)"),
    ),
    Method(
        key="gamma_ratio_asymptotic",
        name="Asymptotic expansion of a ratio of Gamma functions (Stirling series)",
        applies_when="the large-parameter behaviour of Γ(z+a)/Γ(z+b) (or a product of such) is needed — "
                     "e.g. moments of a chi / generalized-gamma distribution as the degrees of freedom k→∞",
        explanation="Route through the logarithm: gamma's own asymptotic series is unimplemented in the CAS, "
                    "but loggamma's Stirling series is. Take logs, expand each loggamma, subtract, exponentiate "
                    "and re-expand → Γ(z+a)/Γ(z+b) ~ z^{a-b}[1 + (a-b)(a+b-1)/(2z) + …]. Closes the "
                    "Gamma-ratio asymptotic hole found in arXiv:2606.23785 (chi-distribution moments).",
        regime="special-function",
        references=("DLMF 5.11.13 (https://dlmf.nist.gov/5.11.E13)",
                    "arXiv:2606.23785 (Controlled Chaos in 4D SCFTs), App. B chi-distribution moments"),
    ),
    Method(
        key="stationary_phase",
        name="Stationary phase / Fourier method (oscillatory integrals)",
        applies_when="rapidly oscillating integrand, e.g. e^(i b x) with large b; standard quadrature fails to converge",
        explanation="Treat the oscillation by stationary-phase asymptotics or by Fourier-transform techniques "
                    "rather than brute-force quadrature; the dominant contribution comes from stationary points "
                    "and endpoints.",
        regime="special-function",
        references=("Bender & Orszag, Advanced Mathematical Methods, ch. 6",),
    ),
    # --- tensor / vector pattern library (seed) ---
    Method(
        key="sym_antisym",
        name="Symmetric × antisymmetric contraction vanishes",
        applies_when="a tensor symmetric in an index pair is contracted with one antisymmetric in the same pair",
        explanation="Relabel the contracted dummy indices: the symmetric factor is unchanged, the antisymmetric "
                    "one flips sign, so the sum equals minus itself — hence it is identically zero. (Curl-of-grad, "
                    "div-of-curl, and d²=0 are all this pattern.)",
        regime="tensor",
        references=("Clairaut/Schwarz — mixed partials commute",
                    "do Carmo, Differential Forms and Applications (d²=0)"),
    ),
    # --- gap-closing integration strategies (close Wikipedia integral-table gaps) ---
    Method(
        key="hyperbolic_exp_rewrite",
        name="Rewrite hyperbolic to exponential, then integrate",
        applies_when="integrand contains hyperbolic functions (sech, csch, ...) the CAS returns "
                     "unevaluated, e.g. ∫sech²x dx",
        explanation="Rewrite the integrand via the defining exponential identities "
                    "(sech x = 2/(eˣ+e⁻ˣ), …) into a rational function of eˣ that the CAS can "
                    "integrate; reconcile the result (which may differ from tanh x by a constant).",
        regime="elementary",
        references=("Wikipedia, List of integrals of hyperbolic functions",),
    ),
    Method(
        key="inverse_function_parts",
        name="Integration by parts with an inverse-(hyperbolic) factor as u",
        applies_when="polynomial × inverse-hyperbolic-of-linear (acosh/asinh/asech/acsch of a x+b), "
                     "or a power thereof, that the CAS fails on directly",
        explanation="One IBP pass with u = the inverse function, dv = the rest dx: differentiating "
                    "u yields an algebraic 1/√(…) factor, so the residual ∫v du is an elementary "
                    "radical integral the CAS closes (recursing for squared inverse factors).",
        regime="elementary",
        references=("Wikipedia, List of integrals of inverse hyperbolic functions",),
    ),
    Method(
        key="complete_square_sub",
        name="Complete the square (Euler substitution) for a quadratic raised to a half-integer power",
        applies_when="a DEFINITE integral with P(x)/(a x²+b x+c)^p, the quadratic irreducible with a "
                     "linear term and p non-integer, e.g. ∫₀^∞ (1+x)/(1+x+x²)^(5/2) dx",
        explanation="Substitute u = x + b/(2a) to complete the square, removing the linear term so the "
                    "denominator becomes (u²+k)^p — the standard form the CAS integrates; the limits "
                    "shift by b/(2a). Surfaced as a gap by arXiv:2606.23785 (RMT r-statistics).",
        regime="elementary",
        references=("arXiv:2606.23785 (Controlled Chaos in 4D SCFTs), r-statistics normalization",),
    ),
    Method(
        key="conformal_block",
        name="SL(2) conformal block k_h = z^h 2F1(h,h;2h;z) (Casimir eigenfunction, eigenvalue h(h-1))",
        applies_when="the 1D / SL(2) global conformal block is needed - the function resumming a primary of "
                     "weight h and its descendants in a 4-point function, or its quadratic-Casimir eigenvalue h(h-1)",
        explanation="The exchanged conformal family is an SL(2) irrep, so the quadratic Casimir acts on it as the "
                    "constant h(h-1). The block k_h(z)=z^h 2F1(h,h;2h;z) is the eigenfunction of the Casimir "
                    "differential operator D_z = z^2(1-z) d^2/dz^2 - z^2 d/dz (Dolan-Osborn normalisation): "
                    "D_z k_h = h(h-1) k_h. The engine applies D_z to the hypergeometric series, reads the eigenvalue "
                    "off the leading z^h balance, and confirms the residual vanishes order by order. The 1D analogue "
                    "of conformal_casimir's Delta(Delta-d).",
        regime="representation-theory",
        references=("Dolan-Osborn, Conformal four point functions and the OPE (https://arxiv.org/abs/hep-th/0011040)",
                    "Simmons-Duffin, TASI Lectures on the Conformal Bootstrap (https://arxiv.org/abs/1602.07982)"),
    ),
    Method(
        key="jacobi_trudi",
        name="Jacobi-Trudi identity s_lambda = det(h_{lambda_i-i+j}) (Schur polynomial)",
        applies_when="a Schur polynomial s_lambda is needed as a determinant of complete homogeneous "
                     "symmetric polynomials — the determinantal backbone of the symmetric-function ring "
                     "(characters, Jack/Macdonald deformations, localization)",
        explanation="The Schur function s_lambda equals det(h_{lambda_i-i+j}), the change of basis from the "
                    "complete homogeneous polynomials h_k (read off prod_i 1/(1-x_i t)=sum_k h_k t^k) to the "
                    "Schur basis. For lambda=(2,1) this is the 2x2 det h_1 h_2 - h_3, whose expansion carries "
                    "the hallmark coefficient 2 on x1 x2 x3. Dual to s_lambda=det(e_{lambda'_i-i+j}); the "
                    "scaffold under Jack/Macdonald and character formulas.",
        regime="representation-theory",
        references=("Macdonald, Symmetric Functions and Hall Polynomials, I.3 (Jacobi-Trudi)",
                    "https://en.wikipedia.org/wiki/Schur_polynomial (Jacobi-Trudi identity; s_(2,1) value)"),
    ),
    Method(
        key="komar_mass",
        name="Komar mass of Schwarzschild M (Killing-vector surface integral)",
        applies_when="the conserved energy/mass of a stationary, asymptotically-flat spacetime is needed "
                     "from its timelike Killing vector — the GR notion of total energy at infinity",
        explanation="The Komar mass is the Noether charge of the timelike Killing vector xi=d/dt: "
                    "M = -(1/8 pi) oint nabla^a xi^b dS_ab. For Schwarzschild the engine takes the "
                    "Christoffel symbols from the curvature pipeline, builds nabla_a xi_b = d_a xi_b - "
                    "Gamma^c_ab xi_c (antisymmetric, since xi is Killing), raises and contracts with the "
                    "r=const 2-sphere surface element, and integrates -> M. nabla^t xi^r=-M/r^2 and the "
                    "-8 pi M flux emerge; nothing is written in. The conserved charge of time-translation symmetry.",
        regime="general-relativity",
        references=("R. M. Wald, General Relativity, ch.11 (Komar mass)",
                    "E. Poisson, A Relativist's Toolkit, sec.4.3.3 (Komar integrals); P. Townsend, gr-qc/9707012"),
    ),
]}


# Established PUBLISHED step-by-step derivation guides per method (see METHOD_STEP_SOURCES.md).
# Found by a literature search (2026-06-26) to GROUND each method's leveled Derivation in how
# authoritative sources teach the steps (rule-8 corroboration). Grade: FULL = source shows the full
# step-by-step; partial = some steps; THIN = only result-statements found -> the engine's Derivation
# fills the pedagogical gap (these are where the tool ADDS value, not where it is unsupported).
STEP_GUIDES: dict[str, str] = {
    "parts": "FULL — Paul's Online Math Notes, Integration by Parts: https://tutorial.math.lamar.edu/classes/calcII/IntegrationByParts.aspx",
    "u_sub": "FULL — Paul's Online Math Notes, Substitution Rule: https://tutorial.math.lamar.edu/classes/calcI/substitutionrule.aspx",
    "partial_fractions": "FULL — ChiliMath / Paul's, Partial Fraction Decomposition: https://www.chilimath.com/lessons/advanced-algebra/partial-fraction-decomposition/",
    "complete_square_sub": "FULL — Paul's, Integrals Involving Quadratics (complete-square + sub): https://tutorial.math.lamar.edu/classes/calcII/integralswithquadratics.aspx",
    "hyperbolic_exp_rewrite": "FULL — Story of Mathematics, Integration of Hyperbolic Functions: https://www.storyofmathematics.com/integration-of-hyperbolic-functions/",
    "inverse_function_parts": "FULL — Krista King, Inverse-hyperbolic integrals (IBP): https://www.kristakingmath.com/blog/inverse-hyperbolic-integrals",
    "contour": "FULL — MIT OCW 18.04 Topic 9, Definite Integrals via the Residue Theorem: https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/",
    "feynman_parameter": "FULL — K. Conrad (UConn), Differentiation under the integral sign: https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf",
    "mellin": "partial — DLMF §2.5 Mellin Transform Methods: https://dlmf.nist.gov/2.5",
    "abel_plana": "FULL — Saharian, Generalized Abel-Plana formula (argument principle): https://arxiv.org/abs/0708.1187",
    "euler_maclaurin": "FULL — Forster (LMU), Euler-Maclaurin Summation: https://www.mathematik.uni-muenchen.de/~forster/v/ann/annth_05.pdf",
    "zeta_reg": "partial->FULL — 4gravitons + arXiv:1806.06245 (analytic continuation to -1/12): https://arxiv.org/abs/1806.06245",
    "analytic_continuation": "FULL — Haiman (Berkeley), Notes on Gamma and Zeta: https://math.berkeley.edu/~mhaiman/math185-summer14/gamma-notes.pdf",
    "dim_reg": "partial — Peskin & Schroeder ch.10.2 (print) / USP QFT lecture 23: https://fma.if.usp.br/~burdman/QFT1/lecture_23.pdf",
    "meijer_g": "THIN — SymPy g-functions algorithm (no mainstream worked-example guide; engine's steps add value): https://docs.sympy.org/latest/modules/integrals/g-functions.html",
    "asymptotic_expansion": "FULL — Majdalani (Auburn), erfc asymptotics by repeated IBP: http://majdalani.eng.auburn.edu/courses/06_perturbations_2/handout_p6_SpFuncExps.pdf",
    "gamma_ratio_asymptotic": "FULL — De Angelis, Stirling's Series Revisited: https://arxiv.org/abs/2305.09873",
    "stationary_phase": "FULL — T. Tao (UCLA 247B), Oscillatory Integrals notes 8: https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf",
    "sym_antisym": "FULL — Wikipedia, Antisymmetric tensor (index-relabel proof): https://en.wikipedia.org/wiki/Antisymmetric_tensor",
    "oscillator_commutator": "partial — Wikipedia, Creation/annihilation operators + Jordan-Schwinger map: https://en.wikipedia.org/wiki/Creation_and_annihilation_operators",
    "dilogarithm": "FULL — Zagier, The Dilogarithm Function: https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/fulltext.pdf",
    "wigner_surmise": "THIN — constants stated not derived in accessible refs (canonical: Mehta, Random Matrices, offline); the engine DERIVES them by solving the moment equations: https://en.wikipedia.org/wiki/Random_matrix#Spacing_distributions",
    "q_pochhammer": "partial — Wikipedia, q-Pochhammer symbol (log = -sum a^n/(n(1-q^n))): https://en.wikipedia.org/wiki/Q-Pochhammer_symbol",
    "airy": "FULL — Bender & Orszag, Advanced Mathematical Methods ch.3 (WKB derivation of Airy asymptotics) + DLMF 9.7: https://dlmf.nist.gov/9.7",
    "bessel_hankel": "THIN — formula in Bessel tables w/o steps; framework: Ramanujan master theorem (arXiv:1801.09211); engine supplies the series+moments steps: https://arxiv.org/abs/1801.09211",
    "casimir": "FULL — Wikipedia, Angular momentum operator, 'Derivation of possible values' (ladder method): https://en.wikipedia.org/wiki/Angular_momentum_operator",
    "conformal_casimir": "FULL — Simmons-Duffin, TASI Lectures on the Conformal Bootstrap (embedding-space Casimir): https://arxiv.org/abs/1602.07982",
    "confluent_0F1": "FULL — Andrews-Askey-Roy, Special Functions ch.4 (power-series matching to Bessel): https://doi.org/10.1017/CBO9781107325937",
    "sturm_liouville": "FULL — Chemistry LibreTexts, Particle in a 1-D Box (ODE -> BCs -> spectrum): https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/05.5%3A_Particle_in_Boxes/Particle_in_a_1-Dimensional_box",
    "conformal_block": "FULL — Simmons-Duffin, TASI Lectures on the Conformal Bootstrap, sec. on the SL(2)/Casimir equation for blocks (D_z k_h = h(h-1)k_h, k_h=z^h 2F1(h,h;2h;z)): https://arxiv.org/abs/1602.07982",
    "jacobi_trudi": "FULL — Macdonald, Symmetric Functions and Hall Polynomials, I.3 (Jacobi-Trudi identity s_lambda=det(h_{lambda_i-i+j})); explicit s_(2,1) tabulated: https://en.wikipedia.org/wiki/Schur_polynomial",
    "komar_mass": "FULL — E. Poisson, A Relativist's Toolkit, ch.4.3.3 (Komar integrals; Schwarzschild Komar mass = M) + Wald GR ch.11; Townsend gr-qc/9707012: https://arxiv.org/abs/gr-qc/9707012",
}


def by_regime(regime: str) -> list[Method]:
    return [m for m in METHODS.values() if m.regime == regime]
