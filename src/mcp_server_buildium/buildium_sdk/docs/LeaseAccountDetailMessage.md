# LeaseAccountDetailMessage

This is an object that represents lease financial details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_deposit** | **float** | Security deposit for the lease. Null if no security deposit exists. | [optional] 
**rent** | **float** | Rent for the lease. Null if no rent exists. | [optional] 

## Example

```python
from buildium_sdk.models.lease_account_detail_message import LeaseAccountDetailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseAccountDetailMessage from a JSON string
lease_account_detail_message_instance = LeaseAccountDetailMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseAccountDetailMessage.to_json())

# convert the object into a dict
lease_account_detail_message_dict = lease_account_detail_message_instance.to_dict()
# create an instance of LeaseAccountDetailMessage from a dict
lease_account_detail_message_from_dict = LeaseAccountDetailMessage.from_dict(lease_account_detail_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


