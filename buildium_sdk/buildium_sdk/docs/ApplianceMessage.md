# ApplianceMessage

Appliance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the appliance. | [optional] 
**name** | **str** | Name of the appliance. | [optional] 
**make** | **str** | Make of the appliance. | [optional] 
**model** | **str** | Model of the appliance. | [optional] 
**description** | **str** | Description of the appliance. | [optional] 

## Example

```python
from buildium_sdk.models.appliance_message import ApplianceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceMessage from a JSON string
appliance_message_instance = ApplianceMessage.from_json(json)
# print the JSON string representation of the object
print(ApplianceMessage.to_json())

# convert the object into a dict
appliance_message_dict = appliance_message_instance.to_dict()
# create an instance of ApplianceMessage from a dict
appliance_message_from_dict = ApplianceMessage.from_dict(appliance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


