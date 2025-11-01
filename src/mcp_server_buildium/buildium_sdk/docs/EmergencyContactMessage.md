# EmergencyContactMessage

This is an object that represents an emergency contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Emergency contact name | [optional] 
**relationship_description** | **str** | Emergency contact relationship to the person. | [optional] 
**phone** | **str** | Emergency contact phone number | [optional] 
**email** | **str** | Emergency contact email address. | [optional] 

## Example

```python
from buildium_sdk.models.emergency_contact_message import EmergencyContactMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EmergencyContactMessage from a JSON string
emergency_contact_message_instance = EmergencyContactMessage.from_json(json)
# print the JSON string representation of the object
print(EmergencyContactMessage.to_json())

# convert the object into a dict
emergency_contact_message_dict = emergency_contact_message_instance.to_dict()
# create an instance of EmergencyContactMessage from a dict
emergency_contact_message_from_dict = EmergencyContactMessage.from_dict(emergency_contact_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


