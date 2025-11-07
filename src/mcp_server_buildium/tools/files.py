"""File management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_file_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register file-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_files(
        entity_type: str | None = None,
        entity_id: int | None = None,
        category_id: int | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List files from Buildium."""
        result = await client.files_api.external_api_files_get_files(
            entitytype=entity_type,
            entityid=entity_id,
            categoryid=category_id,
            limit=limit,
            offset=offset,
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"files": result, "count": len(result)}

    @mcp.tool()
    async def get_file(file_id: int) -> dict[str, Any]:
        """Get a specific file by ID."""
        result = await client.files_api.external_api_files_get_file_by_id(file_id=file_id)
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_file(file_id: int, file_data: dict[str, Any]) -> dict[str, Any]:
        """Update file metadata."""
        try:
            from mcp_server_buildium.buildium_sdk.models.file_put_message import FilePutMessage

            file_message = FilePutMessage(**file_data)
        except ImportError:
            file_message = file_data

        result = await client.files_api.external_api_files_update_file(
            file_id=file_id, file_put_message=file_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_file_upload_request(upload_request: dict[str, Any]) -> dict[str, Any]:
        """Create a file upload request to get an upload URL."""
        try:
            from mcp_server_buildium.buildium_sdk.models.file_upload_request_post_message import (
                FileUploadRequestPostMessage,
            )

            upload_message = FileUploadRequestPostMessage(**upload_request)
        except ImportError:
            upload_message = upload_request

        result = await client.files_api.external_api_file_uploads_create_file_upload_request_async(
            file_upload_request_post_message=upload_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_file_download_request(file_id: int) -> dict[str, Any]:
        """Create a file download request to get a download URL."""
        result = await client.files_api.external_api_file_download_get_file_download_url_async(
            file_id=file_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_file_categories() -> dict[str, Any]:
        """List file categories from Buildium."""
        result = await client.files_api.external_api_file_categories_get_file_categories()
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"categories": result, "count": len(result)}

    @mcp.tool()
    async def create_file_category(category_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new file category."""
        try:
            from mcp_server_buildium.buildium_sdk.models.file_category_post_message import (
                FileCategoryPostMessage,
            )

            category_message = FileCategoryPostMessage(**category_data)
        except ImportError:
            category_message = category_data

        result = await client.files_api.external_api_file_categories_create_file_category(
            file_category_post_message=category_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_file_category(
        category_id: int, category_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a file category."""
        try:
            from mcp_server_buildium.buildium_sdk.models.file_category_put_message import (
                FileCategoryPutMessage,
            )

            category_message = FileCategoryPutMessage(**category_data)
        except ImportError:
            category_message = category_data

        result = await client.files_api.external_api_file_categories_update_file_category(
            file_category_id=category_id, file_category_put_message=category_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
