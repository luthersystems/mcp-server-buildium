# GLAccountPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the general ledger account. The name cannot exceed 50 characters and must be unique across all general ledger accounts. | 
**sub_type** | **str** | Describes the subtype of the general ledger account. | 
**parent_gl_account_id** | **int** | Unique identifier of the parent general ledger account. Indicates if this is a sub general ledger account. | [optional] 
**is_cash_asset** | **bool** | Indicates if an account is a Cash Asset. Can only have a value if SubType is &#x60;CurrentAsset&#x60; | [optional] 
**account_number** | **str** | General ledger account number. The account number cannot exceed 12 characters and must be unique across all general ledger accounts. | [optional] 
**description** | **str** | Description of the general ledger account. The description cannot exceed 250 characters. | [optional] 
**is_contra_account** | **bool** | Indicates whether the account is a contra account. Must be null if &#x60;IsCashAsset&#x60; field is set to true. | [optional] 
**cash_flow_classification** | **str** | Describes the cash flow classification for the general ledger account. Must be null if &#x60;IsCashAsset&#x60; field is set to true. | [optional] 

## Example

```python
from buildium_sdk.models.gl_account_put_message import GLAccountPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccountPutMessage from a JSON string
gl_account_put_message_instance = GLAccountPutMessage.from_json(json)
# print the JSON string representation of the object
print(GLAccountPutMessage.to_json())

# convert the object into a dict
gl_account_put_message_dict = gl_account_put_message_instance.to_dict()
# create an instance of GLAccountPutMessage from a dict
gl_account_put_message_from_dict = GLAccountPutMessage.from_dict(gl_account_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


