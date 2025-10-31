# VendorCategoryMessage

This object represents a vendor category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. | [optional] 
**name** | **str** | Name. | [optional] 
**is_system_category** | **bool** | Indicates whether the category is a system category. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_category_message import VendorCategoryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCategoryMessage from a JSON string
vendor_category_message_instance = VendorCategoryMessage.from_json(json)
# print the JSON string representation of the object
print(VendorCategoryMessage.to_json())

# convert the object into a dict
vendor_category_message_dict = vendor_category_message_instance.to_dict()
# create an instance of VendorCategoryMessage from a dict
vendor_category_message_from_dict = VendorCategoryMessage.from_dict(vendor_category_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


