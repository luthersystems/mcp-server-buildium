# PaidByMessage

Transaction line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | Accounting entity associated with the line item. | [optional] 
**amount** | **float** | Amount of the line item. | [optional] 

## Example

```python
from buildium_sdk.models.paid_by_message import PaidByMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PaidByMessage from a JSON string
paid_by_message_instance = PaidByMessage.from_json(json)
# print the JSON string representation of the object
print(PaidByMessage.to_json())

# convert the object into a dict
paid_by_message_dict = paid_by_message_instance.to_dict()
# create an instance of PaidByMessage from a dict
paid_by_message_from_dict = PaidByMessage.from_dict(paid_by_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


