# OutstandingBalancesLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | General ledger account unique identifier. | [optional] 
**total_balance** | **float** | Total balance of the account on the line item. | [optional] 

## Example

```python
from buildium_sdk.models.outstanding_balances_line_message import OutstandingBalancesLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OutstandingBalancesLineMessage from a JSON string
outstanding_balances_line_message_instance = OutstandingBalancesLineMessage.from_json(json)
# print the JSON string representation of the object
print(OutstandingBalancesLineMessage.to_json())

# convert the object into a dict
outstanding_balances_line_message_dict = outstanding_balances_line_message_instance.to_dict()
# create an instance of OutstandingBalancesLineMessage from a dict
outstanding_balances_line_message_from_dict = OutstandingBalancesLineMessage.from_dict(outstanding_balances_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


