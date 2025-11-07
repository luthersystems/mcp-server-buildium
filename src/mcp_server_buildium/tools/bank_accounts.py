"""Bank account management tools for Buildium."""

from typing import Any

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
        bank_account_id: int, limit: int = 100, offset: int = 0
    ) -> dict[str, Any]:
        """List transactions for a specific bank account."""
        result = await client.bank_accounts_api.external_api_bank_account_transactions_get_bank_account_transactions(
            bank_account_id=bank_account_id, limit=limit, offset=offset
        )
        if hasattr(result, "to_dict"):
            return result.to_dict()
        return (
            result if isinstance(result, dict) else {"transactions": result, "count": len(result)}
        )

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
