# AssociationOwnerPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the owner. The value cannot exceed 127 characters. | 
**last_name** | **str** | Last name of the owner. The value cannot exceed 127 characters. | 
**primary_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the owner. | 
**alternate_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Alternate address of the owner. | [optional] 
**email** | **str** | Email of the owner. | [optional] 
**alternate_email** | **str** | Alternate email of the owner. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers for the association owner. | [optional] 
**emergency_contact** | [**SaveEmergencyContactMessage**](SaveEmergencyContactMessage.md) | Emergency contact information associated with the owner. | [optional] 
**comment** | **str** | Comments about the owner. The value cannot exceed 65,535 characters. | [optional] 
**mailing_preference** | **str** | Mailing preferences for the owner. If an alternate address exists and this value is not provided then the primary address will be set as the preferred address. | [optional] 
**tax_id** | **str** | Taxpayer identification number of the owner. Examples of United States identification numbers are Social Security number or a Employer Identification Number. Valid formats are: &#x60;12-1234567&#x60;, &#x60;123-12-1234&#x60;, &#x60;123456789&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.association_owner_put_message import AssociationOwnerPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnerPutMessage from a JSON string
association_owner_put_message_instance = AssociationOwnerPutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnerPutMessage.to_json())

# convert the object into a dict
association_owner_put_message_dict = association_owner_put_message_instance.to_dict()
# create an instance of AssociationOwnerPutMessage from a dict
association_owner_put_message_from_dict = AssociationOwnerPutMessage.from_dict(association_owner_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


