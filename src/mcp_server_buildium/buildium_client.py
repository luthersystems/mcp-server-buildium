"""Buildium API client using the generated SDK."""

import logging
from types import TracebackType

from .config import BuildiumConfig
from .sdk_imports import (
    ApiClient,
    ApplicantsApi,
    AssociationOwnersApi,
    AssociationsApi,
    AssociationTenantsApi,
    AssociationUnitsApi,
    BankAccountsApi,
    BillsApi,
    BoardMembersApi,
    Configuration,
    FilesApi,
    LeasesApi,
    LeaseTransactionsApi,
    ListingsApi,
    OwnershipAccountsApi,
    RentalOwnersApi,
    RentalPropertiesApi,
    RentalTenantsApi,
    RentalUnitsApi,
    TasksApi,
    VendorsApi,
)

logger = logging.getLogger(__name__)


class BuildiumClient:
    """Buildium API client using the generated SDK with API key headers authentication."""

    def __init__(self, config: BuildiumConfig | None = None):
        """Initialize the Buildium client.

        Args:
            config: Buildium configuration. If None, loads from environment.
        """
        self.config = config or BuildiumConfig.from_env()
        self._sdk_config = self._build_sdk_config()
        self._api_client = ApiClient(self._sdk_config)
        # Buildium authenticates with API key headers, not OAuth.
        self._api_client.set_default_header("x-buildium-client-id", self.config.client_id)
        self._api_client.set_default_header(
            "x-buildium-client-secret", self.config.client_secret.get_secret_value()
        )
        # Never log the default headers: they hold the client secret.
        logger.debug("Initialized Buildium client for %s", self._sdk_config.host)

        # Initialize API clients
        self.associations_api = AssociationsApi(self._api_client)
        self.leases_api = LeasesApi(self._api_client)
        self.lease_transactions_api = LeaseTransactionsApi(self._api_client)
        self.listings_api = ListingsApi(self._api_client)
        self.board_members_api = BoardMembersApi(self._api_client)
        self.ownership_accounts_api = OwnershipAccountsApi(self._api_client)
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

    def _build_sdk_config(self) -> Configuration:
        """Build the SDK configuration.

        The SDK's generated paths already include /v1, so the host must not.
        """
        base_url = self.config.base_url.rstrip("/")
        base_url = base_url.removesuffix("/v1")
        return Configuration(host=base_url)

    async def close(self) -> None:
        """Close the API client."""
        if self._api_client:
            await self._api_client.close()

    async def __aenter__(self) -> "BuildiumClient":
        """Async context manager entry."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Async context manager exit: close the HTTP client."""
        await self.close()
