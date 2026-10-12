"""Helper module to import Buildium SDK."""

# Import SDK components (now a subpackage)
from mcp_server_buildium.buildium_sdk.api import (
    ApplicantsApi,
    AssociationOwnersApi,
    AssociationsApi,
    AssociationTenantsApi,
    AssociationUnitsApi,
    BankAccountsApi,
    BillsApi,
    BoardMembersApi,
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
from mcp_server_buildium.buildium_sdk.api_client import ApiClient
from mcp_server_buildium.buildium_sdk.configuration import Configuration

__all__ = [
    "ApiClient",
    "ApplicantsApi",
    "AssociationOwnersApi",
    "AssociationTenantsApi",
    "AssociationUnitsApi",
    "AssociationsApi",
    "BankAccountsApi",
    "BillsApi",
    "BoardMembersApi",
    "Configuration",
    "FilesApi",
    "LeaseTransactionsApi",
    "LeasesApi",
    "ListingsApi",
    "OwnershipAccountsApi",
    "RentalOwnersApi",
    "RentalPropertiesApi",
    "RentalTenantsApi",
    "RentalUnitsApi",
    "TasksApi",
    "VendorsApi",
]
