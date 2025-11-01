# BudgetDetailsSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | The general ledger account identifier to record the budget details under. | 
**monthly_amounts** | [**BudgetMonthlyAmountsSaveMessage**](BudgetMonthlyAmountsSaveMessage.md) | The budget detailed as monthly amounts | 

## Example

```python
from buildium_sdk.models.budget_details_save_message import BudgetDetailsSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDetailsSaveMessage from a JSON string
budget_details_save_message_instance = BudgetDetailsSaveMessage.from_json(json)
# print the JSON string representation of the object
print(BudgetDetailsSaveMessage.to_json())

# convert the object into a dict
budget_details_save_message_dict = budget_details_save_message_instance.to_dict()
# create an instance of BudgetDetailsSaveMessage from a dict
budget_details_save_message_from_dict = BudgetDetailsSaveMessage.from_dict(budget_details_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


