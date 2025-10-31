# BillMarkupSaveMessage

Bill mark up.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The mark up amount. The value should be relative to the markup &#x60;Type&#x60;. If the mark up &#x60;Type&#x60; is &#x60;Percent&#x60; the value cannot exceed 100. | 
**type** | **str** | The markup type. | 

## Example

```python
from buildium_sdk.models.bill_markup_save_message import BillMarkupSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillMarkupSaveMessage from a JSON string
bill_markup_save_message_instance = BillMarkupSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BillMarkupSaveMessage.to_json())

# convert the object into a dict
bill_markup_save_message_dict = bill_markup_save_message_instance.to_dict()
# create an instance of BillMarkupSaveMessage from a dict
bill_markup_save_message_from_dict = BillMarkupSaveMessage.from_dict(bill_markup_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


