# AccountingEntityMessage

An object that represents an accounting entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The accounting entity unique identifier. | [optional] 
**accounting_entity_type** | **str** | The type of accounting entity. | [optional] 
**href** | **str** | A link to the accounting entity resource. | [optional] 
**unit** | [**UnitEntityMessage**](UnitEntityMessage.md) | The unit for the accounting entity. | [optional] 

## Example

```python
from buildium_sdk.models.accounting_entity_message import AccountingEntityMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingEntityMessage from a JSON string
accounting_entity_message_instance = AccountingEntityMessage.from_json(json)
# print the JSON string representation of the object
print(AccountingEntityMessage.to_json())

# convert the object into a dict
accounting_entity_message_dict = accounting_entity_message_instance.to_dict()
# create an instance of AccountingEntityMessage from a dict
accounting_entity_message_from_dict = AccountingEntityMessage.from_dict(accounting_entity_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


