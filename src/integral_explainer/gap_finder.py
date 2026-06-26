"""Gap finder: holes in the tensor space of solvers = gaps in our maths coverage.

As the corpus scales — ingesting research that has never been structured as a *maths
source* (only seen by LLM pre-training) — the hard question is not "what do we have"
but "what is MISSING". This walks the link graph of the corpus pages plus the problem
tensor space and reports the holes, so a (potentially massive) ingestion knows where to aim:

  * dangling links / methods invoked with NO page — a promised connection we can't make;
  * orphan + under-connected pages — isolated knowledge that should link in;
  * asymmetric links — a one-way "see also" (the reverse edge is missing);
  * DOMAIN coverage vs the target domains — whole areas of maths we don't cover yet;
  * a prioritized "ingest next" list — the highest-leverage holes first.

Cheap (graph-structural, not content), so it scales to thousands of pages.
"""
from __future__ import annotations

# the maths this system aims to cover (CLAUDE.md / PLAN vision), base → advanced
TARGET_DOMAINS = ("algebra", "trigonometry", "calculus", "tensor", "special-function",
                  "asymptotics", "regularization", "transform", "pde", "linear-algebra")


def analyze(patterns, tensor_spaces=(), target_domains=TARGET_DOMAINS) -> dict:
    """patterns: corpus Pattern pages. tensor_spaces: iterable of ProblemGraph.to_dict()
    (the solved problems). Returns a structured gap report."""
    ids = {p.id for p in patterns}
    out_links = {p.id: set(p.links) for p in patterns}
    in_deg = {pid: 0 for pid in ids}

    dangling = []
    for p in patterns:
        for l in p.links:
            if l in ids:
                in_deg[l] += 1
            else:
                dangling.append((p.id, l))

    # methods invoked by the tensor spaces (SolverNode.method) that have no corpus page
    invoked: dict = {}
    for ts in tensor_spaces:
        for n in ts.get("nodes", []):
            m = n.get("method")
            if m:
                invoked.setdefault(m, []).append(n["id"])
    missing_methods = {m: who for m, who in invoked.items() if m not in ids}

    orphans = sorted(pid for pid, d in in_deg.items() if d == 0)
    deg = {pid: in_deg[pid] + len(out_links[pid]) for pid in ids}
    low_degree = sorted(pid for pid in ids if deg[pid] <= 1)
    asym = [(p.id, l) for p in patterns for l in p.links
            if l in ids and p.id not in out_links.get(l, set())]

    by_domain: dict = {}
    for p in patterns:
        by_domain[p.domain] = by_domain.get(p.domain, 0) + 1
    uncovered = [d for d in target_domains if by_domain.get(d, 0) == 0]
    thin = [d for d in target_domains if 0 < by_domain.get(d, 0) <= 3]

    return {
        "n_pages": len(patterns),
        "dangling_links": dangling,
        "missing_methods": missing_methods,
        "orphan_pages": orphans,
        "low_degree_pages": low_degree,
        "asymmetric_links": asym,
        "domain_coverage": dict(sorted(by_domain.items())),
        "uncovered_domains": uncovered,
        "thin_domains": thin,
    }


def ingest_priorities(report) -> list:
    """Rank what to add next — highest-leverage holes first. The ingestion spec."""
    pri = []
    for m, who in report["missing_methods"].items():
        pri.append((1, f"WRITE METHOD '{m}' — invoked by {who} but has no page"))
    for src, dst in report["dangling_links"]:
        pri.append((1, f"WRITE PAGE '{dst}' — linked from [[{src}]] but missing"))
    for d in report["uncovered_domains"]:
        pri.append((2, f"OPEN DOMAIN '{d}' — 0 pages; a whole target area uncovered"))
    for d in report["thin_domains"]:
        pri.append((3, f"DEEPEN domain '{d}' — only {report['domain_coverage'][d]} page(s)"))
    for pid in report["orphan_pages"]:
        pri.append((4, f"CONNECT '{pid}' — nothing links to it (orphan)"))
    pri.sort(key=lambda x: x[0])
    return [msg for _, msg in pri]
