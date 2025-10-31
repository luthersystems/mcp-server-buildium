# BudgetPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the budget. | 
**details** | [**List[BudgetDetailsSaveMessage]**](BudgetDetailsSaveMessage.md) | The financial details associated with the budget. | 

## Example

```python
from buildium_sdk.models.budget_put_message import BudgetPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetPutMessage from a JSON string
budget_put_message_instance = BudgetPutMessage.from_json(json)
# print the JSON string representation of the object
print(BudgetPutMessage.to_json())

# convert the object into a dict
budget_put_message_dict = budget_put_message_instance.to_dict()
# create an instance of BudgetPutMessage from a dict
budget_put_message_from_dict = BudgetPutMessage.from_dict(budget_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


