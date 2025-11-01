# CreditCardAccountMessage

This object represents a credit card account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the gl account associated with the credit card account. | [optional] 
**name** | **str** | The name of the credit card account. | [optional] 
**description** | **str** | Credit card account description. | [optional] 
**payment_due_day** | **str** | The day of the month that payment is due for the credit card account. | [optional] 
**credit_limit** | **float** | The credit limit for the account. | [optional] 
**is_active** | **bool** | Whether the credit card account is active. | [optional] 
**balance** | **float** | The credit card account current balance. | [optional] 

## Example

```python
from buildium_sdk.models.credit_card_account_message import CreditCardAccountMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardAccountMessage from a JSON string
credit_card_account_message_instance = CreditCardAccountMessage.from_json(json)
# print the JSON string representation of the object
print(CreditCardAccountMessage.to_json())

# convert the object into a dict
credit_card_account_message_dict = credit_card_account_message_instance.to_dict()
# create an instance of CreditCardAccountMessage from a dict
credit_card_account_message_from_dict = CreditCardAccountMessage.from_dict(credit_card_account_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


