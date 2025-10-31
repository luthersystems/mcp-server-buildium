# BankAccountReconciliationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Reconciliation unique identifier. | [optional] 
**is_finished** | **bool** | Indicates if reconciliation is completed. | [optional] 
**statement_ending_date** | **date** | Date the reconciliation statement ended. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_reconciliation_message import BankAccountReconciliationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountReconciliationMessage from a JSON string
bank_account_reconciliation_message_instance = BankAccountReconciliationMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountReconciliationMessage.to_json())

# convert the object into a dict
bank_account_reconciliation_message_dict = bank_account_reconciliation_message_instance.to_dict()
# create an instance of BankAccountReconciliationMessage from a dict
bank_account_reconciliation_message_from_dict = BankAccountReconciliationMessage.from_dict(bank_account_reconciliation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


