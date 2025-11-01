# BudgetMonthlyAmountsSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**january** | **float** | The amount for January. | 
**february** | **float** | The amount for February. | 
**march** | **float** | The amount for March. | 
**april** | **float** | The amount for April. | 
**may** | **float** | The amount for May. | 
**june** | **float** | The amount for June. | 
**july** | **float** | The amount for July. | 
**august** | **float** | The amount for August. | 
**september** | **float** | The amount for September. | 
**october** | **float** | The amount for October. | 
**november** | **float** | The amount for November. | 
**december** | **float** | The amount for December. | 

## Example

```python
from buildium_sdk.models.budget_monthly_amounts_save_message import BudgetMonthlyAmountsSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetMonthlyAmountsSaveMessage from a JSON string
budget_monthly_amounts_save_message_instance = BudgetMonthlyAmountsSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BudgetMonthlyAmountsSaveMessage.to_json())

# convert the object into a dict
budget_monthly_amounts_save_message_dict = budget_monthly_amounts_save_message_instance.to_dict()
# create an instance of BudgetMonthlyAmountsSaveMessage from a dict
budget_monthly_amounts_save_message_from_dict = BudgetMonthlyAmountsSaveMessage.from_dict(budget_monthly_amounts_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


