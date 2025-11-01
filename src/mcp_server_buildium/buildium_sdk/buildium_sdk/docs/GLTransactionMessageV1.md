# GLTransactionMessageV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | General ledger transaction unique identifier. | [optional] 
**amount** | **float** | General ledger transaction amount. | [optional] 
**check_number** | **str** | General ledger transaction check number. | [optional] 
**entry_date** | **date** | Date the transaction was made. | [optional] 
**memo** | **str** | General ledger transaction memo. | [optional] 

## Example

```python
from buildium_sdk.models.gl_transaction_message_v1 import GLTransactionMessageV1

# TODO update the JSON string below
json = "{}"
# create an instance of GLTransactionMessageV1 from a JSON string
gl_transaction_message_v1_instance = GLTransactionMessageV1.from_json(json)
# print the JSON string representation of the object
print(GLTransactionMessageV1.to_json())

# convert the object into a dict
gl_transaction_message_v1_dict = gl_transaction_message_v1_instance.to_dict()
# create an instance of GLTransactionMessageV1 from a dict
gl_transaction_message_v1_from_dict = GLTransactionMessageV1.from_dict(gl_transaction_message_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


