# RentalImagePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the image. The description cannot exceed 100 characters. | [optional] 
**show_in_listing** | **bool** | Indicates whether the image will be shown in listings for this rental. | 

## Example

```python
from buildium_sdk.models.rental_image_put_message import RentalImagePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalImagePutMessage from a JSON string
rental_image_put_message_instance = RentalImagePutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalImagePutMessage.to_json())

# convert the object into a dict
rental_image_put_message_dict = rental_image_put_message_instance.to_dict()
# create an instance of RentalImagePutMessage from a dict
rental_image_put_message_from_dict = RentalImagePutMessage.from_dict(rental_image_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


