"""Rental property management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_rental_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register rental-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_rentals(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List rental properties from Buildium.

        Args:
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with rentals list and metadata.
        """
        result = await client.rentals_api.external_api_rentals_get_all_rentals(
            limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"rentals": result, "count": len(result)}

    @mcp.tool()
    async def get_rental(property_id: int) -> dict[str, Any]:
        """Get a specific rental property by ID.

        Args:
            property_id: The property ID.

        Returns:
            Rental property details as dictionary.
        """
        result = await client.rentals_api.external_api_rentals_get_rental_by_id(
            property_id=property_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_rental(rental_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new rental property.

        Args:
            rental_data: Rental property data dictionary with required fields.

        Returns:
            Created rental property details.
        """
        try:
            from mcp_server_buildium.buildium_sdk.models.rental_property_post_message import RentalPropertyPostMessage

            rental_message = RentalPropertyPostMessage(**rental_data)
        except ImportError:
            rental_message = rental_data

        result = await client.rentals_api.external_api_rentals_create_rental_property(
            rental_property_post_message=rental_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_rental(property_id: int, rental_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing rental property.

        Args:
            property_id: The property ID.
            rental_data: Rental property data dictionary with fields to update.

        Returns:
            Updated rental property details.
        """
        try:
            from mcp_server_buildium.buildium_sdk.models.rental_property_put_message import RentalPropertyPutMessage

            rental_message = RentalPropertyPutMessage(**rental_data)
        except ImportError:
            rental_message = rental_data

        result = await client.rentals_api.external_api_rentals_update_rental_property(
            property_id=property_id, rental_property_put_message=rental_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_unit_listings(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List unit listings from Buildium.

        Args:
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with listings list.
        """
        from mcp_server_buildium.buildium_sdk.api.listings_api import ListingsApi

        listings_api = ListingsApi(client._api_client)
        result = await listings_api.external_api_listings_get_unit_listings(
            limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"listings": result, "count": len(result)}
