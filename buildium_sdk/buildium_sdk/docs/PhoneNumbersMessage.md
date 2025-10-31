# PhoneNumbersMessage

Phone numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | **str** | Home phone number. If provided, must be between 10 and 20 characters, ideally formatted as &#x60;(123) 123-1234&#x60;. | [optional] 
**work** | **str** | Work phone number. If provided, must be between 10 and 20 characters, ideally formatted as &#x60;(123) 123-1234&#x60;. | [optional] 
**mobile** | **str** | Mobile phone number. If provided, must be between 10 and 20 characters, ideally formatted as &#x60;(123) 123-1234&#x60;. | [optional] 
**fax** | **str** | Fax number. If provided, must be between 10 and 20 characters, ideally formatted as &#x60;(123) 123-1234&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.phone_numbers_message import PhoneNumbersMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumbersMessage from a JSON string
phone_numbers_message_instance = PhoneNumbersMessage.from_json(json)
# print the JSON string representation of the object
print(PhoneNumbersMessage.to_json())

# convert the object into a dict
phone_numbers_message_dict = phone_numbers_message_instance.to_dict()
# create an instance of PhoneNumbersMessage from a dict
phone_numbers_message_from_dict = PhoneNumbersMessage.from_dict(phone_numbers_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


