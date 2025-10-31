# BankAccountCheckMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Check unique identifier. | [optional] 
**payee** | [**BankAccountCheckPayeeMessage**](BankAccountCheckPayeeMessage.md) | Payee of the check. | [optional] 
**check_number** | **str** | Check number. | [optional] 
**entry_date** | **date** | Date the check was recorded. | [optional] 
**memo** | **str** | Memo associated with the check, if applicable. | [optional] 
**total_amount** | **float** | Sum of all &#x60;Journal.Lines.Amount&#x60; entries in the check. | [optional] 
**lines** | [**List[BankAccountCheckLineMessage]**](BankAccountCheckLineMessage.md) | A collection of line items associated with the check. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_check_message import BankAccountCheckMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCheckMessage from a JSON string
bank_account_check_message_instance = BankAccountCheckMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountCheckMessage.to_json())

# convert the object into a dict
bank_account_check_message_dict = bank_account_check_message_instance.to_dict()
# create an instance of BankAccountCheckMessage from a dict
bank_account_check_message_from_dict = BankAccountCheckMessage.from_dict(bank_account_check_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


