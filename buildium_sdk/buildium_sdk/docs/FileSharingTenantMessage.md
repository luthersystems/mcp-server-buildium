# FileSharingTenantMessage

The file share settings for the tenant file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | **bool** | Indicates whether file is shared with tenants on the lease. | [optional] 
**rental_owners** | **bool** | Indicates whether file is shared with rental owners of the property. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_tenant_message import FileSharingTenantMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingTenantMessage from a JSON string
file_sharing_tenant_message_instance = FileSharingTenantMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingTenantMessage.to_json())

# convert the object into a dict
file_sharing_tenant_message_dict = file_sharing_tenant_message_instance.to_dict()
# create an instance of FileSharingTenantMessage from a dict
file_sharing_tenant_message_from_dict = FileSharingTenantMessage.from_dict(file_sharing_tenant_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


