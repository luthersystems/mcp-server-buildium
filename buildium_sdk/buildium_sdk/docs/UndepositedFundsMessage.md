# UndepositedFundsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_transaction** | [**GLTransactionMessageV1**](GLTransactionMessageV1.md) | General ledger transaction. | [optional] 

## Example

```python
from buildium_sdk.models.undeposited_funds_message import UndepositedFundsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UndepositedFundsMessage from a JSON string
undeposited_funds_message_instance = UndepositedFundsMessage.from_json(json)
# print the JSON string representation of the object
print(UndepositedFundsMessage.to_json())

# convert the object into a dict
undeposited_funds_message_dict = undeposited_funds_message_instance.to_dict()
# create an instance of UndepositedFundsMessage from a dict
undeposited_funds_message_from_dict = UndepositedFundsMessage.from_dict(undeposited_funds_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


