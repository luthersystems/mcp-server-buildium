# LeasePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_type** | **str** | Describes the type of lease.      &#x60;AtWill&#x60; leases are month-to-month leases. Setting a lease as at will tells Buildium when the tenant&#39;s lease initially started, but since there is no lease end date, Buildium will never move the lease to expired, and it will continue to post any automatic transactions (like recurring monthly rent charges or late fees) until you manually end the lease.        &#x60;Fixed&#x60; leases are leases that have specific start and end dates.When the end date occurs, the lease will move from active to expired, and any transactions set to post automatically(like recurring monthly rent charges or late fees) will stop posting.        &#x60;FixedWithRollover&#x60; leases are similar to fixed leases, but instead of Buildium moving this lease to expired as of the end date, it will move the lease to an at will status, which tells Buildium to continue posting monthly rent charges, late fees for you until you manually end the lease. | 
**unit_id** | **int** | Unit unique identifier associated with the lease. | 
**lease_from_date** | **date** | Start date of the lease. | 
**lease_to_date** | **date** | End date of the lease. | [optional] 
**send_welcome_email** | **bool** | Indicates whether to send a welcome email to all tenants on the lease inviting them to the resident center website. | 
**tenants** | [**List[RentalTenantPutMessage]**](RentalTenantPutMessage.md) | List of new tenants to add to the lease. The list cannot exceed five tenants. | [optional] 
**tenant_ids** | **List[int]** | List of identifiers for existing tenants to add to the lease. The list cannot exceed five tenants. | [optional] 
**applicant_ids** | **List[int]** | List of identifiers for applicants to become tenants on the lease. Identifiers must refer to applicants with a Status of &#x60;Approved&#x60;. The list cannot exceed five applicants. | [optional] 
**cosigners** | [**List[LeaseCosignerPostMessage]**](LeaseCosignerPostMessage.md) | List of the cosigners on the lease. | [optional] 
**rent** | [**LeaseRentPostMessage**](LeaseRentPostMessage.md) | Rent charge on the post message | [optional] 
**security_deposit** | [**LeaseSecurityDepositPostMessage**](LeaseSecurityDepositPostMessage.md) | The security deposit. | [optional] 
**prorated_first_month_rent** | **float** | Prorated rent charged for the first month of the lease. Must be null if the lease begins on the first day of a month. | [optional] 
**prorated_last_month_rent** | **float** | Prorated rent charged for the last month of the lease. Must be null if the lease ends on the last day of a month. | [optional] 

## Example

```python
from buildium_sdk.models.lease_post_message import LeasePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeasePostMessage from a JSON string
lease_post_message_instance = LeasePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeasePostMessage.to_json())

# convert the object into a dict
lease_post_message_dict = lease_post_message_instance.to_dict()
# create an instance of LeasePostMessage from a dict
lease_post_message_from_dict = LeasePostMessage.from_dict(lease_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


