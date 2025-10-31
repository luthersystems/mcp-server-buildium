# DepositDetailMessage

Deposit details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_gl_account_id** | **int** | Bank account general ledger identifier. | [optional] 
**payment_transactions** | [**List[PaymentTransactionsMessage]**](PaymentTransactionsMessage.md) | Collection of payments that were included in the bank deposit transaction. | [optional] 

## Example

```python
from buildium_sdk.models.deposit_detail_message import DepositDetailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DepositDetailMessage from a JSON string
deposit_detail_message_instance = DepositDetailMessage.from_json(json)
# print the JSON string representation of the object
print(DepositDetailMessage.to_json())

# convert the object into a dict
deposit_detail_message_dict = deposit_detail_message_instance.to_dict()
# create an instance of DepositDetailMessage from a dict
deposit_detail_message_from_dict = DepositDetailMessage.from_dict(deposit_detail_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


