# FileUploadPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Specifies the type of entity that &#x60;EntityId&#x60; refers to. | 
**entity_id** | **int** | Unique identified of the Entity Type. | [optional] 
**file_name** | **str** | Name of file being uploaded. The value can not exceed 255 characters. | 
**title** | **str** | Title of file upload. The value can not exceed 255 characters. | 
**description** | **str** | Description of file upload. The value can not exceed 1000 characters. | [optional] 
**category_id** | **int** | Unique identified of file category. | 

## Example

```python
from buildium_sdk.models.file_upload_post_message import FileUploadPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadPostMessage from a JSON string
file_upload_post_message_instance = FileUploadPostMessage.from_json(json)
# print the JSON string representation of the object
print(FileUploadPostMessage.to_json())

# convert the object into a dict
file_upload_post_message_dict = file_upload_post_message_instance.to_dict()
# create an instance of FileUploadPostMessage from a dict
file_upload_post_message_from_dict = FileUploadPostMessage.from_dict(file_upload_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


