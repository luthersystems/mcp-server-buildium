"""Vendor management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.vendor_category_save_message import VendorCategorySaveMessage
from ..buildium_sdk.models.vendor_post_message import VendorPostMessage
from ..buildium_sdk.models.vendor_put_message import VendorPutMessage
from ._result import to_result


def register_vendor_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register vendor-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_vendors(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List vendors from Buildium."""
        result = await client.vendors_api.external_api_vendors_get_all_vendors(
            limit=limit, offset=offset
        )
        return to_result(result, "vendors")

    @mcp.tool()
    async def get_vendor(vendor_id: int) -> dict[str, Any]:
        """Get a specific vendor by ID."""
        result = await client.vendors_api.external_api_vendors_get_vendor_by_id(vendor_id=vendor_id)
        return to_result(result)

    @mcp.tool()
    async def create_vendor(vendor_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new vendor."""
        vendor_message = VendorPostMessage(**vendor_data)

        result = await client.vendors_api.external_api_vendors_create_vendor(
            vendor_post_message=vendor_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_vendor(vendor_id: int, vendor_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing vendor."""
        vendor_message = VendorPutMessage(**vendor_data)

        result = await client.vendors_api.external_api_vendors_update_vendor(
            vendor_id=vendor_id, vendor_put_message=vendor_message
        )
        return to_result(result)

    @mcp.tool()
    async def list_vendor_categories() -> dict[str, Any]:
        """List vendor categories from Buildium."""
        result = await client.vendors_api.external_api_vendor_categories_get_all_vendor_categories()
        return to_result(result, "categories")

    @mcp.tool()
    async def create_vendor_category(category_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new vendor category."""
        category_message = VendorCategorySaveMessage(**category_data)

        result = await client.vendors_api.external_api_vendor_categories_create_vendor_category(
            vendor_category_save_message=category_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_vendor_category(
        category_id: int, category_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a vendor category."""
        category_message = VendorCategorySaveMessage(**category_data)

        result = await client.vendors_api.external_api_vendor_categories_update_vendor_category(
            vendor_category_id=category_id, vendor_category_save_message=category_message
        )
        return to_result(result)
