# InsuredTenantMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Tenant unique identifier. | [optional] 
**first_name** | **str** | First name of the tenant. | [optional] 
**last_name** | **str** | Last name of the tenant. | [optional] 
**is_primary_insured** | **bool** | Indicates whether this tenant is the primary insured person on the policy. This only applies to policies with a &#x60;CarrierType&#x60; of &#x60;MSI&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.insured_tenant_message import InsuredTenantMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InsuredTenantMessage from a JSON string
insured_tenant_message_instance = InsuredTenantMessage.from_json(json)
# print the JSON string representation of the object
print(InsuredTenantMessage.to_json())

# convert the object into a dict
insured_tenant_message_dict = insured_tenant_message_instance.to_dict()
# create an instance of InsuredTenantMessage from a dict
insured_tenant_message_from_dict = InsuredTenantMessage.from_dict(insured_tenant_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


