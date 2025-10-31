"""Unit tests for BuildiumClient."""

import time
from unittest.mock import Mock, patch

import httpx
import pytest

from mcp_server_buildium.buildium_client import BuildiumClient
from mcp_server_buildium.config import BuildiumConfig


class TestBuildiumClient:
    """Test cases for BuildiumClient."""

    def test_init_with_config(self):
        """Test client initialization with config."""
        config = BuildiumConfig(
            base_url="https://api.buildium.com/",
            client_id="test-client",
            client_secret="test-secret",
        )
        with patch("httpx.post") as mock_post:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "access_token": "test-token",
                "expires_in": 3600,
            }
            mock_response.raise_for_status = Mock()
            mock_post.return_value = mock_response

            client = BuildiumClient(config=config)
            assert client.config.client_id == "test-client"
            assert client.config.client_secret == "test-secret"
            # Verify SDK API clients are initialized
            assert client.associations_api is not None
            assert client.leases_api is not None
            assert client.rentals_api is not None

    def test_init_from_env(self):
        """Test client initialization from environment."""
        with patch.dict(
            "os.environ",
            {
                "BUILDIUM_BASE_URL": "https://api.buildium.com/",
                "BUILDIUM_CLIENT_ID": "env-client",
                "BUILDIUM_CLIENT_SECRET": "env-secret",
            },
        ):
            with patch("httpx.post") as mock_post:
                mock_response = Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = {
                    "access_token": "test-token",
                    "expires_in": 3600,
                }
                mock_response.raise_for_status = Mock()
                mock_post.return_value = mock_response

                client = BuildiumClient()
                assert client.config.client_id == "env-client"

    @patch("httpx.post")
    def test_get_access_token_success(self, mock_post):
        """Test successful token acquisition."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "test-token-123",
            "expires_in": 3600,
            "token_type": "Bearer",
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        config = BuildiumConfig(
            base_url="https://api.buildium.com/",
            client_id="test-client",
            client_secret="test-secret",
            token_url="https://api.buildium.com/identity/connect/token",
        )
        client = BuildiumClient(config=config)

        token = client._get_access_token()
        assert token == "test-token-123"
        assert client._access_token == "test-token-123"

        # Verify token request
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[1]["data"]["grant_type"] == "client_credentials"
        assert call_args[1]["data"]["client_id"] == "test-client"

    @patch("httpx.post")
    def test_get_access_token_cached(self, mock_post):
        """Test token caching."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "test-token-123",
            "expires_in": 3600,
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        config = BuildiumConfig(
            base_url="https://api.buildium.com/",
            client_id="test-client",
            client_secret="test-secret",
            token_cache_enabled=True,
        )
        client = BuildiumClient(config=config)

        # First call
        token1 = client._get_access_token()
        assert mock_post.call_count == 1

        # Second call should use cache
        token2 = client._get_access_token()
        assert mock_post.call_count == 1  # No new request
        assert token1 == token2

    @patch("httpx.post")
    def test_get_access_token_expired(self, mock_post):
        """Test token refresh when expired."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "test-token-123",
            "expires_in": 1,  # Expires in 1 second
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        config = BuildiumConfig(
            base_url="https://api.buildium.com/",
            client_id="test-client",
            client_secret="test-secret",
            token_cache_enabled=True,
        )
        client = BuildiumClient(config=config)

        # Initial call happens during __init__, so count is already 1
        assert mock_post.call_count == 1

        # Wait for expiry (with buffer, so 2 seconds)
        time.sleep(2)

        # Second call should get new token
        client._get_access_token()
        assert mock_post.call_count == 2

    @patch("httpx.post")
    def test_get_access_token_failure(self, mock_post):
        """Test token acquisition failure."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "401 Unauthorized", request=Mock(), response=mock_response
        )
        mock_post.return_value = mock_response

        config = BuildiumConfig(
            base_url="https://api.buildium.com/",
            client_id="test-client",
            client_secret="test-secret",
        )

        with pytest.raises(httpx.HTTPStatusError):
            BuildiumClient(config=config)

    @patch("httpx.post")
    def test_refresh_token_if_needed(self, mock_post):
        """Test token refresh mechanism."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "test-token-123",
            "expires_in": 3600,
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        config = BuildiumConfig(
            base_url="https://api.buildium.com/",
            client_id="test-client",
            client_secret="test-secret",
        )
        client = BuildiumClient(config=config)

        # Token should already be set
        initial_token = client._access_token
        assert initial_token == "test-token-123"

        # refresh_token_if_needed should not trigger new request if token is valid
        client.refresh_token_if_needed()
        assert mock_post.call_count == 1  # Still only the initial call

        # Verify SDK config has the token
        assert client._sdk_config.access_token == "test-token-123"
