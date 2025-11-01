# VehicleMessage

This is an object that represents a vehicle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**make** | **str** | Make of the vehicle. | [optional] 
**model** | **str** | Model of the vehicle. | [optional] 
**license_plate_number** | **str** | License plate number of the vehicle. | [optional] 
**parking_pass_number** | **str** | Parking pass number assigned to the vehicle. | [optional] 

## Example

```python
from buildium_sdk.models.vehicle_message import VehicleMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleMessage from a JSON string
vehicle_message_instance = VehicleMessage.from_json(json)
# print the JSON string representation of the object
print(VehicleMessage.to_json())

# convert the object into a dict
vehicle_message_dict = vehicle_message_instance.to_dict()
# create an instance of VehicleMessage from a dict
vehicle_message_from_dict = VehicleMessage.from_dict(vehicle_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


