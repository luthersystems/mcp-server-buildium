# BillPaymentMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bill payment unique identifier. | [optional] 
**bank_account_id** | **int** | Unique identifier of the bank account that the payment was made from. | [optional] 
**entry_date** | **date** | Date the payment was made. | [optional] 
**memo** | **str** | A high-level description of the payment. | [optional] 
**check_number** | **str** | Number of the check used to make the payment. | [optional] 
**paid_bill_ids** | **List[int]** | A collection of bill identifiers that the payment was applied to. | [optional] 
**applied_vendor_credits** | [**List[AppliedVendorCreditMessage]**](AppliedVendorCreditMessage.md) | A collection of vendor credits that was applied in the bill payment. | [optional] 
**lines** | [**List[BillPaymentLineMessage]**](BillPaymentLineMessage.md) | A collection of payment line items. | [optional] 

## Example

```python
from buildium_sdk.models.bill_payment_message import BillPaymentMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentMessage from a JSON string
bill_payment_message_instance = BillPaymentMessage.from_json(json)
# print the JSON string representation of the object
print(BillPaymentMessage.to_json())

# convert the object into a dict
bill_payment_message_dict = bill_payment_message_instance.to_dict()
# create an instance of BillPaymentMessage from a dict
bill_payment_message_from_dict = BillPaymentMessage.from_dict(bill_payment_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


