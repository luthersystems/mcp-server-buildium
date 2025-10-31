# BankAccountQuickDepositMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Quick deposit unique identifier. | [optional] 
**entry_date** | **date** | Date the quick deposit was recorded. | [optional] 
**memo** | **str** | Memo associated with the quick deposit, if applicable. | [optional] 
**total_amount** | **float** | Amount included in the quick deposit. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | A rental property, association or company to associate with the quick deposit. | [optional] 
**offset_gl_account_id** | **int** | Offsetting general ledger account identifier. The offsetting general ledger account acts as a label for this deposit. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_quick_deposit_message import BankAccountQuickDepositMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountQuickDepositMessage from a JSON string
bank_account_quick_deposit_message_instance = BankAccountQuickDepositMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountQuickDepositMessage.to_json())

# convert the object into a dict
bank_account_quick_deposit_message_dict = bank_account_quick_deposit_message_instance.to_dict()
# create an instance of BankAccountQuickDepositMessage from a dict
bank_account_quick_deposit_message_from_dict = BankAccountQuickDepositMessage.from_dict(bank_account_quick_deposit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


