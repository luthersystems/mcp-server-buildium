# BillLinePostMessage

Bill line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_entity** | [**AccountingEntitySaveMessage**](AccountingEntitySaveMessage.md) | The accounting entity associated with the bill line item. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. The following general ledger accounts are not valid: Accounts Payable, Accounts Receivable, Undeposited Funds or any general leger account referencing a bank account. | 
**amount** | **float** | Line item amount. | 
**markup** | [**BillMarkupSaveMessage**](BillMarkupSaveMessage.md) | Bill markup. | [optional] 
**memo** | **str** | Memo for the line item. The value cannot exceed 240 characters. | [optional] 

## Example

```python
from buildium_sdk.models.bill_line_post_message import BillLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillLinePostMessage from a JSON string
bill_line_post_message_instance = BillLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(BillLinePostMessage.to_json())

# convert the object into a dict
bill_line_post_message_dict = bill_line_post_message_instance.to_dict()
# create an instance of BillLinePostMessage from a dict
bill_line_post_message_from_dict = BillLinePostMessage.from_dict(bill_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


