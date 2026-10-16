"""Tests for the Buildium client wrapper."""

import logging

import pytest

from mcp_server_buildium.buildium_client import BuildiumClient
from mcp_server_buildium.config import BuildiumConfig

from .conftest import TEST_SECRET, Recorder


@pytest.mark.parametrize(
    ("base_url", "host"),
    [
        ("https://api.buildium.com", "https://api.buildium.com"),
        ("https://apisandbox.buildium.com/", "https://apisandbox.buildium.com"),
        ("https://api.buildium.com/v1", "https://api.buildium.com"),
        ("https://api.buildium.com/v1/", "https://api.buildium.com"),
    ],
)
def test_host_has_no_v1(config: BuildiumConfig, base_url: str, host: str) -> None:
    client = BuildiumClient(config=config.model_copy(update={"base_url": base_url}))
    assert client._sdk_config.host == host


def test_secret_is_never_logged(config: BuildiumConfig, caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.DEBUG):
        BuildiumClient(config=config)
    assert TEST_SECRET not in caplog.text


@pytest.mark.asyncio
async def test_requests_carry_the_api_key_headers(
    recorded_client: tuple[BuildiumClient, Recorder],
) -> None:
    client, recorder = recorded_client
    await client.rentals_api.external_api_rentals_get_all_rentals(limit=1, offset=0)
    (request,) = recorder.requests
    assert request.url.scheme == "https"
    assert request.url.path == "/v1/rentals"
    assert request.headers["x-buildium-client-id"] == "test-client-id"
    assert request.headers["x-buildium-client-secret"] == TEST_SECRET


@pytest.mark.asyncio
async def test_async_context_manager_closes(config: BuildiumConfig) -> None:
    async with BuildiumClient(config=config) as client:
        assert client.config is config
