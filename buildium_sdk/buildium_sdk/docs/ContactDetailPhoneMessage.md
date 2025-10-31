# ContactDetailPhoneMessage

Contact phone numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | **str** | Home phone number. | [optional] 
**work** | **str** | Work phone number. | [optional] 
**mobile** | **str** | Mobile phone number. | [optional] 

## Example

```python
from buildium_sdk.models.contact_detail_phone_message import ContactDetailPhoneMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailPhoneMessage from a JSON string
contact_detail_phone_message_instance = ContactDetailPhoneMessage.from_json(json)
# print the JSON string representation of the object
print(ContactDetailPhoneMessage.to_json())

# convert the object into a dict
contact_detail_phone_message_dict = contact_detail_phone_message_instance.to_dict()
# create an instance of ContactDetailPhoneMessage from a dict
contact_detail_phone_message_from_dict = ContactDetailPhoneMessage.from_dict(contact_detail_phone_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


