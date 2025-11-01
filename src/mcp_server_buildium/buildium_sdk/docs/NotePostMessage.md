# NotePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Note contents. The value cannot exceed 65535 characters. | 

## Example

```python
from buildium_sdk.models.note_post_message import NotePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of NotePostMessage from a JSON string
note_post_message_instance = NotePostMessage.from_json(json)
# print the JSON string representation of the object
print(NotePostMessage.to_json())

# convert the object into a dict
note_post_message_dict = note_post_message_instance.to_dict()
# create an instance of NotePostMessage from a dict
note_post_message_from_dict = NotePostMessage.from_dict(note_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


