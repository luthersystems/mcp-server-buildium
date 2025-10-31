# BankLockboxDataAssociationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association unique identifier. | [optional] 
**name** | **str** | Association name. | [optional] 
**operating_bank_account_id** | **int** | Primary bank account that an association uses for its income and expenses. | [optional] 

## Example

```python
from buildium_sdk.models.bank_lockbox_data_association_message import BankLockboxDataAssociationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankLockboxDataAssociationMessage from a JSON string
bank_lockbox_data_association_message_instance = BankLockboxDataAssociationMessage.from_json(json)
# print the JSON string representation of the object
print(BankLockboxDataAssociationMessage.to_json())

# convert the object into a dict
bank_lockbox_data_association_message_dict = bank_lockbox_data_association_message_instance.to_dict()
# create an instance of BankLockboxDataAssociationMessage from a dict
bank_lockbox_data_association_message_from_dict = BankLockboxDataAssociationMessage.from_dict(bank_lockbox_data_association_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


