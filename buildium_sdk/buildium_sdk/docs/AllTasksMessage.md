# AllTasksMessage

This object represents a task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task unique identifier. | [optional] 
**task_type** | **str** | The task type. | [optional] 
**category** | [**TaskCategoryResponseMessage**](TaskCategoryResponseMessage.md) | Task category. | [optional] 
**title** | **str** | Task title. | [optional] 
**description** | **str** | Task description. | [optional] 
**var_property** | [**PropertyMessage**](PropertyMessage.md) | The property details associated with the task. | [optional] 
**unit_id** | **int** | The unit unique identifier associated with the task. | [optional] 
**unit_agreement** | [**UnitAgreementMessage**](UnitAgreementMessage.md) | The unit agreement that is associated with the task. | [optional] 
**requested_by_user_entity** | [**RequestedByUserEntityMessage**](RequestedByUserEntityMessage.md) | The user entity that requested the task. | [optional] 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the task. | [optional] 
**task_status** | **str** | Task status. | [optional] 
**priority** | **str** | Task priority. | [optional] 
**due_date** | **date** | Task due date. | [optional] 
**created_date_time** | **datetime** | The date and time the task was created. | [optional] 
**last_updated_date_time** | **datetime** | The date and time the task was last updated. | [optional] 

## Example

```python
from buildium_sdk.models.all_tasks_message import AllTasksMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AllTasksMessage from a JSON string
all_tasks_message_instance = AllTasksMessage.from_json(json)
# print the JSON string representation of the object
print(AllTasksMessage.to_json())

# convert the object into a dict
all_tasks_message_dict = all_tasks_message_instance.to_dict()
# create an instance of AllTasksMessage from a dict
all_tasks_message_from_dict = AllTasksMessage.from_dict(all_tasks_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


