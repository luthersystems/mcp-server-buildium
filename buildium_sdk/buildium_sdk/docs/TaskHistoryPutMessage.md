# TaskHistoryPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message to include with the task update. The value can not exceed 65500 characters. | 

## Example

```python
from buildium_sdk.models.task_history_put_message import TaskHistoryPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskHistoryPutMessage from a JSON string
task_history_put_message_instance = TaskHistoryPutMessage.from_json(json)
# print the JSON string representation of the object
print(TaskHistoryPutMessage.to_json())

# convert the object into a dict
task_history_put_message_dict = task_history_put_message_instance.to_dict()
# create an instance of TaskHistoryPutMessage from a dict
task_history_put_message_from_dict = TaskHistoryPutMessage.from_dict(task_history_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


