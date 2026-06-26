r"""LEVELED Derivation for METHOD sturm_liouville (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.sturm_liouville_box. The engine DERIVES the Dirichlet spectrum
    -y'' = lambda y on [0,L],  y(0)=y(L)=0  =>  lambda_n = (n pi / L)^2,  y_n = sin(n pi x / L)
by solving the ODE (dsolve), imposing y(0)=0 to drop the cosine, and reducing y(L)=0 to sin(kL)=0,
whose positive roots k_n=n pi/L it confirms (sin(n pi)=0). Nothing written in. (Surfaced by
arXiv:2606.24328, whose order parameter solves a curved-background Sturm-Liouville problem.)

Sub-methods referenced by the steps:
    sturm_liouville -> { solve a 2nd-order linear ODE, apply boundary conditions, zeros of sine }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"-y''=\lambda y,\ \ y(0)=y(L)=0\ \Rightarrow\ "
       r"\lambda_n=\Big(\tfrac{n\pi}{L}\Big)^{2},\ \ y_n=\sin\!\Big(\tfrac{n\pi x}{L}\Big)")


def build_sturm_liouville_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"a Sturm-Liouville boundary eigenvalue problem — the discrete spectrum of a "
                   r"Schrodinger / order-parameter mode confined to $[0,L]$",
        goal=Goal.SIMPLIFY,
        integral="Dirichlet Sturm-Liouville spectrum lambda_n=(n pi/L)^2 by solving the ODE + BCs")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — the boundaries quantize the spectrum",
          {"plain": r"The equation $-y''=\lambda y$ has wavy solutions for any $\lambda$. What makes the spectrum "
                    r"DISCRETE is the two walls: the wave must vanish at both ends. Only special wavelengths fit a "
                    r"whole number of half-waves between the walls, and those pick out the allowed $\lambda$.",
           "working": r"The ODE alone has a 2-parameter family of solutions; the two boundary conditions $y(0)=y(L)=0$ "
                      r"select a discrete set of $\lambda$ for which a NON-zero solution exists — that's the spectrum.",
           "expert": r"$-d^2/dx^2$ with Dirichlet BCs is a self-adjoint Sturm-Liouville operator; its spectrum is the "
                     r"set of $\lambda$ admitting a non-trivial kernel element, found by solving the ODE and imposing the BCs."},
          forced_by=r"the general solution of $-y''=\lambda y$ has two free constants, and the two Dirichlet conditions "
                    r"turn into a homogeneous system whose non-trivial solvability is a condition ON $\lambda$.",
          payoff=r"the exact quantized spectrum $\lambda_n=(n\pi/L)^2$ and eigenfunctions $\sin(n\pi x/L)$ — the modal "
                 r"basis; a single numeric eigenvalue would miss the whole tower and the $n$-dependence.",
          relies_on=r"a regular self-adjoint problem on a finite interval with separated (Dirichlet) BCs, so the spectrum "
                    r"is real, discrete and bounded below.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — solve, then impose the two boundary conditions",
          {"plain": r"Solve the ODE to get $y=C_1\sin(kx)+C_2\cos(kx)$ with $k=\sqrt\lambda$. The left wall $y(0)=0$ "
                    r"throws away the cosine; the right wall $y(L)=0$ needs $\sin(kL)=0$, true only when $kL$ is a "
                    r"whole number of $\pi$'s.",
           "working": r"$y=C_1\sin(kx)+C_2\cos(kx)$; $y(0)=0\Rightarrow C_2=0$; $y(L)=0\Rightarrow C_1\sin(kL)=0$, and "
                      r"for $C_1\ne0$ this forces $\sin(kL)=0$, i.e. $kL=n\pi$.",
           "expert": r"$y(0)=0$ removes the even mode; $y(L)=0$ with $C_1\ne0$ gives the secular equation $\sin(kL)=0$, "
                     r"roots $k_n=n\pi/L$, hence $\lambda_n=k_n^2$."},
          math=[r"y=C_1\sin(kx)+C_2\cos(kx),\quad k=\sqrt{\lambda};\qquad "
                r"y(0)=0\Rightarrow C_2=0,\quad y(L)=0\Rightarrow \sin(kL)=0"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Solve the ODE and impose the boundary conditions", requires="expert",
           prose=r"From $y=C_1\sin(kx)+C_2\cos(kx)$, $y(0)=0$ kills the cosine and $y(L)=0$ forces $\sin(kL)=0$, "
                 r"so $kL=n\pi$ and $\lambda_n=(n\pi/L)^2$, $y_n=\sin(n\pi x/L)$.",
           math=[r"\lambda_n=\Big(\frac{n\pi}{L}\Big)^{2},\qquad y_n=\sin\!\Big(\frac{n\pi x}{L}\Big)"],
           references=["sub-method: sturm_liouville -> {solve 2nd-order ODE, apply BCs, zeros of sine}"],
           decompose=[
               dict(title="Solve the differential equation", requires="working",
                    prose=r"$-y''=\lambda y$ is the harmonic equation; its general solution is a sine plus a cosine of "
                          r"$kx$ with $k=\sqrt\lambda$.",
                    math=[r"y''+k^2 y=0\ \Rightarrow\ y=C_1\sin(kx)+C_2\cos(kx)"],
                    references=["base method -> library/second-order-linear-ode.md"],
                    decompose=[
                        dict(title="Characteristic roots", requires="plain",
                             prose=r"Trying $y=e^{rx}$ gives $r^2+k^2=0$, $r=\pm ik$, i.e. oscillatory solutions.",
                             math=[r"r^2+k^2=0\ \Rightarrow\ r=\pm i k"]),
                        dict(title="Real sine/cosine form", requires="plain",
                             prose=r"The two complex exponentials combine into $C_1\sin(kx)+C_2\cos(kx)$.",
                             math=[r"y=C_1\sin(kx)+C_2\cos(kx)"]),
                    ]),
               dict(title="Apply y(0)=0 (drop the cosine)", requires="plain",
                    prose=r"At $x=0$, $\sin0=0$ and $\cos0=1$, so $y(0)=C_2=0$: only the sine survives.",
                    math=[r"y(0)=C_2=0\ \Rightarrow\ y=C_1\sin(kx)"],
                    references=["base method -> library/boundary-conditions.md"]),
               dict(title="Apply y(L)=0 (quantize)", requires="working",
                    prose=r"$y(L)=C_1\sin(kL)=0$ with $C_1\ne0$ needs $\sin(kL)=0$. The zeros of sine are at multiples "
                          r"of $\pi$, so $kL=n\pi$, giving $\lambda_n=(n\pi/L)^2$.",
                    math=[r"\sin(kL)=0\ \Rightarrow\ kL=n\pi\ \Rightarrow\ \lambda_n=\Big(\frac{n\pi}{L}\Big)^2"],
                    references=["sub-method: zeros of sine"],
                    decompose=[
                        dict(title="Why a non-trivial mode needs sin(kL)=0", requires="plain",
                             prose=r"If $C_1=0$ the solution is identically zero (not a mode), so we need $\sin(kL)=0$.",
                             math=[r"C_1\ne0\ \Rightarrow\ \sin(kL)=0"]),
                        dict(title="Zeros of sine", requires="plain",
                             prose=r"$\sin\theta=0$ exactly when $\theta=n\pi$; here $\theta=kL$.",
                             math=[r"\sin(kL)=0\iff kL=n\pi,\ n=1,2,\dots"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `sturm_liouville_box` solves the ODE with dsolve, imposes the BCs, and CONFIRMS "
        r"$k_n=n\pi/L$ solves $\sin(kL)=0$ (since $\sin(n\pi)=0$) — returning $\lambda_n=(n\pi/L)^2$, "
        r"$y_n=\sin(n\pi x/L)$, matching the standard particle-in-a-box / Sturm-Liouville spectrum. "
        r"Independent check: each $y_n$ re-satisfies the ODE and both BCs.",
        math=[r"\lambda_n=(n\pi/L)^2,\quad y_n=\sin(n\pi x/L)",
              r"-y_n''=\Big(\tfrac{n\pi}{L}\Big)^2 y_n,\quad y_n(0)=y_n(L)=0"],
        references=["engine: special_methods.sturm_liouville_box (dsolve + BCs + zeros of sine)",
                    "Wikipedia, Sturm-Liouville theory — Dirichlet spectrum (independent)",
                    "arXiv:2606.24328 — curved-background order-parameter eigenproblem"])
    d.result(
        latex=r"\lambda_n=\Big(\frac{n\pi}{L}\Big)^{2},\qquad y_n(x)=\sin\!\Big(\frac{n\pi x}{L}\Big),"
              r"\quad n=1,2,\dots",
        note="spectrum derived by solving the ODE and imposing the boundary conditions (quantization from "
             "sin(kL)=0, confirmed by the engine); opens the PDE / Sturm-Liouville (boundary eigenvalue) track.")
    return d
