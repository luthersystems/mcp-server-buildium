"""Unit management tools for Buildium (rental and association)."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_unit_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register unit-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    # Rental Units
    @mcp.tool()
    async def list_rental_units(
        property_id: int | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List rental units from Buildium."""
        result = await client.rental_units_api.external_api_rental_units_get_rental_units(
            propertyid=property_id, limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"units": result, "count": len(result)}

    @mcp.tool()
    async def get_rental_unit(unit_id: int) -> dict[str, Any]:
        """Get a specific rental unit by ID."""
        result = await client.rental_units_api.external_api_rental_units_get_rental_unit_by_id(
            unit_id=unit_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_rental_unit(unit_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new rental unit."""
        try:
            from mcp_server_buildium.buildium_sdk.models.rental_unit_post_message import RentalUnitPostMessage

            unit_message = RentalUnitPostMessage(**unit_data)
        except ImportError:
            unit_message = unit_data

        result = await client.rental_units_api.external_api_rental_units_create_rental_unit(
            rental_unit_post_message=unit_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_rental_unit(unit_id: int, unit_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing rental unit."""
        try:
            from mcp_server_buildium.buildium_sdk.models.rental_unit_put_message import RentalUnitPutMessage

            unit_message = RentalUnitPutMessage(**unit_data)
        except ImportError:
            unit_message = unit_data

        result = await client.rental_units_api.external_api_rental_units_update_rental_unit(
            unit_id=unit_id, rental_unit_put_message=unit_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    # Association Units
    @mcp.tool()
    async def list_association_units(
        property_id: int | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List association units from Buildium."""
        result = (
            await client.association_units_api.external_api_association_units_get_association_units(
                propertyid=property_id, limit=limit, offset=offset
            )
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"units": result, "count": len(result)}

    @mcp.tool()
    async def create_association_unit(unit_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new association unit."""
        try:
            from mcp_server_buildium.buildium_sdk.models.association_unit_post_message import (
                AssociationUnitPostMessage,
            )

            unit_message = AssociationUnitPostMessage(**unit_data)
        except ImportError:
            unit_message = unit_data

        result = await client.association_units_api.external_api_association_units_create_association_unit(
            association_unit_post_message=unit_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_association_unit(unit_id: int, unit_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing association unit."""
        try:
            from mcp_server_buildium.buildium_sdk.models.association_unit_put_message import (
                AssociationUnitPutMessage,
            )

            unit_message = AssociationUnitPutMessage(**unit_data)
        except ImportError:
            unit_message = unit_data

        result = await client.association_units_api.external_api_association_units_update_association_unit(
            unit_id=unit_id, association_unit_put_message=unit_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
