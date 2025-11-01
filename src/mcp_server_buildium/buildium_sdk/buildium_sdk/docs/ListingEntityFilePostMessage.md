# ListingEntityFilePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Name of file being uploaded. The value can not exceed 255 characters. | 
**description** | **str** | A description of the file. The value cannot exceed 100 characters. | [optional] 
**show_in_listing** | **bool** | Indicates whether the image will be shown in listings. | 

## Example

```python
from buildium_sdk.models.listing_entity_file_post_message import ListingEntityFilePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingEntityFilePostMessage from a JSON string
listing_entity_file_post_message_instance = ListingEntityFilePostMessage.from_json(json)
# print the JSON string representation of the object
print(ListingEntityFilePostMessage.to_json())

# convert the object into a dict
listing_entity_file_post_message_dict = listing_entity_file_post_message_instance.to_dict()
# create an instance of ListingEntityFilePostMessage from a dict
listing_entity_file_post_message_from_dict = ListingEntityFilePostMessage.from_dict(listing_entity_file_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


