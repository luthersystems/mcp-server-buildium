# RentScheduleChargePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | The general ledger account identifier under which to record the rent charge. | 
**amount** | **float** | The amount of the rent charge. | 
**memo** | **str** | Memo for the rent charge. | [optional] 
**post_days_in_advance** | **int** | Number of days in advance of the due date to post the rent charge | [optional] 
**next_due_date** | **date** | Indicates the next date the rent charge will be applied. This date will also be used as the start date for the calculating the &#x60;Cycle&#x60; of when to apply the next charge. The date must be formatted as YYYY-MM-DD. | 

## Example

```python
from buildium_sdk.models.rent_schedule_charge_put_message import RentScheduleChargePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentScheduleChargePutMessage from a JSON string
rent_schedule_charge_put_message_instance = RentScheduleChargePutMessage.from_json(json)
# print the JSON string representation of the object
print(RentScheduleChargePutMessage.to_json())

# convert the object into a dict
rent_schedule_charge_put_message_dict = rent_schedule_charge_put_message_instance.to_dict()
# create an instance of RentScheduleChargePutMessage from a dict
rent_schedule_charge_put_message_from_dict = RentScheduleChargePutMessage.from_dict(rent_schedule_charge_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


