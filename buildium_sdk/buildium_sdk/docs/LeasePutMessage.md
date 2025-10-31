# LeasePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_type** | **str** | Describes the type of lease. | 
**unit_id** | **int** | Unit unique identifier associated with the lease. | 
**lease_from_date** | **date** | Start date of the lease. | 
**lease_to_date** | **date** | End date of the lease. | [optional] 
**is_eviction_pending** | **bool** | Indicates whether the lease has an eviction pending. | 
**automatically_move_out_tenants** | **bool** | Indicates whether to automatically move out all tenants assigned to the lease and set the lease status to past when the lease ends. | [optional] 

## Example

```python
from buildium_sdk.models.lease_put_message import LeasePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeasePutMessage from a JSON string
lease_put_message_instance = LeasePutMessage.from_json(json)
# print the JSON string representation of the object
print(LeasePutMessage.to_json())

# convert the object into a dict
lease_put_message_dict = lease_put_message_instance.to_dict()
# create an instance of LeasePutMessage from a dict
lease_put_message_from_dict = LeasePutMessage.from_dict(lease_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


