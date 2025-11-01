# PaymentTransactionsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Payment transaction unique identifier. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | The accounting entity associated with the payment. | [optional] 
**amount** | **float** | Payment amount. | [optional] 

## Example

```python
from buildium_sdk.models.payment_transactions_message import PaymentTransactionsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransactionsMessage from a JSON string
payment_transactions_message_instance = PaymentTransactionsMessage.from_json(json)
# print the JSON string representation of the object
print(PaymentTransactionsMessage.to_json())

# convert the object into a dict
payment_transactions_message_dict = payment_transactions_message_instance.to_dict()
# create an instance of PaymentTransactionsMessage from a dict
payment_transactions_message_from_dict = PaymentTransactionsMessage.from_dict(payment_transactions_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


