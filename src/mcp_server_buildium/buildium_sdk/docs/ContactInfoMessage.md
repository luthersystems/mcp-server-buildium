# ContactInfoMessage

Contact information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Contact first name. | [optional] 
**last_name** | **str** | Contact last name. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Contact address. | [optional] 
**phone_number** | **str** | Contact phone number. | [optional] 

## Example

```python
from buildium_sdk.models.contact_info_message import ContactInfoMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ContactInfoMessage from a JSON string
contact_info_message_instance = ContactInfoMessage.from_json(json)
# print the JSON string representation of the object
print(ContactInfoMessage.to_json())

# convert the object into a dict
contact_info_message_dict = contact_info_message_instance.to_dict()
# create an instance of ContactInfoMessage from a dict
contact_info_message_from_dict = ContactInfoMessage.from_dict(contact_info_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


