# VendorCategorySaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The category name. | 

## Example

```python
from buildium_sdk.models.vendor_category_save_message import VendorCategorySaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCategorySaveMessage from a JSON string
vendor_category_save_message_instance = VendorCategorySaveMessage.from_json(json)
# print the JSON string representation of the object
print(VendorCategorySaveMessage.to_json())

# convert the object into a dict
vendor_category_save_message_dict = vendor_category_save_message_instance.to_dict()
# create an instance of VendorCategorySaveMessage from a dict
vendor_category_save_message_from_dict = VendorCategorySaveMessage.from_dict(vendor_category_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


