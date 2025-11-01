# FileSharingMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**FileSharingAccountMessage**](FileSharingAccountMessage.md) | Account file sharing settings. | [optional] 
**rental** | [**FileSharingRentalMessage**](FileSharingRentalMessage.md) | Rental file sharing settings. | [optional] 
**rental_unit** | [**FileSharingRentalUnitMesage**](FileSharingRentalUnitMesage.md) | Rental unit file sharing settings. | [optional] 
**lease** | [**FileSharingLeaseMessage**](FileSharingLeaseMessage.md) | Lease file sharing settings. | [optional] 
**tenant** | [**FileSharingTenantMessage**](FileSharingTenantMessage.md) | Tenant file sharing settings. | [optional] 
**rental_owner** | [**FileSharingRentalOwnerMessage**](FileSharingRentalOwnerMessage.md) | Rental owner file sharing settings. | [optional] 
**association** | [**FileSharingAssociationMessage**](FileSharingAssociationMessage.md) | Association file sharing settings. | [optional] 
**association_unit** | [**FileSharingAssociationUnitMessage**](FileSharingAssociationUnitMessage.md) | Association unit file sharing settings. | [optional] 
**ownership_account** | [**FileSharingOwnershipAccountMessage**](FileSharingOwnershipAccountMessage.md) | Ownership account file sharing settings. | [optional] 
**association_owner** | [**FileSharingAssociationOwnerMessage**](FileSharingAssociationOwnerMessage.md) | Association owner file sharing settings. | [optional] 
**vendor** | [**FileSharingVendorMessage**](FileSharingVendorMessage.md) | Vendor file sharing settings. | [optional] 
**committee** | [**FileSharingCommitteeMessage**](FileSharingCommitteeMessage.md) | Committee file sharing settings. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_message import FileSharingMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingMessage from a JSON string
file_sharing_message_instance = FileSharingMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingMessage.to_json())

# convert the object into a dict
file_sharing_message_dict = file_sharing_message_instance.to_dict()
# create an instance of FileSharingMessage from a dict
file_sharing_message_from_dict = FileSharingMessage.from_dict(file_sharing_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


