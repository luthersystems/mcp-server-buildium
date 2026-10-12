"""Bank account management tools for Buildium."""

from datetime import UTC, date, datetime, timedelta
from typing import Any

from fastmcp import FastMCP

from ..buildium_client import BuildiumClient
from ..buildium_sdk.models.bank_account_post_message import BankAccountPostMessage
from ..buildium_sdk.models.bank_account_put_message import BankAccountPutMessage
from ._result import to_result


def register_bank_account_tools(mcp: FastMCP, client: BuildiumClient) -> None:
    """Register bank account-related tools with the MCP server.

    Args:
        mcp: FastMCP server instance.
        client: Buildium client instance.
    """

    @mcp.tool()
    async def list_bank_accounts(limit: int = 100, offset: int = 0) -> dict[str, Any]:
        """List bank accounts from Buildium."""
        result = await client.bank_accounts_api.external_api_bank_accounts_get_all_bank_accounts(
            limit=limit, offset=offset
        )
        return to_result(result, "bankAccounts")

    @mcp.tool()
    async def get_bank_account(bank_account_id: int) -> dict[str, Any]:
        """Get a specific bank account by ID."""
        result = await client.bank_accounts_api.external_api_bank_accounts_get_bank_account(
            bank_account_id=bank_account_id
        )
        return to_result(result)

    @mcp.tool()
    async def create_bank_account(bank_account_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new bank account."""
        account_message = BankAccountPostMessage(**bank_account_data)

        result = await client.bank_accounts_api.external_api_bank_accounts_create_bank_account(
            bank_account_post_message=account_message
        )
        return to_result(result)

    @mcp.tool()
    async def update_bank_account(
        bank_account_id: int, bank_account_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Update an existing bank account."""
        account_message = BankAccountPutMessage(**bank_account_data)

        result = await client.bank_accounts_api.external_api_bank_accounts_update_bank_account(
            bank_account_id=bank_account_id, bank_account_put_message=account_message
        )
        return to_result(result)

    @mcp.tool()
    async def list_bank_account_transactions(
        bank_account_id: int,
        start_date: date | None = None,
        end_date: date | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List transactions for a specific bank account.

        Buildium requires a date range. Without one, the last 30 days (UTC) are listed.

        Args:
            bank_account_id: The bank account ID.
            start_date: First transaction date (YYYY-MM-DD). Default: 30 days before end_date.
            end_date: Last transaction date (YYYY-MM-DD). Default: today.
            limit: Maximum number of results (default: 100).
            offset: Offset for pagination (default: 0).
        """
        end = end_date or datetime.now(UTC).date()
        start = start_date or end - timedelta(days=30)
        if start > end:
            raise ValueError(f"start_date {start} is after end_date {end}")
        api = client.bank_accounts_api
        result = await api.external_api_bank_account_transactions_get_bank_account_transactions(
            bank_account_id=bank_account_id,
            startdate=start,
            enddate=end,
            limit=limit,
            offset=offset,
        )
        return to_result(result, "transactions")

    @mcp.tool()
    async def get_bank_account_transaction(
        bank_account_id: int, transaction_id: int
    ) -> dict[str, Any]:
        """Get a specific bank account transaction by ID."""
        result = await client.bank_accounts_api.external_api_bank_account_transactions_get_bank_account_transaction_by_id(
            bank_account_id=bank_account_id, transaction_id=transaction_id
        )
        return to_result(result)
