# OwnershipAccountLedgerChargeMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Charge unique identifier. | [optional] 
**var_date** | **date** | Date of the charge. | [optional] 
**total_amount** | **float** | Sum of all &#x60;Lines.Amount&#x60; entries in the charge. | [optional] 
**memo** | **str** | Memo associated with the charge. | [optional] 
**bill_id** | **int** | The bill identifier this charge is associated with, if applicable. | [optional] 
**lines** | [**List[OwnershipAccountLedgerChargeLineMessage]**](OwnershipAccountLedgerChargeLineMessage.md) | A collection of line items associated with the charge. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_ledger_charge_message import OwnershipAccountLedgerChargeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountLedgerChargeMessage from a JSON string
ownership_account_ledger_charge_message_instance = OwnershipAccountLedgerChargeMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountLedgerChargeMessage.to_json())

# convert the object into a dict
ownership_account_ledger_charge_message_dict = ownership_account_ledger_charge_message_instance.to_dict()
# create an instance of OwnershipAccountLedgerChargeMessage from a dict
ownership_account_ledger_charge_message_from_dict = OwnershipAccountLedgerChargeMessage.from_dict(ownership_account_ledger_charge_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


