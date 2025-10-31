# TaskCategoryPutMessage

Task category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the task category. | 

## Example

```python
from buildium_sdk.models.task_category_put_message import TaskCategoryPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategoryPutMessage from a JSON string
task_category_put_message_instance = TaskCategoryPutMessage.from_json(json)
# print the JSON string representation of the object
print(TaskCategoryPutMessage.to_json())

# convert the object into a dict
task_category_put_message_dict = task_category_put_message_instance.to_dict()
# create an instance of TaskCategoryPutMessage from a dict
task_category_put_message_from_dict = TaskCategoryPutMessage.from_dict(task_category_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


