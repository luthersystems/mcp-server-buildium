# BankAccountMessage

This is an object that represents a bank account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bank account unique identifier. | [optional] 
**gl_account** | [**GLAccountMessage**](GLAccountMessage.md) | General ledger account. | [optional] 
**check_printing_info** | [**CheckPrintingInfoMessage**](CheckPrintingInfoMessage.md) | Check printing info. | [optional] 
**electronic_payments** | [**ElectronicPaymentsMessage**](ElectronicPaymentsMessage.md) | Electronic Payments. | [optional] 
**name** | **str** | Bank Account name. | [optional] 
**description** | **str** | Bank account description. | [optional] 
**bank_account_type** | **str** | Type of bank account. Values are &#x60;Checking&#x60; or &#x60;Savings&#x60;. | [optional] 
**country** | **str** | The country the bank account is in. | [optional] 
**account_number** | **str** | Bank account number. | [optional] 
**routing_number** | **str** | Bank routing number. | [optional] 
**is_active** | **bool** | Bank Account Status | [optional] 
**balance** | **float** | Bank Account balance | [optional] 
**account_number_unmasked** | **str** | Unmasked bank account number | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_message import BankAccountMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountMessage from a JSON string
bank_account_message_instance = BankAccountMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountMessage.to_json())

# convert the object into a dict
bank_account_message_dict = bank_account_message_instance.to_dict()
# create an instance of BankAccountMessage from a dict
bank_account_message_from_dict = BankAccountMessage.from_dict(bank_account_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


