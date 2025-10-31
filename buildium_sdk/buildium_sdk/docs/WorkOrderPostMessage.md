# WorkOrderPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_details** | **str** | Description of the work order. The value cannot exceed 65,535 characters. | [optional] 
**invoice_number** | **str** | The invoice or reference number that the vendor assigned to the work order. The value cannot exceed 50 characters. | [optional] 
**chargeable_to** | **str** | A description of the entity that will be charged for the work. The value cannot exceed 100 characters. | [optional] 
**entry_allowed** | **str** | Indicates whether entry has been allowed to the unit. | 
**entry_notes** | **str** | Notes specific to entering the unit. The value cannot exceed 65,535 characters. | [optional] 
**vendor_id** | **int** | Vendor unique identifier. | 
**vendor_notes** | **str** | Notes specific to the vendor. The value cannot exceed 65,535 characters. | [optional] 
**entry_contact_id** | **int** | Contact user unique identifier. The user type must be one of the following: &#x60;RentalTenant&#x60;, &#x60;AssociationOwner&#x60;, &#x60;Staff&#x60;, &#x60;RentalOwner&#x60;. | [optional] 
**entry_contact_ids** | **List[int]** | Collection of entry contact user unique identifiers for the work order. The user type of each user in the collection must be one of the following: &#x60;RentalTenant&#x60;, &#x60;AssociationOwner&#x60;, &#x60;Staff&#x60;, &#x60;RentalOwner&#x60;. | [optional] 
**line_items** | [**List[WorkOrderLineItemSaveMessage]**](WorkOrderLineItemSaveMessage.md) | Work order line items. | [optional] 
**task_id** | **int** | Task unique identifier to associate with the work order. | [optional] 
**task** | [**WorkOrderTaskPostMessage**](WorkOrderTaskPostMessage.md) | Task information to create and associate with the work order. | [optional] 

## Example

```python
from buildium_sdk.models.work_order_post_message import WorkOrderPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderPostMessage from a JSON string
work_order_post_message_instance = WorkOrderPostMessage.from_json(json)
# print the JSON string representation of the object
print(WorkOrderPostMessage.to_json())

# convert the object into a dict
work_order_post_message_dict = work_order_post_message_instance.to_dict()
# create an instance of WorkOrderPostMessage from a dict
work_order_post_message_from_dict = WorkOrderPostMessage.from_dict(work_order_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


