# GeneralLedgerEntryMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the transaction associated with the entry. | [optional] 
**var_date** | **date** | Date of the transaction. | [optional] 
**description** | **str** | Transaction description. | [optional] 
**amount** | **float** | Entry amount. | [optional] 
**balance** | **float** | The general ledger account balance after this entry was recorded. | [optional] 
**transaction_type** | **str** | Indicates the type of transaction that occurred. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | The accounting entity associated with the transaction. | [optional] 

## Example

```python
from buildium_sdk.models.general_ledger_entry_message import GeneralLedgerEntryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerEntryMessage from a JSON string
general_ledger_entry_message_instance = GeneralLedgerEntryMessage.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerEntryMessage.to_json())

# convert the object into a dict
general_ledger_entry_message_dict = general_ledger_entry_message_instance.to_dict()
# create an instance of GeneralLedgerEntryMessage from a dict
general_ledger_entry_message_from_dict = GeneralLedgerEntryMessage.from_dict(general_ledger_entry_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


