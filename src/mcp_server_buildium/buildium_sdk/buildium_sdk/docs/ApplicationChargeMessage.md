# ApplicationChargeMessage

This is an object that represents a charge tied to an application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Charge unique identifier. | [optional] 
**var_date** | **date** | Date of the charge. | [optional] 
**total_amount** | **float** | Sum of all &#x60;Lines.Amount&#x60; entries in the charge. | [optional] 
**memo** | **str** | Memo associated with the charge. | [optional] 
**lines** | [**List[ChargeLineMessage]**](ChargeLineMessage.md) | A collection of line items associated with the charge. | [optional] 

## Example

```python
from buildium_sdk.models.application_charge_message import ApplicationChargeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationChargeMessage from a JSON string
application_charge_message_instance = ApplicationChargeMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationChargeMessage.to_json())

# convert the object into a dict
application_charge_message_dict = application_charge_message_instance.to_dict()
# create an instance of ApplicationChargeMessage from a dict
application_charge_message_from_dict = ApplicationChargeMessage.from_dict(application_charge_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


