"""MethodTrace: the structured record the engine emits — the deliverable.

The 'explain' step is the whole point, and it must be *followable*: every step
breaks down into the sub-steps a person could do by hand, and every numeric step
spells out the actual loop that runs. A trace is therefore a TREE of `Step`
nodes, each carrying:

  * a title and the worked `detail` (multi-line math, or what the loop does);
  * an optional `method_key` -> registry name + references (the pedagogical payload);
  * optional `references` of its own (e.g. the specific quadrature scheme);
  * an optional `check` (how this step was verified);
  * `children` — nested sub-steps, arbitrarily deep.

It renders to three consumable forms:
  * `render_markdown()` — nested bullets, to read / reproduce;
  * `render_json()` / `to_dict()` — the tree, to consume programmatically;
  * `render_html()` — nested <details>/<summary>, expandable, to view on a screen.

The old flat `Step(method_key, before, after, justification, check)` call still
works — those fields render as a leaf node.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import json
import re

try:
    from latex2mathml.converter import convert as _latex_to_mathml
    _HAS_L2M = True
except Exception:  # optional — without it we fall back to KaTeX (needs a CDN)
    _HAS_L2M = False


# \Big[ … \Big]_0^1 renders the closing bracket half-height in MathML (a fixed maxsize
# <mo> shrinks as a sub/sup base). Stretchy \left..\right is reliable — normalise to it.
_OPEN = {"[", "(", r"\{", r"\langle", r"\lfloor", r"\lceil"}
_BIG_RE = re.compile(r"\\(?:bigg?|Bigg?)([lrm])?\s*"
                     r"(\\\{|\\\}|\\lfloor|\\rfloor|\\lceil|\\rceil|\\langle|\\rangle|[\[\]()])")


def _normalize_delims(s: str) -> str:
    def repl(m):
        suf, d = m.group(1), m.group(2)
        side = "left" if (suf == "l" or (suf != "r" and d in _OPEN)) else "right"
        return f"\\{side}{d}"
    return _BIG_RE.sub(repl, s)


def _render_math(latex: str, *, block: bool = True) -> str:
    """LaTeX -> self-contained MathML (native, no JS/CDN). `block` for display
    equations, inline otherwise. Falls back to \\[..\\] / \\(..\\) delimiters."""
    if _HAS_L2M:
        # \tfrac renders cramped in MathML; \frac is full size. \Big-family -> \left/\right.
        base = latex.replace(r"\tfrac", r"\frac")
        for cand in (_normalize_delims(base), base):   # normalised first, original as fallback
            try:
                ml = _latex_to_mathml(cand)
                if block:  # latex2mathml emits display="inline"; promote to block (centred)
                    if 'display="inline"' in ml:
                        ml = ml.replace('display="inline"', 'display="block"', 1)
                    elif ml.startswith("<math") and "display=" not in ml.split(">", 1)[0]:
                        ml = ml.replace("<math", '<math display="block"', 1)
                return ml
            except Exception:
                continue
    return ("\\[" + latex + "\\]") if block else ("\\(" + latex + "\\)")


_INLINE_RE = re.compile(r"`([^`]+)`|\$([^$]+)\$")


def _inline(text: str) -> str:
    """Render prose with inline `code` and $math$ spans (HTML); plain text escaped.

    Lets explanations and titles carry typeset math (e.g. "an $\\alpha^{-1/2}$
    endpoint") and code (e.g. "`mp.quadosc(...)`") rather than plain unicode."""
    if not text:
        return ""
    out, last = [], 0
    for m in _INLINE_RE.finditer(text):
        out.append(_esc(text[last:m.start()]))
        if m.group(1) is not None:
            out.append(f"<code>{_esc(m.group(1))}</code>")
        else:
            out.append(_render_math(m.group(2), block=False))
        last = m.end()
    out.append(_esc(text[last:]))
    return "".join(out)


def _lookup(method_key: str):
    try:
        from .methods import METHODS
        return METHODS.get(method_key)
    except Exception:
        return None


def classify_check(check: str) -> tuple[str, str]:
    """Map a check string to (label, kind) with kind in {symbolic,numeric,pslq,none}."""
    c = (check or "").strip()
    low = c.lower()
    if low.startswith("symbolic"):
        return ("symbolic identity", "symbolic")
    if low.startswith("numeric"):
        rest = c.split(":", 1)[1] if ":" in c else ""
        return (f"numeric{(' · ' + rest) if rest else ''}", "numeric")
    if low.startswith("pslq"):
        rest = c.split(":", 1)[1] if ":" in c else ""
        return (f"recognized{(' · ' + rest) if rest else ''}", "pslq")
    if low in ("", "unverified"):
        return ("", "none")
    return (c, "numeric")


@dataclass
class Step:
    # new tree fields
    title: str = ""
    rationale: str = ""                           # WHY this method was chosen (the recognition step)
    # structured DECISION rationale (deeper than rationale; for real design choices)
    forced_by: str = ""                           # the structural facts that make this the move
    payoff: str = ""                              # what it buys, vs what the alternative costs
    relies_on: str = ""                           # the assumption/scope that could break it
    math: tuple = ()                              # display equations, LaTeX (typeset with MathML)
    detail: str = ""                              # prose / what the loop does (multi-line, monospace)
    work: tuple = ()                              # typeset derivation lines (LaTeX), shown ABOVE the result
    section: str = "step"                         # explanation-contract band: "why" / "how" / "step"
    requires: str = "plain"                       # qualification to grasp this step as ONE unit
                                                  # (plain<working<expert); drives the per-level cut
    children: list = field(default_factory=list)  # nested sub-steps
    references: tuple = ()                         # this node's own citations
    # registry link + verification
    method_key: str = ""
    check: str = ""
    # backward-compatible flat fields
    before: str = ""
    after: str = ""
    justification: str = ""
    altitudes: dict = field(default_factory=dict)   # level -> explanation (expert / working / plain)

    def has_decision(self) -> bool:
        return bool(self.forced_by or self.payoff or self.relies_on)

    def has_altitudes(self) -> bool:
        return bool(self.altitudes)

    def add(self, child: "Step") -> "Step":
        self.children.append(child)
        return self

    def heading(self) -> str:
        if self.title:
            return self.title
        m = _lookup(self.method_key)
        return m.name if m else (self.method_key or "step")

    def all_references(self) -> list[str]:
        m = _lookup(self.method_key)
        regrefs = list(m.references) if m else []
        return list(self.references) + [r for r in regrefs if r not in self.references]

    def to_dict(self) -> dict:
        label, kind = classify_check(self.check)
        return {
            "heading": self.heading(),
            "method_key": self.method_key or None,
            "rationale": self.rationale or None,
            "decision": ({"forced_by": self.forced_by or None,
                          "payoff": self.payoff or None,
                          "relies_on": self.relies_on or None}
                         if self.has_decision() else None),
            "justification": self.justification or None,
            "altitudes": self.altitudes or None,
            "math": list(self.math),
            "detail": self.detail or None,
            "transform": ({"before": self.before, "after": self.after}
                          if (self.before or self.after) else None),
            "check": self.check or None,
            "check_label": label,
            "check_kind": kind,
            "references": self.all_references(),
            "children": [c.to_dict() for c in self.children],
        }


@dataclass
class MethodTrace:
    integral: str                  # short text id (markdown title, plain fallback)
    integral_latex: str = ""       # LaTeX for the header input equation (typeset)
    caption: str = ""              # prose subtitle under the input
    steps: list = field(default_factory=list)
    result: str | None = None      # prose note on the result
    result_latex: str = ""         # LaTeX for the result equation (typeset)

    def add(self, step: Step) -> "MethodTrace":
        self.steps.append(step)
        return self

    @classmethod
    def from_problem(cls, problem) -> "MethodTrace":
        """Build a trace whose header is the input equation + caption from a
        Problem (duck-typed: needs `.latex` and `.caption()`)."""
        return cls(integral=getattr(problem, "integral", "") or problem.latex,
                   integral_latex=problem.latex,
                   caption=problem.caption())

    # ----- form 1: markdown (read / reproduce) ----------------------------
    def render_markdown(self) -> str:
        if self.integral_latex:
            head = "# Method trace\n\n$$\\displaystyle " + self.integral_latex + "$$\n"
            if self.caption:
                head += f"\n*{self.caption}*\n"
        else:
            head = f"# Method trace for `{self.integral}`\n"
        body = "\n".join(_md_node(s, 0) for s in self.steps)
        if self.result_latex:
            tail = "\n\n**Result:**\n\n$$\\displaystyle " + self.result_latex + "$$"
            if self.result:
                tail += f"\n\n{self.result}"
        elif self.result:
            tail = f"\n\n**Result:** `{self.result}`"
        else:
            tail = ""
        return f"{head}\n{body}{tail}\n"

    render = render_markdown

    # ----- form 2: structured tree (programmatic) -------------------------
    def to_dict(self) -> dict:
        return {"integral": self.integral,
                "integral_latex": self.integral_latex or None,
                "caption": self.caption or None,
                "steps": [s.to_dict() for s in self.steps],
                "result": self.result,
                "result_latex": self.result_latex or None}

    def render_json(self, *, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    # ----- form 3: HTML (expandable, view on a screen) --------------------
    def render_html(self, *, standalone: bool = True) -> str:
        nodes = "".join(_html_node(s, 0) for s in self.steps)
        if self.integral_latex:
            header = _math_block(self.integral_latex, "integral")
        else:
            header = f"<div class='integral'><code>{_esc(self.integral)}</code></div>"
        caption = f"<div class='caption'>{_inline(self.caption)}</div>" if self.caption else ""
        if self.result_latex:
            note = f"<div class='rnote'>{_inline(self.result)}</div>" if self.result else ""
            result = (f"<div class='result'><span>result</span>"
                      f"{_math_block(self.result_latex, 'rmath')}{note}</div>")
        elif self.result:
            result = f"<div class='result'><span>result</span><code>{_esc(self.result)}</code></div>"
        else:
            result = ""
        body = (f"<section class='trace'><h1>Method trace</h1>"
                f"{header}{caption}"
                f"<div class='hint'>every step expands — click to follow the working</div>"
                f"{nodes}{result}</section>")
        return body if not standalone else _doc(body, katex=not _HAS_L2M)


# ---------------------------------------------------------------------------
# markdown nesting
# ---------------------------------------------------------------------------
def _md_node(step: Step, depth: int) -> str:
    pad = "  " * depth
    label, _ = classify_check(step.check)
    lines = [f"{pad}- **{step.heading()}**" + (f"  · _{label}_" if label else "")]
    if step.rationale:
        lines.append(f"{pad}  - _why this method:_ {step.rationale}")
    if step.has_decision():
        lines.append(f"{pad}  - **Decision**")
        if step.forced_by:
            lines.append(f"{pad}    - _forced by:_ {step.forced_by}")
        if step.payoff:
            lines.append(f"{pad}    - _payoff:_ {step.payoff}")
        if step.relies_on:
            lines.append(f"{pad}    - _relies on:_ {step.relies_on}")
    if step.justification:
        lines.append(f"{pad}  - {step.justification}")
    if step.has_altitudes():
        lines.append(f"{pad}  - **Explain at:**")
        for k in _alt_keys(step.altitudes):
            lines.append(f"{pad}    - _{k}:_ {step.altitudes[k]}")
    if step.before or step.after:
        lines.append(f"{pad}  - `{step.before}` → `{step.after}`")
    if step.work:
        lines.append(f"{pad}  - working:")
        for w in step.work:
            lines.append(f"{pad}    - $$\\displaystyle {w}$$")
    for m in step.math:
        lines.append(f"{pad}  - $$\\displaystyle {m}$$")
    if step.detail:
        lines.append(f"{pad}  - working:")
        lines.append(f"{pad}    ```")
        for dl in step.detail.splitlines():
            lines.append(f"{pad}    {dl}")
        lines.append(f"{pad}    ```")
    for r in step.all_references():
        lines.append(f"{pad}  - ref: {r}")
    for c in step.children:
        lines.append(_md_node(c, depth + 1))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# HTML nesting (native <details>, expandable, no JS)
# ---------------------------------------------------------------------------
_BADGE = {"symbolic": "#0F6E56", "numeric": "#185FA5", "pslq": "#534AB7", "none": ""}


def _html_inner(step: Step, depth: int) -> str:
    parts = []
    if step.rationale:
        parts.append(f"<div class='rationale'><span class='lbl'>Why this method:</span> "
                     f"{_inline(step.rationale)}</div>")
    if step.has_decision():
        rows = []
        for label, val in (("Forced by", step.forced_by), ("Payoff", step.payoff),
                           ("Relies on", step.relies_on)):
            if val:
                rows.append(f"<div class='drow'><span class='dl'>{label}</span>"
                            f"<span class='dv'>{_inline(val)}</span></div>")
        parts.append(f"<div class='decision'><div class='dh'>Decision</div>{''.join(rows)}</div>")
    if step.justification:
        parts.append(f"<div class='why'>{_inline(step.justification)}</div>")
    if step.has_altitudes():
        parts.append(_altitude_block(step.altitudes))
    # WORKING — the derivation, shown ABOVE the result, OPEN by default, divider per line
    # (rule 7: show the work; don't fear length — these are pages by hand).
    if step.work:
        rows = "".join(f"<div class='wkrow'>{_math_block(w)}</div>" for w in step.work)
        parts.append(f"<details class='wk'><summary>working ({len(step.work)} lines)</summary>"
                     f"<div class='wk-body'>{rows}</div></details>")
    for m in step.math:
        parts.append(_math_block(m))
    if step.before or step.after:
        parts.append(f"<div class='xform'><code>{_esc(step.before)}</code>"
                     f"<span class='arrow'>&rarr;</span><code>{_esc(step.after)}</code></div>")
    # DRILL-DOWN: citations / prose detail, collapsed so the base level stands alone.
    drill = []
    if step.detail:
        drill.append(f"<pre class='work'>{_esc(step.detail)}</pre>")
    refs = step.all_references()
    if refs:
        items = "".join(f"<li>{_esc(r)}</li>" for r in refs)
        drill.append(f"<ul class='refs'>{items}</ul>")
    if drill:
        n = len(refs)
        has_detail = bool(step.detail)
        lbl = "detail & references" if (has_detail and refs) else ("detail" if has_detail else f"references ({n})")
        parts.append(f"<details class='dd'><summary>{lbl}</summary>"
                     f"<div class='dd-body'>{''.join(drill)}</div></details>")
    for c in step.children:
        parts.append(_html_node(c, depth + 1))
    return "".join(parts)


def _html_node(step: Step, depth: int) -> str:
    label, kind = classify_check(step.check)
    col = _BADGE.get(kind, "")
    badge = (f"<span class='badge' style='background:{col}'>{_esc(label)}</span>"
             if label and col else "")
    sep = "&nbsp; " if badge else ""   # keeps title/badge apart even with no CSS
    head = f"<span class='name'>{_inline(step.heading())}</span>{sep}{badge}"
    inner = _html_inner(step, depth)
    if step.children:
        op = " open" if depth == 0 else ""   # base = top-level steps; sub-steps drill down
        return (f"<details class='node d{depth}'{op}><summary>{head}</summary>"
                f"<div class='body'>{inner}</div></details>")
    return f"<div class='node leaf d{depth}'><div class='lead'>{head}</div>{inner}</div>"


def _esc(s) -> str:
    s = "" if s is None else str(s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _attr(s) -> str:
    """Escape for an HTML attribute value (double-quoted)."""
    s = "" if s is None else str(s)
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def _math_block(latex: str, extra_class: str = "") -> str:
    """A display-math block with a copy-LaTeX button. The button copies the SOURCE
    LaTeX (in data-latex), not the rendered MathML — so it pastes into a document.
    The button sits in the non-scrolling wrapper; the math itself scrolls inside."""
    cls = ("mblock " + extra_class).strip()
    return (f"<div class='{cls}'><div class='math'>{_render_math(latex)}</div>"
            f"<button class='copy-tex' type='button' data-latex=\"{_attr(latex)}\""
            f" title='copy LaTeX' aria-label='copy LaTeX'>TeX</button></div>")


_ALT_ORDER = ["expert", "working", "plain"]
_ALT_LABEL = {"expert": "Expert", "working": "Working", "plain": "Plain"}


def _alt_keys(alts: dict) -> list:
    """Altitudes in canonical order (expert→working→plain), unknowns appended."""
    return [k for k in _ALT_ORDER if k in alts] + [k for k in alts if k not in _ALT_ORDER]


def _altitude_block(alts: dict) -> str:
    """A 'explain at' control: pills (Expert/Working/Plain) switching one panel."""
    keys = _alt_keys(alts)
    # lead with the most accessible level ("back to high-school"); expert clicks up
    default = next((k for k in ("plain", "working") if k in keys), keys[0])
    pills, panels = [], []
    for k in keys:
        on = " active" if k == default else ""
        hide = "" if k == default else " hidden"
        pills.append(f"<button class='alt-pill{on}' type='button' data-alt='{_esc(k)}'>"
                     f"{_esc(_ALT_LABEL.get(k, k.title()))}</button>")
        panels.append(f"<div class='alt-panel' data-alt='{_esc(k)}'{hide}>{_inline(alts[k])}</div>")
    return (f"<div class='altitudes'><div class='alt-head'>explain at</div>"
            f"<div class='alt-pills'>{''.join(pills)}</div>{''.join(panels)}</div>")


# Local clipboard handler — no CDN, works offline; degrades gracefully without JS.
_COPY_JS = (
    "<script>document.addEventListener('click',function(e){"
    "var b=e.target.closest('.copy-tex');if(!b||!navigator.clipboard)return;"
    "navigator.clipboard.writeText(b.getAttribute('data-latex')||'').then(function(){"
    "var o=b.textContent;b.textContent='copied';b.classList.add('copied');"
    "setTimeout(function(){b.textContent=o;b.classList.remove('copied');},1200);});"
    "});</script>"
)

# Local altitude toggle — switch which explanation level is shown. No CDN.
_ALT_JS = (
    "<script>document.addEventListener('click',function(e){"
    "var p=e.target.closest('.alt-pill');if(!p)return;var box=p.closest('.altitudes');"
    "var k=p.getAttribute('data-alt');"
    "box.querySelectorAll('.alt-pill').forEach(function(x){x.classList.toggle('active',x===p);});"
    "box.querySelectorAll('.alt-panel').forEach(function(x){x.hidden=x.getAttribute('data-alt')!==k;});"
    "});</script>"
)

# Copy a section's (or the whole level's) LaTeX — gathers every data-latex in scope.
_COPYGRP_JS = (
    "<script>document.addEventListener('click',function(e){"
    "var b=e.target.closest('.copy-all,.copy-band');if(!b||!navigator.clipboard)return;"
    "e.preventDefault();var scope;"
    "if(b.classList.contains('copy-all')){var s=b.closest('.trace');"
    "scope=s.querySelector('.level-track:not([hidden])')||s;}else{scope=b.closest('.band-group');}"
    "var tex=[].map.call(scope.querySelectorAll('[data-latex]'),function(x){"
    "return x.getAttribute('data-latex');}).join('\\n\\n');"
    "navigator.clipboard.writeText(tex).then(function(){var o=b.textContent;b.textContent='copied \\u2713';"
    "b.classList.add('copied');setTimeout(function(){b.textContent=o;b.classList.remove('copied');},1200);});"
    "});</script>"
)

# Local level toggle — switch the WHOLE explanation (a different step sequence per level).
_LEVEL_JS = (
    "<script>document.addEventListener('click',function(e){"
    "var p=e.target.closest('.lvl-pill');if(!p)return;var sec=p.closest('.trace');"
    "var k=p.getAttribute('data-lvl');"
    "sec.querySelectorAll('.lvl-pill').forEach(function(x){x.classList.toggle('active',x===p);});"
    "sec.querySelectorAll('.level-track').forEach(function(x){x.hidden=x.getAttribute('data-lvl')!==k;});"
    "});</script>"
)


_KATEX_VER = "0.16.11"
_STYLE = """
  body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:1500px;
       min-width:min(820px,100%);margin:2rem auto;padding:0 2rem;color:#2c2c2a;line-height:1.55}
  h1{font-size:1.3rem;font-weight:500;margin:0 0 .3rem}
  .integral{margin-bottom:.2rem}
  .integral math{font-size:1.2em}
  .mblock{position:relative}
  .copy-tex{position:absolute;top:.1rem;right:.2rem;font-family:ui-monospace,Menlo,monospace;
       font-size:.62rem;line-height:1.4;border:1px solid rgba(0,0,0,.18);background:#fff;color:#5f5e5a;
       border-radius:5px;padding:.02rem .35rem;cursor:pointer;opacity:.32;transition:opacity .12s}
  .mblock:hover .copy-tex,.copy-tex:focus{opacity:1}
  .copy-tex.copied{color:#0f6e56;border-color:#0f6e56}
  .copy-band,.copy-all{font-family:ui-monospace,Menlo,monospace;font-size:.62rem;font-weight:400;
       text-transform:none;letter-spacing:0;border:1px solid rgba(0,0,0,.2);background:#fff;color:#5f5e5a;
       border-radius:5px;padding:.1rem .5rem;cursor:pointer}
  .copy-band.copied,.copy-all.copied{color:#0f6e56;border-color:#0f6e56}
  .copy-all{margin-left:.4rem}
  .caption{color:#5f5e5a;font-size:.9rem;margin:0 0 1rem}
  .hint{color:#888780;font-size:.8rem;margin-bottom:1rem}
  code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.92em}
  .integral code{font-size:1.05rem}
  .node{border:1px solid rgba(0,0,0,.12);border-radius:10px;margin:.5rem 0}
  details.node>summary{list-style:none;cursor:pointer;padding:.6rem .9rem;display:flex;
       align-items:center;gap:.5rem}
  details.node>summary::-webkit-details-marker{display:none}
  details.node>summary::before{content:"\\25B8";color:#888780;font-size:.8rem;transition:transform .15s}
  details.node[open]>summary::before{transform:rotate(90deg)}
  .leaf>.lead{padding:.6rem .9rem;display:flex;align-items:center;gap:.5rem}
  .name{font-weight:500}
  .badge{margin-left:auto;color:#fff;font-size:.7rem;padding:.12rem .5rem;border-radius:999px;white-space:nowrap}
  .body{padding:0 .9rem .8rem 2rem}
  .leaf .rationale,.leaf .why,.leaf .math,.leaf .xform,.leaf .work,.leaf .refs{margin-left:1.1rem}
  .rationale{background:#f3eefe;border-left:3px solid #7f77dd;border-radius:0 7px 7px 0;
       padding:.45rem .7rem;margin:.3rem 0 .5rem;font-size:.88rem;color:#3c3489}
  .rationale .lbl{font-weight:500;color:#7f77dd}
  .decision{background:#e9f1fb;border-left:3px solid #378add;border-radius:0 7px 7px 0;
       padding:.5rem .75rem;margin:.3rem 0 .6rem}
  .decision .dh{font-size:.64rem;text-transform:uppercase;letter-spacing:.07em;color:#185fa5;
       font-weight:500;margin-bottom:.3rem}
  .decision .drow{font-size:.88rem;line-height:1.55;margin:.2rem 0;color:#0c447c;display:flex;gap:.5rem}
  .decision .dl{flex:0 0 5.2rem;color:#185fa5;font-weight:500}
  .decision .dv{flex:1 1 auto}
  .leaf .decision{margin-left:1.1rem}
  .why{color:#5f5e5a;font-size:.9rem;margin:.1rem 0 .5rem}
  .altitudes{background:#f3f1ea;border-radius:8px;padding:.5rem .7rem;margin:.4rem 0 .6rem}
  .alt-head{font-size:.62rem;text-transform:uppercase;letter-spacing:.07em;color:#888780;margin-bottom:.35rem}
  .alt-pills{display:flex;gap:.3rem;margin-bottom:.45rem;flex-wrap:wrap}
  .alt-pill{font-size:.72rem;border:1px solid rgba(0,0,0,.18);background:#fff;color:#5f5e5a;
       border-radius:999px;padding:.08rem .6rem;cursor:pointer}
  .alt-pill.active{background:#2c2c2a;color:#fff;border-color:#2c2c2a}
  .alt-panel{font-size:.9rem;line-height:1.6;color:#2c2c2a}
  .alt-panel[hidden]{display:none}
  .leaf .altitudes{margin-left:1.1rem}
  .levelbar{display:flex;align-items:center;gap:.4rem;flex-wrap:wrap;margin:.2rem 0 1rem;
       padding:.5rem .7rem;background:#eef1f6;border-radius:8px}
  .levelbar .alt-head{margin:0 .2rem 0 0}
  .lvl-pill{font-size:.82rem;border:1px solid rgba(0,0,0,.18);background:#fff;color:#5f5e5a;
       border-radius:12px;padding:.3rem .8rem;cursor:pointer;text-align:left;line-height:1.25}
  .lvl-pill.active{background:#2c2c2a;color:#fff;border-color:#2c2c2a}
  .lvl-name{display:block;font-weight:600}
  .lvl-aud{display:block;font-size:.68rem;opacity:.8}
  .lvl-n{display:block;font-size:.62rem;opacity:.55}
  .level-track[hidden]{display:none}
  .band{display:flex;align-items:baseline;justify-content:space-between;gap:1rem;
        font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;
        color:#8a5a2b;margin:1.5rem 0 .6rem;padding-bottom:.25rem;
        border-bottom:2px solid rgba(138,90,43,.3)}
  .wk{margin:.3rem 0 .6rem;background:#fbfaf7;border:1px solid #e6e2d8;border-radius:6px}
  .wk>summary{cursor:pointer;font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;
        color:#8a7f63;padding:.3rem .6rem}
  .wk-body{padding:0 .7rem .3rem}
  .wkrow{padding:.5rem 0}
  .wkrow + .wkrow{border-top:1px solid #e0dccf}   /* clear divider between working lines */
  .math{margin:.5rem 0;overflow-x:auto;overflow-y:hidden;padding:.1rem 0 .35rem;max-width:100%}
  math[display="block"]{margin:0;font-size:1.05em}
  .name math,.why math,.rationale math,.caption math,.rnote math{font-size:1em}
  .xform{background:#f3f1ea;border-radius:7px;padding:.4rem .6rem;display:flex;align-items:center;
       gap:.5rem;flex-wrap:wrap;margin:.3rem 0}
  .arrow{color:#888780}
  .work{background:#f7f6f1;border:1px solid rgba(0,0,0,.06);border-radius:7px;padding:.6rem .75rem;
       margin:.4rem 0;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.83rem;
       line-height:1.5;white-space:pre-wrap;overflow-x:auto;color:#2c2c2a}
  .refs{margin:.4rem 0 .2rem;padding-left:1.1rem;color:#888780;font-size:.78rem}
  .refs li{margin:.1rem 0}
  details.dd{margin:.35rem 0}
  details.dd>summary{list-style:none;cursor:pointer;font-size:.74rem;color:#888780;
       display:inline-flex;align-items:center;gap:.3rem;user-select:none}
  details.dd>summary::-webkit-details-marker{display:none}
  details.dd>summary::before{content:"\\25B8";font-size:.66rem;transition:transform .15s}
  details.dd[open]>summary::before{transform:rotate(90deg)}
  .dd-body{padding-top:.25rem}
  .d2,.d3{background:#fbfaf6}
  .result{margin-top:1.1rem;padding:.7rem 1rem;background:#e1f5ee;border-radius:10px}
  .result span{font-size:.7rem;text-transform:uppercase;letter-spacing:.05em;color:#0f6e56}
  .result .rmath{margin:.25rem 0}
  .result .rnote{font-size:.82rem;color:#0f6e56;margin-top:.2rem}
"""
_KATEX_HEAD = f'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{_KATEX_VER}/katex.min.css">'
_KATEX_TAIL = (
    f'<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{_KATEX_VER}/katex.min.js"></script>'
    f'<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/{_KATEX_VER}/contrib/auto-render.min.js"></script>'
    '<script>renderMathInElement(document.body,{delimiters:[{left:"\\\\[",right:"\\\\]",display:true}],throwOnError:false});</script>'
)


def _doc(body: str, *, katex: bool) -> str:
    """Wrap the body in a full HTML document. With MathML (default) it is fully
    self-contained — no JS, no CDN, renders offline. KaTeX is the fallback only
    when latex2mathml is not installed."""
    head_extra = _KATEX_HEAD if katex else ""
    tail_extra = _KATEX_TAIL if katex else ""
    return (f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>Method trace</title>{head_extra}<style>{_STYLE}</style></head>'
            f'<body>{body}{_COPY_JS}{_ALT_JS}{_LEVEL_JS}{_COPYGRP_JS}{tail_extra}</body></html>')


# The explanation contract (CLAUDE.md rule 7): every trace is three ordered bands.
_SECTION_LABEL = {"why": "Why this approach", "how": "How the approach works", "step": "The steps"}


def validate_explanation(trace) -> list:
    """Contract check: an explanation must carry all three bands. Returns warnings."""
    present = {(s.section or "step") for s in trace.steps}
    return [f"missing band: {_SECTION_LABEL[k]}" for k in ("why", "how", "step") if k not in present]


def validate_levels(tracks: dict) -> list:
    """Check the per-level BREAKDOWN is valid (CLAUDE.md rule 7), not just that the
    bands exist. Testing an explanation means checking it at every level:
      - every level carries all three bands;
      - the levels genuinely DIFFER — step count is not identical across all of them
        (the 'fixed count at every level' anti-pattern);
      - decomposition runs the right way — plain has at least as many steps as expert.
    Returns warnings (empty = valid)."""
    warn = []
    for lvl, tr in tracks.items():
        warn += [f"[{lvl}] {m}" for m in validate_explanation(tr)]
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    if len(counts) > 1 and len(set(counts.values())) == 1:
        warn.append(f"all levels have identical step count {counts} — not decomposed per "
                    f"reader (rule 7: step count is emergent, expert collapses / plain expands)")
    if counts.get("plain", 0) < counts.get("expert", 0):
        warn.append(f"plain ({counts.get('plain')}) < expert ({counts.get('expert')}) — "
                    f"decomposition inverted (lower levels should have MORE steps)")
    return warn


# The qualification ladder: the reader level needed to grasp a step as one unit.
_QUAL = {"plain": 1, "working": 2, "expert": 3}


def validate_qualification(tracks: dict) -> list:
    """THE per-level test (CLAUDE.md rule 7): at each reader level, EVERY shown step
    must be understandable by that reader — its required qualification ≤ the reader's
    level. A shown step needing MORE than the level is an un-decomposed leap / an
    altitude ceiling (the method can't reach that reader). Subsumes `validate_levels`
    (bands present + counts genuinely differ)."""
    warn = list(validate_levels(tracks))
    for lvl, tr in tracks.items():
        reader = _QUAL.get(lvl, 1)
        for s in tr.steps:
            need = _QUAL.get(getattr(s, "requires", "plain") or "plain", 1)
            if need > reader:
                warn.append(f"[{lvl}] step '{s.title[:44]}' needs '{s.requires}' qualification "
                            f"but the reader is '{lvl}' — not decomposed to this level (ceiling)")
    return warn


# A step's references cite base pages as `… → library/<page>.md`; pull the slugs out.
_LIBRARY_REF = re.compile(r"library/([A-Za-z0-9_-]+)\.md")


def _library_dir():
    """The pattern-library directory (repo-root/library), located relative to this file
    so the check works regardless of the caller's CWD."""
    from pathlib import Path
    return Path(__file__).resolve().parents[2] / "library"


def validate_references(tracks: dict, library_dir=None) -> list:
    """Reference-existence check (CLAUDE.md rule 11: 'plain bottoms out … steps reference the
    sub-methods they use'). A leaf that cites a nonexistent base page does NOT truly bottom out
    to a base method — but `validate_qualification` only walks the qualification ladder and never
    resolves reference strings, so a dangling `library/<page>.md` ref passes it silently. This
    closes that gap: every `library/<page>.md` cited by a shown step must resolve to a real page.
    Returns warnings (empty = valid); dedup'd per (level, page)."""
    from pathlib import Path
    lib = Path(library_dir) if library_dir is not None else _library_dir()
    warn, seen = [], set()
    for lvl, tr in tracks.items():
        for s in tr.steps:
            for r in s.all_references():
                for page in _LIBRARY_REF.findall(r):
                    if (lib / f"{page}.md").exists() or (lvl, page) in seen:
                        continue
                    seen.add((lvl, page))
                    warn.append(f"[{lvl}] step '{s.title[:44]}' references "
                                f"library/{page}.md which does not exist")
    return warn


def _trace_body_inner(t: "MethodTrace") -> str:
    """The per-level part of a trace: the why / how / step bands + the result (no header).
    Each band is its own <section.band-group> so it can be copied as LaTeX on its own."""
    chunks, cur, in_group = [], None, False
    for s in t.steps:
        sec = s.section or "step"
        if sec != cur:
            if in_group:
                chunks.append("</section>")
            label = _esc(_SECTION_LABEL.get(sec, sec))
            chunks.append(f"<section class='band-group'><h3 class='band'>{label}"
                          f"<button class='copy-band' type='button' title='copy this section as LaTeX'>copy LaTeX</button>"
                          f"</h3>")
            in_group, cur = True, sec
        chunks.append(_html_node(s, 0))
    if in_group:
        chunks.append("</section>")
    nodes = "".join(chunks)
    if t.result_latex:
        note = f"<div class='rnote'>{_inline(t.result)}</div>" if t.result else ""
        result = (f"<div class='result'><span>result</span>"
                  f"{_math_block(t.result_latex, 'rmath')}{note}</div>")
    elif t.result:
        result = f"<div class='result'><span>result</span><code>{_esc(t.result)}</code></div>"
    else:
        result = ""
    return nodes + result


# Each altitude is a named reader (CLAUDE.md rule 7); steps are decomposed to reach them.
_LEVEL_AUDIENCE = {"plain": "high school", "working": "2nd-yr undergrad", "expert": "graduate"}
# Present accessible-first (left→right) and default to the most accessible: people reach for
# "expert" to feel clever and then drown, so lead with the welcoming level and let them climb.
_LEVEL_ORDER = ["plain", "working", "expert"]


def render_leveled(tracks: dict, *, standalone: bool = True) -> str:
    """Render ONE explanation at several levels — a different step sequence per
    level — with a top 'explain at' switch. `tracks` maps level name
    (expert/working/plain) to a MethodTrace. The shared header comes from any track;
    the switch swaps the whole body. Default = the most accessible level present."""
    order = [l for l in _LEVEL_ORDER if l in tracks] + [l for l in tracks if l not in _LEVEL_ORDER]
    first = tracks[order[0]]
    if first.integral_latex:
        header = _math_block(first.integral_latex, "integral")
    else:
        header = f"<div class='integral'><code>{_esc(first.integral)}</code></div>"
    caption = f"<div class='caption'>{_inline(first.caption)}</div>" if first.caption else ""
    default = next((l for l in ("plain", "working") if l in tracks), order[0])
    pills, panels = [], []
    for l in order:
        on = " active" if l == default else ""
        hide = "" if l == default else " hidden"
        n = len(tracks[l].steps)
        aud = _LEVEL_AUDIENCE.get(l, "")
        audsp = f"<span class='lvl-aud'>for {_esc(aud)}</span>" if aud else ""
        pills.append(f"<button class='lvl-pill{on}' type='button' data-lvl='{_esc(l)}'>"
                     f"<span class='lvl-name'>{_esc(_ALT_LABEL.get(l, l.title()))}</span>"
                     f"{audsp}<span class='lvl-n'>{n} steps</span></button>")
        panels.append(f"<div class='level-track' data-lvl='{_esc(l)}'{hide}>{_trace_body_inner(tracks[l])}</div>")
    body = (f"<section class='trace'><h1>Method trace</h1>{header}{caption}"
            f"<div class='levelbar'><span class='alt-head'>explain at</span>{''.join(pills)}"
            f"<button class='copy-all' type='button' title='copy the whole explanation as LaTeX'>Copy all LaTeX</button>"
            f"</div>{''.join(panels)}</section>")
    return body if not standalone else _doc(body, katex=not _HAS_L2M)
