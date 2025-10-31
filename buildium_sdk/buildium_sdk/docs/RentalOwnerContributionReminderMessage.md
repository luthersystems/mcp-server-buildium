# RentalOwnerContributionReminderMessage

Rental owner contribution reminder settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Flag for enabling the reminders. | [optional] 
**recurrence_days** | **int** | Interval of days for the reminder to be sent on. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_contribution_reminder_message import RentalOwnerContributionReminderMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerContributionReminderMessage from a JSON string
rental_owner_contribution_reminder_message_instance = RentalOwnerContributionReminderMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerContributionReminderMessage.to_json())

# convert the object into a dict
rental_owner_contribution_reminder_message_dict = rental_owner_contribution_reminder_message_instance.to_dict()
# create an instance of RentalOwnerContributionReminderMessage from a dict
rental_owner_contribution_reminder_message_from_dict = RentalOwnerContributionReminderMessage.from_dict(rental_owner_contribution_reminder_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


