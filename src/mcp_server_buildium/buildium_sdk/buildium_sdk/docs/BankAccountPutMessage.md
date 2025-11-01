# BankAccountPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_printing_info** | [**CheckPrintingInfoPutMessage**](CheckPrintingInfoPutMessage.md) | Check printing info. | 
**name** | **str** | Bank account name. | 
**description** | **str** | Bank account description. | [optional] 
**bank_account_type** | **str** | Type of bank account. | 
**country** | **str** | The country the bank account exists in. | 
**account_number** | **str** | Bank account number. | [optional] 
**routing_number** | **str** | Bank routing number. If the bank is in Canada, the routing number should be provided as a zero followed by the three digit institution number, followed by the five digit transit number. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_put_message import BankAccountPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountPutMessage from a JSON string
bank_account_put_message_instance = BankAccountPutMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountPutMessage.to_json())

# convert the object into a dict
bank_account_put_message_dict = bank_account_put_message_instance.to_dict()
# create an instance of BankAccountPutMessage from a dict
bank_account_put_message_from_dict = BankAccountPutMessage.from_dict(bank_account_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


