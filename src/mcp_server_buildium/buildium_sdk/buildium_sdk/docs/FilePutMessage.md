# FilePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the file. The value cannot exceed 255 characters. | 
**description** | **str** | A description of the file. The value cannot exceed 65000 characters. | [optional] 
**category_id** | **int** | The category identifier to assign to this file. | 

## Example

```python
from buildium_sdk.models.file_put_message import FilePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FilePutMessage from a JSON string
file_put_message_instance = FilePutMessage.from_json(json)
# print the JSON string representation of the object
print(FilePutMessage.to_json())

# convert the object into a dict
file_put_message_dict = file_put_message_instance.to_dict()
# create an instance of FilePutMessage from a dict
file_put_message_from_dict = FilePutMessage.from_dict(file_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


