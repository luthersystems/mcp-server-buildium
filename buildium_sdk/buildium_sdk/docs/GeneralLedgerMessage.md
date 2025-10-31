# GeneralLedgerMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the entries. | [optional] 
**gl_account_name** | **str** | Name of the general ledger account associated with the entries. | [optional] 
**beginning_balance** | **float** | The general ledger account balance based on the date range requested. | [optional] 
**total_amount** | **float** | The sum of the entry amounts that were recorded under this general ledger account within the date range requested. | [optional] 
**entries** | [**List[GeneralLedgerEntryMessage]**](GeneralLedgerEntryMessage.md) | Entries applied to the general ledger account. | [optional] 

## Example

```python
from buildium_sdk.models.general_ledger_message import GeneralLedgerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerMessage from a JSON string
general_ledger_message_instance = GeneralLedgerMessage.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerMessage.to_json())

# convert the object into a dict
general_ledger_message_dict = general_ledger_message_instance.to_dict()
# create an instance of GeneralLedgerMessage from a dict
general_ledger_message_from_dict = GeneralLedgerMessage.from_dict(general_ledger_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


