# RentalAppliancePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | Rental property unique identifier that the appliance belongs to. | 
**unit_id** | **int** | Rental unit unique identifier that the appliance belongs to. | [optional] 
**name** | **str** | The name of the appliance. The name cannot exceed 100 characters. | 
**make** | **str** | The make of the appliance. The make cannot exceed 30 characters. | [optional] 
**model** | **str** | The model of the appliance. The model cannot exceed 30 characters. | [optional] 
**description** | **str** | The description of the appliance. The description cannot exceed 500 characters. | [optional] 
**install_date** | **date** | The install date for the appliance&#39;s warranty. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**warranty_end_date** | **date** | The end date for the appliance&#39;s warranty. The warranty&#39;s end date cannot be before the installed date, if it exists. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.rental_appliance_post_message import RentalAppliancePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalAppliancePostMessage from a JSON string
rental_appliance_post_message_instance = RentalAppliancePostMessage.from_json(json)
# print the JSON string representation of the object
print(RentalAppliancePostMessage.to_json())

# convert the object into a dict
rental_appliance_post_message_dict = rental_appliance_post_message_instance.to_dict()
# create an instance of RentalAppliancePostMessage from a dict
rental_appliance_post_message_from_dict = RentalAppliancePostMessage.from_dict(rental_appliance_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


