# AssociationUnitMessage

This object represents a home owners association unit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association unit unique identifier. | [optional] 
**association_id** | **int** | Association unique identifier that the unit belongs to. | [optional] 
**association_name** | **str** | Association name that the unit belongs to. | [optional] 
**unit_number** | **str** | Unit number. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Unit address. | [optional] 
**unit_bedrooms** | **str** | Number of bedrooms in the unit. | [optional] 
**unit_bathrooms** | **str** | Number of bathrooms in the unit. | [optional] 
**unit_size** | **int** | Size of the unit. | [optional] 

## Example

```python
from buildium_sdk.models.association_unit_message import AssociationUnitMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationUnitMessage from a JSON string
association_unit_message_instance = AssociationUnitMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationUnitMessage.to_json())

# convert the object into a dict
association_unit_message_dict = association_unit_message_instance.to_dict()
# create an instance of AssociationUnitMessage from a dict
association_unit_message_from_dict = AssociationUnitMessage.from_dict(association_unit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


