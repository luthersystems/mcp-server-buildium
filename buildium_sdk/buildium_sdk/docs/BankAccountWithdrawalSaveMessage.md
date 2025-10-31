# BankAccountWithdrawalSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date the withdrawal was recorded. | 
**offset_gl_account_id** | **int** | Offsetting general ledger account identifier. The offsetting general ledger account acts as a label for this withdrawal. For instance, if you&#39;re withdrawing money due to a bank fee, you might select the \&quot;Bank fees\&quot; expense account. | 
**amount** | **float** | Withdrawal amount. | 
**memo** | **str** | Memo associated with the withdrawal, if applicable. | [optional] 
**accounting_entity** | [**AccountingEntitySaveMessage**](AccountingEntitySaveMessage.md) | A rental property, association or company to associate with the withdrawal. | 

## Example

```python
from buildium_sdk.models.bank_account_withdrawal_save_message import BankAccountWithdrawalSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountWithdrawalSaveMessage from a JSON string
bank_account_withdrawal_save_message_instance = BankAccountWithdrawalSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountWithdrawalSaveMessage.to_json())

# convert the object into a dict
bank_account_withdrawal_save_message_dict = bank_account_withdrawal_save_message_instance.to_dict()
# create an instance of BankAccountWithdrawalSaveMessage from a dict
bank_account_withdrawal_save_message_from_dict = BankAccountWithdrawalSaveMessage.from_dict(bank_account_withdrawal_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


