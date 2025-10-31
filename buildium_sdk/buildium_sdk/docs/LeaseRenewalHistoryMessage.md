# LeaseRenewalHistoryMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lease renewal unique identifier. | [optional] 
**lease_id** | **int** | Lease unique identifier. | [optional] 
**lease_status** | **str** | Indicates the status of the lease. | [optional] 
**lease_from_date** | **date** | Start date of the lease. | [optional] 
**lease_to_date** | **date** | End date of the lease. | [optional] 
**lease_type** | **str** | Describes the type of lease. | [optional] 
**rent** | **float** | Rent for the lease. | [optional] 
**rent_id** | **int** | The unique identifier of the scheduled Rent entity. If the renewal is not associated with a Rent entity then the value will be &#x60;NULL&#x60;. | [optional] 
**tenant_ids** | **List[int]** | Unique identifiers of tenants on the lease. | [optional] 
**created_date_time** | **datetime** | Date and time the lease renewal was created. | [optional] 
**last_updated_date_time** | **datetime** | The date and time the lease renewal was last updated. | [optional] 

## Example

```python
from buildium_sdk.models.lease_renewal_history_message import LeaseRenewalHistoryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRenewalHistoryMessage from a JSON string
lease_renewal_history_message_instance = LeaseRenewalHistoryMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseRenewalHistoryMessage.to_json())

# convert the object into a dict
lease_renewal_history_message_dict = lease_renewal_history_message_instance.to_dict()
# create an instance of LeaseRenewalHistoryMessage from a dict
lease_renewal_history_message_from_dict = LeaseRenewalHistoryMessage.from_dict(lease_renewal_history_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


