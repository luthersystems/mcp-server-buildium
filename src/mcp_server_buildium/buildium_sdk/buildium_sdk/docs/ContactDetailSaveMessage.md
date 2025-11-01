# ContactDetailSaveMessage

The contact details of the person who made the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the contact. | 
**last_name** | **str** | Last name of the contact. | [optional] 
**email** | **str** | Email of the contact. | [optional] 
**phone_numbers** | [**ContactDetailSavePhoneMessage**](ContactDetailSavePhoneMessage.md) | Contact phone numbers. | [optional] 

## Example

```python
from buildium_sdk.models.contact_detail_save_message import ContactDetailSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailSaveMessage from a JSON string
contact_detail_save_message_instance = ContactDetailSaveMessage.from_json(json)
# print the JSON string representation of the object
print(ContactDetailSaveMessage.to_json())

# convert the object into a dict
contact_detail_save_message_dict = contact_detail_save_message_instance.to_dict()
# create an instance of ContactDetailSaveMessage from a dict
contact_detail_save_message_from_dict = ContactDetailSaveMessage.from_dict(contact_detail_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


