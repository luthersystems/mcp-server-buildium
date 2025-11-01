# AssociationUnitPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_number** | **str** | Unit Number. Must be unique within the association and cannot exceed 30 characters. | 
**unit_size** | **int** | Size of the unit. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Unit address. | 
**unit_bedrooms** | **str** | Number of bedrooms in the unit. | [optional] 
**unit_bathrooms** | **str** | Number of bathrooms in the unit. | [optional] 

## Example

```python
from buildium_sdk.models.association_unit_put_message import AssociationUnitPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationUnitPutMessage from a JSON string
association_unit_put_message_instance = AssociationUnitPutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationUnitPutMessage.to_json())

# convert the object into a dict
association_unit_put_message_dict = association_unit_put_message_instance.to_dict()
# create an instance of AssociationUnitPutMessage from a dict
association_unit_put_message_from_dict = AssociationUnitPutMessage.from_dict(association_unit_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


