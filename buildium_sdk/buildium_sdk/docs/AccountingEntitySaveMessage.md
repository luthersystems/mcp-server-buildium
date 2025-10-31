# AccountingEntitySaveMessage

Object to represent an Accounting Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the accounting entity | 
**accounting_entity_type** | **str** | The type of the accounting entity | 
**unit_id** | **int** | The unit unique identifier for the accounting entity. | [optional] 

## Example

```python
from buildium_sdk.models.accounting_entity_save_message import AccountingEntitySaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingEntitySaveMessage from a JSON string
accounting_entity_save_message_instance = AccountingEntitySaveMessage.from_json(json)
# print the JSON string representation of the object
print(AccountingEntitySaveMessage.to_json())

# convert the object into a dict
accounting_entity_save_message_dict = accounting_entity_save_message_instance.to_dict()
# create an instance of AccountingEntitySaveMessage from a dict
accounting_entity_save_message_from_dict = AccountingEntitySaveMessage.from_dict(accounting_entity_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


