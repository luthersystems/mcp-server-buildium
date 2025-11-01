# BudgetMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Budget unique identifier. | [optional] 
**name** | **str** | Name of the budget. | [optional] 
**start_date** | **date** | Start date of the budget. | [optional] 
**end_date** | **date** | End date of the budget. | [optional] 
**var_property** | [**PropertyMessage**](PropertyMessage.md) | The property details associated with the budget. | [optional] 
**details** | [**List[BudgetDetailsMessage]**](BudgetDetailsMessage.md) | The details of the budget. | [optional] 

## Example

```python
from buildium_sdk.models.budget_message import BudgetMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetMessage from a JSON string
budget_message_instance = BudgetMessage.from_json(json)
# print the JSON string representation of the object
print(BudgetMessage.to_json())

# convert the object into a dict
budget_message_dict = budget_message_instance.to_dict()
# create an instance of BudgetMessage from a dict
budget_message_from_dict = BudgetMessage.from_dict(budget_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


