"""Configuration management for Buildium MCP Server."""

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

# Load .env file if it exists
load_dotenv()


class BuildiumConfig(BaseSettings):
    """Buildium API key configuration (API key headers, not OAuth)."""

    base_url: str = Field(
        default="https://api.buildium.com",
        description="Buildium API base URL without /v1 (prod: https://api.buildium.com, sandbox: https://apisandbox.buildium.com). The SDK adds /v1 to paths automatically.",
    )
    client_id: str = Field(
        ..., description="Buildium API client ID (used as x-buildium-client-id header)"
    )
    client_secret: str = Field(
        ..., description="Buildium API client secret (used as x-buildium-client-secret header)"
    )
    categories: str | None = Field(
        default=None,
        description="Comma-separated list of tool categories to enable (e.g., 'associations,leases,rentals'). If not specified, all categories are enabled.",
    )

    model_config = {
        "env_prefix": "BUILDIUM_",
        "case_sensitive": False,
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",  # Ignore extra fields like old BUILDIUM_SCOPE, BUILDIUM_TOKEN_CACHE_ENABLED
    }

    @classmethod
    def from_env(cls) -> "BuildiumConfig":
        """Load configuration from environment variables."""
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
