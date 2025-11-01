# WorkOrderLineItemMessage

Work order line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | General ledger account unique identifier. | [optional] 
**quantity** | **float** | Line item quantity. | [optional] 
**memo** | **str** | Line item memo. | [optional] 
**unit_price** | **float** | Line item unit price. | [optional] 

## Example

```python
from buildium_sdk.models.work_order_line_item_message import WorkOrderLineItemMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderLineItemMessage from a JSON string
work_order_line_item_message_instance = WorkOrderLineItemMessage.from_json(json)
# print the JSON string representation of the object
print(WorkOrderLineItemMessage.to_json())

# convert the object into a dict
work_order_line_item_message_dict = work_order_line_item_message_instance.to_dict()
# create an instance of WorkOrderLineItemMessage from a dict
work_order_line_item_message_from_dict = WorkOrderLineItemMessage.from_dict(work_order_line_item_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


