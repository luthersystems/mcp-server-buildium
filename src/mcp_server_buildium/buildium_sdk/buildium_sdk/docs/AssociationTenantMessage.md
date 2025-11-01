# AssociationTenantMessage

This object represents a home owner association tenant.

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
**move_in_date** | **date** | Move in date for the tenant. | [optional] 
**move_out_date** | **date** | Move out date for the tenant. | [optional] 
**created_date_time** | **datetime** | Date and time the tenant was created. | [optional] 

## Example

```python
from buildium_sdk.models.association_tenant_message import AssociationTenantMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTenantMessage from a JSON string
association_tenant_message_instance = AssociationTenantMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationTenantMessage.to_json())

# convert the object into a dict
association_tenant_message_dict = association_tenant_message_instance.to_dict()
# create an instance of AssociationTenantMessage from a dict
association_tenant_message_from_dict = AssociationTenantMessage.from_dict(association_tenant_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


