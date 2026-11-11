#!/usr/bin/env python3
"""METANODA agent team: public-source research -> strategy -> draft -> independent QA.
The model receives only a public URL and earlier stage outputs. It has no repository
read/write, shell, or publishing tools. Private repository files are never passed in.
"""
from __future__ import annotations
import json, os, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "operations" / "agent_runs"
PUBLIC_SOURCE = "https://tatyana-open-dialogue.gv966ysyr2.chatgpt.site/"
ALLOWED_HOST = "tatyana-open-dialogue.gv966ysyr2.chatgpt.site"

AGENTS = [
    ("01_source_auditor", "SOURCE AUDITOR",
     "Inspect only the public source URL. Extract explicit claims into an evidence ledger: claim, supporting URL/section, confidence, wording limits. Do not infer or embellish. If inaccessible, say BLOCKED."),
    ("02_strategy", "DISTRIBUTION STRATEGIST",
     "Using only the evidence ledger, propose one practical organic distribution action: audience, channel fit, objective, format, measurable success signal. No paid ads, spam, mass messaging, follow/unfollow, fake engagement, follower guarantees, or invented product claims."),
    ("03_editor", "BILINGUAL EDITOR",
     "Prepare one concise draft in Russian and English based only on the evidence and strategy. Preserve authorship: METANODA is the author system/term of Tatyana Sinyugina. Do not attribute AI interpretation or research coordination to her. Add source link. Do not mention children, families, case details, personal data, or unpublished research. Mark DRAFT — NOT PUBLISHED."),
    ("04_independent_qa", "INDEPENDENT QUALITY REVIEWER",
     "Independently audit the draft against the evidence and strategy: factual support, authorship, privacy, RU/EN consistency, platform safety. Start with exactly PASS or FAIL and list findings. Unsupported claims, authorship confusion, private/child data, or misleading promises mean FAIL. Do not silently rewrite."),
]

def run_agent(name, role, instruction, context, workdir):
    prompt = f"""You are {role} in a controlled METANODA multi-agent pipeline.
Boundaries: use only the public URL and context below; do not infer private information;
do not access or modify repository files; do not publish, contact people, create accounts,
or spend money. Separate verified facts from hypotheses and cite URLs.

Task: {instruction}
Public source URL: {PUBLIC_SOURCE}
Earlier stage context:
{context if context else "(No earlier stage output.)"}
Return a concise structured result. If the source cannot be read, say BLOCKED.
"""
    cmd = ["copilot", "-p", prompt, "-s", "--no-ask-user",
           "--available-tools=web_fetch", "--allow-tool=url", f"--allow-url=https://{ALLOWED_HOST}"]
    result = subprocess.run(cmd, cwd=str(workdir), text=True, capture_output=True,
                            timeout=600, check=False)
    if result.returncode:
        detail = (result.stderr or result.stdout or "No diagnostic").strip()
        raise RuntimeError(f"{name} failed ({result.returncode}): {detail[-2500:]}")
    output = result.stdout.strip()
    if not output:
        raise RuntimeError(f"{name} returned empty output")
    return output

def main():
    if not os.environ.get("COPILOT_GITHUB_TOKEN"):
        print("BLOCKED: missing repository secret COPILOT_GITHUB_TOKEN")
        return 3
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = OUTPUT_ROOT / stamp
    run_dir.mkdir(parents=True, exist_ok=False)
    outputs, context = {}, ""
    try:
        with tempfile.TemporaryDirectory(prefix="metanoda-agent-sandbox-") as tmp:
            for filename, role, instruction in AGENTS:
                print(f"RUNNING: {role}", flush=True)
                output = run_agent(filename, role, instruction, context, Path(tmp))
                outputs[filename] = output
                (run_dir / f"{filename}.md").write_text(output + "\n", encoding="utf-8")
                context += f"\n\n## {role}\n{output}\n"
        qa = outputs["04_independent_qa"].lstrip().upper()
        passed = qa.startswith("PASS")
        summary = {
            "system": "METANODA_AGENT_TEAM", "run_utc": stamp,
            "source": PUBLIC_SOURCE, "agents_completed": list(outputs),
            "qa_status": "PASS" if passed else "FAIL",
            "publication_status": "NOT_PUBLISHED",
            "publication_authorization": "NOT_GRANTED",
            "private_repository_files_sent_to_model": False,
            "model_tools": ["url"]
        }
        (run_dir / "summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"RESULT: {'QA_PASS' if passed else 'QA_FAIL'}")
        print(f"REPORT: {run_dir.relative_to(ROOT)}")
        return 0 if passed else 2
    except Exception as exc:
        (run_dir / "failure.txt").write_text(str(exc) + "\n", encoding="utf-8")
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 4

if __name__ == "__main__":
    raise SystemExit(main())
