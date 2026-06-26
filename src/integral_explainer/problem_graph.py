"""ProblemGraph: nested problems as a DAG of solvers — the 'tensor space'.

A real problem usually decomposes into SUB-PROBLEMS solved in sequence (one's result
feeds the next), and sub-problems are SHARED across branches (Z₁ appears in every
Blitz correlator; the Tricomi-U reduction under all of them). This represents that
as a directed acyclic graph:

  * a node is a (sub-)problem;
  * `deps` are the sub-problems it needs solved FIRST (the 'spot nested problems,
    solve in sequence' requirement — a node with deps is nested, a leaf is atomic);
  * `method` links the node to the corpus page that solves it (an edge into the wiki).

Solving = a dependency-ordered walk (leaves first). The graph itself is the navigable
space of solvers; a well-mapped space makes GAPS visible (a needed reduction with no
method, a dangling 'reduces to X' with no X). Persist + accumulate it across problems.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SolverNode:
    id: str
    title: str = ""
    method: str = ""              # corpus method-page id that solves this (edge into the wiki)
    deps: tuple = ()              # sub-problem ids needed first (solved in sequence)
    solve: object = None          # callable(results: dict, ctx: dict) -> value
    note: str = ""

    @property
    def nested(self) -> bool:
        return bool(self.deps)


class ProblemGraph:
    def __init__(self):
        self.nodes: dict = {}

    def add(self, node: SolverNode) -> "ProblemGraph":
        self.nodes[node.id] = node
        return self

    def order(self) -> list:
        """Topological order (deps before dependents). Raises on a cycle or a dangling dep."""
        seen, temp, out = set(), set(), []

        def visit(nid):
            if nid in seen:
                return
            if nid not in self.nodes:
                raise KeyError(f"dangling dependency: '{nid}' is needed but has no solver node")
            if nid in temp:
                raise ValueError(f"dependency cycle at '{nid}'")
            temp.add(nid)
            for d in self.nodes[nid].deps:
                visit(d)
            temp.discard(nid)
            seen.add(nid)
            out.append(nid)

        for nid in self.nodes:
            visit(nid)
        return out

    def solve(self, ctx: dict | None = None) -> dict:
        """Solve every node deps-first. Returns {id: value}."""
        ctx = ctx or {}
        results: dict = {}
        for nid in self.order():
            n = self.nodes[nid]
            results[nid] = n.solve(results, ctx) if n.solve else None
        return results

    def nested_problems(self) -> list:
        return [n.id for n in self.nodes.values() if n.nested]

    def shared_nodes(self) -> dict:
        """Nodes depended on by MORE THAN ONE other node (the interlinks: Z₁, Tricomi)."""
        indeg: dict = {nid: 0 for nid in self.nodes}
        for n in self.nodes.values():
            for d in n.deps:
                indeg[d] = indeg.get(d, 0) + 1
        return {nid: deg for nid, deg in indeg.items() if deg > 1}

    def edges(self) -> list:
        """The tensor space: ('feeds', child, parent) dependency edges and
        ('method', method_page, node) solved-by edges into the corpus."""
        e = []
        for n in self.nodes.values():
            for d in n.deps:
                e.append(("feeds", d, n.id))
            if n.method:
                e.append(("method", n.method, n.id))
        return e

    def to_dict(self) -> dict:
        return {"nodes": [{"id": n.id, "title": n.title, "method": n.method,
                           "deps": list(n.deps), "note": n.note} for n in self.nodes.values()],
                "edges": [list(x) for x in self.edges()]}

    def render_tree(self, root: str, results: dict | None = None, fmt=str, _ind: int = 0) -> str:
        """ASCII dependency tree under `root` (shared nodes appear under each parent —
        that's the view; `shared_nodes()` reveals they're one node in the DAG)."""
        n = self.nodes[root]
        tag = f"  [{n.method}]" if n.method else ""
        val = ""
        if results and results.get(root) is not None:
            try:
                val = f"  = {fmt(results[root])}"
            except Exception:
                val = ""
        lines = ["    " * _ind + f"{'└─ ' if _ind else ''}{n.title or n.id}{tag}{val}"]
        for d in n.deps:
            lines.append(self.render_tree(d, results, fmt, _ind + 1))
        return "\n".join(lines)
