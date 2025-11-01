# GeneralJournalEntryPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_entity** | [**AccountingEntitySaveMessage**](AccountingEntitySaveMessage.md) | A rental property, association or company to associate with the general journal entry. | 
**var_date** | **date** | Date of the general journal entry. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | Description of the general journal entry. Must be no longer than 240 characters. | [optional] 
**lines** | [**List[GeneralJournalEntryLineSaveMessage]**](GeneralJournalEntryLineSaveMessage.md) | A list of general journal entry lines. At least two lines are required. The total amount of the debit PostingType lines must equal the total of the credit PostingType lines. | 

## Example

```python
from buildium_sdk.models.general_journal_entry_post_message import GeneralJournalEntryPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralJournalEntryPostMessage from a JSON string
general_journal_entry_post_message_instance = GeneralJournalEntryPostMessage.from_json(json)
# print the JSON string representation of the object
print(GeneralJournalEntryPostMessage.to_json())

# convert the object into a dict
general_journal_entry_post_message_dict = general_journal_entry_post_message_instance.to_dict()
# create an instance of GeneralJournalEntryPostMessage from a dict
general_journal_entry_post_message_from_dict = GeneralJournalEntryPostMessage.from_dict(general_journal_entry_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


