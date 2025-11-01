# BudgetMonthlyAmountsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**january** | **float** | The amount for January. | [optional] 
**february** | **float** | The amount for February. | [optional] 
**march** | **float** | The amount for March. | [optional] 
**april** | **float** | The amount for April. | [optional] 
**may** | **float** | The amount for May. | [optional] 
**june** | **float** | The amount for June. | [optional] 
**july** | **float** | The amount for July. | [optional] 
**august** | **float** | The amount for August. | [optional] 
**september** | **float** | The amount for September. | [optional] 
**october** | **float** | The amount for October. | [optional] 
**november** | **float** | The amount for November. | [optional] 
**december** | **float** | The amount for December. | [optional] 

## Example

```python
from buildium_sdk.models.budget_monthly_amounts_message import BudgetMonthlyAmountsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetMonthlyAmountsMessage from a JSON string
budget_monthly_amounts_message_instance = BudgetMonthlyAmountsMessage.from_json(json)
# print the JSON string representation of the object
print(BudgetMonthlyAmountsMessage.to_json())

# convert the object into a dict
budget_monthly_amounts_message_dict = budget_monthly_amounts_message_instance.to_dict()
# create an instance of BudgetMonthlyAmountsMessage from a dict
budget_monthly_amounts_message_from_dict = BudgetMonthlyAmountsMessage.from_dict(budget_monthly_amounts_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


