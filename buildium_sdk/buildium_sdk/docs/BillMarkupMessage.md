# BillMarkupMessage

Bill mark up.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The mark up amount. | [optional] 
**type** | **str** | The markup type. | [optional] 

## Example

```python
from buildium_sdk.models.bill_markup_message import BillMarkupMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillMarkupMessage from a JSON string
bill_markup_message_instance = BillMarkupMessage.from_json(json)
# print the JSON string representation of the object
print(BillMarkupMessage.to_json())

# convert the object into a dict
bill_markup_message_dict = bill_markup_message_instance.to_dict()
# create an instance of BillMarkupMessage from a dict
bill_markup_message_from_dict = BillMarkupMessage.from_dict(bill_markup_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


