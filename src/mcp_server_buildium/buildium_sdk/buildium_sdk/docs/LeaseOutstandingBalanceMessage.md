# LeaseOutstandingBalanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_id** | **int** | Lease unique identifier. | [optional] 
**property_id** | **int** | Property unique identifier. | [optional] 
**unit_id** | **int** | Property unit unique identifier. | [optional] 
**balance0_to30_days** | **float** | Outstanding balance due from within the last 30 days. | [optional] 
**balance31_to60_days** | **float** | Outstanding balance due from within 31 to 60 days ago. | [optional] 
**balance61_to90_days** | **float** | Outstanding balance due from within 61 to 90 days ago. | [optional] 
**balance_over90_days** | **float** | Outstanding balance due from over 90 days ago. | [optional] 
**total_balance** | **float** | Total outstanding balance due. | [optional] 
**balances** | [**List[OutstandingBalancesLineMessage]**](OutstandingBalancesLineMessage.md) | Breakdown of outstanding balance due by general ledger account. | [optional] 
**past_due_email_sent_date** | **datetime** | Date of notification for outstanding balance. | [optional] 
**eviction_pending_date** | **date** | Date of notification for pending eviction. | [optional] 
**is_notice_given** | **bool** | Indicates if notice was sent. | [optional] 

## Example

```python
from buildium_sdk.models.lease_outstanding_balance_message import LeaseOutstandingBalanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseOutstandingBalanceMessage from a JSON string
lease_outstanding_balance_message_instance = LeaseOutstandingBalanceMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseOutstandingBalanceMessage.to_json())

# convert the object into a dict
lease_outstanding_balance_message_dict = lease_outstanding_balance_message_instance.to_dict()
# create an instance of LeaseOutstandingBalanceMessage from a dict
lease_outstanding_balance_message_from_dict = LeaseOutstandingBalanceMessage.from_dict(lease_outstanding_balance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


