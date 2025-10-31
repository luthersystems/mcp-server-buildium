# AssociationOwnerToExistingOwnershipAccountPostMessage

This object represents the Association Owner to add to an existing Ownership Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ownership_account_id** | **int** | Ownership account Id for the owner. | 
**send_welcome_email** | **bool** | Send a welcome email to any homeowner at the association | 
**primary_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the owner. | 
**alternate_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Alternate address of the owner. | [optional] 
**first_name** | **str** | First name of the owner. The value can not exceed 127 characters. | 
**last_name** | **str** | Last name of the owner. The value can not exceed 127 characters. | 
**board_member_term** | [**AssociationOwnerBoardTermPostMessage**](AssociationOwnerBoardTermPostMessage.md) | Association board member terms for the owner. | [optional] 
**is_owner_occupied** | **bool** | Indicates if the association owner occupies a unit(s) within the association. | 
**email** | **str** | Email of owner. | [optional] 
**alternate_email** | **str** | Alternate email of owner. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers for the owner. | [optional] 
**date_of_birth** | **date** | Date Of Birth for the owner. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**emergency_contact** | [**SaveEmergencyContactMessage**](SaveEmergencyContactMessage.md) | Emergency Contact information associated with the owner. | [optional] 
**comment** | **str** | Comments about the owner. The value can not exceed 65,535 characters. | [optional] 
**mailing_preference** | **str** | Mailing preferences for the owner. If an alternate address exists and this value is not provided then the primary address will be set as the preferred address. | [optional] 
**tax_id** | **str** | Taxpayer identification number of the owner. Examples of United States identification numbers are Social Security number or a Employer Identification Number. Valid formats are: &#x60;12-1234567&#x60;, &#x60;123-12-1234&#x60;, &#x60;123456789&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.association_owner_to_existing_ownership_account_post_message import AssociationOwnerToExistingOwnershipAccountPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationOwnerToExistingOwnershipAccountPostMessage from a JSON string
association_owner_to_existing_ownership_account_post_message_instance = AssociationOwnerToExistingOwnershipAccountPostMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationOwnerToExistingOwnershipAccountPostMessage.to_json())

# convert the object into a dict
association_owner_to_existing_ownership_account_post_message_dict = association_owner_to_existing_ownership_account_post_message_instance.to_dict()
# create an instance of AssociationOwnerToExistingOwnershipAccountPostMessage from a dict
association_owner_to_existing_ownership_account_post_message_from_dict = AssociationOwnerToExistingOwnershipAccountPostMessage.from_dict(association_owner_to_existing_ownership_account_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


