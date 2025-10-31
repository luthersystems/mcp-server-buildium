# TaskSubCategoryMessage

Task subcategory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task subcategory unique identifier. | [optional] 
**name** | **str** | Name of the task subcategory. | [optional] 

## Example

```python
from buildium_sdk.models.task_sub_category_message import TaskSubCategoryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSubCategoryMessage from a JSON string
task_sub_category_message_instance = TaskSubCategoryMessage.from_json(json)
# print the JSON string representation of the object
print(TaskSubCategoryMessage.to_json())

# convert the object into a dict
task_sub_category_message_dict = task_sub_category_message_instance.to_dict()
# create an instance of TaskSubCategoryMessage from a dict
task_sub_category_message_from_dict = TaskSubCategoryMessage.from_dict(task_sub_category_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


