# RentalApplianceServiceHistoryPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** | Specifies the type of service that occured. | 
**var_date** | **date** | Date the service was performed. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | 
**details** | **str** | The service history details associated with the appliance. The description cannot exceed 100 characters. | [optional] 

## Example

```python
from buildium_sdk.models.rental_appliance_service_history_post_message import RentalApplianceServiceHistoryPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalApplianceServiceHistoryPostMessage from a JSON string
rental_appliance_service_history_post_message_instance = RentalApplianceServiceHistoryPostMessage.from_json(json)
# print the JSON string representation of the object
print(RentalApplianceServiceHistoryPostMessage.to_json())

# convert the object into a dict
rental_appliance_service_history_post_message_dict = rental_appliance_service_history_post_message_instance.to_dict()
# create an instance of RentalApplianceServiceHistoryPostMessage from a dict
rental_appliance_service_history_post_message_from_dict = RentalApplianceServiceHistoryPostMessage.from_dict(rental_appliance_service_history_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


