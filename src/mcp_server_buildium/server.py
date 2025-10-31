"""Main MCP server entry point for Buildium."""

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

# Create FastMCP server
mcp = FastMCP("buildium")

# Initialize Buildium client and config
config = BuildiumConfig.from_env()
buildium_client = BuildiumClient(config=config)

# Register tools based on enabled categories
if config.is_category_enabled("associations"):
    register_association_tools(mcp, buildium_client)
if config.is_category_enabled("leases"):
    register_lease_tools(mcp, buildium_client)
if config.is_category_enabled("rentals"):
    register_rental_tools(mcp, buildium_client)
if config.is_category_enabled("applicants"):
    register_applicant_tools(mcp, buildium_client)
if config.is_category_enabled("tenants"):
    register_tenant_tools(mcp, buildium_client)
if config.is_category_enabled("owners"):
    register_owner_tools(mcp, buildium_client)
if config.is_category_enabled("units"):
    register_unit_tools(mcp, buildium_client)
if config.is_category_enabled("vendors"):
    register_vendor_tools(mcp, buildium_client)
if config.is_category_enabled("tasks"):
    register_task_tools(mcp, buildium_client)
if config.is_category_enabled("bills"):
    register_bill_tools(mcp, buildium_client)
if config.is_category_enabled("files"):
    register_file_tools(mcp, buildium_client)
if config.is_category_enabled("bank_accounts"):
    register_bank_account_tools(mcp, buildium_client)


def main() -> None:
    """Run the MCP server (stdio by default)."""
    mcp.run()


if __name__ == "__main__":
    main()
