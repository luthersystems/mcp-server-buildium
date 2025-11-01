# BankAccountReconciliationBalanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difference** | **float** | Difference between beginning balance and ending balance of the reconciliation. | [optional] 
**statement_balance** | [**BankReconciliationStatementBalanceMessage**](BankReconciliationStatementBalanceMessage.md) | Statement balance of the reconciliation. | [optional] 
**cleared_balance** | [**BankReconciliationClearedBalanceMessage**](BankReconciliationClearedBalanceMessage.md) | Cleared balance of the reconciliation. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_reconciliation_balance_message import BankAccountReconciliationBalanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountReconciliationBalanceMessage from a JSON string
bank_account_reconciliation_balance_message_instance = BankAccountReconciliationBalanceMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountReconciliationBalanceMessage.to_json())

# convert the object into a dict
bank_account_reconciliation_balance_message_dict = bank_account_reconciliation_balance_message_instance.to_dict()
# create an instance of BankAccountReconciliationBalanceMessage from a dict
bank_account_reconciliation_balance_message_from_dict = BankAccountReconciliationBalanceMessage.from_dict(bank_account_reconciliation_balance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


