# LeaseChargeRecurringTransactionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the recurring charge schedule. | [optional] 
**lease_id** | **int** | The unique identifier of the lease that the recurring charge will be applied to. | [optional] 
**gl_account_id** | **int** | The general ledger account unique identifier the recurring charge is applied to. | [optional] 
**rent_id** | **int** | The unique identifier of the scheduled Rent entity. If the charge is not associated with a Rent entity then the value will be &#x60;NULL&#x60;. | [optional] 
**amount** | **float** | The amount of the recurring charge. | [optional] 
**memo** | **str** | Memo associated with the recurring charge. | [optional] 
**occurrences_remaining** | **int** | The number of remaining times this recurring charge will be processed. | [optional] 
**first_occurrence_date** | **date** | The date the first occurence this charge was processed. | [optional] 
**next_occurrence_date** | **date** | The next date the scheduled charge will be processed. | [optional] 
**post_days_in_advance** | **int** | The number of days ahead of the transaction date the charge will post on the lease ledger. This setting is used to add the charge to the ledger ahead of it&#39;s due date for visibility. For example, if the &#x60;FirstOccurrenceDate&#x60; is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022. | [optional] 
**frequency** | **str** | Specifies the frequency at which the recurring charge will be processed. | [optional] 
**duration** | **str** | Specifies the period of time/occurrences the recurring charge will be processed. Note, if the &#x60;Frequency&#x60; field is set to &#x60;OneTime&#x60; this field should be set to &#x60;NULL&#x60; as any submitted value will be ignored. | [optional] 

## Example

```python
from buildium_sdk.models.lease_charge_recurring_transaction_message import LeaseChargeRecurringTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseChargeRecurringTransactionMessage from a JSON string
lease_charge_recurring_transaction_message_instance = LeaseChargeRecurringTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseChargeRecurringTransactionMessage.to_json())

# convert the object into a dict
lease_charge_recurring_transaction_message_dict = lease_charge_recurring_transaction_message_instance.to_dict()
# create an instance of LeaseChargeRecurringTransactionMessage from a dict
lease_charge_recurring_transaction_message_from_dict = LeaseChargeRecurringTransactionMessage.from_dict(lease_charge_recurring_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


