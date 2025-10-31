"""Bill management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_bill_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register bill-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_bills(
        vendor_id: int | None = None,
        status: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List bills from Buildium."""
        result = await client.bills_api.external_api_bills_get_bills(
            vendorid=vendor_id, status=status, limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"bills": result, "count": len(result)}

    @mcp.tool()
    async def get_bill(bill_id: int) -> dict[str, Any]:
        """Get a specific bill by ID."""
        result = await client.bills_api.external_api_bills_get_bill_by_id(bill_id=bill_id)
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_bill(bill_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new bill."""
        try:
            from buildium_sdk.models.bill_post_message import BillPostMessage

            bill_message = BillPostMessage(**bill_data)
        except ImportError:
            bill_message = bill_data

        result = await client.bills_api.external_api_bills_create_bill(
            bill_post_message=bill_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_bill(bill_id: int, bill_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing bill."""
        try:
            from buildium_sdk.models.bill_put_message import BillPutMessage

            bill_message = BillPutMessage(**bill_data)
        except ImportError:
            bill_message = bill_data

        result = await client.bills_api.external_api_bills_update_bill(
            bill_id=bill_id, bill_put_message=bill_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_bill_payments(bill_id: int) -> dict[str, Any]:
        """List payments for a specific bill."""
        result = await client.bills_api.external_api_bill_payments_read_get_bill_payments(
            bill_id=bill_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"payments": result, "count": len(result)}

    @mcp.tool()
    async def get_bill_payment(bill_id: int, payment_id: int) -> dict[str, Any]:
        """Get a specific bill payment by ID."""
        result = await client.bills_api.external_api_bill_payments_read_get_bill_payment_by_id(
            bill_id=bill_id, payment_id=payment_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_bill_payment(bill_id: int, payment_data: dict[str, Any]) -> dict[str, Any]:
        """Create a payment for a bill."""
        try:
            from buildium_sdk.models.bill_payment_post_message import BillPaymentPostMessage

            payment_message = BillPaymentPostMessage(**payment_data)
        except ImportError:
            payment_message = payment_data

        result = await client.bills_api.external_api_bill_payments_write_create_bill_payment(
            bill_id=bill_id, bill_payment_post_message=payment_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
