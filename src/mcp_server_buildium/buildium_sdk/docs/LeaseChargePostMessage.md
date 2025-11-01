# LeaseChargePostMessage

This is an object that represents a charge related to a lease

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the charge. The date must be formatted as YYYY-MM-DD. | [optional] 
**memo** | **str** | Memo associated with the charge. The value cannot exceed 65 characters. | [optional] 
**bill_id** | **int** | Unique identifier of the bill this charge is associated to. If provided, the property of the lease the  charge is being created in must be in at least one line item of the bill. | [optional] 
**lines** | [**List[LeaseChargeLineSaveMessage]**](LeaseChargeLineSaveMessage.md) | A collection of line items included in the charge. At least one line item is required. | [optional] 

## Example

```python
from buildium_sdk.models.lease_charge_post_message import LeaseChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseChargePostMessage from a JSON string
lease_charge_post_message_instance = LeaseChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseChargePostMessage.to_json())

# convert the object into a dict
lease_charge_post_message_dict = lease_charge_post_message_instance.to_dict()
# create an instance of LeaseChargePostMessage from a dict
lease_charge_post_message_from_dict = LeaseChargePostMessage.from_dict(lease_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


