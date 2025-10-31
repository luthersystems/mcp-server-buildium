# BankAccountCheckPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee** | [**BankAccountCheckPayeeSaveMessage**](BankAccountCheckPayeeSaveMessage.md) | Payee of the transaction. | 
**check_number** | **str** | Check number. | [optional] 
**entry_date** | **date** | Date the check was recorded. | 
**memo** | **str** | Memo associated with the check, if applicable. | [optional] 
**lines** | [**List[BankAccountCheckLineSaveMessage]**](BankAccountCheckLineSaveMessage.md) | A collection of line items to associate with the check. | 

## Example

```python
from buildium_sdk.models.bank_account_check_put_message import BankAccountCheckPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCheckPutMessage from a JSON string
bank_account_check_put_message_instance = BankAccountCheckPutMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountCheckPutMessage.to_json())

# convert the object into a dict
bank_account_check_put_message_dict = bank_account_check_put_message_instance.to_dict()
# create an instance of BankAccountCheckPutMessage from a dict
bank_account_check_put_message_from_dict = BankAccountCheckPutMessage.from_dict(bank_account_check_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


