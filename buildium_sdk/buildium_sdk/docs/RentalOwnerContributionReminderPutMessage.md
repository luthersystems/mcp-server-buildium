# RentalOwnerContributionReminderPutMessage

Rental owner contribution reminder settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Flag for enabling the reminders. | [optional] 
**recurrence_days** | **int** | Interval of days for the reminder to be sent on. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_contribution_reminder_put_message import RentalOwnerContributionReminderPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerContributionReminderPutMessage from a JSON string
rental_owner_contribution_reminder_put_message_instance = RentalOwnerContributionReminderPutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerContributionReminderPutMessage.to_json())

# convert the object into a dict
rental_owner_contribution_reminder_put_message_dict = rental_owner_contribution_reminder_put_message_instance.to_dict()
# create an instance of RentalOwnerContributionReminderPutMessage from a dict
rental_owner_contribution_reminder_put_message_from_dict = RentalOwnerContributionReminderPutMessage.from_dict(rental_owner_contribution_reminder_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


