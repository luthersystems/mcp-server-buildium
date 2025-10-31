# AnnouncementSenderMessage

The Buildium user who published the announcement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the user who sent the announcement. | [optional] 
**display_name** | **str** | Display name of the user who sent the announcement. | [optional] 
**href** | **str** | A link to the user resource. | [optional] 

## Example

```python
from buildium_sdk.models.announcement_sender_message import AnnouncementSenderMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementSenderMessage from a JSON string
announcement_sender_message_instance = AnnouncementSenderMessage.from_json(json)
# print the JSON string representation of the object
print(AnnouncementSenderMessage.to_json())

# convert the object into a dict
announcement_sender_message_dict = announcement_sender_message_instance.to_dict()
# create an instance of AnnouncementSenderMessage from a dict
announcement_sender_message_from_dict = AnnouncementSenderMessage.from_dict(announcement_sender_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


