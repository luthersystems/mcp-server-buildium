"""Applicant management tools for Buildium."""

from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_applicant_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register applicant-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_applicants(
        email: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List rental applicants from Buildium.

        Args:
            email: Optional email address to filter by.
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with applicants list and metadata.
        """
        result = await client.applicants_api.external_api_applicants_get_applicants(
            email=email, limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"applicants": result, "count": len(result)}

    @mcp.tool()
    async def get_applicant(applicant_id: int) -> dict[str, Any]:
        """Get a specific applicant by ID.

        Args:
            applicant_id: The applicant ID.

        Returns:
            Applicant details as dictionary.
        """
        result = await client.applicants_api.external_api_applicants_get_applicant_by_id(
            applicant_id=applicant_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_applicant(applicant_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new applicant.

        Args:
            applicant_data: Applicant data dictionary with required fields.

        Returns:
            Created applicant details.
        """
        try:
            from buildium_sdk.models.applicant_post_message import ApplicantPostMessage

            applicant_message = ApplicantPostMessage(**applicant_data)
        except ImportError:
            applicant_message = applicant_data

        result = await client.applicants_api.external_api_applicants_create_applicant(
            applicant_post_message=applicant_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_applicant(applicant_id: int, applicant_data: dict[str, Any]) -> dict[str, Any]:
        """Update an existing applicant.

        Args:
            applicant_id: The applicant ID.
            applicant_data: Updated applicant data dictionary.

        Returns:
            Updated applicant details.
        """
        try:
            from buildium_sdk.models.applicant_put_message import ApplicantPutMessage

            applicant_message = ApplicantPutMessage(**applicant_data)
        except ImportError:
            applicant_message = applicant_data

        result = await client.applicants_api.external_api_applicants_update_applicant(
            applicant_id=applicant_id, applicant_put_message=applicant_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_applicant_applications(applicant_id: int) -> dict[str, Any]:
        """List applications for a specific applicant.

        Args:
            applicant_id: The applicant ID.

        Returns:
            Dictionary with applications list.
        """
        result = await client.applicants_api.external_api_applicant_applications_get_applications_for_applicant(
            applicant_id=applicant_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return (
            result if isinstance(result, dict) else {"applications": result, "count": len(result)}
        )

    @mcp.tool()
    async def get_application(applicant_id: int, application_id: int) -> dict[str, Any]:
        """Get a specific application by ID.

        Args:
            applicant_id: The applicant ID.
            application_id: The application ID.

        Returns:
            Application details as dictionary.
        """
        result = await client.applicants_api.external_api_applicant_applications_get_application_for_applicant_by_id(
            applicant_id=applicant_id, application_id=application_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_application(
        applicant_id: int, application_id: int, application_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update an application status.

        Args:
            applicant_id: The applicant ID.
            application_id: The application ID.
            application_data: Updated application data dictionary.

        Returns:
            Updated application details.
        """
        try:
            from buildium_sdk.models.application_put_message import ApplicationPutMessage

            application_message = ApplicationPutMessage(**application_data)
        except ImportError:
            application_message = application_data

        result = await client.applicants_api.external_api_applicant_applications_update_application(
            applicant_id=applicant_id,
            application_id=application_id,
            application_put_message=application_message,
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_applicant_groups(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List applicant groups from Buildium.

        Args:
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).

        Returns:
            Dictionary with applicant groups list.
        """
        result = await client.applicants_api.external_api_applicant_groups_get_applicant_groups(
            limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return (
            result
            if isinstance(result, dict)
            else {"applicantGroups": result, "count": len(result)}
        )

    @mcp.tool()
    async def create_applicant_group(group_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new applicant group.

        Args:
            group_data: Applicant group data dictionary.

        Returns:
            Created applicant group details.
        """
        try:
            from buildium_sdk.models.applicant_group_post_message import ApplicantGroupPostMessage

            group_message = ApplicantGroupPostMessage(**group_data)
        except ImportError:
            group_message = group_data

        result = await client.applicants_api.external_api_applicant_groups_create_applicant_group(
            applicant_group_post_message=group_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_applicant_group(group_id: int, group_data: dict[str, Any]) -> dict[str, Any]:
        """Update an applicant group.

        Args:
            group_id: The applicant group ID.
            group_data: Updated group data dictionary.

        Returns:
            Updated applicant group details.
        """
        try:
            from buildium_sdk.models.applicant_group_put_message import ApplicantGroupPutMessage

            group_message = ApplicantGroupPutMessage(**group_data)
        except ImportError:
            group_message = group_data

        result = await client.applicants_api.external_api_applicant_groups_update_applicant_group(
            applicant_group_id=group_id, applicant_group_put_message=group_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
