# OwnershipAccountOutstandingBalanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ownership_account_id** | **int** | Ownership account unique identifier. | [optional] 
**association_id** | **int** | Association unique identifier . | [optional] 
**unit_id** | **int** | Association unit unique identifier. | [optional] 
**balance0_to30_days** | **float** | Outstanding balance due from within the last 30 days. | [optional] 
**balance31_to60_days** | **float** | Outstanding balance due from within 31 to 60 days ago. | [optional] 
**balance61_to90_days** | **float** | Outstanding balance due from within 61 to 90 days ago. | [optional] 
**balance_over90_days** | **float** | Outstanding balance due from over 90 days ago. | [optional] 
**total_balance** | **float** | Total outstanding balance due. | [optional] 
**balances** | [**List[OutstandingBalancesLineMessage]**](OutstandingBalancesLineMessage.md) | Breakdown of outstanding balance due by general ledger account. | [optional] 
**past_due_email_sent_date** | **datetime** | Date of notification for outstanding balance. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_outstanding_balance_message import OwnershipAccountOutstandingBalanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountOutstandingBalanceMessage from a JSON string
ownership_account_outstanding_balance_message_instance = OwnershipAccountOutstandingBalanceMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountOutstandingBalanceMessage.to_json())

# convert the object into a dict
ownership_account_outstanding_balance_message_dict = ownership_account_outstanding_balance_message_instance.to_dict()
# create an instance of OwnershipAccountOutstandingBalanceMessage from a dict
ownership_account_outstanding_balance_message_from_dict = OwnershipAccountOutstandingBalanceMessage.from_dict(ownership_account_outstanding_balance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


