# RentalOwnerContributionDataPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contribution_requests** | [**List[RentalOwnerContributionPutMessage]**](RentalOwnerContributionPutMessage.md) | The contribution request details associated with the task. | [optional] 
**reminder_settings** | [**RentalOwnerContributionReminderPutMessage**](RentalOwnerContributionReminderPutMessage.md) | The contribution request reminder settings. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_contribution_data_put_message import RentalOwnerContributionDataPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerContributionDataPutMessage from a JSON string
rental_owner_contribution_data_put_message_instance = RentalOwnerContributionDataPutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerContributionDataPutMessage.to_json())

# convert the object into a dict
rental_owner_contribution_data_put_message_dict = rental_owner_contribution_data_put_message_instance.to_dict()
# create an instance of RentalOwnerContributionDataPutMessage from a dict
rental_owner_contribution_data_put_message_from_dict = RentalOwnerContributionDataPutMessage.from_dict(rental_owner_contribution_data_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


