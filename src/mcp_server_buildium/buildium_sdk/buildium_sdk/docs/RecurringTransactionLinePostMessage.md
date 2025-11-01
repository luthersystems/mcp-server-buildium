# RecurringTransactionLinePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. The account must be a liability or income type. | 
**amount** | **float** | Line item amount. | 

## Example

```python
from buildium_sdk.models.recurring_transaction_line_post_message import RecurringTransactionLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringTransactionLinePostMessage from a JSON string
recurring_transaction_line_post_message_instance = RecurringTransactionLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(RecurringTransactionLinePostMessage.to_json())

# convert the object into a dict
recurring_transaction_line_post_message_dict = recurring_transaction_line_post_message_instance.to_dict()
# create an instance of RecurringTransactionLinePostMessage from a dict
recurring_transaction_line_post_message_from_dict = RecurringTransactionLinePostMessage.from_dict(recurring_transaction_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


