# LeaseChargeLineSaveMessage

This is an object that represents a line item on a lease charge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. | 
**reference_number** | **str** | Reference number for the line item. The value cannot exceed 30 characters. | [optional] 

## Example

```python
from buildium_sdk.models.lease_charge_line_save_message import LeaseChargeLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseChargeLineSaveMessage from a JSON string
lease_charge_line_save_message_instance = LeaseChargeLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseChargeLineSaveMessage.to_json())

# convert the object into a dict
lease_charge_line_save_message_dict = lease_charge_line_save_message_instance.to_dict()
# create an instance of LeaseChargeLineSaveMessage from a dict
lease_charge_line_save_message_from_dict = LeaseChargeLineSaveMessage.from_dict(lease_charge_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


