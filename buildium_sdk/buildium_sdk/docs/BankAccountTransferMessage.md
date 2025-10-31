# BankAccountTransferMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transfer unique identifier. | [optional] 
**entry_date** | **date** | Date the transfer was recorded. | [optional] 
**memo** | **str** | Memo associated with the transfer, if applicable. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | A rental property, association or company to associate with the withdrawal. | [optional] 
**total_amount** | **float** | Total amount of the transfer. | [optional] 
**transfer_to_bank_account_id** | **int** | Bank account identifier the money was transferred to. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_transfer_message import BankAccountTransferMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountTransferMessage from a JSON string
bank_account_transfer_message_instance = BankAccountTransferMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountTransferMessage.to_json())

# convert the object into a dict
bank_account_transfer_message_dict = bank_account_transfer_message_instance.to_dict()
# create an instance of BankAccountTransferMessage from a dict
bank_account_transfer_message_from_dict = BankAccountTransferMessage.from_dict(bank_account_transfer_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


