# BankAccountReconciliationTransactionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Reconciliation transaction unique identifier. | [optional] 
**entry_date** | **date** | Date the reconciliation transaction entered. | [optional] 
**total_amount** | **float** | Total amount of the reconciliation transaction. | [optional] 
**reconciliation_status** | **str** | Status of the reconciliation transaction. | [optional] 
**transaction_type** | **str** | Type of transaction. | [optional] 
**memo** | **str** | Memo associated with the transaction, if applicable. | [optional] 
**payment_method** | **str** | The payment method used for the transaction. | [optional] 
**check_number** | **str** | Check number associated with the transaction, if applicable. | [optional] 
**payee_user_id** | **int** | The payee&#39;s user unique identifier. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_reconciliation_transaction_message import BankAccountReconciliationTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountReconciliationTransactionMessage from a JSON string
bank_account_reconciliation_transaction_message_instance = BankAccountReconciliationTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountReconciliationTransactionMessage.to_json())

# convert the object into a dict
bank_account_reconciliation_transaction_message_dict = bank_account_reconciliation_transaction_message_instance.to_dict()
# create an instance of BankAccountReconciliationTransactionMessage from a dict
bank_account_reconciliation_transaction_message_from_dict = BankAccountReconciliationTransactionMessage.from_dict(bank_account_reconciliation_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


