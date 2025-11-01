# ApplicationReversePaymentOtherBankChargePostMessage

Fee assessed by the bank for the application reversed payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | Expense general ledger account to associate the bank fee. | 
**total_amount** | **float** | Total amount of the bank fee. | 

## Example

```python
from buildium_sdk.models.application_reverse_payment_other_bank_charge_post_message import ApplicationReversePaymentOtherBankChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationReversePaymentOtherBankChargePostMessage from a JSON string
application_reverse_payment_other_bank_charge_post_message_instance = ApplicationReversePaymentOtherBankChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationReversePaymentOtherBankChargePostMessage.to_json())

# convert the object into a dict
application_reverse_payment_other_bank_charge_post_message_dict = application_reverse_payment_other_bank_charge_post_message_instance.to_dict()
# create an instance of ApplicationReversePaymentOtherBankChargePostMessage from a dict
application_reverse_payment_other_bank_charge_post_message_from_dict = ApplicationReversePaymentOtherBankChargePostMessage.from_dict(application_reverse_payment_other_bank_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


