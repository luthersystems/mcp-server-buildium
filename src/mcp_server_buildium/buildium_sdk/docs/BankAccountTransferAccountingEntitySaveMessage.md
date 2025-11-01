# BankAccountTransferAccountingEntitySaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The accounting entity unique identifier. | 
**accounting_entity_type** | **str** | The type of accounting entity. | 
**unit_id** | **int** | The unit unique identifier for the accounting entity. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_transfer_accounting_entity_save_message import BankAccountTransferAccountingEntitySaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountTransferAccountingEntitySaveMessage from a JSON string
bank_account_transfer_accounting_entity_save_message_instance = BankAccountTransferAccountingEntitySaveMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountTransferAccountingEntitySaveMessage.to_json())

# convert the object into a dict
bank_account_transfer_accounting_entity_save_message_dict = bank_account_transfer_accounting_entity_save_message_instance.to_dict()
# create an instance of BankAccountTransferAccountingEntitySaveMessage from a dict
bank_account_transfer_accounting_entity_save_message_from_dict = BankAccountTransferAccountingEntitySaveMessage.from_dict(bank_account_transfer_accounting_entity_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


