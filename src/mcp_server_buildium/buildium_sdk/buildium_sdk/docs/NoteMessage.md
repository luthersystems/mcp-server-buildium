# NoteMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Note unique identifier. | [optional] 
**note** | **str** | Note contents. | [optional] 
**last_updated_by_user** | [**LastUpdatedByUserMessage**](LastUpdatedByUserMessage.md) | User who most recently updated the note. | [optional] 

## Example

```python
from buildium_sdk.models.note_message import NoteMessage

# TODO update the JSON string below
json = "{}"
# create an instance of NoteMessage from a JSON string
note_message_instance = NoteMessage.from_json(json)
# print the JSON string representation of the object
print(NoteMessage.to_json())

# convert the object into a dict
note_message_dict = note_message_instance.to_dict()
# create an instance of NoteMessage from a dict
note_message_from_dict = NoteMessage.from_dict(note_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


