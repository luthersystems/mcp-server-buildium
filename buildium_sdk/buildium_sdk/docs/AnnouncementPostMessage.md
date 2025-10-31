# AnnouncementPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The subject of the announcement. Note, this will only show up in announcements sent via email and in the Resident Center. The value cannot exceed 100 characters. | 
**body** | **str** | The content of the announcement. The value cannot exceed 65535 characters. Note: if your message is over 140 characters, the announcement will not be sent via SMS. Announcement texts are available for US numbers only. | 
**expiration_date** | **date** | Optional date that indicates when the announcement should be removed from the Resident Center. If no date is provided the announcement will appear indefinitely The date must be formatted as YYYY-MM-DD. | [optional] 
**notify_association_tenants** | **bool** | Indicates whether to include notifying the association tenants in addition to the association owners when publishing the announcement. Note this is only pertains to announcements sent to residents of &#x60;Association&#x60; properties. | 
**include_alternate_email** | **bool** | Indicates whether to send the announcement to alternate emails in addition to the main email addresses when publishing the announcement. | 
**property_ids** | **List[int]** | A list of association and/or rental property unique identifiers whose residents should receive the announcement. | 

## Example

```python
from buildium_sdk.models.announcement_post_message import AnnouncementPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementPostMessage from a JSON string
announcement_post_message_instance = AnnouncementPostMessage.from_json(json)
# print the JSON string representation of the object
print(AnnouncementPostMessage.to_json())

# convert the object into a dict
announcement_post_message_dict = announcement_post_message_instance.to_dict()
# create an instance of AnnouncementPostMessage from a dict
announcement_post_message_from_dict = AnnouncementPostMessage.from_dict(announcement_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


