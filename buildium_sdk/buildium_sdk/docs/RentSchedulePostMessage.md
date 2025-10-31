# RentSchedulePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Indicates the start of the rent schedule. The date must be formatted as YYYY-MM-DD.  If no rent schedules exist on a lease, this date must match the lease start date. | [optional] 
**rent_cycle** | **str** | Indicates the cadence of when rent charges will be applied. | 
**backdate_charges** | **bool** | Indicates if charges that should have posted prior to the date of Rent creation should be posted immediately with the appropriate dates. | 
**charges** | [**List[RentScheduleChargePostMessage]**](RentScheduleChargePostMessage.md) | List of charges to apply to the lease. | 

## Example

```python
from buildium_sdk.models.rent_schedule_post_message import RentSchedulePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentSchedulePostMessage from a JSON string
rent_schedule_post_message_instance = RentSchedulePostMessage.from_json(json)
# print the JSON string representation of the object
print(RentSchedulePostMessage.to_json())

# convert the object into a dict
rent_schedule_post_message_dict = rent_schedule_post_message_instance.to_dict()
# create an instance of RentSchedulePostMessage from a dict
rent_schedule_post_message_from_dict = RentSchedulePostMessage.from_dict(rent_schedule_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


