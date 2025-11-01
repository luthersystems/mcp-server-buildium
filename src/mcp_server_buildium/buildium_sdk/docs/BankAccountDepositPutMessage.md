# BankAccountDepositPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date the deposit was recorded. | 
**memo** | **str** | Memo associated with the deposit, if applicable. | [optional] 
**lines** | [**List[BankAccountDepositLineSaveMessage]**](BankAccountDepositLineSaveMessage.md) | A collection of line items associated with the deposit. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_deposit_put_message import BankAccountDepositPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDepositPutMessage from a JSON string
bank_account_deposit_put_message_instance = BankAccountDepositPutMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountDepositPutMessage.to_json())

# convert the object into a dict
bank_account_deposit_put_message_dict = bank_account_deposit_put_message_instance.to_dict()
# create an instance of BankAccountDepositPutMessage from a dict
bank_account_deposit_put_message_from_dict = BankAccountDepositPutMessage.from_dict(bank_account_deposit_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


