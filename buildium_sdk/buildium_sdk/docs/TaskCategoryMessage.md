# TaskCategoryMessage

Task category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task category unique identifier. | [optional] 
**name** | **str** | Name of the task category. | [optional] 
**is_system_category** | **bool** | Indicates whether the category is a system category. Note, system categories can not be edited. | [optional] 
**sub_categories** | [**List[TaskSubCategoryMessage]**](TaskSubCategoryMessage.md) | Subcategories associated with the task category. | [optional] 

## Example

```python
from buildium_sdk.models.task_category_message import TaskCategoryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategoryMessage from a JSON string
task_category_message_instance = TaskCategoryMessage.from_json(json)
# print the JSON string representation of the object
print(TaskCategoryMessage.to_json())

# convert the object into a dict
task_category_message_dict = task_category_message_instance.to_dict()
# create an instance of TaskCategoryMessage from a dict
task_category_message_from_dict = TaskCategoryMessage.from_dict(task_category_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


