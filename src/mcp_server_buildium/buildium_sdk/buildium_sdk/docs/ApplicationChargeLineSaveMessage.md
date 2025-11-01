# ApplicationChargeLineSaveMessage

This is an object that represents a line item on an application charge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. | 
**memo** | **str** | The general ledger account description under which the line item amount will be recorded. The value cannot exceed 245 characters | [optional] 
**reference_number** | **str** | Reference number for the line item. The value cannot exceed 30 characters. | [optional] 

## Example

```python
from buildium_sdk.models.application_charge_line_save_message import ApplicationChargeLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationChargeLineSaveMessage from a JSON string
application_charge_line_save_message_instance = ApplicationChargeLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationChargeLineSaveMessage.to_json())

# convert the object into a dict
application_charge_line_save_message_dict = application_charge_line_save_message_instance.to_dict()
# create an instance of ApplicationChargeLineSaveMessage from a dict
application_charge_line_save_message_from_dict = ApplicationChargeLineSaveMessage.from_dict(application_charge_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


