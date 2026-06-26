"""Run the FULL test suite (every marker, including slow) and append the outcome to
FULL_SUITE_LOG.md — the durable record of when the whole suite last ran green.

Why this exists (James, 2026-06-25): reducing coverage to gain speed is a failure route hidden in
efficiency. Iteration may run a targeted subset (`pytest -m "not slow"`, a single file, `-k ...`),
but the WHOLE suite must be run and RECORDED at each milestone so nothing silently rots. This script
is that record.

Usage:  python tests/run_full_suite.py ["short note on what changed"]
"""
import datetime
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
LOG = HERE / "FULL_SUITE_LOG.md"


def main():
    note = sys.argv[1] if len(sys.argv) > 1 else ""
    when = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # -o addopts= clears any ini default so EVERYTHING runs (slow included)
    proc = subprocess.run([sys.executable, "-m", "pytest", "-o", "addopts=", "-q", "--durations=0"],
                          cwd=ROOT, capture_output=True, text=True)
    out = (proc.stdout or "") + (proc.stderr or "")
    # the pytest summary line, e.g. "402 passed, 1 xfailed in 431.20s"
    summ = next((ln.strip() for ln in reversed(out.splitlines())
                 if re.search(r"\d+ (passed|failed|error)", ln)), "(no summary)")
    status = "PASS" if proc.returncode == 0 else "FAIL"

    if not LOG.exists():
        LOG.write_text(
            "# Full test-suite run log\n\n"
            "Every run of the WHOLE suite (all markers, incl. slow) is recorded here. Iteration may\n"
            "use targeted subsets, but the full suite is run + logged at each milestone so coverage\n"
            "is never silently reduced. Most recent run is the bottom row.\n\n"
            "| when | status | pytest summary | note |\n|---|---|---|---|\n", encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"| {when} | {status} | {summ} | {note} |\n")

    print(f"[{status}] {summ}")
    print(f"recorded -> {LOG}")
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
