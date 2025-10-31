"""Helper module to import Buildium SDK."""

import sys
from pathlib import Path

# Add SDK to path if not installed as package
_sdk_path = Path(__file__).parent.parent.parent / "buildium_sdk"
if str(_sdk_path) not in sys.path:
    sys.path.insert(0, str(_sdk_path))

# Import SDK components
from buildium_sdk.api import (  # noqa: E402
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
from buildium_sdk.api_client import ApiClient  # noqa: E402
from buildium_sdk.configuration import Configuration  # noqa: E402

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
