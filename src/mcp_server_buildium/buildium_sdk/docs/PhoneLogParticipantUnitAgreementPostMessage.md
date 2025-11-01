# PhoneLogParticipantUnitAgreementPostMessage

The unit agreement associated with the participant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unit agreement unique identifier. Note, if a value is provided in this field then &#x60;Type&#x60; must also be provided. | [optional] 
**type** | **str** | The type of unit agreement. Note, this field is required if a value is provided for the &#x60;Id&#x60; field. | [optional] 

## Example

```python
from buildium_sdk.models.phone_log_participant_unit_agreement_post_message import PhoneLogParticipantUnitAgreementPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneLogParticipantUnitAgreementPostMessage from a JSON string
phone_log_participant_unit_agreement_post_message_instance = PhoneLogParticipantUnitAgreementPostMessage.from_json(json)
# print the JSON string representation of the object
print(PhoneLogParticipantUnitAgreementPostMessage.to_json())

# convert the object into a dict
phone_log_participant_unit_agreement_post_message_dict = phone_log_participant_unit_agreement_post_message_instance.to_dict()
# create an instance of PhoneLogParticipantUnitAgreementPostMessage from a dict
phone_log_participant_unit_agreement_post_message_from_dict = PhoneLogParticipantUnitAgreementPostMessage.from_dict(phone_log_participant_unit_agreement_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


