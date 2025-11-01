# MultipleBillPaymentsPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_id** | **int** | Unique identifier of the bank account that the payment was made from. | 
**entry_date** | **date** | Date the payment was made. | 
**queue_checks_for_printing** | **bool** | Indicates whether to queue local check printing. Bank account associated with the bill must have check printing enabled to be true. | [optional] 
**bill_ids** | **List[int]** | Unique identifiers of bills for full payment. Bill ids cannot be present here if they are part of the &#x60;PaymentAllocations&#x60; collection. | 
**vendor_credit_ids** | **List[int]** | Unique identifiers of the vendor credits to apply to the payment. | [optional] 
**payment_allocations** | [**List[MultipleBillPaymentAllocationLinePostMessage]**](MultipleBillPaymentAllocationLinePostMessage.md) | A collection of payment allocations for individual bills. Bill ids cannot be present here if they are fully paid as part of the &#x60;BillIds&#x60; collection. | [optional] 

## Example

```python
from buildium_sdk.models.multiple_bill_payments_post_message import MultipleBillPaymentsPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleBillPaymentsPostMessage from a JSON string
multiple_bill_payments_post_message_instance = MultipleBillPaymentsPostMessage.from_json(json)
# print the JSON string representation of the object
print(MultipleBillPaymentsPostMessage.to_json())

# convert the object into a dict
multiple_bill_payments_post_message_dict = multiple_bill_payments_post_message_instance.to_dict()
# create an instance of MultipleBillPaymentsPostMessage from a dict
multiple_bill_payments_post_message_from_dict = MultipleBillPaymentsPostMessage.from_dict(multiple_bill_payments_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


