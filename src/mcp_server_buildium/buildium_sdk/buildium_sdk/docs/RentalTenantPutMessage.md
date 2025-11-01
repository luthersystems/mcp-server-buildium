# RentalTenantPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the tenant. The value cannot exceed 127 characters. | 
**last_name** | **str** | Last name of the tenant. The value cannot exceed 127 characters. | 
**email** | **str** | Email of the tenant. | [optional] 
**alternate_email** | **str** | Alternate email of the tenant. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers for the tenant. | [optional] 
**date_of_birth** | **date** | Date of birth for the tenant. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**comment** | **str** | Comments about the tenant. The value cannot exceed 65,535 characters. | [optional] 
**tax_id** | **str** | Tax identifier of the tenant. Valid formats are: &#x60;12-1234567&#x60;, &#x60;123-12-1234&#x60;, &#x60;123456789&#x60; | [optional] 
**emergency_contact** | [**SaveEmergencyContactMessage**](SaveEmergencyContactMessage.md) | Emergency contact information associated with the tenant. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the tenant. | 
**alternate_address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Alternate address of the tenant. | [optional] 
**mailing_preference** | **str** | Mailing preference for the tenant. If an alternate address exists and this value is not provided then the primary address will be set as the preferred address. | [optional] 

## Example

```python
from buildium_sdk.models.rental_tenant_put_message import RentalTenantPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalTenantPutMessage from a JSON string
rental_tenant_put_message_instance = RentalTenantPutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalTenantPutMessage.to_json())

# convert the object into a dict
rental_tenant_put_message_dict = rental_tenant_put_message_instance.to_dict()
# create an instance of RentalTenantPutMessage from a dict
rental_tenant_put_message_from_dict = RentalTenantPutMessage.from_dict(rental_tenant_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


