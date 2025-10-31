# ContactDetailMessage

Contact information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Contact first name. | [optional] 
**last_name** | **str** | Contact last name. | [optional] 
**email** | **str** | Contact email. | [optional] 
**phone_numbers** | [**ContactDetailPhoneMessage**](ContactDetailPhoneMessage.md) | Contact phone numbers. | [optional] 

## Example

```python
from buildium_sdk.models.contact_detail_message import ContactDetailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailMessage from a JSON string
contact_detail_message_instance = ContactDetailMessage.from_json(json)
# print the JSON string representation of the object
print(ContactDetailMessage.to_json())

# convert the object into a dict
contact_detail_message_dict = contact_detail_message_instance.to_dict()
# create an instance of ContactDetailMessage from a dict
contact_detail_message_from_dict = ContactDetailMessage.from_dict(contact_detail_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


