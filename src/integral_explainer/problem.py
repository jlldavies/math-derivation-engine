"""Problem: the structured input — how a user poses a question.

The input is a triple (see PLAN.md §4):
  * expression  — LaTeX / math string, the precise channel;
  * represents  — what it represents (meaning / context); for tensors the
    *essential* data (metric, coordinates, declared symmetries, index ranges);
  * goal        — what they want done.

A natural-language front-end (M1) formalizes a word description into this triple;
for now a Problem is constructed directly. `MethodTrace.from_problem(p)` builds the
trace header (the input equation + caption) straight from it.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Goal(str, Enum):
    EVALUATE = "evaluate"      # compute a closed form / value
    SIMPLIFY = "simplify"      # reduce to a simpler equivalent form
    EXPAND = "expand"          # asymptotic / series expansion
    PROVE = "prove"            # prove an identity / statement
    RECOGNIZE = "recognize"    # which method/pattern applies, and why


@dataclass
class Problem:
    latex: str                                    # the expression (precise channel)
    represents: str = ""                          # what it represents (meaning / context)
    goal: "Goal | str" = Goal.EVALUATE
    context: dict = field(default_factory=dict)   # domain data: metric, coords, symmetries, index ranges, ...
    integral: str = ""                            # optional plain-text id (markdown title / fallback)

    def goal_str(self) -> str:
        return self.goal.value if isinstance(self.goal, Goal) else str(self.goal)

    def caption(self) -> str:
        """Prose subtitle for the trace header: what it represents + the goal."""
        bits = []
        if self.represents:
            bits.append(self.represents)
        bits.append(f"goal: {self.goal_str()}")
        return "  ·  ".join(bits)
