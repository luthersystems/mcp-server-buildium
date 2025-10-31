# FileCategoryPutMessage

File Category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file category. The value cannot exceed 100 characters. | 

## Example

```python
from buildium_sdk.models.file_category_put_message import FileCategoryPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileCategoryPutMessage from a JSON string
file_category_put_message_instance = FileCategoryPutMessage.from_json(json)
# print the JSON string representation of the object
print(FileCategoryPutMessage.to_json())

# convert the object into a dict
file_category_put_message_dict = file_category_put_message_instance.to_dict()
# create an instance of FileCategoryPutMessage from a dict
file_category_put_message_from_dict = FileCategoryPutMessage.from_dict(file_category_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


