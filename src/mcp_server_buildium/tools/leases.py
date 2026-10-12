"""Lease management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.lease_post_message import LeasePostMessage
from ..buildium_sdk.models.lease_put_message import LeasePutMessage
from ._result import to_result


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
            unit_id: Optional unit ID. The Buildium endpoint has no unit filter, so this
                keeps only the matching leases of the returned page.
            lease_status: Optional lease status filter (e.g., "Active", "Future", "Past").
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with leases list and metadata.
        """
        result = await client.leases_api.external_api_leases_get_leases(
            propertyids=[property_id] if property_id is not None else None,
            leasestatuses=[lease_status] if lease_status is not None else None,
            limit=limit,
            offset=offset,
        )
        if unit_id is not None:
            # The leases endpoint has no unit filter; filter the page here.
            result = [lease for lease in result if lease.unit_id == unit_id]
        return to_result(result, "leases")

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
        lease_id: int, limit: int = 100, offset: int = 0
    ) -> dict[str, Any]:
        """List transactions for a specific lease.

        Args:
            lease_id: The lease ID.
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with transactions list.
        """
        api = client.lease_transactions_api
        result = await api.external_api_lease_ledger_transactions_get_lease_ledgers(
            lease_id=lease_id, limit=limit, offset=offset
        )
        return to_result(result, "transactions")
