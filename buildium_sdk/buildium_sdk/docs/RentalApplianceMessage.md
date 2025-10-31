# RentalApplianceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Appliance unique identifier. | [optional] 
**property_id** | **int** | Rental property unique identifier that the appliance belongs to. | [optional] 
**unit_id** | **int** | Rental unit unique identifier that the appliance belongs to. | [optional] 
**name** | **str** | Name of the appliance. | [optional] 
**make** | **str** | Make of the appliance. | [optional] 
**model** | **str** | Model of the appliance. | [optional] 
**description** | **str** | Description of the appliance. | [optional] 
**warranty_end_date** | **date** | Warranty end date of the appliance. | [optional] 

## Example

```python
from buildium_sdk.models.rental_appliance_message import RentalApplianceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalApplianceMessage from a JSON string
rental_appliance_message_instance = RentalApplianceMessage.from_json(json)
# print the JSON string representation of the object
print(RentalApplianceMessage.to_json())

# convert the object into a dict
rental_appliance_message_dict = rental_appliance_message_instance.to_dict()
# create an instance of RentalApplianceMessage from a dict
rental_appliance_message_from_dict = RentalApplianceMessage.from_dict(rental_appliance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


