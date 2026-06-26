"""integral-explainer: a method-explanation engine for hard/divergent integrals.

Not a solver. The goal is to expose *which method applies and why* (the
recognition step), verified numerically for divergent objects.

See DESIGN.md for the architecture and starting milestones.
"""

__version__ = "0.0.1"

from .trace import (MethodTrace, Step, render_leveled, validate_explanation,
                    validate_levels, validate_qualification, validate_references)
from .derivation import Derivation
from .problem_graph import ProblemGraph, SolverNode
from .gap_finder import analyze as find_gaps, ingest_priorities, TARGET_DOMAINS
from .methods import METHODS, Method
from .problem import Problem, Goal
from .library import (Pattern, load_patterns, recognize as recognize_pattern,
                      trace_from_pattern, leveled_trace_from_pattern)
from .proposer import propose, propose_with_llm, build_recognition_prompt
from .executor import reduce_integral, ExecResult, verify_closed_form
from .oracle import high_precision, high_precision_osc, recognize, agree

__all__ = [
    "MethodTrace", "Step", "render_leveled", "validate_explanation", "validate_levels",
    "validate_qualification", "validate_references", "Derivation", "ProblemGraph", "SolverNode",
    "find_gaps", "ingest_priorities", "TARGET_DOMAINS",
    "METHODS", "Method",
    "Problem", "Goal",
    "Pattern", "load_patterns", "recognize_pattern", "trace_from_pattern",
    "leveled_trace_from_pattern",
    "propose", "propose_with_llm", "build_recognition_prompt",
    "reduce_integral", "ExecResult", "verify_closed_form",
    "high_precision", "high_precision_osc", "recognize", "agree",
    "__version__",
]
