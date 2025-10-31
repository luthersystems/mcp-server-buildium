# BankAccountReconciliationBalancePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_checks_and_withdrawals** | **float** | Total amount of checks and withdrawals of the reconciliation statement balance. | 
**total_deposits_and_additions** | **float** | Total amount of deposits and additions of the reconciliation statement balance. | 
**ending_balance** | **float** | Ending balance of the reconciliation statement balance. | 

## Example

```python
from buildium_sdk.models.bank_account_reconciliation_balance_put_message import BankAccountReconciliationBalancePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountReconciliationBalancePutMessage from a JSON string
bank_account_reconciliation_balance_put_message_instance = BankAccountReconciliationBalancePutMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountReconciliationBalancePutMessage.to_json())

# convert the object into a dict
bank_account_reconciliation_balance_put_message_dict = bank_account_reconciliation_balance_put_message_instance.to_dict()
# create an instance of BankAccountReconciliationBalancePutMessage from a dict
bank_account_reconciliation_balance_put_message_from_dict = BankAccountReconciliationBalancePutMessage.from_dict(bank_account_reconciliation_balance_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


