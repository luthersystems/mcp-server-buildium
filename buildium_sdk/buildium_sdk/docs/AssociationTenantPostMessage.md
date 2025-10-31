# AssociationTenantPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of tenant. The value cannot exceed 127 characters. | 
**last_name** | **str** | Last name of tenant. The value cannot exceed 127 characters. | 
**email** | **str** | Email of tenant. | [optional] 
**alternate_email** | **str** | Alternate email of tenant. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers for the tenant. | [optional] 
**date_of_birth** | **date** | Date of birth for the tenant. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**comment** | **str** | Comments about the tenant. The value cannot exceed 65,535 characters. | [optional] 
**emergency_contact** | [**SaveEmergencyContactMessage**](SaveEmergencyContactMessage.md) | Emergency contact information associated with the tenant. | [optional] 
**primary_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the tenant. | 
**alternate_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Alternate address of the tenant. | [optional] 
**move_in_date** | **date** | Move in date for the tenant. This date is not editable and can only be set when creating the tenant. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**move_out_date** | **date** | Move out date for the tenant. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**ownership_account_id** | **int** | Ownership account id for the tenant. | 

## Example

```python
from buildium_sdk.models.association_tenant_post_message import AssociationTenantPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTenantPostMessage from a JSON string
association_tenant_post_message_instance = AssociationTenantPostMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationTenantPostMessage.to_json())

# convert the object into a dict
association_tenant_post_message_dict = association_tenant_post_message_instance.to_dict()
# create an instance of AssociationTenantPostMessage from a dict
association_tenant_post_message_from_dict = AssociationTenantPostMessage.from_dict(association_tenant_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


