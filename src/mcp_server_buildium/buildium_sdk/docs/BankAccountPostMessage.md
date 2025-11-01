# BankAccountPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_printing_info** | [**CheckPrintingInfoPostMessage**](CheckPrintingInfoPostMessage.md) | Check printing info. | [optional] 
**name** | **str** | Bank account name. | 
**description** | **str** | Bank account description. | [optional] 
**bank_account_type** | **str** | Type of bank account. | 
**country** | **str** | The country the bank account exists in. | 
**account_number** | **str** | Bank account number. | [optional] 
**routing_number** | **str** | Bank routing number. If the bank is in Canada, the routing number should be provided as a zero followed by the three digit institution number, followed by the five digit transit number. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_post_message import BankAccountPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountPostMessage from a JSON string
bank_account_post_message_instance = BankAccountPostMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountPostMessage.to_json())

# convert the object into a dict
bank_account_post_message_dict = bank_account_post_message_instance.to_dict()
# create an instance of BankAccountPostMessage from a dict
bank_account_post_message_from_dict = BankAccountPostMessage.from_dict(bank_account_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


