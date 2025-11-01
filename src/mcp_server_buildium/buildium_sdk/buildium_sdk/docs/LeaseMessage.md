# LeaseMessage

This object represents a rental property lease.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lease unique identifier. | [optional] 
**property_id** | **int** | Rental property unique identifier. | [optional] 
**unit_id** | **int** | Unit unique identifier. | [optional] 
**unit_number** | **str** | Unit number specified in the lease. | [optional] 
**lease_from_date** | **date** | Start date of the lease. | [optional] 
**lease_to_date** | **date** | End date of the lease. | [optional] 
**lease_type** | **str** | Describes the type of lease. | [optional] 
**lease_status** | **str** | Indicates the status of the lease. | [optional] 
**is_eviction_pending** | **bool** | Indicates whether the lease has an eviction pending. | [optional] 
**term_type** | **str** | Describes the term type of the lease. | [optional] 
**renewal_offer_status** | **str** | Describes the status of the renewal offer. Null if no renewal offer exists. | [optional] 
**current_tenants** | [**List[TenantMessage]**](TenantMessage.md) | List of the current tenants on the lease. | [optional] 
**current_number_of_occupants** | **int** | Count of current tenants. | [optional] 
**account_details** | [**LeaseAccountDetailMessage**](LeaseAccountDetailMessage.md) | Financial details of the lease. | [optional] 
**cosigners** | [**List[CosignerMessage]**](CosignerMessage.md) | List of the cosigners on the lease. | [optional] 
**automatically_move_out_tenants** | **bool** | Indicates whether to automatically move out all tenants assigned to the lease and set the lease status to past when the lease ends. | [optional] 
**created_date_time** | **datetime** | Date and time the lease was created. | [optional] 
**last_updated_date_time** | **datetime** | The date and time the lease was last updated. | [optional] 
**move_out_data** | [**List[LeaseMoveOutDataMessage]**](LeaseMoveOutDataMessage.md) | Move out data of lease | [optional] 
**payment_due_day** | **int** | Day of the month payment is due. | [optional] 
**tenants** | [**List[LeaseTenantMessage]**](LeaseTenantMessage.md) | List of all tenants ever associated with the lease | [optional] 

## Example

```python
from buildium_sdk.models.lease_message import LeaseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseMessage from a JSON string
lease_message_instance = LeaseMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseMessage.to_json())

# convert the object into a dict
lease_message_dict = lease_message_instance.to_dict()
# create an instance of LeaseMessage from a dict
lease_message_from_dict = LeaseMessage.from_dict(lease_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


