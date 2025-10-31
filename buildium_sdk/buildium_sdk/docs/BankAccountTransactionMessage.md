# BankAccountTransactionMessage

Bank account transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction unique identifier. | [optional] 
**entry_date** | **date** | Date of the transaction. | [optional] 
**transaction_type** | **str** | Type of transaction. | [optional] 
**check_number** | **str** | Check number associated with the transaction, if applicable. | [optional] 
**memo** | **str** | Memo associated with the transaction, if applicable. | [optional] 
**amount** | **float** | The total amount of the transaction. | [optional] 
**reconciliation_status** | **str** | Indicates the reconciliation status of the transaction. | [optional] 
**paid_by** | [**List[PaidByMessage]**](PaidByMessage.md) | The entity that made the payment. | [optional] 
**paid_to** | [**List[PayeeMessage]**](PayeeMessage.md) | The entity that received the payment. | [optional] 
**balance** | **float** | The bank account balance after this transaction was applied. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_transaction_message import BankAccountTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountTransactionMessage from a JSON string
bank_account_transaction_message_instance = BankAccountTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountTransactionMessage.to_json())

# convert the object into a dict
bank_account_transaction_message_dict = bank_account_transaction_message_instance.to_dict()
# create an instance of BankAccountTransactionMessage from a dict
bank_account_transaction_message_from_dict = BankAccountTransactionMessage.from_dict(bank_account_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


