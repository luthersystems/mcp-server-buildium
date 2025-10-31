# ImageReorderRequestPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | Unique identifiers for the images. The request must contain the ids of all images. | 

## Example

```python
from buildium_sdk.models.image_reorder_request_put_message import ImageReorderRequestPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ImageReorderRequestPutMessage from a JSON string
image_reorder_request_put_message_instance = ImageReorderRequestPutMessage.from_json(json)
# print the JSON string representation of the object
print(ImageReorderRequestPutMessage.to_json())

# convert the object into a dict
image_reorder_request_put_message_dict = image_reorder_request_put_message_instance.to_dict()
# create an instance of ImageReorderRequestPutMessage from a dict
image_reorder_request_put_message_from_dict = ImageReorderRequestPutMessage.from_dict(image_reorder_request_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


