"""Bank account management tools for Buildium."""

from typing import Any, Optional

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient


def register_bank_account_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register bank account-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_bank_accounts(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List bank accounts from Buildium."""
        result = await client.bank_accounts_api.external_api_bank_accounts_get_bank_accounts(
            limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return (
            result if isinstance(result, dict) else {"bankAccounts": result, "count": len(result)}
        )

    @mcp.tool()
    async def get_bank_account(bank_account_id: int) -> dict[str, Any]:
        """Get a specific bank account by ID."""
        result = await client.bank_accounts_api.external_api_bank_accounts_get_bank_account_by_id(
            bank_account_id=bank_account_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def create_bank_account(bank_account_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new bank account."""
        try:
            from mcp_server_buildium.buildium_sdk.models.bank_account_post_message import (
                BankAccountPostMessage,
            )

            account_message = BankAccountPostMessage(**bank_account_data)
        except ImportError:
            account_message = bank_account_data

        result = await client.bank_accounts_api.external_api_bank_accounts_create_bank_account(
            bank_account_post_message=account_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def update_bank_account(
        bank_account_id: int, bank_account_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update an existing bank account."""
        try:
            from mcp_server_buildium.buildium_sdk.models.bank_account_put_message import (
                BankAccountPutMessage,
            )

            account_message = BankAccountPutMessage(**bank_account_data)
        except ImportError:
            account_message = bank_account_data

        result = await client.bank_accounts_api.external_api_bank_accounts_update_bank_account(
            bank_account_id=bank_account_id, bank_account_put_message=account_message
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result

    @mcp.tool()
    async def list_bank_account_transactions(
        bank_account_id: int,
        startdate: str,
        enddate: str,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List transactions for a specific bank account.

        LOCAL PATCH (2026-04-07): Added required `startdate` and `enddate` params.
        Buildium's underlying API requires both for this endpoint, but the original
        MCP tool wrapper omitted them, causing every call to fail with a missing
        required argument error.

        Args:
            bank_account_id: The bank account ID.
            startdate: Filter transactions on or after this date (YYYY-MM-DD). Required.
            enddate: Filter transactions on or before this date (YYYY-MM-DD). Required.
            limit: Maximum number of results (default: 100, max 1000).
            offset: Offset for pagination (default: 0).
        """
        from datetime import date as _date

        result = await client.bank_accounts_api.external_api_bank_account_transactions_get_bank_account_transactions(
            bank_account_id=bank_account_id,
            startdate=_date.fromisoformat(startdate),
            enddate=_date.fromisoformat(enddate),
            limit=limit,
            offset=offset,
        )
        if isinstance(result, list):
            return {
                "transactions": [r.to_dict() if hasattr(r, "to_dict") else r for r in result],
                "count": len(result),
            }
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else {"transactions": result}

    @mcp.tool()
    async def get_bank_account_transaction(
        bank_account_id: int, transaction_id: int
    ) -> dict[str, Any]:
        """Get a specific bank account transaction by ID."""
        result = await client.bank_accounts_api.external_api_bank_account_transactions_get_bank_account_transaction_by_id(
            bank_account_id=bank_account_id, transaction_id=transaction_id
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return result if isinstance(result, dict) else result
