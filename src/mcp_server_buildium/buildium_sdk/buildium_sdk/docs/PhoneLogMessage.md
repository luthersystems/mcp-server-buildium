# PhoneLogMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Phone log unique identifier. | [optional] 
**participant** | [**ParticipantMessage**](ParticipantMessage.md) | The participant in the phone call. | [optional] 
**logged_by_staff_user** | [**LoggedByStaffUserMessage**](LoggedByStaffUserMessage.md) | The staff member that logged the call. | [optional] 
**subject** | **str** | Subject of the phone call. | [optional] 
**description** | **str** | Description of the phone call. | [optional] 
**call_date_time** | **datetime** | The date and time in UTC of when the call took place. | [optional] 

## Example

```python
from buildium_sdk.models.phone_log_message import PhoneLogMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneLogMessage from a JSON string
phone_log_message_instance = PhoneLogMessage.from_json(json)
# print the JSON string representation of the object
print(PhoneLogMessage.to_json())

# convert the object into a dict
phone_log_message_dict = phone_log_message_instance.to_dict()
# create an instance of PhoneLogMessage from a dict
phone_log_message_from_dict = PhoneLogMessage.from_dict(phone_log_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


