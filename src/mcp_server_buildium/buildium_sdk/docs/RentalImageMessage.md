# RentalImageMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rental image unique identifier. | [optional] 
**description** | **str** | Description of the image. | [optional] 
**physical_file_name** | **str** | Physical name of the file on the server. | [optional] 
**provider** | **str** | The provider for the image. If an external provider is not used to host the image, this will be set to &#x60;None&#x60;. | [optional] 
**show_in_listing** | **bool** | Indicates whether the image will be shown in listings for this rental. | [optional] 

## Example

```python
from buildium_sdk.models.rental_image_message import RentalImageMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalImageMessage from a JSON string
rental_image_message_instance = RentalImageMessage.from_json(json)
# print the JSON string representation of the object
print(RentalImageMessage.to_json())

# convert the object into a dict
rental_image_message_dict = rental_image_message_instance.to_dict()
# create an instance of RentalImageMessage from a dict
rental_image_message_from_dict = RentalImageMessage.from_dict(rental_image_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


