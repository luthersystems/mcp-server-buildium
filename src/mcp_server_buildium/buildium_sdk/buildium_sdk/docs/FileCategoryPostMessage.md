# FileCategoryPostMessage

File category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file category. The value cannot exceed 100 characters. | 

## Example

```python
from buildium_sdk.models.file_category_post_message import FileCategoryPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileCategoryPostMessage from a JSON string
file_category_post_message_instance = FileCategoryPostMessage.from_json(json)
# print the JSON string representation of the object
print(FileCategoryPostMessage.to_json())

# convert the object into a dict
file_category_post_message_dict = file_category_post_message_instance.to_dict()
# create an instance of FileCategoryPostMessage from a dict
file_category_post_message_from_dict = FileCategoryPostMessage.from_dict(file_category_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


