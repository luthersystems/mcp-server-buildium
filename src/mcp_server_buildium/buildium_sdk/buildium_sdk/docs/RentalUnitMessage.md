# RentalUnitMessage

This object represents a rental property unit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rental unit unique identifier. | [optional] 
**property_id** | **int** | Rental property unique identifier that the unit belongs to. | [optional] 
**building_name** | **str** | Building name that the unit belongs to. | [optional] 
**unit_number** | **str** | Unit number. | [optional] 
**description** | **str** | Description of the unit. | [optional] 
**market_rent** | **float** | Market rent of the unit. This value is separate from the lease rent and is typically used for rental listings. Null if no value is set. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the unit. | [optional] 
**unit_bedrooms** | **str** | Number of bedrooms in the unit. Null if no value is set. | [optional] 
**unit_bathrooms** | **str** | Number of bathrooms in the unit. Null if no value is set. | [optional] 
**unit_size** | **int** | Size of the unit. Null if no value is set. | [optional] 
**is_unit_listed** | **bool** | Whether the unit is currently listed for rent.                Note: this value is transient and determined at query time based on whether an active listing exists for the unit. Because this value is not persisted in the database, changes to value are not reflected in the last updated date for the unit. | [optional] 
**is_unit_occupied** | **bool** | Whether the unit is currently being rented by a tenent.                Note: this value is transient and determined at query time based on whether an active lease exists for the unit. Because this value is not persisted in the database, changes to value are not reflected in the last updated date for the unit. | [optional] 

## Example

```python
from buildium_sdk.models.rental_unit_message import RentalUnitMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalUnitMessage from a JSON string
rental_unit_message_instance = RentalUnitMessage.from_json(json)
# print the JSON string representation of the object
print(RentalUnitMessage.to_json())

# convert the object into a dict
rental_unit_message_dict = rental_unit_message_instance.to_dict()
# create an instance of RentalUnitMessage from a dict
rental_unit_message_from_dict = RentalUnitMessage.from_dict(rental_unit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


