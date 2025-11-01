# ParticipantMessage

The participant in the phone call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | The unique identifier for the participant entity. | [optional] 
**entity_resources** | [**List[ParticipantResourceMessage]**](ParticipantResourceMessage.md) | A list of the participants entity types and links to the entity resource. Note, that a participant can have more than one type assigned to them. For example, they could be both a vendor and a rental owner. | [optional] 
**unit_agreement** | [**UnitAgreementMessage**](UnitAgreementMessage.md) | The unit agreement associated with the participant. | [optional] 

## Example

```python
from buildium_sdk.models.participant_message import ParticipantMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantMessage from a JSON string
participant_message_instance = ParticipantMessage.from_json(json)
# print the JSON string representation of the object
print(ParticipantMessage.to_json())

# convert the object into a dict
participant_message_dict = participant_message_instance.to_dict()
# create an instance of ParticipantMessage from a dict
participant_message_from_dict = ParticipantMessage.from_dict(participant_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


