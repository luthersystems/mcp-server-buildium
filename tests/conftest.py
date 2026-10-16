"""Shared fixtures for the offline unit tests."""

from collections.abc import AsyncIterator, Callable

import httpx
import pytest
import pytest_asyncio

from mcp_server_buildium.buildium_client import BuildiumClient
from mcp_server_buildium.config import BuildiumConfig

TEST_SECRET = "test-secret-value-1234"  # noqa: S105 -- a fake credential for offline tests


@pytest.fixture
def config(monkeypatch: pytest.MonkeyPatch) -> BuildiumConfig:
    """A configuration that never reads the developer's environment or .env file."""
    for name in ("BUILDIUM_BASE_URL", "BUILDIUM_CATEGORIES"):
        monkeypatch.delenv(name, raising=False)
    return BuildiumConfig(
        _env_file=None,
        client_id="test-client-id",
        client_secret=TEST_SECRET,
    )


class Recorder:
    """Records the requests the SDK sends and answers each with a canned body."""

    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []
        self.respond: Callable[[httpx.Request], httpx.Response] = lambda _req: httpx.Response(
            200, json=[]
        )

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.respond(request)


@pytest_asyncio.fixture
async def recorded_client(config: BuildiumConfig) -> AsyncIterator[tuple[BuildiumClient, Recorder]]:
    """A Buildium client whose HTTP traffic goes to a recorder instead of the network."""
    recorder = Recorder()
    client = BuildiumClient(config=config)
    rest = client._api_client.rest_client
    rest.pool_manager = httpx.AsyncClient(transport=httpx.MockTransport(recorder))
    try:
        yield client, recorder
    finally:
        await client.close()
