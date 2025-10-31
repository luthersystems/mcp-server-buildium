# BankReconciliationClearedBalanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_checks_and_withdrawals** | **float** | Total amount of checks and withdrawals of the reconciliation cleared balance. | [optional] 
**total_deposits_and_additions** | **float** | Total amount of deposits and additions of the reconciliation cleared balance. | [optional] 
**ending_balance** | **float** | Ending balance of the reconciliation cleared balance. | [optional] 
**beginning_balance** | **float** | Beginning balance of the reconciliation cleared balance. | [optional] 

## Example

```python
from buildium_sdk.models.bank_reconciliation_cleared_balance_message import BankReconciliationClearedBalanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankReconciliationClearedBalanceMessage from a JSON string
bank_reconciliation_cleared_balance_message_instance = BankReconciliationClearedBalanceMessage.from_json(json)
# print the JSON string representation of the object
print(BankReconciliationClearedBalanceMessage.to_json())

# convert the object into a dict
bank_reconciliation_cleared_balance_message_dict = bank_reconciliation_cleared_balance_message_instance.to_dict()
# create an instance of BankReconciliationClearedBalanceMessage from a dict
bank_reconciliation_cleared_balance_message_from_dict = BankReconciliationClearedBalanceMessage.from_dict(bank_reconciliation_cleared_balance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


