# BankAccountCheckLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the line item. | [optional] 
**gl_account_id** | **int** | General ledger account unique identifier the line item is related to. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | The type of accounting entity. | [optional] 
**memo** | **str** | Memo for the line item. | [optional] 
**reference_number** | **str** | Reference number for the line item. | [optional] 
**amount** | **float** | Amount of the line item. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_check_line_message import BankAccountCheckLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCheckLineMessage from a JSON string
bank_account_check_line_message_instance = BankAccountCheckLineMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountCheckLineMessage.to_json())

# convert the object into a dict
bank_account_check_line_message_dict = bank_account_check_line_message_instance.to_dict()
# create an instance of BankAccountCheckLineMessage from a dict
bank_account_check_line_message_from_dict = BankAccountCheckLineMessage.from_dict(bank_account_check_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


