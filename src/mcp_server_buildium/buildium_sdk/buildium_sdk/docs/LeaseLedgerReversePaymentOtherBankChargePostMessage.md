# LeaseLedgerReversePaymentOtherBankChargePostMessage

Fee assessed by the bank for the reversed payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | Expense general ledger account to associate the bank fee. | 
**total_amount** | **float** | Total amount of the bank fee. | 

## Example

```python
from buildium_sdk.models.lease_ledger_reverse_payment_other_bank_charge_post_message import LeaseLedgerReversePaymentOtherBankChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerReversePaymentOtherBankChargePostMessage from a JSON string
lease_ledger_reverse_payment_other_bank_charge_post_message_instance = LeaseLedgerReversePaymentOtherBankChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerReversePaymentOtherBankChargePostMessage.to_json())

# convert the object into a dict
lease_ledger_reverse_payment_other_bank_charge_post_message_dict = lease_ledger_reverse_payment_other_bank_charge_post_message_instance.to_dict()
# create an instance of LeaseLedgerReversePaymentOtherBankChargePostMessage from a dict
lease_ledger_reverse_payment_other_bank_charge_post_message_from_dict = LeaseLedgerReversePaymentOtherBankChargePostMessage.from_dict(lease_ledger_reverse_payment_other_bank_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


