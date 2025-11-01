# RetailCashUnitMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unit unique identifier. | [optional] 
**unit_number** | **str** | Unit number. | [optional] 
**href** | **str** | A link to the resource endpoint associated with the unit. | [optional] 

## Example

```python
from buildium_sdk.models.retail_cash_unit_message import RetailCashUnitMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RetailCashUnitMessage from a JSON string
retail_cash_unit_message_instance = RetailCashUnitMessage.from_json(json)
# print the JSON string representation of the object
print(RetailCashUnitMessage.to_json())

# convert the object into a dict
retail_cash_unit_message_dict = retail_cash_unit_message_instance.to_dict()
# create an instance of RetailCashUnitMessage from a dict
retail_cash_unit_message_from_dict = RetailCashUnitMessage.from_dict(retail_cash_unit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


