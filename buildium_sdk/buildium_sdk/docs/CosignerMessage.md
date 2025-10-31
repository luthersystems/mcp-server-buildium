# CosignerMessage

This object represents a rental property cosigner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Cosigner unique identifier. | [optional] 
**first_name** | **str** | First name of the cosigner. | [optional] 
**last_name** | **str** | Last name of the cosigner. | [optional] 
**email** | **str** | Email for the cosigner. | [optional] 
**alternate_email** | **str** | Alternate Email for the cosigner. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers for the cosigner. | [optional] 
**created_date_time** | **datetime** | Created date of this cosigner record. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the cosigner. | [optional] 
**alternate_address** | [**AddressMessage**](AddressMessage.md) | Alternate address for the cosigner. | [optional] 
**mailing_preference** | **str** | Mailing preference for the cosigner. | [optional] 

## Example

```python
from buildium_sdk.models.cosigner_message import CosignerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CosignerMessage from a JSON string
cosigner_message_instance = CosignerMessage.from_json(json)
# print the JSON string representation of the object
print(CosignerMessage.to_json())

# convert the object into a dict
cosigner_message_dict = cosigner_message_instance.to_dict()
# create an instance of CosignerMessage from a dict
cosigner_message_from_dict = CosignerMessage.from_dict(cosigner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


