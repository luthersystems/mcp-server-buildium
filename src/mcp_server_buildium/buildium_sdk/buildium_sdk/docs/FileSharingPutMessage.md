# FileSharingPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**FileSharingAccountPutMessage**](FileSharingAccountPutMessage.md) | Account file sharing settings. Note, can only update this property if the file is an account&#39;s file. | [optional] 
**rental** | [**FileSharingRentalPutMessage**](FileSharingRentalPutMessage.md) | Rental file sharing settings. Note, can only update this property if the file is a rental&#39;s file. | [optional] 
**rental_unit** | [**FileSharingRentalUnitPutMesage**](FileSharingRentalUnitPutMesage.md) | Rental unit file sharing settings. Note, can only update this property if the file is a rental unit&#39;s file. | [optional] 
**lease** | [**FileSharingLeasePutMessage**](FileSharingLeasePutMessage.md) | Lease file sharing settings. Note, can only update this property if the file is a lease&#39;s file. | [optional] 
**tenant** | [**FileSharingTenantPutMessage**](FileSharingTenantPutMessage.md) | Tenant file sharing settings. Note, can only update this property if the file is a tenant&#39;s file. | [optional] 
**rental_owner** | [**FileSharingRentalOwnerPutMessage**](FileSharingRentalOwnerPutMessage.md) | Rental owner file sharing settings. Note, can only update this property if the file is a rental owner&#39;s file. | [optional] 
**association** | [**FileSharingAssociationPutMessage**](FileSharingAssociationPutMessage.md) | Association file sharing settings. Note, can only update this property if the file is an association&#39;s file. | [optional] 
**association_unit** | [**FileSharingAssociationUnitPutMessage**](FileSharingAssociationUnitPutMessage.md) | Association unit file sharing settings. Note, can only update this property if the file is an association unit&#39;s file. | [optional] 
**ownership_account** | [**FileSharingOwnershipAccountPutMessage**](FileSharingOwnershipAccountPutMessage.md) | Ownership account file sharing settings. Note, can only update this property if the file is an ownership account&#39;s file. | [optional] 
**association_owner** | [**FileSharingAssociationOwnerPutMessage**](FileSharingAssociationOwnerPutMessage.md) | Association owner file sharing settings. Note, can only update this property if the file is an association owner&#39;s file. | [optional] 
**vendor** | [**FileSharingVendorPutMessage**](FileSharingVendorPutMessage.md) | Vendor file sharing settings. Note, can only update this property if the file is a vendor&#39;s file. | [optional] 
**committee** | [**FileSharingCommitteePutMessage**](FileSharingCommitteePutMessage.md) | Committee file sharing settings. Note, can only update this property if the file is a committee&#39;s file. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_put_message import FileSharingPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingPutMessage from a JSON string
file_sharing_put_message_instance = FileSharingPutMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingPutMessage.to_json())

# convert the object into a dict
file_sharing_put_message_dict = file_sharing_put_message_instance.to_dict()
# create an instance of FileSharingPutMessage from a dict
file_sharing_put_message_from_dict = FileSharingPutMessage.from_dict(file_sharing_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


