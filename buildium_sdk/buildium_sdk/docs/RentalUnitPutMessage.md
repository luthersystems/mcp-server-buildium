# RentalUnitPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_number** | **str** | Unit number. Must be unique within the rental property and cannot exceed 30 characters. | 
**unit_size** | **int** | Size of the unit. | [optional] 
**market_rent** | **float** | Market rent of the unit. This value is separate from the lease rent and is typically used for rental listings. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Rental unit address. | 
**unit_bedrooms** | **str** | Number of bedrooms in the unit. | [optional] 
**unit_bathrooms** | **str** | Number of bathrooms in the unit. | [optional] 
**description** | **str** | Description of the unit. The description cannot exceed 65,535 characters. | [optional] 

## Example

```python
from buildium_sdk.models.rental_unit_put_message import RentalUnitPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalUnitPutMessage from a JSON string
rental_unit_put_message_instance = RentalUnitPutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalUnitPutMessage.to_json())

# convert the object into a dict
rental_unit_put_message_dict = rental_unit_put_message_instance.to_dict()
# create an instance of RentalUnitPutMessage from a dict
rental_unit_put_message_from_dict = RentalUnitPutMessage.from_dict(rental_unit_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


