"""Tenant management tools for Buildium (rental and association)."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.association_tenant_post_message import AssociationTenantPostMessage
from ..buildium_sdk.models.association_tenant_put_message import AssociationTenantPutMessage
from ..buildium_sdk.models.rental_tenant_post_message import RentalTenantPostMessage
from ..buildium_sdk.models.rental_tenant_put_message import RentalTenantPutMessage
from ._result import to_result


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
            propertyids=[property_id] if property_id is not None else None,
            unitids=[unit_id] if unit_id is not None else None,
            leasetermstatuses=[status] if status is not None else None,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "tenants")

    @mcp.tool()
    async def get_rental_tenant(tenant_id: int) -> dict[str, Any]:
        """Get a specific rental tenant by ID."""
        result = await client.rental_tenants_api.external_api_rental_tenants_get_tenant_by_id(
            tenant_id=tenant_id
        )
        return to_result(result)

    @mcp.tool()
    async def create_rental_tenant(tenant_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new rental tenant."""
        tenant_message = RentalTenantPostMessage(**tenant_data)

        result = await client.rental_tenants_api.external_api_rental_tenants_create_rental_tenant(
            rental_tenant_post_message=tenant_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_rental_tenant(tenant_id: int, tenant_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing rental tenant."""
        tenant_message = RentalTenantPutMessage(**tenant_data)

        result = await client.rental_tenants_api.external_api_rental_tenants_update_rental_tenant(
            tenant_id=tenant_id, rental_tenant_put_message=tenant_message
        )
        return to_result(result)

    # Association Tenants
    @mcp.tool()
    async def list_association_tenants(
        property_id: int | None = None,
        status: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List association tenants from Buildium."""
        api = client.association_tenants_api
        result = await api.external_api_association_tenants_get_association_tenants(
            associationids=[property_id] if property_id is not None else None,
            statuses=[status] if status is not None else None,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "tenants")

    @mcp.tool()
    async def create_association_tenant(tenant_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new association tenant."""
        tenant_message = AssociationTenantPostMessage(**tenant_data)

        result = await client.association_tenants_api.external_api_association_tenants_create_association_tenant(
            association_tenant_post_message=tenant_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_association_tenant(
        tenant_id: int, tenant_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update an existing association tenant."""
        tenant_message = AssociationTenantPutMessage(**tenant_data)

        result = await client.association_tenants_api.external_api_association_tenants_update_association_tenant(
            tenant_id=tenant_id, association_tenant_put_message=tenant_message
        )
        return to_result(result)
