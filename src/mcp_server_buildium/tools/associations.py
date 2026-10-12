"""Association management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.association_post_message import AssociationPostMessage
from ..buildium_sdk.models.association_put_message import AssociationPutMessage
from ._result import to_result


def register_association_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register association-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_associations(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List associations from Buildium.

        Args:
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with associations list and metadata.
        """
        result = await client.associations_api.external_api_associations_get_associations(
            limit=limit, offset=offset
        )
        # Convert SDK model to dict
        return to_result(result, "associations")

    @mcp.tool()
    async def get_association(association_id: int) -> dict[str, Any]:
        """Get a specific association by ID.

        Args:
            association_id: The association ID.

        Returns:
            Association details as dictionary.
        """
        result = await client.associations_api.external_api_associations_get_association_by_id(
            association_id=association_id
        )
        return to_result(result)

    @mcp.tool()
    async def create_association(association_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new association.

        Args:
            association_data: Association data dictionary with required fields.

        Returns:
            Created association details.
        """
        # Convert dict to SDK model
        association_message = AssociationPostMessage(**association_data)
        result = await client.associations_api.external_api_associations_create_association(
            association_post_message=association_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_association(
        association_id: int, association_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update an existing association.

        Args:
            association_id: The association ID.
            association_data: Association data dictionary with fields to update.

        Returns:
            Updated association details.
        """
        association_message = AssociationPutMessage(**association_data)
        result = await client.associations_api.external_api_associations_update_association(
            association_id=association_id, association_put_message=association_message
        )
        return to_result(result)

    @mcp.tool()
    async def list_association_board_members(
        association_id: int, limit: int = 100, offset: int = 0
    ) -> dict[str, Any]:
        """List board members for a specific association.

        Args:
            association_id: The association ID.
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with board members list.
        """
        result = await client.board_members_api.external_api_association_board_members_get_all_association_board_members(
            association_id=association_id, limit=limit, offset=offset
        )
        return to_result(result, "boardMembers")

    @mcp.tool()
    async def list_association_ownership_accounts(
        association_id: int, limit: int = 100, offset: int = 0
    ) -> dict[str, Any]:
        """List ownership accounts for a specific association.

        Args:
            association_id: The association ID.
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with ownership accounts list.
        """
        result = await client.ownership_accounts_api.external_api_ownership_accounts_get_all_ownership_accounts(
            associationids=[association_id], limit=limit, offset=offset
        )
        return to_result(result, "ownershipAccounts")
