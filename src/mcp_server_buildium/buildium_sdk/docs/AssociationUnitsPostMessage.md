# AssociationUnitsPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_number** | **str** | Unit number. Must be unique within the association and cannot exceed 30 characters. | 
**association_id** | **int** | Association unique identifier that the unit belongs to. | 
**unit_size** | **int** | Size of the unit. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Unit address. | 
**unit_bedrooms** | **str** | Number of bedrooms in the unit. | [optional] 
**unit_bathrooms** | **str** | Number of bathrooms in the unit. | [optional] 

## Example

```python
from buildium_sdk.models.association_units_post_message import AssociationUnitsPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationUnitsPostMessage from a JSON string
association_units_post_message_instance = AssociationUnitsPostMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationUnitsPostMessage.to_json())

# convert the object into a dict
association_units_post_message_dict = association_units_post_message_instance.to_dict()
# create an instance of AssociationUnitsPostMessage from a dict
association_units_post_message_from_dict = AssociationUnitsPostMessage.from_dict(association_units_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


