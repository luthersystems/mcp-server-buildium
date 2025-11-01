# BudgetDetailsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | The general ledger account unique identifier the budget is related to. | [optional] 
**gl_account_sub_type** | **str** | Describes the subtype of the general ledger account. | [optional] 
**total_amount** | **float** | Sum of all monthly amounts in the budget. | [optional] 
**monthly_amounts** | [**BudgetMonthlyAmountsMessage**](BudgetMonthlyAmountsMessage.md) | The monthly amounts in the budget. | [optional] 

## Example

```python
from buildium_sdk.models.budget_details_message import BudgetDetailsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDetailsMessage from a JSON string
budget_details_message_instance = BudgetDetailsMessage.from_json(json)
# print the JSON string representation of the object
print(BudgetDetailsMessage.to_json())

# convert the object into a dict
budget_details_message_dict = budget_details_message_instance.to_dict()
# create an instance of BudgetDetailsMessage from a dict
budget_details_message_from_dict = BudgetDetailsMessage.from_dict(budget_details_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


