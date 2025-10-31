# BankReconciliationUnclearTransactionsPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[int]** | The transaction identifiers to un-clear for the reconciliation | 

## Example

```python
from buildium_sdk.models.bank_reconciliation_unclear_transactions_post_message import BankReconciliationUnclearTransactionsPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankReconciliationUnclearTransactionsPostMessage from a JSON string
bank_reconciliation_unclear_transactions_post_message_instance = BankReconciliationUnclearTransactionsPostMessage.from_json(json)
# print the JSON string representation of the object
print(BankReconciliationUnclearTransactionsPostMessage.to_json())

# convert the object into a dict
bank_reconciliation_unclear_transactions_post_message_dict = bank_reconciliation_unclear_transactions_post_message_instance.to_dict()
# create an instance of BankReconciliationUnclearTransactionsPostMessage from a dict
bank_reconciliation_unclear_transactions_post_message_from_dict = BankReconciliationUnclearTransactionsPostMessage.from_dict(bank_reconciliation_unclear_transactions_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


