# AssociationOwnerUnitOccupancyPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_occupied** | **bool** | Indicates whether the unit is occupied by the association owner. | 

## Example

```python
from buildium_sdk.models.association_owner_unit_occupancy_put_message import AssociationOwnerUnitOccupancyPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnerUnitOccupancyPutMessage from a JSON string
association_owner_unit_occupancy_put_message_instance = AssociationOwnerUnitOccupancyPutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnerUnitOccupancyPutMessage.to_json())

# convert the object into a dict
association_owner_unit_occupancy_put_message_dict = association_owner_unit_occupancy_put_message_instance.to_dict()
# create an instance of AssociationOwnerUnitOccupancyPutMessage from a dict
association_owner_unit_occupancy_put_message_from_dict = AssociationOwnerUnitOccupancyPutMessage.from_dict(association_owner_unit_occupancy_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


