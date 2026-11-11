#!/usr/bin/env python3
"""METANODA A0 — safe bootstrap runner.

This first deployment is deliberately read-only. It validates that the source
and role handoff package exist before any AI or publishing adapter is enabled.
It never edits author materials, calls external APIs, or publishes content.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "primary_author_source": "Метанода_Татьяны_Синюгиной_RU_EN 2.md",
    "content_handoff": "operations/A6_CONTENT_AGENT_TRAINING_HANDOFF_RU.md",
    "execution_register": "operations/SOCIAL_MEDIA_AGENT_EXECUTION_REGISTER_RU.md",
}

def main() -> int:
    print("METANODA A0 — bootstrap validation")
    failures = []
    for label, rel in REQUIRED.items():
        p = ROOT / rel
        ok = p.is_file() and p.stat().st_size > 0
        print(f"{'OK' if ok else 'BLOCKED'} | {label} | {rel}")
        if not ok:
            failures.append(label)

    print("\nExecution mode: READ_ONLY")
    print("AI model adapter: NOT_CONFIGURED")
    print("Social publishing adapter: DISABLED")
    print("Author-source mutation: FORBIDDEN")
    if failures:
        print("RESULT: BLOCKED — required source files are missing or empty.")
        return 2
    print("RESULT: PASS — source package is present; external execution remains disabled.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
