# TaskCategorySaveMessage

Task category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the task category. | 

## Example

```python
from buildium_sdk.models.task_category_save_message import TaskCategorySaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategorySaveMessage from a JSON string
task_category_save_message_instance = TaskCategorySaveMessage.from_json(json)
# print the JSON string representation of the object
print(TaskCategorySaveMessage.to_json())

# convert the object into a dict
task_category_save_message_dict = task_category_save_message_instance.to_dict()
# create an instance of TaskCategorySaveMessage from a dict
task_category_save_message_from_dict = TaskCategorySaveMessage.from_dict(task_category_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


