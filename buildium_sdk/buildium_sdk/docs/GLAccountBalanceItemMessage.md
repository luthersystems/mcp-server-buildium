# GLAccountBalanceItemMessage

An object that represents an accounting entity's contribution to the general ledger account total balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | The sum of transactions associated with the general ledger account for the given accounting entity. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | Accounting entity associated with the balance. | [optional] 

## Example

```python
from buildium_sdk.models.gl_account_balance_item_message import GLAccountBalanceItemMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccountBalanceItemMessage from a JSON string
gl_account_balance_item_message_instance = GLAccountBalanceItemMessage.from_json(json)
# print the JSON string representation of the object
print(GLAccountBalanceItemMessage.to_json())

# convert the object into a dict
gl_account_balance_item_message_dict = gl_account_balance_item_message_instance.to_dict()
# create an instance of GLAccountBalanceItemMessage from a dict
gl_account_balance_item_message_from_dict = GLAccountBalanceItemMessage.from_dict(gl_account_balance_item_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


