# BankAccountDepositLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the line item. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | A rental property, association or company to associate with the line item. | [optional] 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount is recorded. | [optional] 
**memo** | **str** | Memo for the line item. | [optional] 
**reference_number** | **str** | Reference number for the line item. | [optional] 
**amount** | **float** | Amount of the line item. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_deposit_line_message import BankAccountDepositLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDepositLineMessage from a JSON string
bank_account_deposit_line_message_instance = BankAccountDepositLineMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountDepositLineMessage.to_json())

# convert the object into a dict
bank_account_deposit_line_message_dict = bank_account_deposit_line_message_instance.to_dict()
# create an instance of BankAccountDepositLineMessage from a dict
bank_account_deposit_line_message_from_dict = BankAccountDepositLineMessage.from_dict(bank_account_deposit_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


