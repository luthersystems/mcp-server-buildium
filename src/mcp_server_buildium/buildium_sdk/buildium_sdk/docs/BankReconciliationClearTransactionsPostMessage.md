# BankReconciliationClearTransactionsPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | The transaction identifiers to clear for the reconciliation | 

## Example

```python
from buildium_sdk.models.bank_reconciliation_clear_transactions_post_message import BankReconciliationClearTransactionsPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankReconciliationClearTransactionsPostMessage from a JSON string
bank_reconciliation_clear_transactions_post_message_instance = BankReconciliationClearTransactionsPostMessage.from_json(json)
# print the JSON string representation of the object
print(BankReconciliationClearTransactionsPostMessage.to_json())

# convert the object into a dict
bank_reconciliation_clear_transactions_post_message_dict = bank_reconciliation_clear_transactions_post_message_instance.to_dict()
# create an instance of BankReconciliationClearTransactionsPostMessage from a dict
bank_reconciliation_clear_transactions_post_message_from_dict = BankReconciliationClearTransactionsPostMessage.from_dict(bank_reconciliation_clear_transactions_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


