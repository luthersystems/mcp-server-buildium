# NotePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Note contents. The value cannot exceed 65535 characters. | 

## Example

```python
from buildium_sdk.models.note_put_message import NotePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of NotePutMessage from a JSON string
note_put_message_instance = NotePutMessage.from_json(json)
# print the JSON string representation of the object
print(NotePutMessage.to_json())

# convert the object into a dict
note_put_message_dict = note_put_message_instance.to_dict()
# create an instance of NotePutMessage from a dict
note_put_message_from_dict = NotePutMessage.from_dict(note_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


