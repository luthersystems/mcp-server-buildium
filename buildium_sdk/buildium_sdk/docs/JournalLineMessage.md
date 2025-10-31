# JournalLineMessage

This is an object that represents a line item for a journal entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account** | [**GLAccountMessage**](GLAccountMessage.md) | General ledger account the line item is related to. | [optional] 
**amount** | **float** | Amount of the line item. | [optional] 
**is_cash_posting** | **bool** | Indicates whether the line item is a cash posting. | [optional] 
**reference_number** | **str** | Reference number for the line item. | [optional] 
**memo** | **str** | Memo for the line item. | [optional] 
**property_id** | **int** | PropertyId associated with the line item. | [optional] 
**unit_id** | **int** | UnitId associated with the line item. | [optional] 

## Example

```python
from buildium_sdk.models.journal_line_message import JournalLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JournalLineMessage from a JSON string
journal_line_message_instance = JournalLineMessage.from_json(json)
# print the JSON string representation of the object
print(JournalLineMessage.to_json())

# convert the object into a dict
journal_line_message_dict = journal_line_message_instance.to_dict()
# create an instance of JournalLineMessage from a dict
journal_line_message_from_dict = JournalLineMessage.from_dict(journal_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


