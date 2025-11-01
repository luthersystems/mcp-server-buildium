# WorkOrderTaskPostMessage

Task information to create and associate with the work order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Task title. The title can not exceed 127 characters. | 
**due_date** | **date** | Task due date. The date must be formatted as YYYY-MM-DD. | [optional] 
**priority** | **str** | Task priority. | 
**status** | **str** | Task status. | 
**property_id** | **int** | The unique identifier of property associated with the request. The assigned property must be active. | [optional] 
**unit_id** | **int** | The unique identifier of the unit associated with the request. The unit must be associated with the &#x60;PropertyId&#x60; specified. | [optional] 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the request. The user must be a &#x60;Staff&#x60; user type. | 

## Example

```python
from buildium_sdk.models.work_order_task_post_message import WorkOrderTaskPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderTaskPostMessage from a JSON string
work_order_task_post_message_instance = WorkOrderTaskPostMessage.from_json(json)
# print the JSON string representation of the object
print(WorkOrderTaskPostMessage.to_json())

# convert the object into a dict
work_order_task_post_message_dict = work_order_task_post_message_instance.to_dict()
# create an instance of WorkOrderTaskPostMessage from a dict
work_order_task_post_message_from_dict = WorkOrderTaskPostMessage.from_dict(work_order_task_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


