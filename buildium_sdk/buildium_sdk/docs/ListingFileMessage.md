# ListingFileMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates the media type of file. | [optional] 
**name** | **str** | The name of the file. | [optional] 
**url** | **str** | The the full URL to access the file. | [optional] 

## Example

```python
from buildium_sdk.models.listing_file_message import ListingFileMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingFileMessage from a JSON string
listing_file_message_instance = ListingFileMessage.from_json(json)
# print the JSON string representation of the object
print(ListingFileMessage.to_json())

# convert the object into a dict
listing_file_message_dict = listing_file_message_instance.to_dict()
# create an instance of ListingFileMessage from a dict
listing_file_message_from_dict = ListingFileMessage.from_dict(listing_file_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


