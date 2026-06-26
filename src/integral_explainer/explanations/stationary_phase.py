"""Leveled Derivation for the `stationary_phase` method (CLAUDE.md rule 7 + rule 11),
mirroring the ACTUAL engine computation in
`integral_explainer.special_methods.stationary_phase_J0` (the Fresnel master formula).

WORKED TARGET:  J0(x) ~ sqrt(2/(pi x)) cos(x - pi/4),  x -> +infinity.

What the engine REALLY does (special_methods.stationary_phase_J0):
    phi   = sin(theta)                                  # phase of J0(x)=(1/pi)int_0^pi cos(x sin th) dth
    th0   = pi/2          (solve phi'(th)=cos th = 0, the stationary point in (0,pi))
    phi0  = sin(th0)=1,   phi2 = phi''(th0) = -sin(th0) = -1
    amp   = sqrt(2*pi/(x*|phi2|)) = sqrt(2*pi/x)        # Fresnel coefficient
    contrib = amp*exp(i*(x*phi0 + sign(phi2)*pi/4))     # = sqrt(2pi/x) exp(i(x - pi/4))
    return  re(contrib/pi) = sqrt(2/(pi x)) cos(x - pi/4)

The decompose tree is cut by `requires` so plain/working/expert step counts EMERGE and
DIFFER. Each step references the SUB-METHOD it uses (integral representation; critical
point phi'=0; quadratic/Taylor expansion of the phase; the Fresnel/Gaussian integral;
the amplitude master formula; real-part + cofunction identity).

Local-only scratch (rule 1). Does NOT modify src/. Run:  python scratch/expl_stationary_phase.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

def build_stationary_phase_derivation() -> Derivation:
    problem = Problem(
        latex=r"J_{0}(x)=\frac{1}{\pi}\int_{0}^{\pi}\cos\!\big(x\sin\theta\big)\,d\theta"
              r"\ \sim\ \sqrt{\frac{2}{\pi x}}\,\cos\!\Big(x-\frac{\pi}{4}\Big)",
        represents="leading large-x asymptotics of the Bessel function J0 via stationary phase",
        goal=Goal.EXPAND,
        integral="J0(x) leading asymptotics, x -> infinity")
    d = Derivation(problem)

    # ----- WHY: the recognition / decision (forced-by / payoff / relies-on) ------------------
    d.why("Why stationary phase — the oscillation localises the integral",
          {"plain": r"The integral $\int_0^\pi\cos(x\sin\theta)\,d\theta$ wiggles faster and faster as $x$ grows, "
                    r"so the plus and minus parts almost cancel. They cancel EVERYWHERE except where the wiggling "
                    r"momentarily stops — near $\theta=\pi/2$. So the whole answer comes from a small patch there.",
           "working": r"For large $x$, $e^{ix\sin\theta}$ oscillates rapidly and cancels under integration except "
                      r"near a STATIONARY point of the phase $\phi(\theta)=\sin\theta$ (where $\phi'=0$). Only a "
                      r"neighbourhood of $\theta_0=\pi/2$ contributes at leading order.",
           "expert": r"Stationary phase: for $\int A(\theta)e^{ix\phi(\theta)}d\theta$ with $x\to\infty$, the "
                     r"non-stationary part is $O(x^{-\infty})$ by repeated IBP; the leading term is a Gaussian "
                     r"(Fresnel) contribution localised at the critical points $\phi'(\theta_0)=0$."},
          forced_by=r"the integrand is purely oscillatory in $x$ ($\cos(x\sin\theta)$, phase $\propto x$): ordinary "
                    r"quadrature does not converge and there is no elementary antiderivative, but $\phi=\sin\theta$ "
                    r"HAS an interior critical point $\theta_0=\pi/2$.",
          payoff=r"localising at $\theta_0$ collapses an intractable oscillatory integral to ONE Fresnel integral, "
                 r"and delivers BOTH the $x^{-1/2}$ envelope and the $-\pi/4$ phase shift — structure a single "
                 r"numeric value at one $x$ would hide.",
          relies_on=r"$x\to\infty$ (asymptotic, not exact); $\phi''(\theta_0)\neq0$ (a non-degenerate, quadratic "
                    r"stationary point) so the local model is a clean Gaussian; the amplitude is smooth at $\theta_0$.")

    # ----- HOW: the machinery (the Fresnel master formula) -----------------------------------
    d.how("How it works — the Fresnel master formula",
          {"plain": r"Near the spot where the wiggling stops, the phase looks like a parabola. The integral of "
                    r"$\cos$ of a parabola is a known number (a Fresnel integral). That single number gives the "
                    r"amplitude $\sqrt{2/(\pi x)}$ and the extra angle $-\pi/4$.",
           "working": r"Write $J_0=\tfrac1\pi\operatorname{Re}\int_0^\pi e^{ix\sin\theta}d\theta$. Expand the phase "
                      r"to second order at $\theta_0$ and do the resulting Gaussian/Fresnel integral; the master "
                      r"formula packages the result.",
           "expert": r"The leading stationary-phase term is "
                     r"$A(\theta_0)\sqrt{\tfrac{2\pi}{x|\phi''(\theta_0)|}}\,e^{i\,[x\phi(\theta_0)+\operatorname{sgn}\phi''\,\pi/4]}$; "
                     r"take $\tfrac1\pi\operatorname{Re}$ of it."},
          math=[r"\int_{0}^{\pi}e^{ix\sin\theta}\,d\theta\ \sim\ "
                r"\sqrt{\frac{2\pi}{x\,|\phi''(\theta_0)|}}\;e^{\,i\big(x\phi(\theta_0)+\operatorname{sgn}\phi''(\theta_0)\,\frac{\pi}{4}\big)},"
                r"\qquad \phi(\theta)=\sin\theta"])

    # ----- THE STEPS: ONE expert node; the per-level counts EMERGE from `requires` -----------
    # expert grasps "apply the master formula" as ONE move (requires=expert).
    # working sees its 4 sub-moves. plain decomposes those further still.
    d.step("Apply stationary phase to J0(x)", requires="expert",
           prose=r"Start from $J_0(x)=\tfrac1\pi\operatorname{Re}\int_0^\pi e^{ix\sin\theta}d\theta$. The phase "
                 r"$\phi=\sin\theta$ is stationary at $\theta_0=\pi/2$ with $\phi(\theta_0)=1,\ \phi''(\theta_0)=-1$; "
                 r"the master formula then gives the amplitude and the $-\pi/4$ shift directly.",
           math=[r"J_0(x)\sim\frac{1}{\pi}\operatorname{Re}\!\left[\sqrt{\frac{2\pi}{x}}\,"
                 r"e^{\,i(x-\pi/4)}\right]=\sqrt{\frac{2}{\pi x}}\,\cos\!\Big(x-\frac{\pi}{4}\Big)"],
           references=["sub-method: stationary_phase = {integral representation, critical point, "
                       "Fresnel integral, amplitude formula}"],
           decompose=[
               # --- working sub-move 1: integral representation (requires=working) -----------
               dict(title="Put J0 in oscillatory form", requires="working",
                    prose=r"Use the standard integral representation and write the cosine as the real part of a "
                          r"complex exponential, so the integral has the form $\int A\,e^{ix\phi}d\theta$.",
                    math=[r"J_0(x)=\frac{1}{\pi}\int_{0}^{\pi}\cos(x\sin\theta)\,d\theta"
                          r"=\frac{1}{\pi}\operatorname{Re}\int_{0}^{\pi}e^{ix\sin\theta}\,d\theta,\quad \phi(\theta)=\sin\theta"],
                    references=["base method -> library/bessel-integral-representation.md",
                                "base method -> library/eulers-formula.md"],
                    decompose=[
                        dict(title="The integral representation of J0", requires="plain",
                             prose=r"$J_0(x)$ is DEFINED (one standard form) by this average of $\cos(x\sin\theta)$ "
                                   r"over $\theta\in[0,\pi]$ — take it as the starting point.",
                             math=[r"J_0(x)=\frac{1}{\pi}\int_{0}^{\pi}\cos(x\sin\theta)\,d\theta"],
                             references=["base method -> library/bessel-integral-representation.md"]),
                        dict(title="Cosine as the real part of e^{i(...)}", requires="plain",
                             prose=r"Euler's formula: $\cos\alpha=\operatorname{Re}\,e^{i\alpha}$. With "
                                   r"$\alpha=x\sin\theta$ the integrand becomes a pure phase $e^{ix\sin\theta}$.",
                             math=[r"\cos(x\sin\theta)=\operatorname{Re}\,e^{ix\sin\theta}"],
                             references=["base method -> library/eulers-formula.md"]),
                    ]),
               # --- working sub-move 2: find the stationary point (requires=working) ---------
               dict(title="Find the stationary point of the phase", requires="working",
                    prose=r"The phase is $\phi=\sin\theta$. Solve $\phi'(\theta)=0$ on $(0,\pi)$ to locate where the "
                          r"oscillation momentarily stops, then read off the phase value and its curvature there.",
                    math=[r"\phi'(\theta)=\cos\theta=0\ \Rightarrow\ \theta_0=\frac{\pi}{2};\qquad "
                          r"\phi(\theta_0)=1,\quad \phi''(\theta_0)=-\sin\tfrac{\pi}{2}=-1"],
                    references=["base method -> library/critical-points.md  (solve f'=0)"],
                    decompose=[
                        dict(title="Differentiate the phase and set it to zero", requires="plain",
                             prose=r"The slope of $\sin\theta$ is $\cos\theta$. It is zero (a flat spot) at "
                                   r"$\theta_0=\pi/2$ inside $(0,\pi)$.",
                             math=[r"\frac{d}{d\theta}\sin\theta=\cos\theta=0\ \Rightarrow\ \theta_0=\frac{\pi}{2}"],
                             references=["base method -> library/critical-points.md"]),
                        dict(title="Value and curvature at the stationary point", requires="plain",
                             prose=r"Plug $\theta_0$ in: the height is $\sin(\pi/2)=1$; the second derivative "
                                   r"$\phi''=-\sin\theta$ gives curvature $-1$ (a downward bend).",
                             math=[r"\phi(\theta_0)=\sin\tfrac{\pi}{2}=1,\qquad "
                                   r"\phi''(\theta)=-\sin\theta\ \Rightarrow\ \phi''(\theta_0)=-1"],
                             references=["base method -> library/second-derivative.md"]),
                    ]),
               # --- working sub-move 3: the local Fresnel/Gaussian integral (requires=working)
               dict(title="Do the local Fresnel integral", requires="working",
                    prose=r"Near $\theta_0$ the phase is a parabola, $\phi\approx 1-\tfrac12(\theta-\theta_0)^2$. The "
                          r"remaining integral is a Fresnel/Gaussian integral whose value carries the $\sqrt{1/x}$ "
                          r"size and the $\pm\pi/4$ rotation.",
                    math=[r"\int_{-\infty}^{\infty}e^{\,i\frac{x\phi''}{2}u^{2}}\,du"
                          r"=\sqrt{\frac{2\pi}{x|\phi''|}}\;e^{\,i\,\operatorname{sgn}(\phi'')\,\pi/4}"],
                    references=["base method -> library/fresnel-integral.md",
                                "base method -> library/gaussian-integral.md  (analytic continuation)"],
                    decompose=[
                        dict(title="Expand the phase to second order", requires="plain",
                             prose=r"A smooth function near a flat spot looks like its tangent parabola. Since "
                                   r"$\phi'(\theta_0)=0$, $\phi(\theta)\approx\phi(\theta_0)+\tfrac12\phi''(\theta_0)(\theta-\theta_0)^2$.",
                             math=[r"\phi(\theta)\approx 1+\tfrac12(-1)(\theta-\theta_0)^2"
                                   r"=1-\tfrac12(\theta-\theta_0)^2"],
                             references=["base method -> library/taylor-expansion.md"]),
                        dict(title="The Fresnel integral value", requires="plain",
                             prose=r"$\int_{-\infty}^{\infty}e^{iau^2}du=\sqrt{\pi/|a|}\,e^{i\,\operatorname{sgn}(a)\pi/4}$ "
                                   r"(a Gaussian integral rotated into the complex plane). Here $a=x\phi''/2$.",
                             math=[r"\int_{-\infty}^{\infty}e^{iau^{2}}\,du=\sqrt{\frac{\pi}{|a|}}\;"
                                   r"e^{\,i\,\operatorname{sgn}(a)\pi/4},\qquad a=\frac{x\phi''}{2}"],
                             references=["base method -> library/fresnel-integral.md"]),
                    ]),
               # --- working sub-move 4: assemble the master formula + take Re (requires=working)
               dict(title="Assemble the amplitude and take the real part", requires="working",
                    prose=r"Multiply the phase factor $e^{ix\phi(\theta_0)}$ by the Fresnel result, divide by $\pi$, "
                          r"and take the real part. With $\phi(\theta_0)=1$ and $\operatorname{sgn}\phi''=-1$ this is "
                          r"$\sqrt{2/(\pi x)}\cos(x-\pi/4)$.",
                    math=[r"J_0(x)\sim\frac1\pi\operatorname{Re}\Big[\sqrt{\tfrac{2\pi}{x}}\,e^{i(x-\pi/4)}\Big]"
                          r"=\sqrt{\frac{2}{\pi x}}\cos\!\Big(x-\frac{\pi}{4}\Big)"],
                    references=["base method -> library/complex-modulus-argument.md"],
                    decompose=[
                        dict(title="Combine the two phases", requires="plain",
                             prose=r"The bulk phase $e^{ix\cdot 1}$ times the Fresnel rotation "
                                   r"$e^{-i\pi/4}$ (since $\operatorname{sgn}\phi''=-1$) gives the total angle $x-\pi/4$.",
                             math=[r"e^{ix\phi(\theta_0)}\cdot e^{i\,\operatorname{sgn}(\phi'')\pi/4}"
                                   r"=e^{ix}\,e^{-i\pi/4}=e^{i(x-\pi/4)}"]),
                        dict(title="Collect the amplitude", requires="plain",
                             prose=r"$\tfrac1\pi\sqrt{2\pi/x}=\sqrt{2/(\pi x)}$ — the $1/\sqrt{x}$ decaying envelope.",
                             math=[r"\frac{1}{\pi}\sqrt{\frac{2\pi}{x}}=\sqrt{\frac{2}{\pi x}}"]),
                        dict(title="Take the real part", requires="plain",
                             prose=r"$\operatorname{Re}\,e^{i(x-\pi/4)}=\cos(x-\pi/4)$, giving the final oscillation.",
                             math=[r"\sqrt{\frac{2}{\pi x}}\,\operatorname{Re}\,e^{i(x-\pi/4)}"
                                   r"=\sqrt{\frac{2}{\pi x}}\,\cos\!\Big(x-\frac{\pi}{4}\Big)"],
                             references=["base method -> library/eulers-formula.md"]),
                    ]),
           ])

    # ----- VERIFY: two independent checks (engine gate + SymPy equivalence) -------------------
    d.verify(
        r"Two independent checks, neither used to derive the answer. The engine's "
        r"`special_methods.stationary_phase_J0()` runs exactly this stationary-phase computation in "
        r"SymPy and returns $\sqrt{2}\,\sin(x+\pi/4)/(\sqrt{\pi}\sqrt{x})$; the cofunction identity "
        r"$\sin(x+\pi/4)=\cos(x-\pi/4)$ shows that equals our closed form. The external gate "
        r"(P2400 stationary-phase notes) asserts the SAME $\sqrt{2/(\pi x)}\cos(x-\pi/4)$.",
        math=[r"\sqrt{2}\,\frac{\sin(x+\pi/4)}{\sqrt{\pi}\sqrt{x}}"
              r"=\sqrt{\frac{2}{\pi x}}\,\cos\!\Big(x-\frac{\pi}{4}\Big)\quad(\sin(\alpha+\tfrac\pi2-\tfrac\pi4)\ \text{identity})"],
        references=["engine: special_methods.stationary_phase_J0 (SymPy executor)",
                    "external gate: external_gates.CAPABILITY_GATES['stationary_phase'] -> "
                    "phys.uconn.edu P2400 stationary-phase.pdf",
                    "method: library/stationary-phase.md"])
    d.result(
        latex=r"J_0(x)\ \sim\ \sqrt{\frac{2}{\pi x}}\,\cos\!\Big(x-\frac{\pi}{4}\Big)\qquad(x\to\infty)",
        note="derived (not quoted) by the Fresnel master formula; matches the engine's "
             "stationary_phase_J0 output and the published P2400 result.")
    return d
