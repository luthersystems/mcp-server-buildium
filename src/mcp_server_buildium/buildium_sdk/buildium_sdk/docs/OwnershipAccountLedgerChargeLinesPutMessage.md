# OwnershipAccountLedgerChargeLinesPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. The account must be a liability or income type. | 
**reference_number** | **str** | Reference number associated with the charge. The value cannot exceed 30 characters. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_ledger_charge_lines_put_message import OwnershipAccountLedgerChargeLinesPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountLedgerChargeLinesPutMessage from a JSON string
ownership_account_ledger_charge_lines_put_message_instance = OwnershipAccountLedgerChargeLinesPutMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountLedgerChargeLinesPutMessage.to_json())

# convert the object into a dict
ownership_account_ledger_charge_lines_put_message_dict = ownership_account_ledger_charge_lines_put_message_instance.to_dict()
# create an instance of OwnershipAccountLedgerChargeLinesPutMessage from a dict
ownership_account_ledger_charge_lines_put_message_from_dict = OwnershipAccountLedgerChargeLinesPutMessage.from_dict(ownership_account_ledger_charge_lines_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


