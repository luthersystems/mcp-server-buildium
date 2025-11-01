# GLAccountBalanceMessage

Represents the balance amount of a general ledger account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_balance** | **float** | The sum of transactions across all accounting entities (rental properties, association properties and your company) that are associated with the given general ledger account. | [optional] 
**gl_account** | [**GLAccountMessage**](GLAccountMessage.md) | General ledger account the balance is related to. | [optional] 
**accounting_entity_balances** | [**List[GLAccountBalanceItemMessage]**](GLAccountBalanceItemMessage.md) | A collection of accounting entity balances that make up the &#x60;TotalBalance&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.gl_account_balance_message import GLAccountBalanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccountBalanceMessage from a JSON string
gl_account_balance_message_instance = GLAccountBalanceMessage.from_json(json)
# print the JSON string representation of the object
print(GLAccountBalanceMessage.to_json())

# convert the object into a dict
gl_account_balance_message_dict = gl_account_balance_message_instance.to_dict()
# create an instance of GLAccountBalanceMessage from a dict
gl_account_balance_message_from_dict = GLAccountBalanceMessage.from_dict(gl_account_balance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


