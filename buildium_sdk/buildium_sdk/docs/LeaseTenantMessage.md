# LeaseTenantMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Tenant unique identifier. | [optional] 
**status** | **str** | Indicates the tenant&#39;s current status in relation to the lease. | [optional] 
**move_in_date** | **date** | Indicates the tenant&#39;s move-in date. | [optional] 

## Example

```python
from buildium_sdk.models.lease_tenant_message import LeaseTenantMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseTenantMessage from a JSON string
lease_tenant_message_instance = LeaseTenantMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseTenantMessage.to_json())

# convert the object into a dict
lease_tenant_message_dict = lease_tenant_message_instance.to_dict()
# create an instance of LeaseTenantMessage from a dict
lease_tenant_message_from_dict = LeaseTenantMessage.from_dict(lease_tenant_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


