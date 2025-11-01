# InternalTransactionStatusMessage

This object represents the status for internal transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_pending** | **bool** | Indicates whether the transaction is pending processing. | [optional] 
**result_date** | **date** | The date the transaction was processed. | [optional] 
**result_code** | **str** | The result code of the transaction. | [optional] 

## Example

```python
from buildium_sdk.models.internal_transaction_status_message import InternalTransactionStatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransactionStatusMessage from a JSON string
internal_transaction_status_message_instance = InternalTransactionStatusMessage.from_json(json)
# print the JSON string representation of the object
print(InternalTransactionStatusMessage.to_json())

# convert the object into a dict
internal_transaction_status_message_dict = internal_transaction_status_message_instance.to_dict()
# create an instance of InternalTransactionStatusMessage from a dict
internal_transaction_status_message_from_dict = InternalTransactionStatusMessage.from_dict(internal_transaction_status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


