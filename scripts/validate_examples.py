#!/usr/bin/env python3
"""Validate example JSON files against pa-schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Install jsonschema: pip install jsonschema", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "pa_solution_pipeline_packet.v1.1.json"
EXAMPLES = [
    ROOT / "examples" / "email-sb123" / "packet.v1.1.json",
]


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    failed = False
    for path in EXAMPLES:
        data = json.loads(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            failed = True
            print(f"FAIL {path}")
            for err in errors[:5]:
                print(f"  - {err.message}")
        else:
            print(f"OK   {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
