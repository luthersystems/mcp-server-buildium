"""Lease management tools for Buildium."""

from datetime import date
from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.lease_message import LeaseMessage
from ..buildium_sdk.models.lease_post_message import LeasePostMessage
from ..buildium_sdk.models.lease_put_message import LeasePutMessage
from ._result import to_result

# Buildium's largest page, and how many pages a unit_id search may read.
UNIT_SCAN_PAGE_SIZE = 1000
UNIT_SCAN_MAX_PAGES = 20


def register_lease_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register lease-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_leases(
        property_id: int | None = None,
        unit_id: int | None = None,
        lease_status: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List leases from Buildium.

        Args:
            property_id: Optional property ID to filter by.
            unit_id: Optional unit ID to filter by. Buildium's leases endpoint has no unit
                filter, so this reads every matching lease (pass property_id to keep that
                small) and applies limit and offset to the leases of the unit.
            lease_status: Optional lease status filter (e.g., "Active", "Future", "Past").
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with leases list and metadata.
        """
        propertyids = [property_id] if property_id is not None else None
        leasestatuses = [lease_status] if lease_status is not None else None
        if unit_id is None:
            result = await client.leases_api.external_api_leases_get_leases(
                propertyids=propertyids, leasestatuses=leasestatuses, limit=limit, offset=offset
            )
            return to_result(result, "leases")

        matches: list[LeaseMessage] = []
        for page in range(UNIT_SCAN_MAX_PAGES):
            batch = await client.leases_api.external_api_leases_get_leases(
                propertyids=propertyids,
                leasestatuses=leasestatuses,
                limit=UNIT_SCAN_PAGE_SIZE,
                offset=page * UNIT_SCAN_PAGE_SIZE,
            )
            matches.extend(lease for lease in batch if lease.unit_id == unit_id)
            if len(batch) < UNIT_SCAN_PAGE_SIZE:
                return to_result(matches[offset : offset + limit], "leases")
        raise ValueError(
            f"more than {UNIT_SCAN_MAX_PAGES * UNIT_SCAN_PAGE_SIZE} leases to search for "
            "unit_id; pass property_id to narrow the search"
        )

    @mcp.tool()
    async def get_lease(lease_id: int) -> dict[str, Any]:
        """Get a specific lease by ID.

        Args:
            lease_id: The lease ID.

        Returns:
            Lease details as dictionary.
        """
        result = await client.leases_api.external_api_leases_get_lease_by_id(lease_id=lease_id)
        return to_result(result)

    @mcp.tool()
    async def create_lease(lease_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new lease.

        Args:
            lease_data: Lease data dictionary with required fields (propertyId, unitId, etc.).

        Returns:
            Created lease details.
        """
        lease_message = LeasePostMessage(**lease_data)

        result = await client.leases_api.external_api_leases_create_lease(
            lease_post_message=lease_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_lease(lease_id: int, lease_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing lease.

        Args:
            lease_id: The lease ID.
            lease_data: Lease data dictionary with fields to update.

        Returns:
            Updated lease details.
        """
        lease_message = LeasePutMessage(**lease_data)

        result = await client.leases_api.external_api_leases_update_lease(
            lease_id=lease_id, lease_put_message=lease_message
        )
        return to_result(result)

    @mcp.tool()
    async def list_lease_transactions(
        lease_id: int,
        transaction_date_from: date | None = None,
        transaction_date_to: date | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List ledger transactions for a specific lease.

        Args:
            lease_id: The lease ID.
            transaction_date_from: Optional earliest transaction date (YYYY-MM-DD).
            transaction_date_to: Optional latest transaction date (YYYY-MM-DD).
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with transactions list.
        """
        api = client.lease_transactions_api
        result = await api.external_api_lease_ledger_transactions_get_lease_ledgers(
            lease_id=lease_id,
            transactiondatefrom=transaction_date_from,
            transactiondateto=transaction_date_to,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "transactions")
