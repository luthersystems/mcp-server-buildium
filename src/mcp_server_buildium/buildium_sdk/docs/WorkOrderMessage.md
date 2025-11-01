# WorkOrderMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Work order unique identifier. | [optional] 
**task** | [**WorkOrderTaskMessage**](WorkOrderTaskMessage.md) | Task information related to the work order. | [optional] 
**title** | **str** | Work order title. | [optional] 
**due_date** | **date** | Work order due date. | [optional] 
**priority** | **str** | Work order  priority. | [optional] 
**status** | **str** | Work order status. | [optional] 
**work_details** | **str** | Description of the work order. | [optional] 
**invoice_number** | **str** | The invoice or reference number that the vendor assigned to the invoice. | [optional] 
**chargeable_to** | **str** | A description of the entity that will be charged for the work. | [optional] 
**entry_allowed** | **str** | Indicates whether entry has been allowed to the unit. | [optional] 
**entry_notes** | **str** | Notes specific to entering the unit. | [optional] 
**vendor_id** | **int** | Vendor unique identifier. | [optional] 
**vendor_notes** | **str** | Notes specific to the vendor. | [optional] 
**entry_contact** | [**WorkOrderEntryContactMessage**](WorkOrderEntryContactMessage.md) | Entry contact for the work order | [optional] 
**entry_contacts** | [**List[WorkOrderEntryContactMessage]**](WorkOrderEntryContactMessage.md) | A collection of all entry contacts for the work order | [optional] 
**bill_transaction_id** | **int** | Unique identifier for the bill related to this work order. This field will be &#x60;null&#x60; if no bill is related to this work order.  If the BillTransactionIds field is available, please refer to that field instead of this one going forward. | [optional] 
**bill_transaction_ids** | **List[int]** | A collection of unique identifiers for the bills related to this work order. | [optional] 
**amount** | **float** | The total amount of the work order. | [optional] 
**line_items** | [**List[WorkOrderLineItemMessage]**](WorkOrderLineItemMessage.md) | A collection of line items associated with the work order. | [optional] 

## Example

```python
from buildium_sdk.models.work_order_message import WorkOrderMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderMessage from a JSON string
work_order_message_instance = WorkOrderMessage.from_json(json)
# print the JSON string representation of the object
print(WorkOrderMessage.to_json())

# convert the object into a dict
work_order_message_dict = work_order_message_instance.to_dict()
# create an instance of WorkOrderMessage from a dict
work_order_message_from_dict = WorkOrderMessage.from_dict(work_order_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


