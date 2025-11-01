# WorkOrderEntryContactResourceMessage

Work order entry contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Contact entity type. | [optional] 
**href** | **str** | Link to the contact resource. | [optional] 

## Example

```python
from buildium_sdk.models.work_order_entry_contact_resource_message import WorkOrderEntryContactResourceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderEntryContactResourceMessage from a JSON string
work_order_entry_contact_resource_message_instance = WorkOrderEntryContactResourceMessage.from_json(json)
# print the JSON string representation of the object
print(WorkOrderEntryContactResourceMessage.to_json())

# convert the object into a dict
work_order_entry_contact_resource_message_dict = work_order_entry_contact_resource_message_instance.to_dict()
# create an instance of WorkOrderEntryContactResourceMessage from a dict
work_order_entry_contact_resource_message_from_dict = WorkOrderEntryContactResourceMessage.from_dict(work_order_entry_contact_resource_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


