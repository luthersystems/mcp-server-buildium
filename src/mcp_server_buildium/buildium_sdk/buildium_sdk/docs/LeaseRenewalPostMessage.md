# LeaseRenewalPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_type** | **str** | Describes the type of lease. | 
**lease_to_date** | **date** | End date of the lease. This is required if &#x60;LeaseType&#x60; is &#x60;Fixed&#x60; or &#x60;FixedWithRollover&#x60; | [optional] 
**automatically_move_out_tenants** | **bool** | Indicates whether to automatically move out all tenants assigned to the lease and set the lease status to past when the lease ends. | [optional] 
**rent** | [**LeaseRentPostMessage**](LeaseRentPostMessage.md) | The rent for the lease. | 
**cosigners** | [**List[LeaseCosignerPostMessage]**](LeaseCosignerPostMessage.md) | List of the cosigners to create on the lease. | [optional] 
**tenant_ids** | **List[int]** | Unique identifiers of existing tenants to include on the lease. The request must include at least one tenant in this property OR the &#x60;Tenants&#x60; property. | [optional] 
**tenants** | [**List[RentalTenantRenewalPostMessage]**](RentalTenantRenewalPostMessage.md) | List of new tenants to create on the lease. The request must include at least one tenant in this property OR the &#x60;TenantIds&#x60; property. | [optional] 
**send_welcome_email** | **bool** | Indicates whether to send a welcome email to all tenants on the lease inviting them to the resident center website. | 
**recurring_charges_to_stop** | **List[int]** | Unique identifiers of existing recurring charges on the lease to stop. | [optional] 
**recurring_charges_to_create** | [**List[ChargeRecurringTransactionPostMessage]**](ChargeRecurringTransactionPostMessage.md) | List of new recurring charges to create. | [optional] 
**recurring_charges_to_update** | [**List[ChargeRecurringTransactionPutMessage]**](ChargeRecurringTransactionPutMessage.md) | List of existing recurring charges to update. | [optional] 

## Example

```python
from buildium_sdk.models.lease_renewal_post_message import LeaseRenewalPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRenewalPostMessage from a JSON string
lease_renewal_post_message_instance = LeaseRenewalPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseRenewalPostMessage.to_json())

# convert the object into a dict
lease_renewal_post_message_dict = lease_renewal_post_message_instance.to_dict()
# create an instance of LeaseRenewalPostMessage from a dict
lease_renewal_post_message_from_dict = LeaseRenewalPostMessage.from_dict(lease_renewal_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


