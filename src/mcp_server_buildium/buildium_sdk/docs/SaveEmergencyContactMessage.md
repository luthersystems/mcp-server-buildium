# SaveEmergencyContactMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is an object that represents an emergency contact. | [optional] 
**relationship_description** | **str** | Emergency contact relationship to the person. | [optional] 
**phone** | **str** | Emergency contact phone number | [optional] 
**email** | **str** | Emergency contact email address. | [optional] 

## Example

```python
from buildium_sdk.models.save_emergency_contact_message import SaveEmergencyContactMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SaveEmergencyContactMessage from a JSON string
save_emergency_contact_message_instance = SaveEmergencyContactMessage.from_json(json)
# print the JSON string representation of the object
print(SaveEmergencyContactMessage.to_json())

# convert the object into a dict
save_emergency_contact_message_dict = save_emergency_contact_message_instance.to_dict()
# create an instance of SaveEmergencyContactMessage from a dict
save_emergency_contact_message_from_dict = SaveEmergencyContactMessage.from_dict(save_emergency_contact_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


