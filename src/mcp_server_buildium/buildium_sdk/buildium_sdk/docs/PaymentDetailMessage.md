# PaymentDetailMessage

This object represents payment details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | The payment method used for the transaction. | [optional] 
**payee** | [**PayeeMessage**](PayeeMessage.md) | The payee of the transaction. | [optional] 
**is_internal_transaction** | **bool** | Whether the transaction is processed internally. | [optional] 
**internal_transaction_status** | [**InternalTransactionStatusMessage**](InternalTransactionStatusMessage.md) | The status of the transaction. Note, this is only applicable for if &#x60;IsInternalTransaction&#x60; is &#x60;true&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.payment_detail_message import PaymentDetailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailMessage from a JSON string
payment_detail_message_instance = PaymentDetailMessage.from_json(json)
# print the JSON string representation of the object
print(PaymentDetailMessage.to_json())

# convert the object into a dict
payment_detail_message_dict = payment_detail_message_instance.to_dict()
# create an instance of PaymentDetailMessage from a dict
payment_detail_message_from_dict = PaymentDetailMessage.from_dict(payment_detail_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


