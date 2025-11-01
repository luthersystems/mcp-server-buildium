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
    FilesApi,
    LeasesApi,
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
    "Configuration",
    "AssociationsApi",
    "LeasesApi",
    "RentalPropertiesApi",
    "ApplicantsApi",
    "RentalTenantsApi",
    "AssociationTenantsApi",
    "RentalOwnersApi",
    "AssociationOwnersApi",
    "RentalUnitsApi",
    "AssociationUnitsApi",
    "VendorsApi",
    "TasksApi",
    "BillsApi",
    "FilesApi",
    "BankAccountsApi",
]
