# BankReconciliationPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_ending_date** | **date** | Date the reconciliation statement ended. The value must be formatted as YYYY-MM-DD. | 

## Example

```python
from buildium_sdk.models.bank_reconciliation_put_message import BankReconciliationPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankReconciliationPutMessage from a JSON string
bank_reconciliation_put_message_instance = BankReconciliationPutMessage.from_json(json)
# print the JSON string representation of the object
print(BankReconciliationPutMessage.to_json())

# convert the object into a dict
bank_reconciliation_put_message_dict = bank_reconciliation_put_message_instance.to_dict()
# create an instance of BankReconciliationPutMessage from a dict
bank_reconciliation_put_message_from_dict = BankReconciliationPutMessage.from_dict(bank_reconciliation_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


