# MultipleBillPaymentAllocationLinePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_id** | **int** | Unique identifier of the bill. | [optional] 
**lines** | [**List[BillPaymentLinePostMessage]**](BillPaymentLinePostMessage.md) | A collection of payment line items. | [optional] 

## Example

```python
from buildium_sdk.models.multiple_bill_payment_allocation_line_post_message import MultipleBillPaymentAllocationLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleBillPaymentAllocationLinePostMessage from a JSON string
multiple_bill_payment_allocation_line_post_message_instance = MultipleBillPaymentAllocationLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(MultipleBillPaymentAllocationLinePostMessage.to_json())

# convert the object into a dict
multiple_bill_payment_allocation_line_post_message_dict = multiple_bill_payment_allocation_line_post_message_instance.to_dict()
# create an instance of MultipleBillPaymentAllocationLinePostMessage from a dict
multiple_bill_payment_allocation_line_post_message_from_dict = MultipleBillPaymentAllocationLinePostMessage.from_dict(multiple_bill_payment_allocation_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


