# RentalUnitImagePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the image. The description cannot exceed 100 characters. | [optional] 
**show_in_listing** | **bool** | Indicates whether the image will be shown in listings for this unit. | 

## Example

```python
from buildium_sdk.models.rental_unit_image_put_message import RentalUnitImagePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalUnitImagePutMessage from a JSON string
rental_unit_image_put_message_instance = RentalUnitImagePutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalUnitImagePutMessage.to_json())

# convert the object into a dict
rental_unit_image_put_message_dict = rental_unit_image_put_message_instance.to_dict()
# create an instance of RentalUnitImagePutMessage from a dict
rental_unit_image_put_message_from_dict = RentalUnitImagePutMessage.from_dict(rental_unit_image_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


