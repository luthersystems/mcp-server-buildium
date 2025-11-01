# LeaseRenewalMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lease renewal unique identifier. | [optional] 
**lease_status** | **str** | Indicates the status of the lease. | [optional] 
**lease_from_date** | **date** | Start date of the lease. | [optional] 
**lease_to_date** | **date** | End date of the lease. | [optional] 
**lease_type** | **str** | Describes the type of lease. | [optional] 
**rent** | **float** | Rent for the lease. | [optional] 
**rent_id** | **int** | The unique identifier of the scheduled Rent entity. If the renewal is not associated with a Rent entity then the value will be &#x60;NULL&#x60;. | [optional] 
**tenant_ids** | **List[int]** | Unique identifiers of tenants on the lease. | [optional] 

## Example

```python
from buildium_sdk.models.lease_renewal_message import LeaseRenewalMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRenewalMessage from a JSON string
lease_renewal_message_instance = LeaseRenewalMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseRenewalMessage.to_json())

# convert the object into a dict
lease_renewal_message_dict = lease_renewal_message_instance.to_dict()
# create an instance of LeaseRenewalMessage from a dict
lease_renewal_message_from_dict = LeaseRenewalMessage.from_dict(lease_renewal_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


