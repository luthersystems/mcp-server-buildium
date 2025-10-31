# Buildium MCP Server

**Experimental** Model Context Protocol (MCP) server for Buildium Property Management API, built with Python + FastMCP. Uses API key authentication for server-to-server communication.

## ⚠️ Status & Disclaimers

* **Experimental**: Not production-ready; no SLA; APIs and behavior may change.
* **No affiliation with Buildium**: This is a community integration. Buildium is a trademark of Buildium, LLC.
* **Security**: Do **not** commit secrets. Treat client IDs and secrets as sensitive; use a secrets manager. **Use at your own risk.**

## Features

* 🔐 **API Key Authentication** - Secure server-to-server authentication via headers
* 🏘️ **81 Tools Across 12 Categories** - Comprehensive property management coverage
* 📋 **Selective Tool Loading** - Enable only the categories you need
* 🏢 **Multi-Property Types** - Rentals, associations, and units
* 🔌 **MCP Protocol** - Compatible with Claude Desktop, Cursor, and other MCP clients

## Requirements

* Python 3.11+
* `uv` package manager (or `pip`)
* Buildium API credentials (client ID and client secret)

## Installation

### Using `uv` (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the package
uv pip install -e "git+https://github.com/luthersystems/mcp-server-buildium.git"
```

### Using `pip`

```bash
pip install git+https://github.com/luthersystems/mcp-server-buildium.git
```

## Configuration

Configure the server using environment variables:

```bash
# API Base URL (no /v1 suffix - SDK adds it automatically)
BUILDIUM_BASE_URL=https://api.buildium.com  # Production
# BUILDIUM_BASE_URL=https://apisandbox.buildium.com  # Sandbox

# API Key Credentials
BUILDIUM_CLIENT_ID=your-client-id
BUILDIUM_CLIENT_SECRET=your-client-secret

# Optional: Selective Tool Categories (comma-separated)
# If not specified, all categories are enabled
BUILDIUM_CATEGORIES=associations,leases,rentals
```

### Tool Categories

Control which tool categories are enabled using the `BUILDIUM_CATEGORIES` environment variable:

| Category | Tools | Description |
|----------|-------|-------------|
| `associations` | 6 | Homeowner association management |
| `leases` | 5 | Lease agreements and transactions |
| `rentals` | 5 | Rental properties and listings |
| `applicants` | 10 | Rental applicants and applications |
| `tenants` | 7 | Tenant management (rental & association) |
| `owners` | 8 | Property owner management |
| `units` | 7 | Individual unit management |
| `vendors` | 7 | Vendor and service provider management |
| `tasks` | 5 | Task and to-do management |
| `bills` | 7 | Bill and payment management |
| `files` | 8 | Document and file management |
| `bank_accounts` | 6 | Bank account and transaction management |

**Total: 81 tools**

If `BUILDIUM_CATEGORIES` is not set, all 81 tools across all 12 categories are enabled.

### Environment File

Create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
# Edit .env with your credentials
```

## Usage

### Running the Server

```bash
# With uv
uv run mcp-server-buildium

# Or with Python
python -m mcp_server_buildium.server
```

### Using with Claude Desktop

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "buildium": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/luthersystems/mcp-server-buildium",
        "mcp-server-buildium"
      ],
      "env": {
        "BUILDIUM_BASE_URL": "https://apisandbox.buildium.com/",
        "BUILDIUM_CLIENT_ID": "your-client-id",
        "BUILDIUM_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

## Available Tools (81 total)

### Associations (6 tools)
* `list_associations` - List all associations
* `get_association` - Get association details by ID
* `create_association` - Create a new association
* `update_association` - Update an existing association
* `list_association_board_members` - List board members for an association
* `list_association_ownership_accounts` - List ownership accounts for an association

### Leases (5 tools)
* `list_leases` - List leases with optional filters
* `get_lease` - Get lease details by ID
* `create_lease` - Create a new lease
* `update_lease` - Update an existing lease
* `list_lease_transactions` - List transactions for a lease

### Rentals (5 tools)
* `list_rentals` - List rental properties
* `get_rental` - Get rental property details by ID
* `create_rental` - Create a new rental property
* `update_rental` - Update an existing rental property
* `list_unit_listings` - List unit listings for rentals

### Applicants (10 tools)
* `list_applicants` - List rental applicants
* `get_applicant` - Get applicant details by ID
* `create_applicant` - Create a new applicant
* `update_applicant` - Update an existing applicant
* `list_applicant_applications` - List applications for an applicant
* `get_application` - Get application details by ID
* `update_application` - Update an application
* `list_applicant_groups` - List applicant groups
* `create_applicant_group` - Create a new applicant group
* `update_applicant_group` - Update an applicant group

### Tenants (7 tools)
* `list_rental_tenants` - List rental tenants
* `get_rental_tenant` - Get rental tenant details by ID
* `create_rental_tenant` - Create a new rental tenant
* `update_rental_tenant` - Update a rental tenant
* `list_association_tenants` - List association tenants
* `create_association_tenant` - Create a new association tenant
* `update_association_tenant` - Update an association tenant

### Owners (8 tools)
* `list_rental_owners` - List rental property owners
* `get_rental_owner` - Get rental owner details by ID
* `create_rental_owner` - Create a new rental owner
* `update_rental_owner` - Update a rental owner
* `list_association_owners` - List association owners
* `get_association_owner` - Get association owner details by ID
* `create_association_owner` - Create a new association owner
* `update_association_owner` - Update an association owner

### Units (7 tools)
* `list_rental_units` - List rental units
* `get_rental_unit` - Get rental unit details by ID
* `create_rental_unit` - Create a new rental unit
* `update_rental_unit` - Update a rental unit
* `list_association_units` - List association units
* `create_association_unit` - Create a new association unit
* `update_association_unit` - Update an association unit

### Vendors (7 tools)
* `list_vendors` - List vendors
* `get_vendor` - Get vendor details by ID
* `create_vendor` - Create a new vendor
* `update_vendor` - Update an existing vendor
* `list_vendor_categories` - List vendor categories
* `create_vendor_category` - Create a new vendor category
* `update_vendor_category` - Update a vendor category

### Tasks (5 tools)
* `list_tasks` - List tasks
* `get_task` - Get task details by ID
* `list_task_categories` - List task categories
* `create_task_category` - Create a new task category
* `update_task_category` - Update a task category

### Bills (7 tools)
* `list_bills` - List bills
* `get_bill` - Get bill details by ID
* `create_bill` - Create a new bill
* `update_bill` - Update an existing bill
* `list_bill_payments` - List payments for bills
* `get_bill_payment` - Get bill payment details by ID
* `create_bill_payment` - Create a new bill payment

### Files (8 tools)
* `list_files` - List files
* `get_file` - Get file details by ID
* `update_file` - Update file metadata
* `create_file_upload_request` - Create a file upload request
* `create_file_download_request` - Create a file download request
* `list_file_categories` - List file categories
* `create_file_category` - Create a new file category
* `update_file_category` - Update a file category

### Bank Accounts (6 tools)
* `list_bank_accounts` - List bank accounts
* `get_bank_account` - Get bank account details by ID
* `create_bank_account` - Create a new bank account
* `update_bank_account` - Update a bank account
* `list_bank_account_transactions` - List transactions for a bank account
* `get_bank_account_transaction` - Get bank account transaction details by ID

## Example Usage

### Example Prompts

> "List all rental properties in Buildium"

> "Show me lease #12345"

> "Create a new lease for property 100, unit 205"

> "List all associations"

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/luthersystems/mcp-server-buildium.git
cd mcp-server-buildium

# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv pip install -e ".[dev]"
```

### Running Tests

```bash
# Run unit tests (no credentials needed)
uv run pytest tests/ --ignore=tests/test_integration.py

# Run with coverage
uv run pytest --cov=mcp_server_buildium --cov-report=html

# Run linter
uv run ruff check .

# Format code
uv run ruff format .
```

### Integration Tests (Optional)

Integration tests validate real Buildium API authentication. They are **skipped by default** and only run when you provide real credentials.

**To enable integration tests:**

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Fill in your Buildium credentials in `.env`:
   ```bash
   BUILDIUM_BASE_URL=https://apisandbox.buildium.com/
   BUILDIUM_CLIENT_ID=your-client-id
   BUILDIUM_CLIENT_SECRET=your-client-secret
   ```

3. Run integration tests:
   ```bash
   uv run pytest tests/test_integration.py -v
   ```

**Test Credentials (Sandbox):**
- Client ID: `54f6ac5b-5629-4934-a930-d2c8174fcf4a`
- Client Secret: `tHXJx7mFoCEXtqCvBL3oV1Fv6hHb5WVokKHIvT1cUIA=`
- Base URL: `https://apisandbox.buildium.com/`

### CI/CD Setup (GitHub Actions)

To run integration tests in GitHub Actions:

1. **Add GitHub repository secrets:**
   * Go to your repo → **Settings** → **Secrets and variables** → **Actions**
   * Add the following secrets:
     * `BUILDIUM_BASE_URL`: `https://apisandbox.buildium.com/`
     * `BUILDIUM_CLIENT_ID`: Your client ID
     * `BUILDIUM_CLIENT_SECRET`: Your client secret

2. **The CI workflow will automatically run integration tests** when these secrets are present

**Note**: The integration tests will be skipped in PRs from forks (for security), but will run on pushes to main/develop branches.

**What the integration tests verify:**

* ✅ OAuth authentication works with your credentials
* ✅ Access token can be obtained successfully
* ✅ API calls work (tests `list_associations`, `list_rentals`, `list_leases`)
* ✅ Token refresh mechanism works

**Note**: Integration tests require a Buildium developer account (sandbox environment recommended).

## Generating SDK from OpenAPI Spec

If you want to generate a Python SDK from the Buildium OpenAPI spec:

```bash
# Generate SDK (requires Java for OpenAPI Generator)
make generate-sdk

# The generated SDK will be in buildium_sdk/ directory
```

See `Makefile` for more details.

## Project Structure

```
mcp-server-buildium/
├── src/mcp_server_buildium/
│   ├── __init__.py
│   ├── server.py           # Main FastMCP server
│   ├── config.py           # Configuration management
│   ├── buildium_client.py  # OAuth auth & API client
│   └── tools/
│       ├── associations.py # Association tools
│       ├── leases.py       # Lease tools
│       └── rentals.py      # Rental tools
├── tests/
│   ├── test_buildium_client.py
│   └── test_integration.py
├── pyproject.toml
└── README.md
```

## Troubleshooting

### "Failed to obtain access token"

* Verify client ID and secret are correct
* Check base URL is correct (sandbox vs production)
* Ensure token URL is accessible
* Verify scopes are correct

### "401 Unauthorized"

* Check credentials are valid
* Verify API endpoint URLs
* Ensure OAuth scopes include required permissions

### "Connection timeout"

* Check internet connectivity
* Verify firewall settings
* Try sandbox environment first

## API Endpoints

* **Production**: `https://api.buildium.com/`
* **Sandbox**: `https://apisandbox.buildium.com/`

## Security Best Practices

1. **Never commit credentials** - Use `.gitignore` and environment variables
2. **Use secrets management** - Store credentials in secure vaults (AWS Secrets Manager, etc.)
3. **Rotate credentials regularly** - Generate new client secrets periodically
4. **Limit token lifetime** - Use shorter expiration for sensitive operations
5. **Monitor API usage** - Check Buildium dashboard for unusual activity
6. **Use sandbox environment** - Test with sandbox accounts before production

## Architecture

* **Language**: Python 3.11+
* **Framework**: FastMCP
* **Auth**: OAuth 2.0 client credentials flow
* **Transport**: stdio (MCP protocol)
* **HTTP Client**: httpx
* **Testing**: pytest with mocks

## References

* [Buildium Developer Documentation](https://developer.buildium.com/)
* [Model Context Protocol](https://modelcontextprotocol.io)
* [FastMCP Framework](https://github.com/jlowin/fastmcp)
* [OAuth 2.0 Client Credentials Flow](https://oauth.net/2/grant-types/client-credentials/)

## License

MIT

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## Support

This is an experimental community project. For Buildium API issues, consult the [Buildium Developer Center](https://developer.buildium.com/).

