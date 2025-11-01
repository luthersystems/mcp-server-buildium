# AssociationOwnerMessage

This object represents an owner of a unit(s) that exists within a home owner association.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**email** | **str** | Email. | [optional] 
**alternate_email** | **str** | Alternate email. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers of the association user. | [optional] 
**primary_address** | [**AddressMessage**](AddressMessage.md) | Primary address. | [optional] 
**alternate_address** | [**AddressMessage**](AddressMessage.md) | Alternate address. | [optional] 
**comment** | **str** | General comments. | [optional] 
**emergency_contact** | [**EmergencyContactMessage**](EmergencyContactMessage.md) | Emergency contact information. | [optional] 
**ownership_accounts** | [**List[AssociationOwnershipAccountMessage]**](AssociationOwnershipAccountMessage.md) | List of associated ownership accounts. | [optional] 
**mailing_preference** | **str** | Indicates the association owner&#39;s mailing preference. | [optional] 
**vehicles** | [**List[VehicleMessage]**](VehicleMessage.md) | List of vehicles associated with the association owner. | [optional] 
**occupies_unit** | **bool** | Indicates if the association owner occupies a unit(s) within the association. | [optional] 
**board_member_terms** | [**List[AssociationOwnerBoardTermMessage]**](AssociationOwnerBoardTermMessage.md) | List of Board Member Terms for the given Association Owner(s) | [optional] 
**created_date_time** | **datetime** | Date and time the association owner was created. | [optional] 
**tax_id** | **str** | Taxpayer identification number. Examples of United States identification numbers are Social Security number or a Employer Identification Number. | [optional] 
**delinquency_status** | **str** | Indicates the delinquency status of the association owner. | [optional] 

## Example

```python
from buildium_sdk.models.association_owner_message import AssociationOwnerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnerMessage from a JSON string
association_owner_message_instance = AssociationOwnerMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnerMessage.to_json())

# convert the object into a dict
association_owner_message_dict = association_owner_message_instance.to_dict()
# create an instance of AssociationOwnerMessage from a dict
association_owner_message_from_dict = AssociationOwnerMessage.from_dict(association_owner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


