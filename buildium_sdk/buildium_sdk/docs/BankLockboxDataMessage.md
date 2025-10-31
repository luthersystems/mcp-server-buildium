# BankLockboxDataMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association** | [**BankLockboxDataAssociationMessage**](BankLockboxDataAssociationMessage.md) | Association information. | [optional] 
**ownership_accounts** | [**List[BankLockboxDataOwnershipAccountMessage]**](BankLockboxDataOwnershipAccountMessage.md) | Information about ownership accounts that belong to the association. | [optional] 

## Example

```python
from buildium_sdk.models.bank_lockbox_data_message import BankLockboxDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankLockboxDataMessage from a JSON string
bank_lockbox_data_message_instance = BankLockboxDataMessage.from_json(json)
# print the JSON string representation of the object
print(BankLockboxDataMessage.to_json())

# convert the object into a dict
bank_lockbox_data_message_dict = bank_lockbox_data_message_instance.to_dict()
# create an instance of BankLockboxDataMessage from a dict
bank_lockbox_data_message_from_dict = BankLockboxDataMessage.from_dict(bank_lockbox_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


