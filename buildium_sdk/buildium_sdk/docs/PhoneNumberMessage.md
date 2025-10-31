# PhoneNumberMessage

This is an object that represents a phone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Phone number. | [optional] 
**type** | **str** | Indicates the type of phone number. | [optional] 

## Example

```python
from buildium_sdk.models.phone_number_message import PhoneNumberMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberMessage from a JSON string
phone_number_message_instance = PhoneNumberMessage.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberMessage.to_json())

# convert the object into a dict
phone_number_message_dict = phone_number_message_instance.to_dict()
# create an instance of PhoneNumberMessage from a dict
phone_number_message_from_dict = PhoneNumberMessage.from_dict(phone_number_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


