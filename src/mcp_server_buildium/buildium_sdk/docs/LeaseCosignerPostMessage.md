# LeaseCosignerPostMessage

This object represents a rental lease cosigner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the cosigner. | 
**last_name** | **str** | Last name of the cosigner. | 
**email** | **str** | Email for the cosigner. | [optional] 
**alternate_email** | **str** | Alternate Email for the cosigner. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | List of phone numbers for the cosigner. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the cosigner. | [optional] 
**alternate_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Alternate address for the cosigner. | [optional] 
**mailing_preference** | **str** | Mailing preferences for the cosigner. If an alternate address exists and this value is not provided then the primary address will be set as the preferred address. | [optional] 

## Example

```python
from buildium_sdk.models.lease_cosigner_post_message import LeaseCosignerPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseCosignerPostMessage from a JSON string
lease_cosigner_post_message_instance = LeaseCosignerPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseCosignerPostMessage.to_json())

# convert the object into a dict
lease_cosigner_post_message_dict = lease_cosigner_post_message_instance.to_dict()
# create an instance of LeaseCosignerPostMessage from a dict
lease_cosigner_post_message_from_dict = LeaseCosignerPostMessage.from_dict(lease_cosigner_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


