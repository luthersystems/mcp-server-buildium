# BankLockboxDataOwnershipAccountMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association ownership account unique identifier. | [optional] 
**unit_number** | **str** | Unit number of the unit for this ownership account. | [optional] 
**unit_address** | [**AddressMessage**](AddressMessage.md) | Address of the unit for this ownership account. | [optional] 
**delinquency_status** | **str** | Indicates the delinquency status of the ownership account | [optional] 
**association_owners** | [**List[BankLockboxDataAssociationOwnerMessage]**](BankLockboxDataAssociationOwnerMessage.md) | Association owners for this ownership account. | [optional] 

## Example

```python
from buildium_sdk.models.bank_lockbox_data_ownership_account_message import BankLockboxDataOwnershipAccountMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankLockboxDataOwnershipAccountMessage from a JSON string
bank_lockbox_data_ownership_account_message_instance = BankLockboxDataOwnershipAccountMessage.from_json(json)
# print the JSON string representation of the object
print(BankLockboxDataOwnershipAccountMessage.to_json())

# convert the object into a dict
bank_lockbox_data_ownership_account_message_dict = bank_lockbox_data_ownership_account_message_instance.to_dict()
# create an instance of BankLockboxDataOwnershipAccountMessage from a dict
bank_lockbox_data_ownership_account_message_from_dict = BankLockboxDataOwnershipAccountMessage.from_dict(bank_lockbox_data_ownership_account_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


