# ApplicationReversePaymentPostMessage

This is an object that represents a reversed payment tied to an application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date of the transaction. The date must be formatted as YYYY-MM-DD. | 
**payment_transaction_id** | **int** | Transaction identifier of the payment to reverse. Note, this payment transaction must be deposited. | 
**nsf_charge** | [**ApplicationReversePaymentChargePostMessage**](ApplicationReversePaymentChargePostMessage.md) | Non-sufficient funds (NSF) charge. | [optional] 
**bank_fee** | [**ApplicationReversePaymentOtherBankChargePostMessage**](ApplicationReversePaymentOtherBankChargePostMessage.md) | Bank for fee assessed for the reversed payment operating account. | [optional] 
**deposit_trust_account_bank_fee** | [**ApplicationReversePaymentOtherBankChargePostMessage**](ApplicationReversePaymentOtherBankChargePostMessage.md) | Bank for fee assessed for the reversed payment deposit trust account. | [optional] 

## Example

```python
from buildium_sdk.models.application_reverse_payment_post_message import ApplicationReversePaymentPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationReversePaymentPostMessage from a JSON string
application_reverse_payment_post_message_instance = ApplicationReversePaymentPostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationReversePaymentPostMessage.to_json())

# convert the object into a dict
application_reverse_payment_post_message_dict = application_reverse_payment_post_message_instance.to_dict()
# create an instance of ApplicationReversePaymentPostMessage from a dict
application_reverse_payment_post_message_from_dict = ApplicationReversePaymentPostMessage.from_dict(application_reverse_payment_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


