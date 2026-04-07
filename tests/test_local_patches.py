"""Regression tests for the four production-bug fixes documented in the local-patches branch.

These tests do NOT require live Buildium credentials. They use the model classes
directly (for the int-enum bug) and inspect/monkeypatch the tool wrappers to
verify they call the correct SDK methods with the correct kwargs.
"""
from __future__ import annotations

import inspect
from datetime import date
from unittest.mock import AsyncMock, MagicMock

import pytest


# ---------------------------------------------------------------------------
# Bug #1 — RenewalOfferStatus int crash on lease 450441
# ---------------------------------------------------------------------------

class TestLeaseMessageAcceptsIntRenewalStatus:
    """Buildium returns RenewalOfferStatus as an integer code (e.g. 13) for some
    leases despite the OpenAPI spec declaring it a string enum. The SDK's
    pydantic StrictStr validation used to crash on these. After the codemod
    loosened the type to Any and made the enum validator pass ints through,
    these records should deserialize cleanly.
    """

    def test_int_renewal_offer_status_passes_through(self):
        from mcp_server_buildium.buildium_sdk.models.lease_message import LeaseMessage

        record = {
            "Id": 450441,
            "PropertyId": 163993,
            "UnitId": 487661,
            "UnitNumber": "1627 Darby Dr.",
            "LeaseFromDate": "2019-12-27",
            "LeaseToDate": "2026-04-30",
            "LeaseType": "FixedWithRollover",
            "LeaseStatus": "Active",
            "IsEvictionPending": False,
            "TermType": "Standard",
            "RenewalOfferStatus": 13,  # ← the int code that broke pydantic
            "CurrentTenants": None,
            "CurrentNumberOfOccupants": 1,
            "AccountDetails": None,
            "Cosigners": None,
            "AutomaticallyMoveOutTenants": False,
            "CreatedDateTime": "2020-02-14T16:10:41Z",
            "LastUpdatedDateTime": "2026-03-23T20:46:15Z",
            "MoveOutData": None,
            "PaymentDueDay": 1,
            "Tenants": None,
        }
        msg = LeaseMessage.from_dict(record)
        assert msg.id == 450441
        assert msg.renewal_offer_status == 13
        assert msg.lease_status == "Active"

    def test_string_renewal_offer_status_still_works(self):
        from mcp_server_buildium.buildium_sdk.models.lease_message import LeaseMessage

        record = {
            "Id": 1,
            "RenewalOfferStatus": "Generated",
        }
        msg = LeaseMessage.from_dict(record)
        assert msg.renewal_offer_status == "Generated"

    def test_null_renewal_offer_status_still_works(self):
        from mcp_server_buildium.buildium_sdk.models.lease_message import LeaseMessage

        record = {"Id": 1, "RenewalOfferStatus": None}
        msg = LeaseMessage.from_dict(record)
        assert msg.renewal_offer_status is None


# ---------------------------------------------------------------------------
# Bug #2 — list_lease_transactions called nonexistent SDK method
# ---------------------------------------------------------------------------

class TestListLeaseTransactionsCallsCorrectMethod:
    """Original bug: tools/leases.py called
    `external_api_lease_transactions_get_lease_transactions(...)` which does
    not exist on LeaseTransactionsApi. The real method is
    `external_api_lease_ledger_transactions_get_lease_ledgers`. Verify the
    tool source uses the correct method name and exposes date-range filters.
    """

    def test_source_calls_correct_method(self):
        from mcp_server_buildium.tools import leases as leases_tools

        src = inspect.getsource(leases_tools.register_lease_tools)
        assert "external_api_lease_ledger_transactions_get_lease_ledgers" in src, (
            "list_lease_transactions must call the correct SDK method"
        )
        # Make sure the old (nonexistent) name isn't being CALLED — only mentioned
        # in the docstring/comments is fine.
        assert "transactions_api.external_api_lease_transactions" not in src, (
            "old (nonexistent) method name must not be called"
        )

    def test_source_exposes_date_range_filters(self):
        from mcp_server_buildium.tools import leases as leases_tools

        src = inspect.getsource(leases_tools.register_lease_tools)
        assert "transactiondatefrom" in src
        assert "transactiondateto" in src

    def test_method_exists_on_sdk(self):
        from mcp_server_buildium.buildium_sdk.api.lease_transactions_api import (
            LeaseTransactionsApi,
        )

        assert hasattr(
            LeaseTransactionsApi,
            "external_api_lease_ledger_transactions_get_lease_ledgers",
        )
        assert not hasattr(
            LeaseTransactionsApi,
            "external_api_lease_transactions_get_lease_transactions",
        )


# ---------------------------------------------------------------------------
# Bug #3 — list_bank_account_transactions missing required startdate/enddate
# ---------------------------------------------------------------------------

class TestListBankAccountTransactionsRequiresDates:
    """Original bug: the MCP tool wrapper omitted startdate and enddate
    parameters that the underlying Buildium API requires. Every call failed
    with a missing-required-argument error. The fix adds both as required
    string (YYYY-MM-DD) params on the tool and passes them through.
    """

    def test_source_exposes_startdate_and_enddate(self):
        from mcp_server_buildium.tools import bank_accounts as bank_tools

        src = inspect.getsource(bank_tools.register_bank_account_tools)
        # Both must be present in the function signature, not just the body.
        assert "startdate: str" in src
        assert "enddate: str" in src

    def test_dates_are_passed_to_sdk_call(self):
        from mcp_server_buildium.tools import bank_accounts as bank_tools

        src = inspect.getsource(bank_tools.register_bank_account_tools)
        # The SDK call must pass startdate=... and enddate=... as date objects.
        assert "startdate=_date.fromisoformat(startdate)" in src
        assert "enddate=_date.fromisoformat(enddate)" in src


# ---------------------------------------------------------------------------
# Bug #4 — list_leases property_id wrong kwarg, unit_id unsupported
# ---------------------------------------------------------------------------

class TestListLeasesFilterWiring:
    """Original bug: tools/leases.py passed `propertyid=` (singular) but the
    SDK expects `propertyids=` (plural list). Also `unitid=` was passed but
    the SDK has no such kwarg — Buildium's API has no native unit_id filter
    on this endpoint at all. The fix list-wraps property_id and applies
    unit_id as a client-side filter.
    """

    def test_source_uses_propertyids_plural_list(self):
        from mcp_server_buildium.tools import leases as leases_tools

        src = inspect.getsource(leases_tools.register_lease_tools)
        assert 'kwargs["propertyids"] = [property_id]' in src, (
            "property_id must be wrapped as a list under the 'propertyids' kwarg"
        )
        assert '"propertyid"' not in src, "old singular kwarg must be removed"
        assert '"unitid"' not in src, "non-existent unitid kwarg must be removed"

    def test_unit_id_is_applied_client_side(self):
        from mcp_server_buildium.tools import leases as leases_tools

        src = inspect.getsource(leases_tools.register_lease_tools)
        assert "if unit_id is not None:" in src
        # The filter must look up UnitId on each lease record.
        assert "UnitId" in src or "unit_id" in src

    def test_sdk_signature_uses_propertyids_list(self):
        """Sanity-check that the underlying SDK method really takes List[int]
        — confirms the fix matches reality."""
        from mcp_server_buildium.buildium_sdk.api.leases_api import LeasesApi

        sig = inspect.signature(LeasesApi.external_api_leases_get_leases)
        assert "propertyids" in sig.parameters
        assert "propertyid" not in sig.parameters
