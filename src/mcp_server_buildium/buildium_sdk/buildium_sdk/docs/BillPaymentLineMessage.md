# BillPaymentLineMessage

Payment line items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_entity** | [**BillPaymentAccountingEntityMessage**](BillPaymentAccountingEntityMessage.md) | The accounting entity associated with the bill line item. | [optional] 
**gl_account_id** | **int** | The general ledger account the line item is allocated to. | [optional] 
**amount** | **float** | Line item amount. | [optional] 

## Example

```python
from buildium_sdk.models.bill_payment_line_message import BillPaymentLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentLineMessage from a JSON string
bill_payment_line_message_instance = BillPaymentLineMessage.from_json(json)
# print the JSON string representation of the object
print(BillPaymentLineMessage.to_json())

# convert the object into a dict
bill_payment_line_message_dict = bill_payment_line_message_instance.to_dict()
# create an instance of BillPaymentLineMessage from a dict
bill_payment_line_message_from_dict = BillPaymentLineMessage.from_dict(bill_payment_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


