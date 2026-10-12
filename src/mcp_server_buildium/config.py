"""Configuration management for Buildium MCP Server."""

from urllib.parse import urlsplit

from dotenv import load_dotenv
from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_BASE_URL = "https://api.buildium.com"

# Load a .env file into the environment if one exists (found by walking up from
# this package, then the working directory). Variables already set win.
load_dotenv()


class BuildiumConfig(BaseSettings):
    """Buildium API key configuration (API key headers, not OAuth)."""

    model_config = SettingsConfigDict(
        env_prefix="BUILDIUM_",
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
        # Ignore extra fields like the old BUILDIUM_SCOPE and BUILDIUM_TOKEN_URL.
        extra="ignore",
    )

    base_url: str = Field(
        default=DEFAULT_BASE_URL,
        description=(
            "Buildium API base URL without /v1 (prod: https://api.buildium.com, "
            "sandbox: https://apisandbox.buildium.com). The SDK adds /v1 to paths. "
            "Must use https, because every request carries the client secret."
        ),
    )
    client_id: str = Field(
        ..., min_length=1, description="Buildium API client ID (x-buildium-client-id header)"
    )
    client_secret: SecretStr = Field(
        ..., description="Buildium API client secret (x-buildium-client-secret header)"
    )
    categories: str | None = Field(
        default=None,
        description=(
            "Comma-separated list of tool categories to enable "
            "(e.g., 'associations,leases,rentals'). If not set, all categories are enabled."
        ),
    )

    @field_validator("base_url", mode="before")
    @classmethod
    def _default_empty_base_url(cls, value: object) -> object:
        # Deployments that template the variable (connectorhub) set it to ""
        # when no URL is configured; treat that as unset.
        if isinstance(value, str) and not value.strip():
            return DEFAULT_BASE_URL
        return value

    @field_validator("base_url")
    @classmethod
    def _require_https(cls, value: str) -> str:
        value = value.strip()
        parts = urlsplit(value)
        if parts.scheme != "https" or not parts.hostname:
            raise ValueError("base_url must be an https:// URL with a host")
        if parts.username or parts.password or parts.query or parts.fragment:
            raise ValueError("base_url must not contain credentials, a query or a fragment")
        return value

    @field_validator("client_secret")
    @classmethod
    def _require_secret(cls, value: SecretStr) -> SecretStr:
        if not value.get_secret_value():
            raise ValueError("client_secret must not be empty")
        return value

    @classmethod
    def from_env(cls) -> "BuildiumConfig":
        """Load configuration from environment variables (and a .env file, if present)."""
        return cls()

    def get_enabled_categories(self) -> set[str] | None:
        """Get enabled categories as a set.

        Returns:
            Set of category names if categories are specified, None if all should be enabled.
        """
        if not self.categories:
            return None  # None means all categories enabled
        return {cat.strip().lower() for cat in self.categories.split(",") if cat.strip()}

    def is_category_enabled(self, category: str) -> bool:
        """Check if a category is enabled.

        Args:
            category: Category name to check.

        Returns:
            True if category is enabled, False otherwise.
        """
        enabled = self.get_enabled_categories()
        if enabled is None:
            return True  # All categories enabled
        return category.lower() in enabled
