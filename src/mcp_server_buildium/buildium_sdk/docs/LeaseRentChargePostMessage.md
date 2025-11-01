# LeaseRentChargePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the charge. | 
**gl_account_id** | **int** | The general ledger account identifier under which to record the charge. | 
**next_due_date** | **date** | Indicates the next date the charge will be applied to the lease ledger. This date will also be used as the start date for the calculating the &#x60;Cycle&#x60; of when to apply the next charge. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | Memo for the charge. | [optional] 

## Example

```python
from buildium_sdk.models.lease_rent_charge_post_message import LeaseRentChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRentChargePostMessage from a JSON string
lease_rent_charge_post_message_instance = LeaseRentChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseRentChargePostMessage.to_json())

# convert the object into a dict
lease_rent_charge_post_message_dict = lease_rent_charge_post_message_instance.to_dict()
# create an instance of LeaseRentChargePostMessage from a dict
lease_rent_charge_post_message_from_dict = LeaseRentChargePostMessage.from_dict(lease_rent_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


