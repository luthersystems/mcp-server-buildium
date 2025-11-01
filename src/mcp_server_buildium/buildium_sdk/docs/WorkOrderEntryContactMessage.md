# WorkOrderEntryContactMessage

Contact entity for the work order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contact entity unique identifier. | [optional] 
**resources** | [**List[WorkOrderEntryContactResourceMessage]**](WorkOrderEntryContactResourceMessage.md) | List of contact entity resources. | [optional] 

## Example

```python
from buildium_sdk.models.work_order_entry_contact_message import WorkOrderEntryContactMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderEntryContactMessage from a JSON string
work_order_entry_contact_message_instance = WorkOrderEntryContactMessage.from_json(json)
# print the JSON string representation of the object
print(WorkOrderEntryContactMessage.to_json())

# convert the object into a dict
work_order_entry_contact_message_dict = work_order_entry_contact_message_instance.to_dict()
# create an instance of WorkOrderEntryContactMessage from a dict
work_order_entry_contact_message_from_dict = WorkOrderEntryContactMessage.from_dict(work_order_entry_contact_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


