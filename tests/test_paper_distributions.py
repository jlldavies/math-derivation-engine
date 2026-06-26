"""Paper gates (rule 10) — closed-form maths of arXiv:2606.23785 "Controlled Chaos in 4D SCFTs",
Section 2 + Appendix B (chi / generalized-gamma distributions) + Appendix C (spectral rigidity).

The ENGINE'S CAS executor (sympy, the same `sp.integrate` `solve_integral` wraps) does the maths;
we only verify the result equals the value PUBLISHED in the paper (and, where noted, the standard
textbook reference) — checking someone else's homework, not our own. Each gate cites the .tex line.

The large-k asymptotic SERIES of a Gamma ratio (sympy's gamma.aseries raises PoleError) was the one
hole; it is now CLOSED by the `gamma_ratio_asymptotic` method (loggamma Stirling route) — the
module-bottom tests show the engine deriving the paper's μ, σ², ⟨1/Z⟩ leading forms.
"""
import os
import sys

import pytest
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.strategies import solve_integral                       # noqa: E402
from integral_explainer.special_methods import gamma_ratio_asymptotic          # noqa: E402

y, z, x, s, lam, r = sp.symbols("y z x s lambda r", positive=True)
k, n, p, m = sp.symbols("k n p m", positive=True)
a, d, c = sp.symbols("a d c", positive=True)
G = sp.gamma


# ===== Section 2 — level-statistics normalizations (engine search; numeric limits) ==========
def test_poisson_spacing_normalized():           # eq. line 317: ρ_Poisson(s)=e^{-s}
    assert solve_integral("exp(-s)", 0, "oo", var="s")["best"][1] == 1


def test_poisson_rstatistics_normalized():       # eq. line 321: P_Poisson(r)=1/(1+r)^2
    assert solve_integral("1/(1+r)**2", 0, "oo", var="r")["best"][1] == 1


def test_wigner_semicircle_normalized():         # eq. line 331: ρ(λ)=√(4-λ²)/2π on [-2,2]
    assert sp.simplify(solve_integral("sqrt(4-x**2)/(2*pi)", -2, 2)["best"][1] - 1) == 0


# ===== Appendix B — chi distribution χ_k  (eq. lines 2146-2155) ==============================
CHI = y ** (k - 1) * sp.exp(-y ** 2 / 2) / (2 ** (k / 2 - 1) * G(k / 2))


def test_chi_pdf_normalized_symbolic_k():        # ∫₀^∞ ρ_Y(y;k) dy = 1
    assert sp.simplify(sp.integrate(CHI, (y, 0, sp.oo)) - 1) == 0


def test_chi_moment_formula_symbolic_k_n():      # μ_n = 2^{n/2} Γ((k+n)/2)/Γ(k/2)
    mu_n = sp.integrate(CHI * y ** n, (y, 0, sp.oo))
    assert sp.simplify(mu_n - 2 ** (n / 2) * G((k + n) / 2) / G(k / 2)) == 0


def test_chi3_mean_and_second_moment():          # the b_i~χ relevant case; mean & μ_2=k
    chi3 = y ** 2 * sp.exp(-y ** 2 / 2) / (2 ** (sp.Rational(3, 2) - 1) * G(sp.Rational(3, 2)))
    assert sp.simplify(sp.integrate(chi3 * y, (y, 0, sp.oo)) - 2 * sp.sqrt(2 / sp.pi)) == 0
    assert sp.simplify(sp.integrate(chi3 * y ** 2, (y, 0, sp.oo)) - 3) == 0


# ===== Appendix B — power-of-chi  Z = Y^p  (eq. lines 2159-2177) =============================
RHO_Z = z ** (k / p - 1) * sp.exp(-z ** (2 / p) / 2) / (p * 2 ** (k / 2 - 1) * G(k / 2))


def test_power_chi_pdf_normalized():             # ∫₀^∞ ρ_Z dz = 1
    assert sp.simplify(sp.integrate(RHO_Z, (z, 0, sp.oo)) - 1) == 0


def test_power_chi_mean():                       # ⟨Z⟩ = 2^{p/2} Γ((k+p)/2)/Γ(k/2)
    EZ = sp.integrate(RHO_Z * z, (z, 0, sp.oo))
    assert sp.simplify(EZ - 2 ** (p / 2) * G((k + p) / 2) / G(k / 2)) == 0


def test_power_chi_variance():                   # Var = 2^p(Γ((k+2p)/2)/Γ(k/2) - (Γ((k+p)/2)/Γ(k/2))²)
    EZ = sp.integrate(RHO_Z * z, (z, 0, sp.oo))
    EZ2 = sp.integrate(RHO_Z * z ** 2, (z, 0, sp.oo))
    want = 2 ** p * (G((k + 2 * p) / 2) / G(k / 2) - (G((k + p) / 2) / G(k / 2)) ** 2)
    assert sp.simplify((EZ2 - EZ ** 2) - want) == 0


def test_power_chi_reciprocal():                 # ⟨1/Z⟩ = 2^{-p/2} Γ((k-p)/2)/Γ(k/2), valid k>p
    # parametrize k = m+p (m>0) so the convergence condition k>p holds automatically
    rho = z ** ((m + p) / p - 1) * sp.exp(-z ** (2 / p) / 2) / (p * 2 ** ((m + p) / 2 - 1) * G((m + p) / 2))
    Einv = sp.integrate(rho / z, (z, 0, sp.oo))
    assert sp.simplify(Einv - 2 ** (-p / 2) * G(m / 2) / G((m + p) / 2)) == 0


# ===== Appendix B — generalized gamma & the χ^p ↔ GenGamma equivalence (eq. lines 2184-2190) =
def test_generalized_gamma_normalized_symbolic():   # ∫₀^∞ (c/(a^d Γ(d/c))) x^{d-1} e^{-(x/a)^c} dx = 1
    gg = (c / (a ** d * G(d / c))) * x ** (d - 1) * sp.exp(-(x / a) ** c)
    assert sp.simplify(sp.integrate(gg, (x, 0, sp.oo)) - 1) == 0


def test_chi_power_equals_generalized_gamma():      # χ_k^p = GenGamma(2^{p/2}, k/p, 2/p), PDF identity
    rho_chi_p = x ** (k / p - 1) * sp.exp(-x ** (2 / p) / 2) / (p * 2 ** (k / 2 - 1) * G(k / 2))
    aa, dd, cc = 2 ** (p / 2), k / p, 2 / p
    gg = (cc / (aa ** dd * G(dd / cc))) * x ** (dd - 1) * sp.exp(-(x / aa) ** cc)
    assert sp.simplify(rho_chi_p - gg) == 0


# ===== Appendix C — spectral rigidity Δ₃ (eq. lines 2233-2272) ===============================
def test_spectral_rigidity_least_squares_derivation():
    # Dyson-Mehta Δ₃ = (1/E) min_{A,B} ∫_{-E/2}^{E/2} (N_unf(α+x)-A-Bx)² dx.  With the staircase
    # moments J0=∫N, J1=∫xN, K=∫N² over [-E/2,E/2] (and ∫1=E, ∫x=0, ∫x²=E³/12), the ENGINE's CAS
    # minimizes over (A,B) and must reproduce eq.(2.x): Δ₃ = K/E - J0²/E² - 12 J1²/E⁴.
    A, B, E, J0, J1, K = sp.symbols("A B E J0 J1 K")
    F = K - 2 * A * J0 - 2 * B * J1 + A ** 2 * E + B ** 2 * E ** 3 / 12
    As = sp.solve(sp.diff(F, A), A)[0]
    Bs = sp.solve(sp.diff(F, B), B)[0]
    assert As == J0 / E and Bs == 12 * J1 / E ** 3
    D3 = sp.simplify(F.subs({A: As, B: Bs}) / E)
    assert sp.simplify(D3 - (K / E - J0 ** 2 / E ** 2 - 12 * J1 ** 2 / E ** 4)) == 0


@pytest.mark.parametrize("label,expr,approx", [
    ("GOE", sp.log(2 * sp.pi) + sp.EulerGamma - sp.Rational(5, 4) - sp.pi ** 2 / 8, -0.0687),
    ("GUE", sp.log(2 * sp.pi) + sp.EulerGamma - sp.Rational(5, 4), 1.1651),
    ("GSE", sp.log(4 * sp.pi) + sp.EulerGamma - sp.Rational(5, 4) + sp.pi ** 2 / 8, 3.0919),
])
def test_spectral_rigidity_universal_constants(label, expr, approx):
    # eq.(Delta3_GOE/GUE/GSE) lines 2262-2272: the asymptotic Δ₃ ≃ (1/cπ²)[ln E + const]
    assert abs(float(expr) - approx) < 5e-4


# ===== HOLE NOW CLOSED — large-k asymptotic series of a Gamma ratio (gamma_ratio_asymptotic) ==
# The paper's large-k expansions (lines 2170-2181): μ = k^{p/2}+…, σ² = ½p²k^{p-1}+…,
# ⟨1/Z⟩ = k^{-p/2}+…. sympy's gamma.aseries raises PoleError, so we built `gamma_ratio_asymptotic`
# (loggamma Stirling route). These tests show the ENGINE now DERIVES the paper's stated forms.
def test_gamma_ratio_asymptotic_reproduces_dlmf():       # DLMF 5.11.13 (the published reference)
    z, a, b = sp.symbols("z a b", positive=True)
    got = gamma_ratio_asymptotic([z + a], [z + b], z, 1)
    assert sp.simplify(got - z ** (a - b) * (1 + (a - b) * (a + b - 1) / (2 * z))) == 0


def test_paper_mean_leading_kpow():                      # μ = 2^{p/2}Γ((k+p)/2)/Γ(k/2) ~ k^{p/2}
    mu = 2 ** (p / 2) * gamma_ratio_asymptotic([(k + p) / 2], [k / 2], k, 1)
    assert sp.limit(mu / k ** (p / 2), k, sp.oo) == 1


@pytest.mark.parametrize("pv", [2, 3, 5])                # the variance whose LEADING terms cancel
def test_paper_variance_leading_halfp2(pv):              # σ² ~ ½ p² k^{p-1} (line 2170)
    EZ = 2 ** sp.Rational(pv, 2) * gamma_ratio_asymptotic([(k + pv) / 2], [k / 2], k, 3)
    EZ2 = 2 ** pv * gamma_ratio_asymptotic([(k + 2 * pv) / 2], [k / 2], k, 3)
    var = sp.expand(EZ2 - EZ ** 2)
    assert sp.limit(var / k ** (pv - 1), k, sp.oo) == sp.Rational(1, 2) * pv ** 2


def test_paper_reciprocal_leading_kpow():                # ⟨1/Z⟩ = 2^{-p/2}Γ((k-p)/2)/Γ(k/2) ~ k^{-p/2}
    mm = sp.symbols("mm", positive=True)                 # k = mm+p so k-p = mm > 0
    einv = 2 ** (-p / 2) * gamma_ratio_asymptotic([mm / 2], [(mm + p) / 2], mm, 1)
    assert sp.limit(einv * mm ** (p / 2), mm, sp.oo) == 1
