"""Task management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


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
        result = await client.tasks_api.external_api_tasks_get_tasks(
            tasktype=task_type, assignedtouserid=assigned_to_user_id, limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"tasks": result, "count": len(result)}

    @mcp.tool()
    async def get_task(task_id: int) -> dict[str, Any]:
        """Get a specific task by ID."""
        result = await client.tasks_api.external_api_tasks_get_task_by_id(task_id=task_id)
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_task_categories() -> dict[str, Any]:
        """List task categories from Buildium."""
        result = await client.tasks_api.external_api_task_categories_get_all_task_categories()
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"categories": result, "count": len(result)}

    @mcp.tool()
    async def create_task_category(category_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new task category."""
        try:
            from buildium_sdk.models.task_category_post_message import TaskCategoryPostMessage

            category_message = TaskCategoryPostMessage(**category_data)
        except ImportError:
            category_message = category_data

        result = await client.tasks_api.external_api_task_categories_create_task_category(
            task_category_post_message=category_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_task_category(
        category_id: int, category_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a task category."""
        try:
            from buildium_sdk.models.task_category_put_message import TaskCategoryPutMessage

            category_message = TaskCategoryPutMessage(**category_data)
        except ImportError:
            category_message = category_data

        result = await client.tasks_api.external_api_task_categories_update_task_category(
            task_category_id=category_id, task_category_put_message=category_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
