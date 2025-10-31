# BankReconciliationStatementBalanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_checks_and_withdrawals** | **float** | Total amount of checks and withdrawals of the reconciliation statement balance. | [optional] 
**total_deposits_and_additions** | **float** | Total amount of deposits and additions of the reconciliation statement balance. | [optional] 
**ending_balance** | **float** | Ending balance of the reconciliation statement balance. | [optional] 
**beginning_balance** | **float** | Beginning balance of the reconciliation statement balance. | [optional] 

## Example

```python
from buildium_sdk.models.bank_reconciliation_statement_balance_message import BankReconciliationStatementBalanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankReconciliationStatementBalanceMessage from a JSON string
bank_reconciliation_statement_balance_message_instance = BankReconciliationStatementBalanceMessage.from_json(json)
# print the JSON string representation of the object
print(BankReconciliationStatementBalanceMessage.to_json())

# convert the object into a dict
bank_reconciliation_statement_balance_message_dict = bank_reconciliation_statement_balance_message_instance.to_dict()
# create an instance of BankReconciliationStatementBalanceMessage from a dict
bank_reconciliation_statement_balance_message_from_dict = BankReconciliationStatementBalanceMessage.from_dict(bank_reconciliation_statement_balance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


