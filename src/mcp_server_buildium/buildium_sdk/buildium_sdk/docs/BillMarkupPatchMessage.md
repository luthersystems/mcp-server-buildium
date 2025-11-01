# BillMarkupPatchMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The mark up amount. The value should be relative to the markup &#x60;Type&#x60;. If the mark up &#x60;Type&#x60; is &#x60;Percent&#x60; the value cannot exceed 100. | [optional] 
**type** | **str** | The markup type. | [optional] 

## Example

```python
from buildium_sdk.models.bill_markup_patch_message import BillMarkupPatchMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillMarkupPatchMessage from a JSON string
bill_markup_patch_message_instance = BillMarkupPatchMessage.from_json(json)
# print the JSON string representation of the object
print(BillMarkupPatchMessage.to_json())

# convert the object into a dict
bill_markup_patch_message_dict = bill_markup_patch_message_instance.to_dict()
# create an instance of BillMarkupPatchMessage from a dict
bill_markup_patch_message_from_dict = BillMarkupPatchMessage.from_dict(bill_markup_patch_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


