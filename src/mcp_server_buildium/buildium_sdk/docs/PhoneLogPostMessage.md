# PhoneLogPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**PhoneLogParticipantPostMessage**](PhoneLogParticipantPostMessage.md) | The participant in the phone call. | 
**subject** | **str** | Subject of the phone call. This value is restricted to a maximum of 255 characters. | 
**description** | **str** | Description of the phone call. This value is restricted to a maximum of 65,535 characters. | 
**call_date_time** | **datetime** | The date and time the call took place. Time of the phone call must be UTC. Example format: \&quot;2021-01-26T13:59:15Z\&quot; | 

## Example

```python
from buildium_sdk.models.phone_log_post_message import PhoneLogPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneLogPostMessage from a JSON string
phone_log_post_message_instance = PhoneLogPostMessage.from_json(json)
# print the JSON string representation of the object
print(PhoneLogPostMessage.to_json())

# convert the object into a dict
phone_log_post_message_dict = phone_log_post_message_instance.to_dict()
# create an instance of PhoneLogPostMessage from a dict
phone_log_post_message_from_dict = PhoneLogPostMessage.from_dict(phone_log_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


