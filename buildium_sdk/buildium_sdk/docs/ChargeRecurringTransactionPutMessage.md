# ChargeRecurringTransactionPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the charge. | 
**gl_account_id** | **int** | The general ledger account unique identifier under which the charge amount will be recorded. The general ledger account can only be an income or liability account. | 
**amount** | **float** | The amount to record when applying the charge to the lease ledger. | 
**memo** | **str** | Memo associated with the recurring charge. This value cannot exceed 65 characters. | [optional] 
**first_occurrence_date** | **date** | The date the charge will first be processed. This value along with the &#x60;Frequency&#x60; is also used as the basis for the date set on the transactions in future occurrences. | 
**post_days_in_advance** | **int** | Specifies the number of days ahead of the transaction date the charge will post on the lease ledger. This setting can be used to add the charge to the ledger ahead of the due date for visibility. For example, if the &#x60;FirstOccurrenceDate&#x60; is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022. Note, the value must be between 0 to 45 or set to 60, 75 or 90. | 
**frequency** | **str** | Specifies the frequency at which the recurring charge will be processed. | 
**duration** | **str** | Specifies the period of time/occurrences the recurring payment will be processed. Note, if the &#x60;Frequency&#x60; field is set to &#x60;OneTime&#x60; this field should be set to &#x60;NULL&#x60; as any submitted value will be ignored. | [optional] 
**number_of_occurrences** | **int** | Indicates the number of times the recurring transaction should be processed. This value is required if the &#x60;Duration&#x60; field is set to &#x60;SpecificNumber&#x60;. This value can not exceed 100. | [optional] 

## Example

```python
from buildium_sdk.models.charge_recurring_transaction_put_message import ChargeRecurringTransactionPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeRecurringTransactionPutMessage from a JSON string
charge_recurring_transaction_put_message_instance = ChargeRecurringTransactionPutMessage.from_json(json)
# print the JSON string representation of the object
print(ChargeRecurringTransactionPutMessage.to_json())

# convert the object into a dict
charge_recurring_transaction_put_message_dict = charge_recurring_transaction_put_message_instance.to_dict()
# create an instance of ChargeRecurringTransactionPutMessage from a dict
charge_recurring_transaction_put_message_from_dict = ChargeRecurringTransactionPutMessage.from_dict(charge_recurring_transaction_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


