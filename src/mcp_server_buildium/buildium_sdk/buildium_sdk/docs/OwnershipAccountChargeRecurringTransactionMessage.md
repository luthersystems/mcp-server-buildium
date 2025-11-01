# OwnershipAccountChargeRecurringTransactionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the recurring charge schedule. | [optional] 
**ownership_account_id** | **int** | The unique identifier of the ownership account that the recurring charge will be applied to. | [optional] 
**gl_account_id** | **int** | The general ledger account unique identifier the recurring charge is applied to. | [optional] 
**rent_id** | **int** | The unique identifier of the scheduled Rent entity. If the charge is not associated with a Rent entity then the value will be &#x60;NULL&#x60;. | [optional] 
**amount** | **float** | The amount of the recurring charge. | [optional] 
**memo** | **str** | Memo associated with the recurring charge. | [optional] 
**first_occurrence_date** | **date** | The date the first occurence this charge was processed. | [optional] 
**next_occurrence_date** | **date** | The next date the scheduled charge will be processed. | [optional] 
**post_days_in_advance** | **int** | Specifies the number of days ahead of the transaction date the charge will post on the lease ledger. This setting can be used to add the charge to the ledger ahead of the due date for visibility. For example, if the &#x60;FirstOccurrenceDate&#x60; is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022. | [optional] 
**occurrences_remaining** | **int** | The number of remaining times this recurring charge will be processed. | [optional] 
**frequency** | **str** | Indicates the frequency at which the recurring charge is processed. | [optional] 
**duration** | **str** | Specifies the period of time/occurrences the recurring charge will be processed. Note, if the &#x60;Frequency&#x60; field is set to &#x60;OneTime&#x60; this field should be set to &#x60;NULL&#x60; as any submitted value will be ignored. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_charge_recurring_transaction_message import OwnershipAccountChargeRecurringTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountChargeRecurringTransactionMessage from a JSON string
ownership_account_charge_recurring_transaction_message_instance = OwnershipAccountChargeRecurringTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountChargeRecurringTransactionMessage.to_json())

# convert the object into a dict
ownership_account_charge_recurring_transaction_message_dict = ownership_account_charge_recurring_transaction_message_instance.to_dict()
# create an instance of OwnershipAccountChargeRecurringTransactionMessage from a dict
ownership_account_charge_recurring_transaction_message_from_dict = OwnershipAccountChargeRecurringTransactionMessage.from_dict(ownership_account_charge_recurring_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


