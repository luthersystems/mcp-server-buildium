# AnnouncementMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the announcement. | [optional] 
**subject** | **str** | Subject line of the announcement. | [optional] 
**body** | **str** | Content of the announcement. | [optional] 
**announcement_date** | **date** | Date the announcement was published. | [optional] 
**expiration_date** | **date** | Indicates the date on which the announcement will be removed from the Resident Center. | [optional] 
**channels** | **List[str]** | List of the distribution channels the announcement was sent through. | [optional] 
**sender** | [**AnnouncementSenderMessage**](AnnouncementSenderMessage.md) | The Buildium user who published the announcement. | [optional] 

## Example

```python
from buildium_sdk.models.announcement_message import AnnouncementMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementMessage from a JSON string
announcement_message_instance = AnnouncementMessage.from_json(json)
# print the JSON string representation of the object
print(AnnouncementMessage.to_json())

# convert the object into a dict
announcement_message_dict = announcement_message_instance.to_dict()
# create an instance of AnnouncementMessage from a dict
announcement_message_from_dict = AnnouncementMessage.from_dict(announcement_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


