# VideoLinkRequestPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_url** | **str** | The URL of the video. Only Youtube and Vimeo URLs are supported. The URL cannot exceed 255 characters. | 
**show_in_listing** | **bool** | Indicates whether the video will be shown in the listing. | 

## Example

```python
from buildium_sdk.models.video_link_request_post_message import VideoLinkRequestPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VideoLinkRequestPostMessage from a JSON string
video_link_request_post_message_instance = VideoLinkRequestPostMessage.from_json(json)
# print the JSON string representation of the object
print(VideoLinkRequestPostMessage.to_json())

# convert the object into a dict
video_link_request_post_message_dict = video_link_request_post_message_instance.to_dict()
# create an instance of VideoLinkRequestPostMessage from a dict
video_link_request_post_message_from_dict = VideoLinkRequestPostMessage.from_dict(video_link_request_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


