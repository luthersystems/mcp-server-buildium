# TaskCategoryResponseMessage

Task category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task category unique identifier. | [optional] 
**name** | **str** | Name of the task category. | [optional] 
**href** | **str** | A link to the task category resource. | [optional] 
**sub_category** | [**TaskSubCategoryMessage**](TaskSubCategoryMessage.md) | Subcategory associated with the task category. | [optional] 

## Example

```python
from buildium_sdk.models.task_category_response_message import TaskCategoryResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategoryResponseMessage from a JSON string
task_category_response_message_instance = TaskCategoryResponseMessage.from_json(json)
# print the JSON string representation of the object
print(TaskCategoryResponseMessage.to_json())

# convert the object into a dict
task_category_response_message_dict = task_category_response_message_instance.to_dict()
# create an instance of TaskCategoryResponseMessage from a dict
task_category_response_message_from_dict = TaskCategoryResponseMessage.from_dict(task_category_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


