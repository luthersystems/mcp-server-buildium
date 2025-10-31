# GeneralLedgerJournalMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memo** | **str** | Memo associated with the journal. | [optional] 
**lines** | [**List[GeneralLedgerJournalLineMessage]**](GeneralLedgerJournalLineMessage.md) | A collection of line items associated with the journal. | [optional] 

## Example

```python
from buildium_sdk.models.general_ledger_journal_message import GeneralLedgerJournalMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerJournalMessage from a JSON string
general_ledger_journal_message_instance = GeneralLedgerJournalMessage.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerJournalMessage.to_json())

# convert the object into a dict
general_ledger_journal_message_dict = general_ledger_journal_message_instance.to_dict()
# create an instance of GeneralLedgerJournalMessage from a dict
general_ledger_journal_message_from_dict = GeneralLedgerJournalMessage.from_dict(general_ledger_journal_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


