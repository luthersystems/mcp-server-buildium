# LeaseRentPostMessage

The rent for the lease. When provided in the request the charges for the specified amount will be automatically applied to the lease ledger on the cadence specified in the `Cycle`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle** | **str** | Indicates the cadence of when rent &#x60;Charges&#x60; will be applied automatically to the lease ledger. | 
**charges** | [**List[LeaseRentChargePostMessage]**](LeaseRentChargePostMessage.md) | List of charges to apply to the lease. | 

## Example

```python
from buildium_sdk.models.lease_rent_post_message import LeaseRentPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRentPostMessage from a JSON string
lease_rent_post_message_instance = LeaseRentPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseRentPostMessage.to_json())

# convert the object into a dict
lease_rent_post_message_dict = lease_rent_post_message_instance.to_dict()
# create an instance of LeaseRentPostMessage from a dict
lease_rent_post_message_from_dict = LeaseRentPostMessage.from_dict(lease_rent_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


