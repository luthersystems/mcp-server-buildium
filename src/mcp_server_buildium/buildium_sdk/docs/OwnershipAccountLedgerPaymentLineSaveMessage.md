# OwnershipAccountLedgerPaymentLineSaveMessage

This is an object that represents a line item on an Ownership Account Ledger Payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. | 

## Example

```python
from buildium_sdk.models.ownership_account_ledger_payment_line_save_message import OwnershipAccountLedgerPaymentLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountLedgerPaymentLineSaveMessage from a JSON string
ownership_account_ledger_payment_line_save_message_instance = OwnershipAccountLedgerPaymentLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountLedgerPaymentLineSaveMessage.to_json())

# convert the object into a dict
ownership_account_ledger_payment_line_save_message_dict = ownership_account_ledger_payment_line_save_message_instance.to_dict()
# create an instance of OwnershipAccountLedgerPaymentLineSaveMessage from a dict
ownership_account_ledger_payment_line_save_message_from_dict = OwnershipAccountLedgerPaymentLineSaveMessage.from_dict(ownership_account_ledger_payment_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


