# BankAccountCheckLineSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. | 
**accounting_entity** | [**BankAccountCheckAccountingEntitySaveMessage**](BankAccountCheckAccountingEntitySaveMessage.md) | Accounting entity associated with the line item. | 
**memo** | **str** | Memo for the line item. | [optional] 
**reference_number** | **str** | Reference number for the line item. | [optional] 
**amount** | **float** | Amount of the line item. | 

## Example

```python
from buildium_sdk.models.bank_account_check_line_save_message import BankAccountCheckLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCheckLineSaveMessage from a JSON string
bank_account_check_line_save_message_instance = BankAccountCheckLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountCheckLineSaveMessage.to_json())

# convert the object into a dict
bank_account_check_line_save_message_dict = bank_account_check_line_save_message_instance.to_dict()
# create an instance of BankAccountCheckLineSaveMessage from a dict
bank_account_check_line_save_message_from_dict = BankAccountCheckLineSaveMessage.from_dict(bank_account_check_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


