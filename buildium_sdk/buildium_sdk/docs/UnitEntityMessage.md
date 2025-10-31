# UnitEntityMessage

An object that represents a unit for a building.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unit unique identifier | [optional] 
**href** | **str** | A link to the unit resource. | [optional] 

## Example

```python
from buildium_sdk.models.unit_entity_message import UnitEntityMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UnitEntityMessage from a JSON string
unit_entity_message_instance = UnitEntityMessage.from_json(json)
# print the JSON string representation of the object
print(UnitEntityMessage.to_json())

# convert the object into a dict
unit_entity_message_dict = unit_entity_message_instance.to_dict()
# create an instance of UnitEntityMessage from a dict
unit_entity_message_from_dict = UnitEntityMessage.from_dict(unit_entity_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


