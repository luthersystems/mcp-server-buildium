# RecurringTransactionLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | The general ledger account unique identifier the recurring transaction is related to. | [optional] 
**amount** | **float** | Amount of the line item. | [optional] 

## Example

```python
from buildium_sdk.models.recurring_transaction_line_message import RecurringTransactionLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringTransactionLineMessage from a JSON string
recurring_transaction_line_message_instance = RecurringTransactionLineMessage.from_json(json)
# print the JSON string representation of the object
print(RecurringTransactionLineMessage.to_json())

# convert the object into a dict
recurring_transaction_line_message_dict = recurring_transaction_line_message_instance.to_dict()
# create an instance of RecurringTransactionLineMessage from a dict
recurring_transaction_line_message_from_dict = RecurringTransactionLineMessage.from_dict(recurring_transaction_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


