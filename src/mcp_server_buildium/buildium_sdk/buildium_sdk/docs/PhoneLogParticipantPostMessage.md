# PhoneLogParticipantPostMessage

The participant in the phone call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of participant entity. | 
**entity_id** | **int** | The unique identifier for the participant entity. | 
**unit_agreement** | [**PhoneLogParticipantUnitAgreementPostMessage**](PhoneLogParticipantUnitAgreementPostMessage.md) | The unit agreement associated with the participant. | [optional] 

## Example

```python
from buildium_sdk.models.phone_log_participant_post_message import PhoneLogParticipantPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneLogParticipantPostMessage from a JSON string
phone_log_participant_post_message_instance = PhoneLogParticipantPostMessage.from_json(json)
# print the JSON string representation of the object
print(PhoneLogParticipantPostMessage.to_json())

# convert the object into a dict
phone_log_participant_post_message_dict = phone_log_participant_post_message_instance.to_dict()
# create an instance of PhoneLogParticipantPostMessage from a dict
phone_log_participant_post_message_from_dict = PhoneLogParticipantPostMessage.from_dict(phone_log_participant_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


