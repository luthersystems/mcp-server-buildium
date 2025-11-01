# GLAccountMessage

A message that represents a general ledger account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | General ledger account unique identifier. | [optional] 
**account_number** | **str** | General ledger account number. | [optional] 
**name** | **str** | Name of the general ledger account. | [optional] 
**description** | **str** | Description of the general ledger account. | [optional] 
**type** | **str** | Describes the type of general ledger account. | [optional] 
**sub_type** | **str** | Describes the subtype of the general ledger account. | [optional] 
**is_default_gl_account** | **bool** | Indicates if the general ledger account is a default for auto populating fields. | [optional] 
**default_account_name** | **str** | Indicates the original name of the general ledger account if it is a default account. | [optional] 
**is_contra_account** | **bool** | Indicates whether the account is a contra account. | [optional] 
**is_bank_account** | **bool** | Indicates whether the account is a bank account. | [optional] 
**cash_flow_classification** | **str** | Describes the cash flow classification for the general ledger account. | [optional] 
**exclude_from_cash_balances** | **bool** | Indicates whether transactions associated with the account should be excluded from cash balances. | [optional] 
**sub_accounts** | [**List[GLAccountMessage]**](GLAccountMessage.md) | Children general ledger accounts. The relationship only goes one level deep. | [optional] 
**is_active** | **bool** | Indicates whether the account is active. | [optional] 
**parent_gl_account_id** | **int** | Unique identifier of the parent general ledger account, if applicable. | [optional] 

## Example

```python
from buildium_sdk.models.gl_account_message import GLAccountMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccountMessage from a JSON string
gl_account_message_instance = GLAccountMessage.from_json(json)
# print the JSON string representation of the object
print(GLAccountMessage.to_json())

# convert the object into a dict
gl_account_message_dict = gl_account_message_instance.to_dict()
# create an instance of GLAccountMessage from a dict
gl_account_message_from_dict = GLAccountMessage.from_dict(gl_account_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


