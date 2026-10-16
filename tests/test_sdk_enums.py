"""Response models accept enum values the OpenAPI spec does not list.

Buildium returned RenewalOfferStatus 13 for a production lease, which the
generated model rejected (luthersystems/mcp-server-buildium#3, reported by
TripBower8502). scripts/lenient_response_enums.py loosens every response
model; request models keep their strict checks.
"""

import importlib.util
import inspect
from pathlib import Path

import pytest
from pydantic import ValidationError

from mcp_server_buildium.buildium_sdk.models.lease_message import LeaseMessage
from mcp_server_buildium.buildium_sdk.models.lease_post_message import LeasePostMessage


@pytest.mark.parametrize("status", [13, "Generated", "AValueAddedLater", None])
def test_lease_response_accepts_any_renewal_offer_status(status: object) -> None:
    lease = LeaseMessage.from_dict(
        {"Id": 450441, "LeaseStatus": "Active", "RenewalOfferStatus": status}
    )
    assert lease is not None
    assert lease.renewal_offer_status == status
    assert lease.lease_status == "Active"


def test_request_models_keep_strict_enums() -> None:
    with pytest.raises(ValidationError, match="enum"):
        LeasePostMessage.model_validate(
            {
                "LeaseType": "NotALeaseType",
                "UnitId": 1,
                "LeaseFromDate": "2026-01-01",
                "SendWelcomeEmail": False,
            }
        )


def test_codemod_is_applied() -> None:
    """A regenerated SDK fails here until scripts/lenient_response_enums.py runs."""
    path = Path(__file__).resolve().parent.parent / "scripts" / "lenient_response_enums.py"
    spec = importlib.util.spec_from_file_location("lenient_response_enums", path)
    assert spec is not None
    assert spec.loader is not None
    codemod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(codemod)

    responses, requests = codemod.model_sets()
    assert not responses & requests
    for model in responses:
        source = Path(inspect.getfile(model)).read_text()
        assert codemod.patch(source) == source, model.__name__
