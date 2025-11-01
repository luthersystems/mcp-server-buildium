# LeaseLedgerReversePaymentNSFChargePostMessage

Non-sufficient funds (NSF) charge to the tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | Income general ledger income account to record the charge under. | 
**total_amount** | **float** | Total amount to charge the tenant. | 

## Example

```python
from buildium_sdk.models.lease_ledger_reverse_payment_nsf_charge_post_message import LeaseLedgerReversePaymentNSFChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerReversePaymentNSFChargePostMessage from a JSON string
lease_ledger_reverse_payment_nsf_charge_post_message_instance = LeaseLedgerReversePaymentNSFChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerReversePaymentNSFChargePostMessage.to_json())

# convert the object into a dict
lease_ledger_reverse_payment_nsf_charge_post_message_dict = lease_ledger_reverse_payment_nsf_charge_post_message_instance.to_dict()
# create an instance of LeaseLedgerReversePaymentNSFChargePostMessage from a dict
lease_ledger_reverse_payment_nsf_charge_post_message_from_dict = LeaseLedgerReversePaymentNSFChargePostMessage.from_dict(lease_ledger_reverse_payment_nsf_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


