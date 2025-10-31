"""Integration tests for Buildium API (require real credentials)."""

import os

import pytest
import pytest_asyncio

from mcp_server_buildium.buildium_client import BuildiumClient
from mcp_server_buildium.config import BuildiumConfig

# Skip all tests in this module unless credentials are available
INTEGRATION_TESTS_ENABLED = bool(
    os.getenv("BUILDIUM_CLIENT_ID") and os.getenv("BUILDIUM_CLIENT_SECRET")
)

pytestmark = pytest.mark.skipif(
    not INTEGRATION_TESTS_ENABLED,
    reason="Integration tests require BUILDIUM_CLIENT_ID and BUILDIUM_CLIENT_SECRET",
)


@pytest_asyncio.fixture
async def buildium_client():
    """Create a Buildium client from environment variables."""
    config = BuildiumConfig.from_env()
    client = BuildiumClient(config=config)
    try:
        yield client
    finally:
        await client.close()


class TestBuildiumIntegration:
    """Integration tests that require real Buildium API credentials."""

    @pytest.mark.asyncio
    async def test_list_rentals(self, buildium_client):
        """Test listing rental properties using SDK."""
        result = await buildium_client.rentals_api.external_api_rentals_get_all_rentals(
            limit=1, offset=0
        )
        assert result is not None
        # Result may be empty if no rentals exist, but should not raise an error

    @pytest.mark.asyncio
    async def test_list_associations(self, buildium_client):
        """Test listing associations using SDK."""
        result = await buildium_client.associations_api.external_api_associations_get_associations(
            limit=1, offset=0
        )
        assert result is not None
        # Result may be empty if no associations exist, but should not raise an error

    @pytest.mark.asyncio
    async def test_list_leases(self, buildium_client):
        """Test listing leases using SDK."""
        result = await buildium_client.leases_api.external_api_leases_get_leases(limit=1, offset=0)
        assert result is not None
        # Result may be empty if no leases exist, but should not raise an error
