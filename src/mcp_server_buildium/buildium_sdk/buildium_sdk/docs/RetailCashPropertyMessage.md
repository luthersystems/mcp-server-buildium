# RetailCashPropertyMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The property unique identifier. | [optional] 
**name** | **str** | The property name. | [optional] 
**type** | **str** | The property type. | [optional] 
**href** | **str** | A link to the property entity resource. | [optional] 

## Example

```python
from buildium_sdk.models.retail_cash_property_message import RetailCashPropertyMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RetailCashPropertyMessage from a JSON string
retail_cash_property_message_instance = RetailCashPropertyMessage.from_json(json)
# print the JSON string representation of the object
print(RetailCashPropertyMessage.to_json())

# convert the object into a dict
retail_cash_property_message_dict = retail_cash_property_message_instance.to_dict()
# create an instance of RetailCashPropertyMessage from a dict
retail_cash_property_message_from_dict = RetailCashPropertyMessage.from_dict(retail_cash_property_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


