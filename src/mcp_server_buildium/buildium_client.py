"""Buildium API client using the generated SDK."""

from .config import BuildiumConfig
from .sdk_imports import (  # noqa: E402
    ApiClient,
    ApplicantsApi,
    AssociationOwnersApi,
    AssociationsApi,
    AssociationTenantsApi,
    AssociationUnitsApi,
    BankAccountsApi,
    BillsApi,
    Configuration,
    FilesApi,
    LeasesApi,
    RentalOwnersApi,
    RentalPropertiesApi,
    RentalTenantsApi,
    RentalUnitsApi,
    TasksApi,
    VendorsApi,
)


class BuildiumClient:
    """Buildium API client using the generated SDK with API key headers authentication."""

    def __init__(self, config: BuildiumConfig | None = None):
        """Initialize the Buildium client.

        Args:
            config: Buildium configuration. If None, loads from environment.
        """
        self.config = config or BuildiumConfig.from_env()
        self._sdk_config: Configuration | None = None
        self._api_client: ApiClient | None = None

        # Initialize SDK configuration and API client
        self._initialize_sdk()

        # Initialize API clients
        self.associations_api = AssociationsApi(self._api_client)
        self.leases_api = LeasesApi(self._api_client)
        self.rentals_api = RentalPropertiesApi(self._api_client)
        self.applicants_api = ApplicantsApi(self._api_client)
        self.rental_tenants_api = RentalTenantsApi(self._api_client)
        self.association_tenants_api = AssociationTenantsApi(self._api_client)
        self.rental_owners_api = RentalOwnersApi(self._api_client)
        self.association_owners_api = AssociationOwnersApi(self._api_client)
        self.rental_units_api = RentalUnitsApi(self._api_client)
        self.association_units_api = AssociationUnitsApi(self._api_client)
        self.vendors_api = VendorsApi(self._api_client)
        self.tasks_api = TasksApi(self._api_client)
        self.bills_api = BillsApi(self._api_client)
        self.files_api = FilesApi(self._api_client)
        self.bank_accounts_api = BankAccountsApi(self._api_client)

    def _initialize_sdk(self) -> None:
        """Initialize the SDK configuration and API client with API key headers."""
        # The SDK's generated paths already include /v1, so base_url should NOT include /v1
        # e.g., base_url should be https://apisandbox.buildium.com (not .../v1)
        base_url = self.config.base_url.rstrip("/")
        # Remove /v1 if it's in the base_url (the SDK paths already include it)
        if base_url.endswith("/v1"):
            base_url = base_url[:-3]  # Remove /v1

        self._sdk_config = Configuration(host=base_url)
        self._api_client = ApiClient(self._sdk_config)
        # Set API key headers as default headers (Buildium uses headers, not OAuth)
        self._api_client.set_default_header("x-buildium-client-id", self.config.client_id)
        self._api_client.set_default_header("x-buildium-client-secret", self.config.client_secret)

        # Log initialization details
        import logging
        logger = logging.getLogger(__name__)
        logger.debug("Initialized Buildium client:")
        logger.debug("  Base URL: %s", base_url)
        logger.debug("  Default headers: %s", self._api_client.default_headers)

    async def close(self) -> None:
        """Close the API client."""
        if self._api_client:
            await self._api_client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
