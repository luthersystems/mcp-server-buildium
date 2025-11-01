# ContactDetailSavePhoneMessage

Contact phone numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | **str** | Home phone number. If provided, the value must be between 10 and 20 characters, ideally formatted as &#x60;(123) 123-1234&#x60;. | [optional] 
**work** | **str** | Work phone number. If provided, the value must be between 10 and 20 characters, ideally formatted as &#x60;(123) 123-1234&#x60;. | [optional] 
**mobile** | **str** | Mobile phone number. If provided, the value must be between 10 and 20 characters, ideally formatted as &#x60;(123) 123-1234&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.contact_detail_save_phone_message import ContactDetailSavePhoneMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetailSavePhoneMessage from a JSON string
contact_detail_save_phone_message_instance = ContactDetailSavePhoneMessage.from_json(json)
# print the JSON string representation of the object
print(ContactDetailSavePhoneMessage.to_json())

# convert the object into a dict
contact_detail_save_phone_message_dict = contact_detail_save_phone_message_instance.to_dict()
# create an instance of ContactDetailSavePhoneMessage from a dict
contact_detail_save_phone_message_from_dict = ContactDetailSavePhoneMessage.from_dict(contact_detail_save_phone_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


