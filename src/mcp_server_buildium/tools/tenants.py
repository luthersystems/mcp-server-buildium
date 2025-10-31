"""Tenant management tools for Buildium (rental and association)."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_tenant_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register tenant-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    # Rental Tenants
    @mcp.tool()
    async def list_rental_tenants(
        property_id: int | None = None,
        unit_id: int | None = None,
        status: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List rental tenants from Buildium."""
        result = await client.rental_tenants_api.external_api_rental_tenants_get_all_tenants(
            propertyid=property_id,
            unitid=unit_id,
            status=status,
            limit=limit,
            offset=offset,
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"tenants": result, "count": len(result)}

    @mcp.tool()
    async def get_rental_tenant(tenant_id: int) -> dict[str, Any]:
        """Get a specific rental tenant by ID."""
        result = await client.rental_tenants_api.external_api_rental_tenants_get_tenant_by_id(
            tenant_id=tenant_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_rental_tenant(tenant_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new rental tenant."""
        try:
            from buildium_sdk.models.rental_tenant_post_message import RentalTenantPostMessage

            tenant_message = RentalTenantPostMessage(**tenant_data)
        except ImportError:
            tenant_message = tenant_data

        result = await client.rental_tenants_api.external_api_rental_tenants_create_rental_tenant(
            rental_tenant_post_message=tenant_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_rental_tenant(tenant_id: int, tenant_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing rental tenant."""
        try:
            from buildium_sdk.models.rental_tenant_put_message import RentalTenantPutMessage

            tenant_message = RentalTenantPutMessage(**tenant_data)
        except ImportError:
            tenant_message = tenant_data

        result = await client.rental_tenants_api.external_api_rental_tenants_update_rental_tenant(
            tenant_id=tenant_id, rental_tenant_put_message=tenant_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    # Association Tenants
    @mcp.tool()
    async def list_association_tenants(
        property_id: int | None = None,
        status: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List association tenants from Buildium."""
        result = await client.association_tenants_api.external_api_association_tenants_get_association_tenants(
            propertyid=property_id, status=status, limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"tenants": result, "count": len(result)}

    @mcp.tool()
    async def create_association_tenant(tenant_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new association tenant."""
        try:
            from buildium_sdk.models.association_tenant_post_message import (
                AssociationTenantPostMessage,
            )

            tenant_message = AssociationTenantPostMessage(**tenant_data)
        except ImportError:
            tenant_message = tenant_data

        result = await client.association_tenants_api.external_api_association_tenants_create_association_tenant(
            association_tenant_post_message=tenant_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_association_tenant(
        tenant_id: int, tenant_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update an existing association tenant."""
        try:
            from buildium_sdk.models.association_tenant_put_message import (
                AssociationTenantPutMessage,
            )

            tenant_message = AssociationTenantPutMessage(**tenant_data)
        except ImportError:
            tenant_message = tenant_data

        result = await client.association_tenants_api.external_api_association_tenants_update_association_tenant(
            tenant_id=tenant_id, association_tenant_put_message=tenant_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
