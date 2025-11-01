# LeaseLedgerDepositWithholdingLinePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | General ledger account identifier under which the line item amount will be recorded. Must be an Income account. | 

## Example

```python
from buildium_sdk.models.lease_ledger_deposit_withholding_line_put_message import LeaseLedgerDepositWithholdingLinePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerDepositWithholdingLinePutMessage from a JSON string
lease_ledger_deposit_withholding_line_put_message_instance = LeaseLedgerDepositWithholdingLinePutMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerDepositWithholdingLinePutMessage.to_json())

# convert the object into a dict
lease_ledger_deposit_withholding_line_put_message_dict = lease_ledger_deposit_withholding_line_put_message_instance.to_dict()
# create an instance of LeaseLedgerDepositWithholdingLinePutMessage from a dict
lease_ledger_deposit_withholding_line_put_message_from_dict = LeaseLedgerDepositWithholdingLinePutMessage.from_dict(lease_ledger_deposit_withholding_line_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


