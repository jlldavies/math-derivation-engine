"""Leveled Derivation for the `analytic_continuation` capability (CLAUDE.md rule 7 + 11).

REAL realization (NOT re-solved by us): special_methods.residue_of_gamma(m) =
    sp.simplify(sp.residue(sp.gamma(z), z, -m))
i.e. SymPy analytically continues Γ past its convergent strip (the Euler integral
∫_0^∞ t^{z-1} e^{-t} dt only converges for Re z > 0) and reads the residue off the
Laurent expansion at the pole z = -m. The worked target is the m-th one:

    Res(Γ, z = -m) = (-1)^m / m!.

The STEP TREE below mirrors that computation: continue Γ off the strip via the
functional equation Γ(z+1)=zΓ(z) (analytic-continuation sub-method) → locate the pole
→ take the residue of a simple pole (residue sub-method: limit of (z+m)·f) → evaluate
the finite leftover by the factorial/known-values sub-methods.

The per-level step COUNTS EMERGE from the `requires`/`decompose` cut, never hand-set.
Run:  python scratch/expl_analytic_continuation.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

from .. import special_methods as sm
import sympy as sp

HDR = r"\Gamma(z)=\int_{0}^{\infty} t^{\,z-1}e^{-t}\,dt \ \ (\operatorname{Re}z>0)\ \longrightarrow\ \operatorname{Res}_{z=-m}\Gamma(z)"

def build_analytic_continuation_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the residue of the analytically-continued Gamma function at its pole $z=-m$",
        goal=Goal.EVALUATE,
        integral="Res(Gamma, z = -m)")
    d = Derivation(problem)

    # ---- WHY (recognition / decision) -------------------------------------
    d.why("Why this approach — continue Γ off its convergent strip, then take a residue",
          {"plain": r"The integral defining $\Gamma(z)$ only makes sense when $z$ is to the right of $0$; "
                    r"at $z=-m$ it blows up. But there is a single sensible way to extend $\Gamma$ to the "
                    r"left, and near $z=-m$ it behaves like $\tfrac{c}{z+m}$. The number $c$ on top is what "
                    r"we want — the 'residue'.",
           "working": r"The Euler integral converges only for $\operatorname{Re}z>0$, so it cannot be "
                      r"evaluated at $z=-m$. Analytic continuation (the functional equation) extends "
                      r"$\Gamma$ to a meromorphic function with simple poles at $z=0,-1,-2,\dots$; the "
                      r"residue at $z=-m$ is then a finite, well-defined number.",
           "expert": r"$\Gamma$ is meromorphic on $\mathbb{C}$ with simple poles at the non-positive "
                     r"integers; off the half-plane $\operatorname{Re}z>0$ it is fixed by analytic "
                     r"continuation of the Euler integral via $\Gamma(z+1)=z\Gamma(z)$. The pole at "
                     r"$z=-m$ is simple, so its residue is the clean local invariant."},
          forced_by=r"the Euler integral diverges at $z=-m$ (it sits left of the convergence boundary "
                    r"$\operatorname{Re}z>0$), so the value cannot be read off the integral directly — yet "
                    r"$\Gamma$ extends uniquely past the strip.",
          payoff=r"a residue is a finite, basis-free number that encodes the strength of the singularity; "
                 r"continuing $\Gamma$ and reading the residue gives the whole family $\frac{(-1)^m}{m!}$ at "
                 r"once, where a bare divergent integral gives nothing.",
          relies_on=r"the identity theorem (analytic continuation is unique) and the pole at $z=-m$ being "
                    r"SIMPLE — both supplied by the functional equation $\Gamma(z+1)=z\Gamma(z)$.")

    # ---- HOW (the machinery) ----------------------------------------------
    d.how("How the approach works — the functional equation gives the continuation and the residue",
          {"plain": r"The rule $\Gamma(z+1)=z\,\Gamma(z)$ lets us rewrite $\Gamma(z)$ using a value of "
                    r"$\Gamma$ to the right, where it is finite. Doing this $m{+}1$ times moves the argument "
                    r"into the safe region and exposes the $\tfrac{1}{z+m}$ blow-up.",
           "working": r"Iterating $\Gamma(z)=\Gamma(z+m+1)\big/\big(z(z+1)\cdots(z+m)\big)$ continues "
                      r"$\Gamma$ to $\operatorname{Re}z>-m-1$. The denominator vanishes simply at $z=-m$, "
                      r"so the pole is simple and its residue is $\lim_{z\to-m}(z+m)\Gamma(z)$.",
           "expert": r"$\Gamma(z)=\dfrac{\Gamma(z+m+1)}{\prod_{k=0}^{m}(z+k)}$ exhibits the simple pole at "
                     r"$z=-m$; the residue is the limit of $(z+m)\Gamma(z)$, i.e. $\Gamma(1)$ over the "
                     r"product of the surviving factors."},
          math=[r"\Gamma(z+1)=z\,\Gamma(z)\ \Longrightarrow\ "
                r"\Gamma(z)=\frac{\Gamma(z+m+1)}{z(z+1)\cdots(z+m)},\qquad "
                r"\operatorname{Res}_{z=-m}\Gamma(z)=\lim_{z\to-m}(z+m)\,\Gamma(z)"])

    # ---- STEP (the worked execution) --------------------------------------
    # ONE qualification tree. expert grasps "continue + residue" as a single move;
    # working sees its 3 sub-moves; plain decomposes those further. Counts EMERGE.
    d.step("Continue Γ to z = -m and read off the residue", requires="expert",
           prose=r"Use $\Gamma(z)=\Gamma(z+m+1)/\big(z(z+1)\cdots(z+m)\big)$ to continue past the strip; "
                 r"the pole at $z=-m$ is simple, and $\operatorname{Res}=\lim_{z\to-m}(z+m)\Gamma(z)="
                 r"\Gamma(1)/\prod_{k=0}^{m-1}(k-m)=(-1)^m/m!$.",
           math=[r"\operatorname{Res}_{z=-m}\Gamma(z)"
                 r"=\lim_{z\to-m}(z+m)\,\frac{\Gamma(z+m+1)}{\prod_{k=0}^{m}(z+k)}"
                 r"=\frac{\Gamma(1)}{\prod_{k=0,\,k\ne m}^{m}(k-m)}=\frac{(-1)^m}{m!}"],
           references=["method: library/analytic-continuation.md",
                       "method: library/residue.md"],
           decompose=[
               # --- sub-move 1: analytic continuation via the functional equation ---
               dict(title="Continue Γ past the strip with the functional equation",
                    requires="working",
                    prose=r"The Euler integral converges only for $\operatorname{Re}z>0$. Apply "
                          r"$\Gamma(z+1)=z\Gamma(z)$ repeatedly to express $\Gamma(z)$ through "
                          r"$\Gamma(z+m+1)$, whose argument has real part $>0$ near $z=-m$.",
                    math=[r"\Gamma(z)=\frac{\Gamma(z+m+1)}{z(z+1)\cdots(z+m)}"],
                    references=["sub-method: analytic continuation → library/analytic-continuation.md"],
                    decompose=[
                        dict(title="One step of the recurrence", requires="plain",
                             prose=r"The functional equation, read backwards, lowers the argument by one and "
                                   r"divides by $z$. This is just $\Gamma(z+1)=z\,\Gamma(z)$ rearranged.",
                             math=[r"\Gamma(z)=\frac{\Gamma(z+1)}{z}"],
                             references=["base → library/gamma-functional-equation.md"]),
                        dict(title="Iterate m+1 times into the safe region", requires="plain",
                             prose=r"Repeat until the argument is $z+m+1$, whose real part is positive near "
                                   r"$z=-m$; each step contributes one factor to the denominator.",
                             math=[r"\Gamma(z)=\frac{\Gamma(z+1)}{z}=\frac{\Gamma(z+2)}{z(z+1)}=\cdots"
                                   r"=\frac{\Gamma(z+m+1)}{z(z+1)\cdots(z+m)}"],
                             references=["base → library/induction.md"]),
                    ]),
               # --- sub-move 2: the pole is simple, take its residue ---
               dict(title="Identify the simple pole and take its residue",
                    requires="working",
                    prose=r"The factor $(z+m)$ in the denominator vanishes to first order at $z=-m$ while the "
                          r"numerator $\Gamma(z+m+1)\to\Gamma(1)\ne0$ stays finite — a simple pole. Its "
                          r"residue is the limit of $(z+m)$ times the function.",
                    math=[r"\operatorname{Res}_{z=-m}\Gamma(z)=\lim_{z\to-m}(z+m)\,\Gamma(z)"
                          r"=\lim_{z\to-m}\frac{\Gamma(z+m+1)}{\prod_{k=0}^{m-1}(z+k)}"],
                    references=["sub-method: residue of a simple pole → library/residue.md"],
                    decompose=[
                        dict(title="Why the pole is simple", requires="plain",
                             prose=r"Exactly one denominator factor, $(z+m)$, is zero at $z=-m$; the others "
                                   r"$z,z+1,\dots,z+m-1$ are nonzero there. One zero on the bottom = a simple "
                                   r"pole.",
                             math=[r"z+m\to0,\qquad z+k\to k-m\ne0\ \ (0\le k\le m-1)"],
                             references=["base → library/poles-and-zeros.md"]),
                        dict(title="Cancel (z+m) and take the limit", requires="plain",
                             prose=r"Multiplying by $(z+m)$ removes the single bad factor; the rest is "
                                   r"continuous, so just substitute $z=-m$.",
                             math=[r"(z+m)\,\Gamma(z)=\frac{\Gamma(z+m+1)}{\prod_{k=0}^{m-1}(z+k)}"
                                   r"\ \xrightarrow{\,z\to-m\,}\ \frac{\Gamma(1)}{\prod_{k=0}^{m-1}(k-m)}"],
                             references=["base → library/limits.md"]),
                    ]),
               # --- sub-move 3: evaluate the finite leftover ---
               dict(title="Evaluate the finite leftover to (-1)^m / m!",
                    requires="working",
                    prose=r"Use $\Gamma(1)=1$ and simplify the product $\prod_{k=0}^{m-1}(k-m)$: it is "
                          r"$(-1)^m m!$, giving the residue $(-1)^m/m!$.",
                    math=[r"\frac{\Gamma(1)}{\prod_{k=0}^{m-1}(k-m)}=\frac{1}{(-1)^m m!}=\frac{(-1)^m}{m!}"],
                    references=["sub-method: factorial / known values → library/factorial.md"],
                    decompose=[
                        dict(title="The known value Γ(1) = 1", requires="plain",
                             prose=r"At argument $1$ the Gamma function is the plain factorial $0!=1$ "
                                   r"(the Euler integral $\int_0^\infty e^{-t}dt=1$).",
                             math=[r"\Gamma(1)=0!=1"],
                             references=["base → library/gaussian-and-gamma-values.md"]),
                        dict(title="Simplify the product of the surviving factors", requires="plain",
                             prose=r"Each factor $k-m$ for $k=0,\dots,m-1$ is negative; pull out the $m$ minus "
                                   r"signs as $(-1)^m$ and the magnitudes $m,m-1,\dots,1$ as $m!$.",
                             math=[r"\prod_{k=0}^{m-1}(k-m)=\prod_{k=0}^{m-1}\!-(m-k)"
                                   r"=(-1)^m\,(m)(m-1)\cdots(1)=(-1)^m\,m!"],
                             references=["base → library/products-and-factorials.md"]),
                        dict(title="Assemble the residue", requires="plain",
                             prose=r"Put $\Gamma(1)=1$ over $(-1)^m m!$ and tidy the sign "
                                   r"($1/(-1)^m=(-1)^m$).",
                             math=[r"\operatorname{Res}_{z=-m}\Gamma(z)=\frac{1}{(-1)^m m!}=\frac{(-1)^m}{m!}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks; not used to derive) -------------------
    m_chk = 3
    engine_val = sm.residue_of_gamma(m_chk)          # the ENGINE's computation (sp.residue of Γ)
    formula_val = sp.Rational((-1) ** m_chk, sp.factorial(m_chk))
    agree = sp.simplify(engine_val - formula_val) == 0
    d.verify(
        r"Two independent checks, neither used to derive the answer. The engine's "
        r"`special_methods.residue_of_gamma(m)` calls SymPy's `sp.residue(sp.gamma(z),z,-m)`, "
        r"which Laurent-expands the analytically-continued $\Gamma$ and reads the residue — it "
        r"returns the same $(-1)^m/m!$, matched here at $m=3$ against the closed form.",
        math=[r"\text{engine }(m=3):\ \operatorname{Res}_{z=-3}\Gamma(z)=" + sp.latex(engine_val),
              r"\text{formula }(m=3):\ \frac{(-1)^3}{3!}=" + sp.latex(formula_val)
              + r"\quad(\text{agree: " + ("yes" if agree else "NO") + r"})"],
        references=["SymPy residue of the continued Γ — engine special_methods.residue_of_gamma",
                    "external gate: MIT 18.04 topic13 — Res(Γ,-3) = -1/6",
                    "method: library/analytic-continuation.md"])
    d.result(latex=r"\operatorname{Res}_{z=-m}\Gamma(z)=\frac{(-1)^m}{m!}",
             note=f"verified against the engine's sp.residue of the continued Γ at m={m_chk} "
                  f"({sp.latex(engine_val)} = {sp.latex(formula_val)}).")
    return d

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    d = build_analytic_continuation_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level step counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[]  (no warnings — VALID)")
    print("counts differ:", len(set(counts.values())) > 1)
    assert not qwarn, qwarn
    assert len(set(counts.values())) > 1, counts
