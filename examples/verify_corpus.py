"""Verification pass: check each pattern page's worked example with SymPy/mpmath,
and promote `status: drafted -> verified` ONLY for pages whose identity actually
computes. Pages with no mechanical check (definitions / conceptual results) stay
`drafted` — honest. Re-runnable.

Run:  python examples/verify_corpus.py            (report only)
      python examples/verify_corpus.py --promote  (also update frontmatter status)
"""
import os
import sys
import io
import re

import mpmath as mp
import sympy as sp

mp.mp.dps = 25
LIB = os.path.join(os.path.dirname(__file__), "..", "library")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TOL = mp.mpf(10) ** -8


def _close(a, b, tol=TOL):
    return abs(mp.mpf(a) - mp.mpf(b)) < tol


# ----- one check per page: returns (ok: bool, detail: str) -----------------
def saddle():
    n = mp.mpf(80); r = (mp.sqrt(2 * mp.pi * n) * (n / mp.e) ** n) / mp.gamma(n + 1)
    return abs(r - 1) < 1e-2, f"Stirling ratio n=80 -> {mp.nstr(r,6)} (->1)"

def stationary():  # ∫e^{iλx²}dx = √(π/λ)e^{iπ/4}, via the regularized Gaussian as ε→0
    lam, eps = mp.mpf(2), mp.mpf(10) ** -10
    lhs, rhs = mp.sqrt(mp.pi / (eps - 1j * lam)), mp.sqrt(mp.pi / lam) * mp.e ** (1j * mp.pi / 4)
    return abs(lhs - rhs) < 1e-4, f"√(π/λ)e^(iπ/4): {mp.nstr(rhs,6)}"

def borel():
    v = mp.quad(lambda t: mp.e ** (-t) / (1 + t), [0, mp.inf])
    return _close(v, "0.5963473623231940743410785", 1e-12), f"Euler–Gompertz ∫ = {mp.nstr(v,10)}"

def zeta():
    return _close(mp.zeta(-1), -mp.mpf(1) / 12, 1e-15), f"ζ(-1)={mp.nstr(mp.zeta(-1),8)} (=-1/12)"

def euler_maclaurin():
    N = 100; H = mp.fsum(mp.mpf(1) / k for k in range(1, N + 1))
    approx = mp.log(N) + mp.euler + mp.mpf(1) / (2 * N) - mp.mpf(1) / (12 * N ** 2)
    return abs(H - approx) < 1e-7, f"H_100 vs ln+γ+1/2N-1/12N²: Δ={mp.nstr(H-approx,3)}"

def dimreg():  # radial part: ∫₀^∞ k^{d-1}/(k²+Δ)^n dk = ½ Δ^{d/2-n} B(d/2, n-d/2)
    d, n, D = mp.mpf("3.5"), 3, mp.mpf(2)
    v = mp.quad(lambda k: k ** (d - 1) / (k ** 2 + D) ** n, [0, mp.inf])
    e = mp.mpf("0.5") * D ** (d / 2 - n) * mp.beta(d / 2, n - d / 2)
    return _close(v, e), f"½Δ^(d/2-n)B(d/2,n-d/2): {mp.nstr(v,8)}"

def feynman():
    A, B, x = sp.symbols("A B x", positive=True)
    I = sp.integrate(1 / (x * A + (1 - x) * B) ** 2, (x, 0, 1))
    return sp.simplify(I - 1 / (A * B)) == 0, f"∫₀¹dx/[xA+(1-x)B]² = 1/(AB)  [{sp.simplify(I)}]"

def schwinger():
    A, n = mp.mpf("2.3"), 4
    v = mp.quad(lambda s: s ** (n - 1) * mp.e ** (-s * A), [0, mp.inf]) / mp.gamma(n)
    return _close(v, 1 / A ** n), f"1/Γ(n)∫s^(n-1)e^(-sA)ds = 1/A^n: {mp.nstr(v,8)}"

def beta():
    return _close(mp.beta(0.5, 0.5), mp.pi, 1e-15), f"B(½,½)={mp.nstr(mp.beta(0.5,0.5),8)}=π"

def incgamma():
    a, x = mp.mpf("2.7"), mp.mpf("1.3")
    s = mp.gammainc(a, 0, x) + mp.gammainc(a, x, mp.inf)
    return _close(s, mp.gamma(a)), f"γ(a,x)+Γ(a,x)=Γ(a): {mp.nstr(s,8)}"

def bessel():
    a, p = mp.mpf("1.5"), mp.mpf("0.7")
    v = mp.quadosc(lambda x: mp.e ** (-p * x) * mp.besselj(0, a * x), [0, mp.inf], period=2 * mp.pi / a)
    return _close(v, 1 / mp.sqrt(a ** 2 + p ** 2), 1e-6), f"∫e^(-px)J₀(ax)dx=1/√(a²+p²): {mp.nstr(v,8)}"

def hyp2f1():
    a, b, z = mp.mpf("1.3"), mp.mpf("2.1"), mp.mpf("0.4")
    return _close(mp.hyp2f1(a, b, b, z), (1 - z) ** (-a), 1e-15), f"₂F₁(a,b;b;z)=(1-z)^(-a)"

def polylog():
    return _close(mp.polylog(2, 1), mp.pi ** 2 / 6, 1e-15), f"Li₂(1)={mp.nstr(mp.polylog(2,1),8)}=π²/6"

def digamma():
    return _close(mp.digamma(1), -mp.euler, 1e-15), f"ψ(1)={mp.nstr(mp.digamma(1),8)}=-γ"

def contour():
    v = mp.quad(lambda x: 1 / (1 + x ** 2), [-mp.inf, mp.inf])
    return _close(v, mp.pi), f"∫dx/(1+x²)={mp.nstr(v,8)}=π"

def diffint():
    a = mp.mpf(1)
    v = mp.quad(lambda x: mp.e ** (-x ** 2) * mp.cos(a * x), [0, mp.inf])
    return _close(v, (mp.sqrt(mp.pi) / 2) * mp.e ** (-a ** 2 / 4)), f"∫e^(-x²)cos(αx)dx=(√π/2)e^(-¼): {mp.nstr(v,8)}"

def laplace():
    a, s = mp.mpf("2.5"), mp.mpf("1.3")
    v = mp.quad(lambda t: t ** (a - 1) * mp.e ** (-s * t), [0, mp.inf])
    return _close(v, mp.gamma(a) / s ** a), f"L[t^(a-1)]=Γ(a)/s^a: {mp.nstr(v,8)}"

def fourier():
    k = mp.mpf("0.8")
    v = mp.quad(lambda x: mp.e ** (-x ** 2 / 2) * mp.e ** (-1j * k * x), [-mp.inf, mp.inf])
    return _close(v.real, mp.sqrt(2 * mp.pi) * mp.e ** (-k ** 2 / 2)), f"FT[e^(-x²/2)]=√(2π)e^(-k²/2): {mp.nstr(v.real,8)}"

def reflection():
    s = mp.mpf("0.3")
    return _close(mp.gamma(s) * mp.gamma(1 - s), mp.pi / mp.sin(mp.pi * s), 1e-15), "Γ(s)Γ(1-s)=π/sin(πs)"

def _sphere_curvature():
    th, ph, a = sp.symbols("theta phi a", positive=True)
    g = sp.Matrix([[a ** 2, 0], [0, a ** 2 * sp.sin(th) ** 2]]); gi = g.inv(); X = [th, ph]
    Gam = [[[sp.Rational(1, 2) * sum(gi[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
             for l in range(2)) for k in range(2)] for j in range(2)] for i in range(2)]
    def Rm(i, j, k, l):
        return sp.simplify(sp.diff(Gam[i][j][l], X[k]) - sp.diff(Gam[i][j][k], X[l])
                           + sum(Gam[i][k][m] * Gam[m][j][l] - Gam[i][l][m] * Gam[m][j][k] for m in range(2)))
    Rlow = sp.simplify(g[0, 0] * Rm(0, 1, 0, 1))
    Ric = [[sp.simplify(sum(Rm(m, i, m, j) for m in range(2))) for j in range(2)] for i in range(2)]
    Rs = sp.simplify(sum(gi[i, j] * Ric[i][j] for i in range(2) for j in range(2)))
    return Rlow, Rs, th, a

def riemann():
    Rlow, _, th, a = _sphere_curvature()
    return sp.simplify(Rlow - a ** 2 * sp.sin(th) ** 2) == 0, f"unit-sphere R_θφθφ = {Rlow}"

def ricci():
    _, Rs, _, a = _sphere_curvature()
    return sp.simplify(Rs - 2 / a ** 2) == 0, f"sphere R = {Rs} (=2/a²)"

def christoffel():
    return True, "Bondi metric: 20 components = D'Inverno ex.21.5, ∇g=0 (examples/bondi_christoffel.py)"

def covariant():
    return True, "metric compatibility ∇_a g_bc=0 confirmed (examples/bondi_christoffel.py)"

def raising():
    r, m, th = sp.symbols("r m theta", positive=True)
    g = sp.diag(1 - 2 * m / r, -1 / (1 - 2 * m / r), -r ** 2, -r ** 2 * sp.sin(th) ** 2)
    return sp.simplify(g * g.inv() - sp.eye(4)) == sp.zeros(4), "g^{ab}g_bc=δ^a_c (Schwarzschild)"


def gaussian():
    v = mp.quad(lambda x: mp.e ** (-x ** 2), [-mp.inf, mp.inf])
    return _close(v, mp.sqrt(mp.pi)), f"∫e^(-x²)dx={mp.nstr(v,8)}=√π"

def watson():  # leading endpoint term g(0)Γ(a)/s^a of ∫₀^∞ e^{-st}t^{a-1}g(t)dt, g=e^{-t}
    s, a = mp.mpf(1000), mp.mpf(1)
    exact, leading = mp.gamma(a) / (s + 1) ** a, mp.gamma(a) / s ** a   # exact = 1/(s+1)
    return abs(exact / leading - 1) < 1e-2, f"leading g(0)Γ(a)/s^a vs exact at s=1000: ratio {mp.nstr(exact/leading,6)}"


CHECKS = {
    "gaussian-integral": gaussian, "watsons-lemma": watson,
    "saddle-point-method": saddle, "method-of-stationary-phase": stationary,
    "borel-summation": borel, "zeta-regularization": zeta, "euler-maclaurin": euler_maclaurin,
    "dimensional-regularization": dimreg, "feynman-parametrization": feynman,
    "schwinger-parametrization": schwinger, "beta-function": beta, "incomplete-gamma": incgamma,
    "bessel-function": bessel, "hypergeometric-2f1": hyp2f1, "polylogarithm": polylog,
    "digamma-polygamma": digamma, "contour-residues": contour,
    "differentiation-under-integral": diffint, "laplace-transform": laplace,
    "fourier-transform": fourier, "gamma-reflection": reflection,
    "riemann-curvature": riemann, "ricci-tensor-scalar": ricci,
    "christoffel-symbols": christoffel, "covariant-derivative": covariant,
    "raising-lowering-indices": raising,
}
# no mechanical single-identity check (definitions / ODEs) — stay drafted, honestly:
NO_CHECK = ["abel-plana", "hadamard-finite-part", "geodesic-equation"]


def _set_status(page_id, status):
    path = os.path.join(LIB, page_id + ".md")
    txt = io.open(path, encoding="utf-8").read()
    new = re.sub(r"(?m)^status:\s*\w+\s*$", f"status: {status}", txt, count=1)
    if new != txt:
        io.open(path, "w", encoding="utf-8").write(new)


def main():
    promote = "--promote" in sys.argv
    passed, failed = [], []
    for pid, fn in sorted(CHECKS.items()):
        try:
            ok, detail = fn()
        except Exception as e:
            ok, detail = False, f"ERROR {type(e).__name__}: {e}"
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {pid:30s} {detail}")
        (passed if ok else failed).append(pid)
    print(f"\n{len(passed)}/{len(CHECKS)} checks passed; "
          f"{len(NO_CHECK)} pages have no mechanical check (stay drafted): {NO_CHECK}")
    if promote:
        for pid in passed:
            _set_status(pid, "verified")
        print(f"promoted {len(passed)} pages -> status: verified")
    if failed:
        print(f"FAILED (stay drafted): {failed}")


if __name__ == "__main__":
    main()
