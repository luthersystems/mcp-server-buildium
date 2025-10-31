# BankAccountWithdrawalMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Withdrawal unique identifier. | [optional] 
**entry_date** | **date** | Date the withdrawal was recorded. | [optional] 
**memo** | **str** | Memo associated with the withdrawal, if applicable. | [optional] 
**total_amount** | **float** | Total amount of the withdrawal. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | A rental property, association or company associated with the withdrawal. | [optional] 
**offset_gl_account_id** | **int** | Offsetting general ledger account identifier. The offsetting GL account acts as a label for this withdrawal. For instance, if you&#39;re withdrawing money due to a bank fee, you might select the \&quot;Bank fees\&quot; expense account. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_withdrawal_message import BankAccountWithdrawalMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountWithdrawalMessage from a JSON string
bank_account_withdrawal_message_instance = BankAccountWithdrawalMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountWithdrawalMessage.to_json())

# convert the object into a dict
bank_account_withdrawal_message_dict = bank_account_withdrawal_message_instance.to_dict()
# create an instance of BankAccountWithdrawalMessage from a dict
bank_account_withdrawal_message_from_dict = BankAccountWithdrawalMessage.from_dict(bank_account_withdrawal_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


