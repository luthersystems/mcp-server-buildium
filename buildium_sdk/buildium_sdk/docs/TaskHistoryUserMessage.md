# TaskHistoryUserMessage

User information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] 
**first_name** | **str** | First name of the user. | [optional] 
**last_name** | **str** | Last name of the user. | [optional] 
**href** | **str** | A link to the resource endpoint associated with the user. | [optional] 
**user_type** | **str** | Describes the user type of the user | [optional] 

## Example

```python
from buildium_sdk.models.task_history_user_message import TaskHistoryUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskHistoryUserMessage from a JSON string
task_history_user_message_instance = TaskHistoryUserMessage.from_json(json)
# print the JSON string representation of the object
print(TaskHistoryUserMessage.to_json())

# convert the object into a dict
task_history_user_message_dict = task_history_user_message_instance.to_dict()
# create an instance of TaskHistoryUserMessage from a dict
task_history_user_message_from_dict = TaskHistoryUserMessage.from_dict(task_history_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


