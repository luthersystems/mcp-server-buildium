# FileCategoryMessage

File category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File category unique identifier. | [optional] 
**name** | **str** | Name of the file category. | [optional] 
**is_editable** | **bool** | Indicates whether the category is editable. | [optional] 

## Example

```python
from buildium_sdk.models.file_category_message import FileCategoryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileCategoryMessage from a JSON string
file_category_message_instance = FileCategoryMessage.from_json(json)
# print the JSON string representation of the object
print(FileCategoryMessage.to_json())

# convert the object into a dict
file_category_message_dict = file_category_message_instance.to_dict()
# create an instance of FileCategoryMessage from a dict
file_category_message_from_dict = FileCategoryMessage.from_dict(file_category_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


