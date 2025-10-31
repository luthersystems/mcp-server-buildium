# AssociationOwnerUnitOccupancyStatusMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | **int** | Association unit unique identifier. | [optional] 
**is_occupied** | **bool** | Indicates whether the unit is occupied by the association owner. | [optional] 

## Example

```python
from buildium_sdk.models.association_owner_unit_occupancy_status_message import AssociationOwnerUnitOccupancyStatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnerUnitOccupancyStatusMessage from a JSON string
association_owner_unit_occupancy_status_message_instance = AssociationOwnerUnitOccupancyStatusMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnerUnitOccupancyStatusMessage.to_json())

# convert the object into a dict
association_owner_unit_occupancy_status_message_dict = association_owner_unit_occupancy_status_message_instance.to_dict()
# create an instance of AssociationOwnerUnitOccupancyStatusMessage from a dict
association_owner_unit_occupancy_status_message_from_dict = AssociationOwnerUnitOccupancyStatusMessage.from_dict(association_owner_unit_occupancy_status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


