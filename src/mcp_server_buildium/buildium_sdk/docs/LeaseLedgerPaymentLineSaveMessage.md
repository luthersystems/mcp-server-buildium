# LeaseLedgerPaymentLineSaveMessage

This is an object that represents a line item on a lease ledger payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. | 

## Example

```python
from buildium_sdk.models.lease_ledger_payment_line_save_message import LeaseLedgerPaymentLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerPaymentLineSaveMessage from a JSON string
lease_ledger_payment_line_save_message_instance = LeaseLedgerPaymentLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerPaymentLineSaveMessage.to_json())

# convert the object into a dict
lease_ledger_payment_line_save_message_dict = lease_ledger_payment_line_save_message_instance.to_dict()
# create an instance of LeaseLedgerPaymentLineSaveMessage from a dict
lease_ledger_payment_line_save_message_from_dict = LeaseLedgerPaymentLineSaveMessage.from_dict(lease_ledger_payment_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


