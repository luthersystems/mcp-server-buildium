# BankAccountDepositPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date the deposit was recorded. | 
**memo** | **str** | Memo associated with the deposit, if applicable. | [optional] 
**lines** | [**List[BankAccountDepositLineSaveMessage]**](BankAccountDepositLineSaveMessage.md) | A collection of line items to associate with the deposit. | [optional] 
**payment_transaction_ids** | **List[int]** | A collection of payment transaction identifiers that were included in this deposit transaction. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_deposit_post_message import BankAccountDepositPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDepositPostMessage from a JSON string
bank_account_deposit_post_message_instance = BankAccountDepositPostMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountDepositPostMessage.to_json())

# convert the object into a dict
bank_account_deposit_post_message_dict = bank_account_deposit_post_message_instance.to_dict()
# create an instance of BankAccountDepositPostMessage from a dict
bank_account_deposit_post_message_from_dict = BankAccountDepositPostMessage.from_dict(bank_account_deposit_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


