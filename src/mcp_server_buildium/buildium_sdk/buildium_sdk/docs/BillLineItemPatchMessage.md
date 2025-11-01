# BillLineItemPatchMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bill line item unique identifier. | [optional] 
**accounting_entity** | [**AccountingEntityPatchMessage**](AccountingEntityPatchMessage.md) | The accounting entity associated with the bill line item. | [optional] 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. The following general ledger accounts are not valid: Accounts Payable, Accounts Receivable, Undeposited Funds or any general leger account referencing a bank account. | [optional] 
**amount** | **float** | Line item amount. | [optional] 
**markup** | [**BillMarkupPatchMessage**](BillMarkupPatchMessage.md) | Bill markup. | [optional] 
**memo** | **str** | Memo for the line item. The value cannot exceed 240 characters. | [optional] 

## Example

```python
from buildium_sdk.models.bill_line_item_patch_message import BillLineItemPatchMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillLineItemPatchMessage from a JSON string
bill_line_item_patch_message_instance = BillLineItemPatchMessage.from_json(json)
# print the JSON string representation of the object
print(BillLineItemPatchMessage.to_json())

# convert the object into a dict
bill_line_item_patch_message_dict = bill_line_item_patch_message_instance.to_dict()
# create an instance of BillLineItemPatchMessage from a dict
bill_line_item_patch_message_from_dict = BillLineItemPatchMessage.from_dict(bill_line_item_patch_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


