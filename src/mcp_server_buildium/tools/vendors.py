"""Vendor management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_vendor_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register vendor-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_vendors(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List vendors from Buildium."""
        result = await client.vendors_api.external_api_vendors_get_vendors(
            limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"vendors": result, "count": len(result)}

    @mcp.tool()
    async def get_vendor(vendor_id: int) -> dict[str, Any]:
        """Get a specific vendor by ID."""
        result = await client.vendors_api.external_api_vendors_get_vendor_by_id(vendor_id=vendor_id)
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_vendor(vendor_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new vendor."""
        try:
            from buildium_sdk.models.vendor_post_message import VendorPostMessage

            vendor_message = VendorPostMessage(**vendor_data)
        except ImportError:
            vendor_message = vendor_data

        result = await client.vendors_api.external_api_vendors_create_vendor(
            vendor_post_message=vendor_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_vendor(vendor_id: int, vendor_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing vendor."""
        try:
            from buildium_sdk.models.vendor_put_message import VendorPutMessage

            vendor_message = VendorPutMessage(**vendor_data)
        except ImportError:
            vendor_message = vendor_data

        result = await client.vendors_api.external_api_vendors_update_vendor(
            vendor_id=vendor_id, vendor_put_message=vendor_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_vendor_categories() -> dict[str, Any]:
        """List vendor categories from Buildium."""
        result = await client.vendors_api.external_api_vendor_categories_get_all_vendor_categories()
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"categories": result, "count": len(result)}

    @mcp.tool()
    async def create_vendor_category(category_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new vendor category."""
        try:
            from buildium_sdk.models.vendor_category_post_message import (
                VendorCategoryPostMessage,
            )

            category_message = VendorCategoryPostMessage(**category_data)
        except ImportError:
            category_message = category_data

        result = await client.vendors_api.external_api_vendor_categories_create_vendor_category(
            vendor_category_post_message=category_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_vendor_category(
        category_id: int, category_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a vendor category."""
        try:
            from buildium_sdk.models.vendor_category_put_message import VendorCategoryPutMessage

            category_message = VendorCategoryPutMessage(**category_data)
        except ImportError:
            category_message = category_data

        result = await client.vendors_api.external_api_vendor_categories_update_vendor_category(
            vendor_category_id=category_id, vendor_category_put_message=category_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
