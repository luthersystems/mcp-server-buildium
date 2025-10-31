# GeneralJournalEntryLineSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. Query the General Ledger Account endpoint &lt;a href&#x3D;\&quot;#operation/AccountingExternalApi_GetAllGLAccounts\&quot;&gt;Get All GLAccounts&lt;/a&gt; for a listing of available accounts. | 
**memo** | **str** | Memo for the line item. | [optional] 
**posting_type** | **str** | The posting type for the line item. | 
**amount** | **float** | Amount of the line item. | 

## Example

```python
from buildium_sdk.models.general_journal_entry_line_save_message import GeneralJournalEntryLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralJournalEntryLineSaveMessage from a JSON string
general_journal_entry_line_save_message_instance = GeneralJournalEntryLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(GeneralJournalEntryLineSaveMessage.to_json())

# convert the object into a dict
general_journal_entry_line_save_message_dict = general_journal_entry_line_save_message_instance.to_dict()
# create an instance of GeneralJournalEntryLineSaveMessage from a dict
general_journal_entry_line_save_message_from_dict = GeneralJournalEntryLineSaveMessage.from_dict(general_journal_entry_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


