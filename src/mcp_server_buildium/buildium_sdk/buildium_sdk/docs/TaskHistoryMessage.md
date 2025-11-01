# TaskHistoryMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task history unique identifier. | [optional] 
**priority** | **str** | Task priority. | [optional] 
**task_status** | **str** | Task status. | [optional] 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the task. | [optional] 
**due_date** | **date** | Task due date. | [optional] 
**message** | **str** | Description of the task update. | [optional] 
**shared_with** | **List[str]** | Indicates the who the task update was shared with. | [optional] 
**file_ids** | **List[int]** | List of file unique identifiers associated with the task history. These identifiers can be used to retrieve the file metadata and/or download the files. | [optional] 
**created_date_t_ime** | **datetime** | The date and time the task history was created. | [optional] 
**created_by_user** | [**TaskHistoryUserMessage**](TaskHistoryUserMessage.md) | User that created this task history. | [optional] 
**last_updated_date_time** | **datetime** | The date and time the task was last updated. | [optional] 
**last_updated_by_user** | [**TaskHistoryUserMessage**](TaskHistoryUserMessage.md) | User that last updated this task history. | [optional] 

## Example

```python
from buildium_sdk.models.task_history_message import TaskHistoryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskHistoryMessage from a JSON string
task_history_message_instance = TaskHistoryMessage.from_json(json)
# print the JSON string representation of the object
print(TaskHistoryMessage.to_json())

# convert the object into a dict
task_history_message_dict = task_history_message_instance.to_dict()
# create an instance of TaskHistoryMessage from a dict
task_history_message_from_dict = TaskHistoryMessage.from_dict(task_history_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


