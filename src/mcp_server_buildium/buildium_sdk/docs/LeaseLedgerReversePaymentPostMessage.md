# LeaseLedgerReversePaymentPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date of the transaction. | 
**payment_transaction_id** | **int** | Transaction identifier of the payment to reverse. Note, this payment transaction must be deposited. | 
**nsf_charge** | [**LeaseLedgerReversePaymentNSFChargePostMessage**](LeaseLedgerReversePaymentNSFChargePostMessage.md) | Non-sufficient funds (NSF) charge. | [optional] 
**bank_fee** | [**LeaseLedgerReversePaymentOtherBankChargePostMessage**](LeaseLedgerReversePaymentOtherBankChargePostMessage.md) | Bank for fee assessed for the reversed payment. | [optional] 

## Example

```python
from buildium_sdk.models.lease_ledger_reverse_payment_post_message import LeaseLedgerReversePaymentPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerReversePaymentPostMessage from a JSON string
lease_ledger_reverse_payment_post_message_instance = LeaseLedgerReversePaymentPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerReversePaymentPostMessage.to_json())

# convert the object into a dict
lease_ledger_reverse_payment_post_message_dict = lease_ledger_reverse_payment_post_message_instance.to_dict()
# create an instance of LeaseLedgerReversePaymentPostMessage from a dict
lease_ledger_reverse_payment_post_message_from_dict = LeaseLedgerReversePaymentPostMessage.from_dict(lease_ledger_reverse_payment_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


