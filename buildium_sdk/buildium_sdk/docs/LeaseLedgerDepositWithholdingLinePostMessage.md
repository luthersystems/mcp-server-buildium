# LeaseLedgerDepositWithholdingLinePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | General ledger account identifier under which the line item amount will be recorded. Must be an Income account. | 

## Example

```python
from buildium_sdk.models.lease_ledger_deposit_withholding_line_post_message import LeaseLedgerDepositWithholdingLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerDepositWithholdingLinePostMessage from a JSON string
lease_ledger_deposit_withholding_line_post_message_instance = LeaseLedgerDepositWithholdingLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerDepositWithholdingLinePostMessage.to_json())

# convert the object into a dict
lease_ledger_deposit_withholding_line_post_message_dict = lease_ledger_deposit_withholding_line_post_message_instance.to_dict()
# create an instance of LeaseLedgerDepositWithholdingLinePostMessage from a dict
lease_ledger_deposit_withholding_line_post_message_from_dict = LeaseLedgerDepositWithholdingLinePostMessage.from_dict(lease_ledger_deposit_withholding_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


