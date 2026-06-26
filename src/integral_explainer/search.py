"""Solving as SEARCH — the engine's strategy layer.

LESSON (James, 2026-06-24, from the is_zero polynomial-in-derivatives episode): a solve is
NOT a straight line from problem to answer. Three principles, which together turn solving from
a fixed pipeline into a best-first search over a graph of (state, method):

  (1) DECOMPOSE and push back. A hard goal often can't be hit head-on; split it into a
      sub-problem, solve that, recombine. (is_zero only saw the geodesic cancel after it
      replaced the derivative atoms with plain symbols — a simpler sub-problem — then expanded.)

  (2) BACKTRACK, possibly far. A chosen route dead-ends (simplify stalls, `equals` returns
      None). Like a route-finder going down a road that turns out not to connect, abandon the
      branch and resume elsewhere. The engine must be able to FAIL a branch, not commit to its
      first idea.

  (3) COST is the compass. A monstrous intermediate/result is a SIGNAL to keep looking for a
      cheaper route, not a reason to stop. Complexity is the search heuristic and the
      tie-breaker among successes.

States are (sub-)problems; strategies are transformations (edges); `goal_test` recognises a
solved state; `cost` is its complexity. This is the executable form of the "tensor space of
solvers": methods are nodes, applications are edges, solving walks the graph, and regions no
strategy reaches are the gaps in our coverage. The returned trace (route + dead-ends) is the
route-finder's tracklog — you can SEE where it went wrong.
"""
import heapq
import itertools

import sympy as sp


class Strategy:
    """A named transformation. `expand(state)` returns an iterable of successor states
    (an empty iterable = this route dead-ends here)."""

    def __init__(self, name, expand):
        self.name, self.expand = name, expand


def complexity(state):
    """Default cost / heuristic: structural size."""
    return sp.count_ops(state) if isinstance(state, sp.Basic) else len(repr(state))


def _key(state):
    return sp.srepr(state) if isinstance(state, sp.Basic) else repr(state)


def search(start, strategies, goal_test, *, cost=complexity, budget=400):
    """Best-first search with backtracking.

    Explores the cheapest frontier state first; a state that no strategy can advance is a
    dead-end (recorded, not fatal — the frontier carries the backtrack). Keeps going after the
    first success so a cheaper route can win. Returns the best (lowest-cost) solution, the full
    solution list, the dead-ends, and how many states were expanded — an inspectable tracklog."""
    tie = itertools.count()
    frontier = [(cost(start), next(tie), start, [])]
    seen, deadends, solutions = set(), [], []
    expansions = 0
    while frontier and expansions < budget:
        _, _, state, route = heapq.heappop(frontier)
        k = _key(state)
        if k in seen:
            continue
        seen.add(k)
        expansions += 1
        if goal_test(state):
            solutions.append((cost(state), state, route))
            continue                                      # a cheaper route may still exist
        moved = False
        for strat in strategies:
            for succ in strat.expand(state):
                moved = True
                heapq.heappush(frontier, (cost(succ), next(tie), succ, route + [strat.name]))
        if not moved:
            deadends.append((state, route))               # this road doesn't connect
    solutions.sort(key=lambda t: t[0])
    return {
        "best": solutions[0] if solutions else None,      # (cost, state, route)
        "solutions": solutions,
        "deadends": deadends,
        "expansions": expansions,
    }
