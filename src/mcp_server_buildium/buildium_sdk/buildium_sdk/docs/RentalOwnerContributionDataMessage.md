# RentalOwnerContributionDataMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contribution_requests** | [**List[RentalOwnerContributionMessage]**](RentalOwnerContributionMessage.md) | The contribution request details associated with the task. | [optional] 
**reminder_settings** | [**RentalOwnerContributionReminderMessage**](RentalOwnerContributionReminderMessage.md) | The contribution request reminder settings. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_contribution_data_message import RentalOwnerContributionDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerContributionDataMessage from a JSON string
rental_owner_contribution_data_message_instance = RentalOwnerContributionDataMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerContributionDataMessage.to_json())

# convert the object into a dict
rental_owner_contribution_data_message_dict = rental_owner_contribution_data_message_instance.to_dict()
# create an instance of RentalOwnerContributionDataMessage from a dict
rental_owner_contribution_data_message_from_dict = RentalOwnerContributionDataMessage.from_dict(rental_owner_contribution_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


