# LeaseSecurityDepositPostMessage

The security deposit on the lease. When provided in the request a one-time charge for the specified amount will be applied to the lease ledger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **date** | The date the security deposit is due. This date will be used as the transaction date when applying the charge to the lease ledger. | 
**amount** | **float** | Security deposit amount. | 

## Example

```python
from buildium_sdk.models.lease_security_deposit_post_message import LeaseSecurityDepositPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseSecurityDepositPostMessage from a JSON string
lease_security_deposit_post_message_instance = LeaseSecurityDepositPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseSecurityDepositPostMessage.to_json())

# convert the object into a dict
lease_security_deposit_post_message_dict = lease_security_deposit_post_message_instance.to_dict()
# create an instance of LeaseSecurityDepositPostMessage from a dict
lease_security_deposit_post_message_from_dict = LeaseSecurityDepositPostMessage.from_dict(lease_security_deposit_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


