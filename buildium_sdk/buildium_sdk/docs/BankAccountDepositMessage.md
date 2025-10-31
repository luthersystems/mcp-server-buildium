# BankAccountDepositMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Deposit unique identifier. | [optional] 
**entry_date** | **date** | Date the deposit was recorded. | [optional] 
**memo** | **str** | Memo associated with the deposit, if applicable. | [optional] 
**total_amount** | **float** | Sum of all &#x60;Journal.Lines.Amount&#x60; entries in the deposit. | [optional] 
**lines** | [**List[BankAccountDepositLineMessage]**](BankAccountDepositLineMessage.md) | A collection of line items associated with the deposit. | [optional] 
**payment_transaction_ids** | **List[int]** | A collection of payment transaction identifiers that were included in this deposit transaction. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_deposit_message import BankAccountDepositMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDepositMessage from a JSON string
bank_account_deposit_message_instance = BankAccountDepositMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountDepositMessage.to_json())

# convert the object into a dict
bank_account_deposit_message_dict = bank_account_deposit_message_instance.to_dict()
# create an instance of BankAccountDepositMessage from a dict
bank_account_deposit_message_from_dict = BankAccountDepositMessage.from_dict(bank_account_deposit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


