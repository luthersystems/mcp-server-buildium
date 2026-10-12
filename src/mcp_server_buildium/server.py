"""Main MCP server entry point for Buildium."""

from collections.abc import Callable

from fastmcp import FastMCP

from .buildium_client import BuildiumClient
from .config import BuildiumConfig
from .tools.applicants import register_applicant_tools
from .tools.associations import register_association_tools
from .tools.bank_accounts import register_bank_account_tools
from .tools.bills import register_bill_tools
from .tools.files import register_file_tools
from .tools.leases import register_lease_tools
from .tools.owners import register_owner_tools
from .tools.rentals import register_rental_tools
from .tools.tasks import register_task_tools
from .tools.tenants import register_tenant_tools
from .tools.units import register_unit_tools
from .tools.vendors import register_vendor_tools

# Tool category (the BUILDIUM_CATEGORIES name) -> the function that registers it.
CATEGORIES: dict[str, Callable[[FastMCP, BuildiumClient], None]] = {
    "associations": register_association_tools,
    "leases": register_lease_tools,
    "rentals": register_rental_tools,
    "applicants": register_applicant_tools,
    "tenants": register_tenant_tools,
    "owners": register_owner_tools,
    "units": register_unit_tools,
    "vendors": register_vendor_tools,
    "tasks": register_task_tools,
    "bills": register_bill_tools,
    "files": register_file_tools,
    "bank_accounts": register_bank_account_tools,
}


def create_server(
    config: BuildiumConfig | None = None, client: BuildiumClient | None = None
) -> FastMCP:
    """Build the MCP server with the tools of every enabled category.

    Args:
        config: Buildium configuration. If None, loads from environment.
        client: Buildium client. If None, one is built from ``config``.

    Returns:
        The configured FastMCP server.
    """
    config = config or BuildiumConfig.from_env()
    unknown = (config.get_enabled_categories() or set()) - CATEGORIES.keys()
    if unknown:
        raise ValueError(
            f"BUILDIUM_CATEGORIES has unknown categories {sorted(unknown)}; "
            f"known categories are {sorted(CATEGORIES)}"
        )
    client = client or BuildiumClient(config=config)
    mcp = FastMCP("buildium")
    for category, register in CATEGORIES.items():
        if config.is_category_enabled(category):
            register(mcp, client)
    return mcp


def main() -> None:
    """Run the MCP server (stdio by default)."""
    create_server().run()


if __name__ == "__main__":
    main()
