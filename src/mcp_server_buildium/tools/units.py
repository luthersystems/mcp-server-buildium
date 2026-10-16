"""Unit management tools for Buildium (rental and association)."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.association_unit_put_message import AssociationUnitPutMessage
from ..buildium_sdk.models.association_units_post_message import AssociationUnitsPostMessage
from ..buildium_sdk.models.rental_unit_put_message import RentalUnitPutMessage
from ..buildium_sdk.models.rental_units_post_message import RentalUnitsPostMessage
from ._result import to_result


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
        result = await client.rental_units_api.external_api_rental_units_get_all_rental_units(
            propertyids=[property_id] if property_id is not None else None,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "units")

    @mcp.tool()
    async def get_rental_unit(unit_id: int) -> dict[str, Any]:
        """Get a specific rental unit by ID."""
        result = await client.rental_units_api.external_api_rental_units_get_rental_unit_by_id(
            unit_id=unit_id
        )
        return to_result(result)

    @mcp.tool()
    async def create_rental_unit(unit_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new rental unit."""
        unit_message = RentalUnitsPostMessage(**unit_data)

        result = await client.rental_units_api.external_api_rental_units_create_rental_unit(
            rental_units_post_message=unit_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_rental_unit(unit_id: int, unit_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing rental unit."""
        unit_message = RentalUnitPutMessage(**unit_data)

        result = await client.rental_units_api.external_api_rental_units_update_rental_unit(
            unit_id=unit_id, rental_unit_put_message=unit_message
        )
        return to_result(result)

    # Association Units
    @mcp.tool()
    async def list_association_units(
        property_id: int | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List association units from Buildium."""
        api = client.association_units_api
        result = await api.external_api_association_units_get_all_association_units(
            associationids=[property_id] if property_id is not None else None,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "units")

    @mcp.tool()
    async def create_association_unit(unit_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new association unit."""
        unit_message = AssociationUnitsPostMessage(**unit_data)

        result = await client.association_units_api.external_api_association_units_create_association_unit(
            association_units_post_message=unit_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_association_unit(unit_id: int, unit_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing association unit."""
        unit_message = AssociationUnitPutMessage(**unit_data)

        result = await client.association_units_api.external_api_association_units_update_association_unit(
            unit_id=unit_id, association_unit_put_message=unit_message
        )
        return to_result(result)
