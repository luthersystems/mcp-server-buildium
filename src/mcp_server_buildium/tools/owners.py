"""Owner management tools for Buildium (rental and association)."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.association_owner_put_message import AssociationOwnerPutMessage
from ..buildium_sdk.models.association_owner_to_existing_ownership_account_post_message import (
    AssociationOwnerToExistingOwnershipAccountPostMessage,
)
from ..buildium_sdk.models.rental_owner_post_message import RentalOwnerPostMessage
from ..buildium_sdk.models.rental_owner_put_message import RentalOwnerPutMessage
from ._result import to_result


def register_owner_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register owner-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    # Rental Owners
    @mcp.tool()
    async def list_rental_owners(
        property_id: int | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List rental owners from Buildium."""
        result = await client.rental_owners_api.external_api_rental_owners_get_rental_owners(
            propertyids=[property_id] if property_id is not None else None,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "owners")

    @mcp.tool()
    async def get_rental_owner(owner_id: int) -> dict[str, Any]:
        """Get a specific rental owner by ID."""
        result = await client.rental_owners_api.external_api_rental_owners_get_rental_owner_by_id(
            rental_owner_id=owner_id
        )
        return to_result(result)

    @mcp.tool()
    async def create_rental_owner(owner_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new rental owner."""
        owner_message = RentalOwnerPostMessage(**owner_data)

        result = await client.rental_owners_api.external_api_rental_owners_create_rental_owner(
            rental_owner_post_message=owner_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_rental_owner(owner_id: int, owner_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing rental owner."""
        owner_message = RentalOwnerPutMessage(**owner_data)

        result = await client.rental_owners_api.external_api_rental_owners_update_rental_owner(
            rental_owner_id=owner_id, rental_owner_put_message=owner_message
        )
        return to_result(result)

    # Association Owners
    @mcp.tool()
    async def list_association_owners(
        property_id: int | None = None,
        status: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List association owners from Buildium."""
        api = client.association_owners_api
        result = await api.external_api_association_owners_get_all_association_owners(
            associationids=[property_id] if property_id is not None else None,
            statuses=[status] if status is not None else None,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "owners")

    @mcp.tool()
    async def get_association_owner(owner_id: int) -> dict[str, Any]:
        """Get a specific association owner by ID."""
        result = await client.association_owners_api.external_api_association_owners_get_association_owner_by_id(
            owner_id=owner_id
        )
        return to_result(result)

    @mcp.tool()
    async def create_association_owner(owner_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new association owner."""
        owner_message = AssociationOwnerToExistingOwnershipAccountPostMessage(**owner_data)

        result = await client.association_owners_api.external_api_association_owners_create_association_owner(
            association_owner_to_existing_ownership_account_post_message=owner_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_association_owner(owner_id: int, owner_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing association owner."""
        owner_message = AssociationOwnerPutMessage(**owner_data)

        result = await client.association_owners_api.external_api_association_owners_update_association_owner(
            owner_id=owner_id, association_owner_put_message=owner_message
        )
        return to_result(result)
