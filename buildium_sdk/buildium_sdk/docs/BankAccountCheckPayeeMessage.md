# BankAccountCheckPayeeMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The payee user identifier. | [optional] 
**type** | **str** | The entity type for the payee. | [optional] 
**href** | **str** | A link to the resource endpoint associated with the payee. | [optional] 

## Example

```python
from buildium_sdk.models.bank_account_check_payee_message import BankAccountCheckPayeeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCheckPayeeMessage from a JSON string
bank_account_check_payee_message_instance = BankAccountCheckPayeeMessage.from_json(json)
# print the JSON string representation of the object
print(BankAccountCheckPayeeMessage.to_json())

# convert the object into a dict
bank_account_check_payee_message_dict = bank_account_check_payee_message_instance.to_dict()
# create an instance of BankAccountCheckPayeeMessage from a dict
bank_account_check_payee_message_from_dict = BankAccountCheckPayeeMessage.from_dict(bank_account_check_payee_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


