r"""LEVELED Derivation for METHOD komar_mass (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.komar_mass_schwarzschild. The engine DERIVES the Komar mass of
the Schwarzschild black hole,
    M_Komar = -(1/8 pi) oint_S nabla^a xi^b dS_ab = M,
from the timelike Killing vector xi=d/dt: it takes the Christoffel symbols from the curvature engine,
lowers xi to the 1-form xi_a=g_at, forms nabla_a xi_b = d_a xi_b - Gamma^c_ab xi_c (antisymmetric =>
xi Killing), raises and contracts with the r=const 2-sphere surface element, and integrates. The
intermediates nabla^t xi^r=-M/r^2 and the -8 pi M flux EMERGE; nothing is written in. The GR
conserved charge of time-translation symmetry.

Sub-methods referenced by the steps:
    komar_mass -> { Killing 1-form xi_a=g_ab xi^b, covariant derivative nabla_a xi_b via the
                    curvature engine's Christoffel symbols, oriented 2-sphere surface element dS_ab,
                    sphere integral }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"M_{\text{Komar}}=-\frac{1}{8\pi}\oint_{S}\nabla^{a}\xi^{b}\,dS_{ab}"
       r"\ \xrightarrow{\text{Schwarzschild},\ \xi=\partial_t}\ M")


def build_komar_mass_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the Komar mass of the Schwarzschild black hole — the conserved charge of the "
                   r"timelike Killing vector $\xi=\partial_t$, the GR notion of total energy at infinity",
        goal=Goal.EVALUATE,
        integral="Komar mass of Schwarzschild = M via the Killing-vector surface integral")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — a conserved charge from the time-translation symmetry",
          {"plain": r"Schwarzschild spacetime does not change in time, so it has a time-translation symmetry "
                    r"(a Killing vector $\xi=\partial_t$). Noether-style, that symmetry carries a conserved "
                    r"charge — the total mass — and we collect it as a flux integral over a big sphere, just "
                    r"like reading a total electric charge off a surface in Gauss's law.",
           "working": r"The Komar integral $M=-\tfrac{1}{8\pi}\oint\nabla^a\xi^b\,dS_{ab}$ is the conserved charge "
                      r"of the timelike Killing vector $\xi=\partial_t$. The antisymmetric 'Komar potential' "
                      r"$\nabla^a\xi^b$ plays the role of the field strength, and the closed surface flux gives the "
                      r"mass — independent of the radius of the sphere in vacuum.",
           "expert": r"For a stationary, asymptotically-flat spacetime the Komar mass is the Noether charge of "
                     r"$\xi=\partial_t$: $M=-\tfrac{1}{8\pi}\oint_{S}\nabla^a\xi^b\,dS_{ab}$, equivalently "
                     r"$\tfrac{1}{4\pi}\oint R^a{}_b\xi^b dS_a$ on shell. On Schwarzschild it returns the parameter $M$."},
          forced_by=r"Schwarzschild is stationary ($\partial_t$ Killing) and asymptotically flat, so a Killing-vector "
                    r"surface integral is exactly the conserved energy — and $\nabla_{(a}\xi_{b)}=0$ makes "
                    r"$\nabla^a\xi^b$ the antisymmetric flux of a genuine charge.",
          payoff=r"the exact charge $M$ as a closed-form function of the metric parameter — the geometric meaning "
                 r"(total energy seen at infinity), not a number; a quadrature would lose the $M$-dependence and the "
                 r"radius-independence.",
          relies_on=r"$\xi=\partial_t$ being Killing ($\nabla_{(a}\xi_{b)}=0$), the metric being stationary and "
                    r"asymptotically flat, and the surface element $dS_{ab}=(n_a u_b-n_b u_a)\sqrt{\sigma}\,d\theta\,d\phi$ "
                    r"of the $r=$const 2-sphere.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — lower the Killing vector, take its covariant curl, flux it through the sphere",
          {"plain": r"Write the Killing vector as a 1-form $\xi_a=g_{at}$, take its covariant derivative "
                    r"$\nabla_a\xi_b$ (which uses the Christoffel symbols of the metric), raise the indices, and add "
                    r"up its flow through a sphere of radius $r$. The $r$'s cancel and out drops $M$.",
           "working": r"$\xi^a=\delta^a_t\Rightarrow\xi_a=g_{a t}$; then $\nabla_a\xi_b=\partial_a\xi_b-\Gamma^c{}_{ab}\xi_c$ "
                      r"(antisymmetric, since $\xi$ is Killing). Raise to $\nabla^a\xi^b$, contract with the oriented "
                      r"area element $(n_au_b-n_bu_a)\sqrt{\sigma}$ and integrate over $\theta,\phi$.",
           "expert": r"$\nabla^a\xi^b$ is the antisymmetric Komar 2-form; on Schwarzschild its $tr$ component is "
                     r"$\nabla^t\xi^r=-M/r^2$, and $\nabla^a\xi^b(n_au_b-n_bu_a)=-2M/r^2$ with $\sqrt{\sigma}=r^2\sin\theta$, "
                     r"so the flux is $-8\pi M$ and $M_{\text{Komar}}=-\tfrac1{8\pi}(-8\pi M)=M$."},
          math=[r"\xi^a=\delta^a_t,\quad \xi_a=g_{at},\quad \nabla_a\xi_b=\partial_a\xi_b-\Gamma^c{}_{ab}\xi_c,"
                r"\quad dS_{ab}=(n_au_b-n_bu_a)\sqrt{\sigma}\,d\theta\,d\phi"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Build the Komar integral and read off M", requires="expert",
           prose=r"Take $\xi=\partial_t$ on Schwarzschild, form $\nabla^a\xi^b$ from the Christoffel symbols, "
                 r"contract with the 2-sphere surface element and integrate: $M_{\text{Komar}}=M$.",
           math=[r"M_{\text{Komar}}=-\frac1{8\pi}\oint\nabla^a\xi^b\,dS_{ab}=M"],
           references=["sub-method: komar_mass -> {Killing 1-form, covariant derivative via Christoffel, "
                       "oriented 2-sphere surface element, sphere integral}"],
           decompose=[
               dict(title="Lower the Killing vector to a 1-form", requires="working",
                    prose=r"$\xi=\partial_t$ has components $\xi^a=\delta^a_t$; lower with the metric: "
                          r"$\xi_a=g_{ab}\xi^b=g_{at}=(-(1-2M/r),0,0,0)$.",
                    math=[r"\xi^a=(1,0,0,0),\qquad \xi_a=g_{at}=\big({-}(1-\tfrac{2M}{r}),0,0,0\big)"],
                    references=["sub-method: Killing 1-form xi_a = g_ab xi^b"],
                    decompose=[
                        dict(title="What 'lowering an index' means", requires="plain",
                             prose=r"Multiplying the vector by the metric $g_{ab}$ turns the up-vector $\xi^b$ into the "
                                   r"down-1-form $\xi_a$; with a diagonal metric only the $tt$ entry contributes.",
                             math=[r"\xi_a=\sum_b g_{ab}\xi^b=g_{at}\cdot 1"]),
                    ]),
               dict(title="Covariant derivative via the Christoffel symbols", requires="working",
                    prose=r"$\nabla_a\xi_b=\partial_a\xi_b-\Gamma^c{}_{ab}\xi_c$, with $\Gamma$ supplied by the curvature "
                          r"engine. Because $\xi$ is Killing, $\nabla_a\xi_b$ comes out antisymmetric; the nonzero entry "
                          r"is $\nabla_r\xi_t=-M/r^2$.",
                    math=[r"\nabla_a\xi_b=\partial_a\xi_b-\Gamma^c{}_{ab}\xi_c,\qquad \nabla_{(a}\xi_{b)}=0,"
                          r"\qquad \nabla_r\xi_t=-\tfrac{M}{r^2}"],
                    references=["sub-method: covariant derivative nabla_a xi_b (Christoffel from curvature engine)"],
                    decompose=[
                        dict(title="The covariant-derivative formula", requires="plain",
                             prose=r"A covariant derivative is the ordinary derivative plus a Christoffel correction that "
                                   r"accounts for the curved coordinates: $\nabla_a\xi_b=\partial_a\xi_b-\Gamma^c{}_{ab}\xi_c$.",
                             math=[r"\nabla_a\xi_b=\partial_a\xi_b-\Gamma^c{}_{ab}\xi_c"]),
                        dict(title="Killing means the symmetric part vanishes", requires="plain",
                             prose=r"$\xi=\partial_t$ is a symmetry of the metric, so $\nabla_a\xi_b+\nabla_b\xi_a=0$: only "
                                   r"the antisymmetric 'curl' part survives.",
                             math=[r"\nabla_a\xi_b+\nabla_b\xi_a=0"]),
                    ]),
               dict(title="Raise indices and contract with the surface element", requires="working",
                    prose=r"Raise: $\nabla^a\xi^b=g^{ac}g^{bd}\nabla_c\xi_d$; with the unit timelike/radial normals "
                          r"$u_a,n_a$ the projection is $\nabla^a\xi^b(n_au_b-n_bu_a)=-2M/r^2$, and the area density is "
                          r"$\sqrt{\sigma}=r^2\sin\theta$.",
                    math=[r"\nabla^a\xi^b(n_au_b-n_bu_a)=-\tfrac{2M}{r^2},\qquad \sqrt{\sigma}=r^2\sin\theta"],
                    references=["sub-method: oriented 2-sphere surface element dS_ab"],
                    decompose=[
                        dict(title="Raising indices with the inverse metric", requires="plain",
                             prose=r"Multiplying by $g^{ac}g^{bd}$ pulls both indices up; this is the inverse operation to "
                                   r"lowering.",
                             math=[r"\nabla^a\xi^b=g^{ac}g^{bd}\nabla_c\xi_d"]),
                        dict(title="The r's cancel in the projection", requires="plain",
                             prose=r"The $1/r^2$ from $\nabla^a\xi^b$ multiplies the $r^2$ in the area element, so the "
                                   r"integrand is radius-independent — the hallmark of a conserved charge.",
                             math=[r"\Big({-}\tfrac{2M}{r^2}\Big)\,r^2\sin\theta=-2M\sin\theta"]),
                    ]),
               dict(title="Integrate over the sphere", requires="plain",
                    prose=r"Integrate $-2M\sin\theta$ over $\theta\in[0,\pi],\phi\in[0,2\pi]$: $\int\sin\theta\,d\theta=2$, "
                          r"$\int d\phi=2\pi$, giving flux $-8\pi M$; then $-\tfrac1{8\pi}(-8\pi M)=M$.",
                    math=[r"-\frac{1}{8\pi}\int_0^{2\pi}\!\!\int_0^{\pi}(-2M\sin\theta)\,d\theta\,d\phi"
                          r"=-\frac{1}{8\pi}(-8\pi M)=M"],
                    references=["base method -> library/covariant-derivative.md"]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `komar_mass_schwarzschild()` builds the Schwarzschild metric, takes the Christoffel "
        r"symbols from the curvature engine, forms $\nabla_a\xi_b=\partial_a\xi_b-\Gamma^c{}_{ab}\xi_c$ (verified "
        r"antisymmetric, i.e. $\xi$ Killing), raises and contracts with the 2-sphere element, and integrates — "
        r"returning exactly $M$, the Schwarzschild mass parameter. Nothing is written in: $\nabla^t\xi^r=-M/r^2$ and "
        r"the $-8\pi M$ flux EMERGE from the differentiation. Matches Wald GR ch.11 and Poisson's Relativist's "
        r"Toolkit \S4.3.3.",
        math=[r"\nabla^t\xi^r=-\tfrac{M}{r^2},\quad \oint\nabla^a\xi^b dS_{ab}=-8\pi M\ \Rightarrow\ M_{\text{Komar}}=M",
              r"\text{Wald, GR ch.11; Poisson, A Relativist's Toolkit }\S4.3.3"],
        references=["engine: special_methods.komar_mass_schwarzschild (curvature engine -> Christoffel, "
                    "Killing-vector surface integral)",
                    "R. M. Wald, General Relativity, ch.11 (Komar mass)",
                    "E. Poisson, A Relativist's Toolkit, sec.4.3.3 (Komar integrals)",
                    "P. Townsend, Black Holes (gr-qc/9707012), Komar mass"])
    d.result(
        latex=r"M_{\text{Komar}}=-\frac{1}{8\pi}\oint_{S}\nabla^{a}\xi^{b}\,dS_{ab}=M",
        note="the Komar mass of Schwarzschild derived from xi=d/dt via the curvature engine's Christoffel symbols "
             "(nabla^t xi^r=-M/r^2 emerges; nothing written in) — the GR conserved charge of time-translation symmetry.")
    return d