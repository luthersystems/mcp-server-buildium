# RentalAppliancePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | **int** | The unit identifier the rental appliance belongs to. Must be within the rental property the appliance is in. | [optional] 
**name** | **str** | The name of the rental appliance. The name cannot exceed 100 characters. | 
**make** | **str** | The make of the rental appliance. The make cannot exceed 30 characters. | [optional] 
**model** | **str** | The model of the rental appliance. The model cannot exceed 30 characters. | [optional] 
**description** | **str** | The description of the rental appliance. The description cannot exceed 500 characters. | [optional] 
**warranty_end_date** | **date** | The end date for the rental appliance&#39;s warranty. The warranty&#39;s end date cannot be before the installed date, if it exists. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.rental_appliance_put_message import RentalAppliancePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalAppliancePutMessage from a JSON string
rental_appliance_put_message_instance = RentalAppliancePutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalAppliancePutMessage.to_json())

# convert the object into a dict
rental_appliance_put_message_dict = rental_appliance_put_message_instance.to_dict()
# create an instance of RentalAppliancePutMessage from a dict
rental_appliance_put_message_from_dict = RentalAppliancePutMessage.from_dict(rental_appliance_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


