"""Task management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.task_category_put_message import TaskCategoryPutMessage
from ..buildium_sdk.models.task_category_save_message import TaskCategorySaveMessage
from ._result import to_result


def register_task_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register task-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_tasks(
        task_type: str | None = None,
        assigned_to_user_id: int | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List tasks from Buildium."""
        result = await client.tasks_api.external_api_tasks_get_all_tasks(
            type=task_type,
            assignedtoid=assigned_to_user_id,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "tasks")

    @mcp.tool()
    async def get_task(task_id: int) -> dict[str, Any]:
        """Get a specific task by ID."""
        result = await client.tasks_api.external_api_tasks_get_task_by_id(task_id=task_id)
        return to_result(result)

    @mcp.tool()
    async def list_task_categories(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List task categories from Buildium."""
        result = await client.tasks_api.external_api_task_categories_get_all_task_categories(
            limit=limit, offset=offset
        )
        return to_result(result, "categories")

    @mcp.tool()
    async def create_task_category(category_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new task category."""
        category_message = TaskCategorySaveMessage(**category_data)

        result = await client.tasks_api.external_api_task_categories_create_task_category(
            task_category_save_message=category_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_task_category(
        category_id: int, category_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a task category."""
        category_message = TaskCategoryPutMessage(**category_data)

        result = await client.tasks_api.external_api_task_categories_update_task_category(
            task_category_id=category_id, task_category_put_message=category_message
        )
        return to_result(result)
