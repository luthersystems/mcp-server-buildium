#!/usr/bin/env python3
"""Codemod: defensively loosen all StrictStr enum validators in the buildium SDK.

Buildium's API documentation declares many fields as string enums, but in
production it returns integer codes for some of them (e.g. RenewalOfferStatus
returns int 13 for at least one lease). The auto-generated SDK rejects these
with a pydantic validation error, breaking entire endpoints.

This codemod scans every model file in buildium_sdk/models/ and:

  1. For each field that has a `*_validate_enum` validator, changes its type
     annotation from `StrictStr` (or `Optional[StrictStr]`) to `Any` (or
     `Optional[Any]`). This stops pydantic's strict-string check from rejecting
     ints before the validator can run.

  2. Inserts an int passthrough at the top of each enum validator so the
     unknown int code is returned unchanged instead of raising. Strings still
     fall through to the original (now permissive) validation.

The codemod is idempotent — re-running it on already-patched files is a no-op.

Usage:
    python scripts/lenient_enum_codemod.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src" / "mcp_server_buildium" / "buildium_sdk" / "models"
MARKER = "# CODEMOD: lenient enum"
ENUM_VALIDATOR_RE = re.compile(
    r"@field_validator\('([a-z_][a-z0-9_]*)'\)\s*\n\s*def \1_validate_enum\(cls, value\):"
)
INT_PASSTHROUGH = "        if isinstance(value, int):\n            return value  " + MARKER + "\n"

def patch_file(path: Path) -> tuple[bool, list[str]]:
    """Patch a single model file. Returns (changed, list_of_field_names_patched)."""
    text = path.read_text()
    if MARKER in text:
        return False, []  # Already patched, idempotent skip.

    enum_fields = ENUM_VALIDATOR_RE.findall(text)
    if not enum_fields:
        return False, []

    new_text = text
    for field in enum_fields:
        # 1. Loosen the type annotation. The auto-generated SDK uses two patterns:
        #    field_name: StrictStr = Field(...)
        #    field_name: Optional[StrictStr] = Field(...)
        # We rewrite the type to Any (or Optional[Any]).
        opt_pat = re.compile(rf"^(\s+){field}: Optional\[StrictStr\] = Field\(", re.MULTILINE)
        req_pat = re.compile(rf"^(\s+){field}: StrictStr = Field\(", re.MULTILINE)
        new_text = opt_pat.sub(rf"\1{field}: Optional[Any] = Field(", new_text)
        new_text = req_pat.sub(rf"\1{field}: Any = Field(", new_text)

        # 2. Insert int passthrough into the validator body, right after `if value is None: return value`.
        validator_signature = f"def {field}_validate_enum(cls, value):"
        # Find the validator and inject after the None-check.
        # The pattern in the SDK is consistently:
        #   def NAME_validate_enum(cls, value):
        #       """Validates the enum"""
        #       if value is None:
        #           return value
        #
        #       if value not in set([...]):
        #           raise ValueError(...)
        #       return value
        none_check = "if value is None:\n            return value\n\n"
        anchor = validator_signature + '\n        """Validates the enum"""\n        ' + none_check
        replacement = anchor + INT_PASSTHROUGH
        if anchor in new_text:
            new_text = new_text.replace(anchor, replacement, 1)
        else:
            # Fall back: try without the docstring (some validators may not have it).
            anchor2 = validator_signature + "\n        " + none_check
            replacement2 = anchor2 + INT_PASSTHROUGH
            if anchor2 in new_text:
                new_text = new_text.replace(anchor2, replacement2, 1)

    if new_text == text:
        return False, []

    # Make sure `Any` is imported. Most files already import `Any` from typing —
    # check before adding a duplicate.
    if "from typing import" in new_text and " Any" not in new_text.split("from typing import")[1].split("\n")[0]:
        # The first `from typing import ...` line doesn't include Any. Patch it.
        new_text = re.sub(
            r"^from typing import (.+)$",
            lambda m: f"from typing import {m.group(1)}, Any" if "Any" not in m.group(1) else m.group(0),
            new_text,
            count=1,
            flags=re.MULTILINE,
        )

    path.write_text(new_text)
    return True, enum_fields


def main() -> int:
    if not ROOT.exists():
        print(f"ERROR: model dir not found: {ROOT}", file=sys.stderr)
        return 1
    files_changed = 0
    fields_patched = 0
    skipped_already_patched = 0
    for py_file in sorted(ROOT.glob("*.py")):
        if py_file.name in ("__init__.py",):
            continue
        try:
            changed, fields = patch_file(py_file)
        except Exception as e:
            print(f"  FAIL {py_file.name}: {e}", file=sys.stderr)
            continue
        if changed:
            files_changed += 1
            fields_patched += len(fields)
            print(f"  patched {py_file.name}: {', '.join(fields)}")
        elif MARKER in py_file.read_text():
            skipped_already_patched += 1
    print()
    print(f"Files changed: {files_changed}")
    print(f"Fields patched: {fields_patched}")
    print(f"Already-patched (skipped): {skipped_already_patched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
