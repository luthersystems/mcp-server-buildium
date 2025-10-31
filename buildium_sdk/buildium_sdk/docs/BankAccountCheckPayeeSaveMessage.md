# BankAccountCheckPayeeSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The payee user identifier. | 
**type** | **str** | The payee entity type. | 

## Example

```python
from buildium_sdk.models.bank_account_check_payee_save_message import BankAccountCheckPayeeSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCheckPayeeSaveMessage from a JSON string
bank_account_check_payee_save_message_instance = BankAccountCheckPayeeSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountCheckPayeeSaveMessage.to_json())

# convert the object into a dict
bank_account_check_payee_save_message_dict = bank_account_check_payee_save_message_instance.to_dict()
# create an instance of BankAccountCheckPayeeSaveMessage from a dict
bank_account_check_payee_save_message_from_dict = BankAccountCheckPayeeSaveMessage.from_dict(bank_account_check_payee_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


