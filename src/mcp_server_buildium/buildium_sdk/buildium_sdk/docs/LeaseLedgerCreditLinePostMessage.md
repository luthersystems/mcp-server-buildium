# LeaseLedgerCreditLinePostMessage

Credit line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. The account must be a liability or income type. | 

## Example

```python
from buildium_sdk.models.lease_ledger_credit_line_post_message import LeaseLedgerCreditLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerCreditLinePostMessage from a JSON string
lease_ledger_credit_line_post_message_instance = LeaseLedgerCreditLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerCreditLinePostMessage.to_json())

# convert the object into a dict
lease_ledger_credit_line_post_message_dict = lease_ledger_credit_line_post_message_instance.to_dict()
# create an instance of LeaseLedgerCreditLinePostMessage from a dict
lease_ledger_credit_line_post_message_from_dict = LeaseLedgerCreditLinePostMessage.from_dict(lease_ledger_credit_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


