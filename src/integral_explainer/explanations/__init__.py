"""Per-method leveled Derivations (rule 7 + 11): EXPLANATIONS maps method key -> a builder
returning a validated Derivation. Built by the method-explanations ultracode campaign."""
from .parts import build_parts_derivation
from .partial_fractions import build_partial_fractions_derivation
from .meijer_g import build_meijer_g_derivation
from .contour import build_contour_derivation
from .feynman_parameter import build_feynman_parameter_derivation
from .mellin import build_mellin_derivation
from .zeta_reg import build_zeta_reg_derivation
from .analytic_continuation import build_analytic_continuation_derivation
from .asymptotic_expansion import build_asymptotic_expansion_derivation
from .gamma_ratio_asymptotic import build_gamma_ratio_asymptotic_derivation
from .oscillator_commutator import build_oscillator_commutator_derivation
from .dilogarithm import build_dilogarithm_derivation
from .wigner_surmise import build_wigner_surmise_derivation
from .q_pochhammer import build_q_pochhammer_derivation
from .bessel_hankel import build_bessel_hankel_derivation
from .airy import build_airy_derivation
from .casimir import build_casimir_derivation
from .conformal_casimir import build_conformal_casimir_derivation
from .conformal_block import build_conformal_block_derivation
from .jacobi_trudi import build_jacobi_trudi_derivation
from .komar_mass import build_komar_mass_derivation
from .confluent_0F1 import build_confluent_0F1_derivation
from .sturm_liouville import build_sturm_liouville_derivation
from .stationary_phase import build_stationary_phase_derivation
from .sym_antisym import build_sym_antisym_derivation
from .u_sub import build_u_sub_derivation
from .abel_plana import build_abel_plana_derivation
from .euler_maclaurin import build_euler_maclaurin_derivation
from .dim_reg import build_dim_reg_derivation
from .hyperbolic_exp_rewrite import build_hyperbolic_exp_rewrite_derivation
from .inverse_function_parts import build_inverse_function_parts_derivation
from .complete_square_sub import build_complete_square_sub_derivation

EXPLANATIONS = {
    'complete_square_sub': build_complete_square_sub_derivation,
    'inverse_function_parts': build_inverse_function_parts_derivation,
    'hyperbolic_exp_rewrite': build_hyperbolic_exp_rewrite_derivation,
    'parts': build_parts_derivation,
    'partial_fractions': build_partial_fractions_derivation,
    'meijer_g': build_meijer_g_derivation,
    'contour': build_contour_derivation,
    'feynman_parameter': build_feynman_parameter_derivation,
    'mellin': build_mellin_derivation,
    'zeta_reg': build_zeta_reg_derivation,
    'analytic_continuation': build_analytic_continuation_derivation,
    'asymptotic_expansion': build_asymptotic_expansion_derivation,
    'gamma_ratio_asymptotic': build_gamma_ratio_asymptotic_derivation,
    'oscillator_commutator': build_oscillator_commutator_derivation,
    'dilogarithm': build_dilogarithm_derivation,
    'wigner_surmise': build_wigner_surmise_derivation,
    'q_pochhammer': build_q_pochhammer_derivation,
    'bessel_hankel': build_bessel_hankel_derivation,
    'airy': build_airy_derivation,
    'casimir': build_casimir_derivation,
    'conformal_casimir': build_conformal_casimir_derivation,
    'conformal_block': build_conformal_block_derivation,
    'jacobi_trudi': build_jacobi_trudi_derivation,
    'komar_mass': build_komar_mass_derivation,
    'confluent_0F1': build_confluent_0F1_derivation,
    'sturm_liouville': build_sturm_liouville_derivation,
    'stationary_phase': build_stationary_phase_derivation,
    'sym_antisym': build_sym_antisym_derivation,
    'u_sub': build_u_sub_derivation,
    'abel_plana': build_abel_plana_derivation,
    'euler_maclaurin': build_euler_maclaurin_derivation,
    'dim_reg': build_dim_reg_derivation,
}
