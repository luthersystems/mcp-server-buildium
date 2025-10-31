# FileNamePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Name of file being uploaded. The value can not exceed 255 characters. | 

## Example

```python
from buildium_sdk.models.file_name_post_message import FileNamePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileNamePostMessage from a JSON string
file_name_post_message_instance = FileNamePostMessage.from_json(json)
# print the JSON string representation of the object
print(FileNamePostMessage.to_json())

# convert the object into a dict
file_name_post_message_dict = file_name_post_message_instance.to_dict()
# create an instance of FileNamePostMessage from a dict
file_name_post_message_from_dict = FileNamePostMessage.from_dict(file_name_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


