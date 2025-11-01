# JournalMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memo** | **str** | Memo associated with the journal. | [optional] 
**lines** | [**List[JournalLineMessage]**](JournalLineMessage.md) | A collection of line items associated with the journal. | [optional] 

## Example

```python
from buildium_sdk.models.journal_message import JournalMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JournalMessage from a JSON string
journal_message_instance = JournalMessage.from_json(json)
# print the JSON string representation of the object
print(JournalMessage.to_json())

# convert the object into a dict
journal_message_dict = journal_message_instance.to_dict()
# create an instance of JournalMessage from a dict
journal_message_from_dict = JournalMessage.from_dict(journal_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


