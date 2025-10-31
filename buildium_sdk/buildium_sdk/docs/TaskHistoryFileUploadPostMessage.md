# TaskHistoryFileUploadPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Name of file being uploaded. The value can not exceed 255 characters. | 

## Example

```python
from buildium_sdk.models.task_history_file_upload_post_message import TaskHistoryFileUploadPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskHistoryFileUploadPostMessage from a JSON string
task_history_file_upload_post_message_instance = TaskHistoryFileUploadPostMessage.from_json(json)
# print the JSON string representation of the object
print(TaskHistoryFileUploadPostMessage.to_json())

# convert the object into a dict
task_history_file_upload_post_message_dict = task_history_file_upload_post_message_instance.to_dict()
# create an instance of TaskHistoryFileUploadPostMessage from a dict
task_history_file_upload_post_message_from_dict = TaskHistoryFileUploadPostMessage.from_dict(task_history_file_upload_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


