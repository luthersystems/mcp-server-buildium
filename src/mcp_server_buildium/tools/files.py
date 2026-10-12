"""File management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.file_category_post_message import FileCategoryPostMessage
from ..buildium_sdk.models.file_category_put_message import FileCategoryPutMessage
from ..buildium_sdk.models.file_put_message import FilePutMessage
from ..buildium_sdk.models.file_upload_post_message import FileUploadPostMessage
from ._result import to_result


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
        return to_result(result, "files")

    @mcp.tool()
    async def get_file(file_id: int) -> dict[str, Any]:
        """Get a specific file by ID."""
        result = await client.files_api.external_api_files_get_file_by_id(file_id=file_id)
        return to_result(result)

    @mcp.tool()
    async def update_file(file_id: int, file_data: dict[str, Any]) -> dict[str, Any]:
        """Update file metadata."""
        file_message = FilePutMessage(**file_data)

        result = await client.files_api.external_api_files_update_file(
            file_id=file_id, file_put_message=file_message
        )
        return to_result(result)

    @mcp.tool()
    async def create_file_upload_request(upload_request: dict[str, Any]) -> dict[str, Any]:
        """Create a file upload request to get an upload URL."""
        upload_message = FileUploadPostMessage(**upload_request)

        result = await client.files_api.external_api_files_uploads_create_upload_file_request_async(
            file_upload_post_message=upload_message
        )
        return to_result(result)

    @mcp.tool()
    async def create_file_download_request(file_id: int) -> dict[str, Any]:
        """Create a file download request to get a download URL."""
        result = await client.files_api.external_api_file_download_get_file_download_url_async(
            file_id=file_id
        )
        return to_result(result)

    @mcp.tool()
    async def list_file_categories(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List file categories from Buildium."""
        result = await client.files_api.external_api_file_categories_get_file_categories(
            limit=limit, offset=offset
        )
        return to_result(result, "categories")

    @mcp.tool()
    async def create_file_category(category_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new file category."""
        category_message = FileCategoryPostMessage(**category_data)

        result = await client.files_api.external_api_file_categories_create_file_category(
            file_category_post_message=category_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_file_category(
        category_id: int, category_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a file category."""
        category_message = FileCategoryPutMessage(**category_data)

        result = await client.files_api.external_api_file_categories_update_file_category(
            file_category_id=category_id, file_category_put_message=category_message
        )
        return to_result(result)
