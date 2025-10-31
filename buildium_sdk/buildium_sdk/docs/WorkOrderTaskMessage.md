# WorkOrderTaskMessage

Task information related to the work order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task unique identifier. | [optional] 
**type** | **str** | The task type. | [optional] 
**unit_id** | **int** | The unit unique identifier associated with the task. | [optional] 
**unit_agreement** | [**UnitAgreementMessage**](UnitAgreementMessage.md) | The unit agreement that is associated with the task. | [optional] 
**title** | **str** | Task title. | [optional] 
**due_date** | **date** | Task due date. | [optional] 
**priority** | **str** | Task priority. | [optional] 
**status** | **str** | Task status. | [optional] 

## Example

```python
from buildium_sdk.models.work_order_task_message import WorkOrderTaskMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderTaskMessage from a JSON string
work_order_task_message_instance = WorkOrderTaskMessage.from_json(json)
# print the JSON string representation of the object
print(WorkOrderTaskMessage.to_json())

# convert the object into a dict
work_order_task_message_dict = work_order_task_message_instance.to_dict()
# create an instance of WorkOrderTaskMessage from a dict
work_order_task_message_from_dict = WorkOrderTaskMessage.from_dict(work_order_task_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


