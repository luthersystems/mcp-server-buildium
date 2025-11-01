# BankPendingReconciliationPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_ending_date** | **date** | End date for the reconciliation statement period. The date must be formatted as YYYY-MM-DD. | 
**total_checks_and_withdrawals** | **float** | Sum of all checks and withdrawals for the reconciliation. | [optional] 
**total_deposits_and_additions** | **float** | Sum of all deposits and additions for the reconciliation. | [optional] 
**ending_balance** | **float** | Ending balance of the pending reconciliation. | 

## Example

```python
from buildium_sdk.models.bank_pending_reconciliation_post_message import BankPendingReconciliationPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankPendingReconciliationPostMessage from a JSON string
bank_pending_reconciliation_post_message_instance = BankPendingReconciliationPostMessage.from_json(json)
# print the JSON string representation of the object
print(BankPendingReconciliationPostMessage.to_json())

# convert the object into a dict
bank_pending_reconciliation_post_message_dict = bank_pending_reconciliation_post_message_instance.to_dict()
# create an instance of BankPendingReconciliationPostMessage from a dict
bank_pending_reconciliation_post_message_from_dict = BankPendingReconciliationPostMessage.from_dict(bank_pending_reconciliation_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


