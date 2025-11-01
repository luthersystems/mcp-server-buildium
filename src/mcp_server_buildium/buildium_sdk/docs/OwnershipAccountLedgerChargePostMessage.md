# OwnershipAccountLedgerChargePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the charge. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | Memo associated with the charge. The value cannot exceed 65 characters. | [optional] 
**bill_id** | **int** | Unique identifier of the bill this charge is associated to. If provided, the property of the  ownership account ledger the charge is being created in must be in at least one line item of the bill. | [optional] 
**lines** | [**List[OwnershipAccountLedgerChargeLinesSaveMessage]**](OwnershipAccountLedgerChargeLinesSaveMessage.md) | Collection of line items to be included in the charge. All existing line items will be deleted and replaced with the line items in this request. At least 1 line item is required. | 

## Example

```python
from buildium_sdk.models.ownership_account_ledger_charge_post_message import OwnershipAccountLedgerChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountLedgerChargePostMessage from a JSON string
ownership_account_ledger_charge_post_message_instance = OwnershipAccountLedgerChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountLedgerChargePostMessage.to_json())

# convert the object into a dict
ownership_account_ledger_charge_post_message_dict = ownership_account_ledger_charge_post_message_instance.to_dict()
# create an instance of OwnershipAccountLedgerChargePostMessage from a dict
ownership_account_ledger_charge_post_message_from_dict = OwnershipAccountLedgerChargePostMessage.from_dict(ownership_account_ledger_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


