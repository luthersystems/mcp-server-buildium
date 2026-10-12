#!/usr/bin/env python3
"""Make the enum fields of the SDK's response models accept any value.

Buildium's OpenAPI spec declares many fields as string enums, but the live API
returns values the spec does not list: an integer code (``RenewalOfferStatus``
13 on a production lease) or, as Buildium adds values, a new string. The
generated models reject both, so one such record fails a whole list call.

This rewrites every model a response can contain (found from the SDK's API
signatures, so request models keep their strict checks) so that each enum
field takes a string or an integer, and its validator returns the value
without checking it against the spec's list.

Run it after regenerating the SDK (``make generate-sdk``). It is idempotent.
Based on the codemod in luthersystems/mcp-server-buildium#3 by TripBower8502.

Usage: uv run python scripts/lenient_response_enums.py [--check]
"""

from __future__ import annotations

import inspect
import re
import sys
import typing
from pathlib import Path

import pydantic

import mcp_server_buildium.buildium_sdk.api as sdk_api

MARKER = "# lenient response enum"
VALIDATOR_RE = re.compile(
    r"@field_validator\('([a-z_][a-z0-9_]*)'\)\n    def \1_validate_enum\(cls, value\):\n"
    r'        """Validates the enum"""\n'
)


def _collect(tp: object, out: set[type[pydantic.BaseModel]]) -> None:
    for arg in typing.get_args(tp):
        _collect(arg, out)
    if inspect.isclass(tp) and issubclass(tp, pydantic.BaseModel) and tp not in out:
        out.add(tp)
        for field in tp.model_fields.values():
            _collect(field.annotation, out)


def model_sets() -> tuple[set[type[pydantic.BaseModel]], set[type[pydantic.BaseModel]]]:
    """Return the models reachable from API responses and from API requests."""
    responses: set[type[pydantic.BaseModel]] = set()
    requests: set[type[pydantic.BaseModel]] = set()
    for name in dir(sdk_api):
        cls = getattr(sdk_api, name)
        if not name.endswith("Api"):
            continue
        for method, fn in inspect.getmembers(cls, inspect.iscoroutinefunction):
            if not method.startswith("external_api") or method.endswith(
                ("_with_http_info", "_without_preload_content")
            ):
                continue
            for key, hint in typing.get_type_hints(fn, include_extras=True).items():
                _collect(hint, responses if key == "return" else requests)
    return responses, requests


def patch(text: str) -> str:
    """Return the model source with every enum field made lenient."""
    if MARKER in text:
        return text
    fields = VALIDATOR_RE.findall(text)
    for field in fields:
        text = re.sub(
            rf"^(    {field}: (?:Optional\[)?(?:List\[)?)StrictStr\b",
            r"\1Union[StrictStr, StrictInt]",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    text = VALIDATOR_RE.sub(lambda m: m.group(0) + f"        return value  {MARKER}\n", text)
    if fields and not re.search(r"^from typing import .*\bUnion\b", text, re.MULTILINE):
        text = re.sub(
            r"^from typing import (.*)$",
            r"from typing import \1, Union",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if fields and not re.search(r"^from pydantic import .*\bStrictInt\b", text, re.MULTILINE):
        text = re.sub(
            r"^from pydantic import (.*)$",
            r"from pydantic import \1, StrictInt",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text


def main() -> int:
    check = "--check" in sys.argv[1:]
    responses, requests = model_sets()
    shared = responses & requests
    if shared:
        print(f"models used by both requests and responses: {sorted(m.__name__ for m in shared)}")
        return 2
    stale = []
    for model in sorted(responses, key=lambda m: m.__name__):
        path = Path(inspect.getfile(model))
        text = path.read_text()
        new = patch(text)
        if new != text:
            stale.append(path.name)
            if not check:
                path.write_text(new)
    verb = "need patching" if check else "patched"
    print(f"{len(stale)} response model files {verb}")
    return 1 if check and stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
