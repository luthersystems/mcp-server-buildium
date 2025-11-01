# CreditCardAccountPutMessage

This is an object that represents the request to edit a credit card account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Credit card account name. | 
**description** | **str** | Credit card account description. | [optional] 
**payment_due_day** | **int** | Credit card due day. | [optional] 
**credit_limit** | **float** | Credit card limit. | [optional] 

## Example

```python
from buildium_sdk.models.credit_card_account_put_message import CreditCardAccountPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardAccountPutMessage from a JSON string
credit_card_account_put_message_instance = CreditCardAccountPutMessage.from_json(json)
# print the JSON string representation of the object
print(CreditCardAccountPutMessage.to_json())

# convert the object into a dict
credit_card_account_put_message_dict = credit_card_account_put_message_instance.to_dict()
# create an instance of CreditCardAccountPutMessage from a dict
credit_card_account_put_message_from_dict = CreditCardAccountPutMessage.from_dict(credit_card_account_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


