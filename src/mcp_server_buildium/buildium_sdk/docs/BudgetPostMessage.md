# BudgetPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the budget. | 
**property_id** | **int** | Property unique identifier that the budget belongs to. | 
**start_month** | **str** | The month the fiscal year starts for the budget. | 
**fiscal_year** | **int** | The fiscal year for the budget. The value must be formatted as YYYY. | 
**details** | [**List[BudgetDetailsSaveMessage]**](BudgetDetailsSaveMessage.md) | The financial details associated with the budget. | 

## Example

```python
from buildium_sdk.models.budget_post_message import BudgetPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetPostMessage from a JSON string
budget_post_message_instance = BudgetPostMessage.from_json(json)
# print the JSON string representation of the object
print(BudgetPostMessage.to_json())

# convert the object into a dict
budget_post_message_dict = budget_post_message_instance.to_dict()
# create an instance of BudgetPostMessage from a dict
budget_post_message_from_dict = BudgetPostMessage.from_dict(budget_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


