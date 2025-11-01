# ApplicationChargePostMessage

This is an object that represents a charge related to an application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the charge. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | Memo associated with the charge. The value cannot exceed 65 characters. | [optional] 
**lines** | [**List[ApplicationChargeLineSaveMessage]**](ApplicationChargeLineSaveMessage.md) | A collection of line items included in the charge. At least one line item is required. | [optional] 

## Example

```python
from buildium_sdk.models.application_charge_post_message import ApplicationChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationChargePostMessage from a JSON string
application_charge_post_message_instance = ApplicationChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationChargePostMessage.to_json())

# convert the object into a dict
application_charge_post_message_dict = application_charge_post_message_instance.to_dict()
# create an instance of ApplicationChargePostMessage from a dict
application_charge_post_message_from_dict = ApplicationChargePostMessage.from_dict(application_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


