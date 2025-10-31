# TenantMessage

This object represents a rental property tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Tenant unique identifier. | [optional] 
**first_name** | **str** | First name of the tenant. | [optional] 
**last_name** | **str** | Last name of the tenant. | [optional] 
**email** | **str** | Email for the tenant. | [optional] 
**alternate_email** | **str** | Alternate email of the tenant. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers for the tenant. | [optional] 
**created_date_time** | **datetime** | Created date of this tenant record. | [optional] 
**emergency_contact** | [**EmergencyContactMessage**](EmergencyContactMessage.md) | Name of the tenants emergency contact. | [optional] 
**date_of_birth** | **date** | Tenant date of birth. | [optional] 
**sms_opt_in_status** | **str** | Indicates the tenants SMS opt in status. Null if no status exists for the tenant. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the tenant. | [optional] 
**alternate_address** | [**AddressMessage**](AddressMessage.md) | Alternate address for the tenant. | [optional] 
**mailing_preference** | **str** | Mailing preference for the tenant. | [optional] 
**leases** | [**List[LeaseMessage]**](LeaseMessage.md) | List of leases, regardless of status, that the tenant is associated with. | [optional] 
**comment** | **str** | Comments about the tenant. | [optional] 
**tax_id** | **str** | TaxId of the tenant. | [optional] 

## Example

```python
from buildium_sdk.models.tenant_message import TenantMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TenantMessage from a JSON string
tenant_message_instance = TenantMessage.from_json(json)
# print the JSON string representation of the object
print(TenantMessage.to_json())

# convert the object into a dict
tenant_message_dict = tenant_message_instance.to_dict()
# create an instance of TenantMessage from a dict
tenant_message_from_dict = TenantMessage.from_dict(tenant_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


