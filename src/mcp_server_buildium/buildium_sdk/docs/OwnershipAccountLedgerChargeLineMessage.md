# OwnershipAccountLedgerChargeLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | [optional] 
**gl_account_id** | **int** | Unique ientifier of the general ledger account associated with the charge. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_ledger_charge_line_message import OwnershipAccountLedgerChargeLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountLedgerChargeLineMessage from a JSON string
ownership_account_ledger_charge_line_message_instance = OwnershipAccountLedgerChargeLineMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountLedgerChargeLineMessage.to_json())

# convert the object into a dict
ownership_account_ledger_charge_line_message_dict = ownership_account_ledger_charge_line_message_instance.to_dict()
# create an instance of OwnershipAccountLedgerChargeLineMessage from a dict
ownership_account_ledger_charge_line_message_from_dict = OwnershipAccountLedgerChargeLineMessage.from_dict(ownership_account_ledger_charge_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


