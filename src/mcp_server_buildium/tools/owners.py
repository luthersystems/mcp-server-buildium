"""Owner management tools for Buildium (rental and association)."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


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
        # Build kwargs, only including optional parameters if they have values
        kwargs = {
            "limit": limit,
            "offset": offset,
        }
        if property_id is not None:
            kwargs["propertyid"] = property_id
        
        result = await client.rental_owners_api.external_api_rental_owners_get_rental_owners(**kwargs)
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"owners": result, "count": len(result)}

    @mcp.tool()
    async def get_rental_owner(owner_id: int) -> dict[str, Any]:
        """Get a specific rental owner by ID."""
        result = await client.rental_owners_api.external_api_rental_owners_get_rental_owner_by_id(
            owner_id=owner_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_rental_owner(owner_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new rental owner."""
        try:
            from mcp_server_buildium.buildium_sdk.models.rental_owner_post_message import RentalOwnerPostMessage

            owner_message = RentalOwnerPostMessage(**owner_data)
        except ImportError:
            owner_message = owner_data

        result = await client.rental_owners_api.external_api_rental_owners_create_rental_owner(
            rental_owner_post_message=owner_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_rental_owner(owner_id: int, owner_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing rental owner."""
        try:
            from mcp_server_buildium.buildium_sdk.models.rental_owner_put_message import RentalOwnerPutMessage

            owner_message = RentalOwnerPutMessage(**owner_data)
        except ImportError:
            owner_message = owner_data

        result = await client.rental_owners_api.external_api_rental_owners_update_rental_owner(
            owner_id=owner_id, rental_owner_put_message=owner_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    # Association Owners
    @mcp.tool()
    async def list_association_owners(
        property_id: int | None = None,
        status: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List association owners from Buildium."""
        # Build kwargs, only including optional parameters if they have values
        kwargs = {
            "limit": limit,
            "offset": offset,
        }
        if property_id is not None:
            kwargs["propertyid"] = property_id
        if status is not None:
            kwargs["status"] = status
        
        result = await client.association_owners_api.external_api_association_owners_get_association_owners(**kwargs)
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"owners": result, "count": len(result)}

    @mcp.tool()
    async def get_association_owner(owner_id: int) -> dict[str, Any]:
        """Get a specific association owner by ID."""
        result = await client.association_owners_api.external_api_association_owners_get_association_owner_by_id(
            owner_id=owner_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_association_owner(owner_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new association owner."""
        try:
            from mcp_server_buildium.buildium_sdk.models.association_owner_post_message import (
                AssociationOwnerPostMessage,
            )

            owner_message = AssociationOwnerPostMessage(**owner_data)
        except ImportError:
            owner_message = owner_data

        result = await client.association_owners_api.external_api_association_owners_create_association_owner(
            association_owner_post_message=owner_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_association_owner(owner_id: int, owner_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing association owner."""
        try:
            from mcp_server_buildium.buildium_sdk.models.association_owner_put_message import (
                AssociationOwnerPutMessage,
            )

            owner_message = AssociationOwnerPutMessage(**owner_data)
        except ImportError:
            owner_message = owner_data

        result = await client.association_owners_api.external_api_association_owners_update_association_owner(
            owner_id=owner_id, association_owner_put_message=owner_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
