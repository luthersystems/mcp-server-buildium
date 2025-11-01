# BankAccountQuickDepositSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date the quick deposit was recorded. | 
**offset_gl_account_id** | **int** | Offsetting general ledger account identifier. The offsetting general ledger account acts as a label for this deposit. For instance, if you&#39;re depositing money collected from a washing machine, you might select the \&quot;Laundry income\&quot; account. | 
**amount** | **float** | Amount to be deposited. | 
**memo** | **str** | Memo associated with the quick deposit. | [optional] 
**accounting_entity** | [**AccountingEntitySaveMessage**](AccountingEntitySaveMessage.md) | A rental property, association or company to associate with the quick deposit. | 

## Example

```python
from buildium_sdk.models.bank_account_quick_deposit_save_message import BankAccountQuickDepositSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountQuickDepositSaveMessage from a JSON string
bank_account_quick_deposit_save_message_instance = BankAccountQuickDepositSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountQuickDepositSaveMessage.to_json())

# convert the object into a dict
bank_account_quick_deposit_save_message_dict = bank_account_quick_deposit_save_message_instance.to_dict()
# create an instance of BankAccountQuickDepositSaveMessage from a dict
bank_account_quick_deposit_save_message_from_dict = BankAccountQuickDepositSaveMessage.from_dict(bank_account_quick_deposit_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


