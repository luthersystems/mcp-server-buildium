# BillPaymentPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_id** | **int** | Unique identifier of the bank account that the payment was made from. | 
**entry_date** | **date** | Date the payment was made. | 
**memo** | **str** | A high-level description of the payment. The value cannot exceed 240 characters. | [optional] 
**check_number** | **str** | Number of the check used to make the payment. The value cannot exceed 30 characters. | [optional] 
**lines** | [**List[BillPaymentLinePostMessage]**](BillPaymentLinePostMessage.md) | A collection of payment line items. | 
**vendor_credit_ids** | **List[int]** | Unique identifiers of the vendor credits to apply to the payment. | [optional] 

## Example

```python
from buildium_sdk.models.bill_payment_post_message import BillPaymentPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentPostMessage from a JSON string
bill_payment_post_message_instance = BillPaymentPostMessage.from_json(json)
# print the JSON string representation of the object
print(BillPaymentPostMessage.to_json())

# convert the object into a dict
bill_payment_post_message_dict = bill_payment_post_message_instance.to_dict()
# create an instance of BillPaymentPostMessage from a dict
bill_payment_post_message_from_dict = BillPaymentPostMessage.from_dict(bill_payment_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


