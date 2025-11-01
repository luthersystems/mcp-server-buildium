# BankAccountTransferSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | The date the transfer was recorded. | 
**transfer_to_bank_account_id** | **int** | Bank account identifier the money will be transferred to. | 
**total_amount** | **float** | Total amount to transfer. | 
**memo** | **str** | Memo associated with the transfer, if applicable. | [optional] 
**accounting_entity** | [**BankAccountTransferAccountingEntitySaveMessage**](BankAccountTransferAccountingEntitySaveMessage.md) | A rental property, association or company to associate with the transfer. | 

## Example

```python
from buildium_sdk.models.bank_account_transfer_save_message import BankAccountTransferSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountTransferSaveMessage from a JSON string
bank_account_transfer_save_message_instance = BankAccountTransferSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountTransferSaveMessage.to_json())

# convert the object into a dict
bank_account_transfer_save_message_dict = bank_account_transfer_save_message_instance.to_dict()
# create an instance of BankAccountTransferSaveMessage from a dict
bank_account_transfer_save_message_from_dict = BankAccountTransferSaveMessage.from_dict(bank_account_transfer_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


