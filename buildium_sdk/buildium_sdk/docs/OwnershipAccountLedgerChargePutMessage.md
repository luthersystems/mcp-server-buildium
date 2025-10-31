# OwnershipAccountLedgerChargePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the charge. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | Memo associated with the charge. The value cannot exceed 65 characters. | [optional] 
**lines** | [**List[OwnershipAccountLedgerChargeLinesPutMessage]**](OwnershipAccountLedgerChargeLinesPutMessage.md) | A collection of line items included in the charge. At least one line item is required. | 

## Example

```python
from buildium_sdk.models.ownership_account_ledger_charge_put_message import OwnershipAccountLedgerChargePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountLedgerChargePutMessage from a JSON string
ownership_account_ledger_charge_put_message_instance = OwnershipAccountLedgerChargePutMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountLedgerChargePutMessage.to_json())

# convert the object into a dict
ownership_account_ledger_charge_put_message_dict = ownership_account_ledger_charge_put_message_instance.to_dict()
# create an instance of OwnershipAccountLedgerChargePutMessage from a dict
ownership_account_ledger_charge_put_message_from_dict = OwnershipAccountLedgerChargePutMessage.from_dict(ownership_account_ledger_charge_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


