# ParticipantResourceMessage

The participant in the phone call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates the participant type. | [optional] 
**href** | **str** | A link to the participant resource. | [optional] 

## Example

```python
from buildium_sdk.models.participant_resource_message import ParticipantResourceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantResourceMessage from a JSON string
participant_resource_message_instance = ParticipantResourceMessage.from_json(json)
# print the JSON string representation of the object
print(ParticipantResourceMessage.to_json())

# convert the object into a dict
participant_resource_message_dict = participant_resource_message_instance.to_dict()
# create an instance of ParticipantResourceMessage from a dict
participant_resource_message_from_dict = ParticipantResourceMessage.from_dict(participant_resource_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


