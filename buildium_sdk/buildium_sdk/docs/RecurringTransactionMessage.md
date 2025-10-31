# RecurringTransactionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the recurring transaction schedule. | [optional] 
**transaction_type** | **str** | Indicates the type of transaction to be applied to the ledger. | [optional] 
**is_expired** | **bool** | Indicates if the recurring transaction schedule has expired. | [optional] 
**rent_id** | **int** | The unique identifier of the scheduled Rent entity. This field is only applicable for &#x60;Charge&#x60; transaction types. | [optional] 
**offsetting_gl_account_id** | **int** | Offsetting general ledger account identifier. The offsetting general ledger account acts as the expense account. Note, this field is only applicable for &#x60;Credit&#x60; transaction types. | [optional] 
**lines** | [**List[RecurringTransactionLineMessage]**](RecurringTransactionLineMessage.md) | Line items describing how the transaction is to be allocated when it is processed. | [optional] 
**amount** | **float** | Total amount of the recurring transaction. | [optional] 
**memo** | **str** | Memo associated with the recurring transaction. | [optional] 
**first_occurrence_date** | **date** | The date the first occurrence of this transaction was processed. | [optional] 
**next_occurrence_date** | **date** | The next date the scheduled transaction will be processed. | [optional] 
**post_days_in_advance** | **int** | The number of days ahead of the transaction date the transaction will post on the lease ledger. This setting is used to add the transaction to the ledger ahead of it&#39;s due date for visibility. For example, if the &#x60;FirstOccurrenceDate&#x60; is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022. | [optional] 
**frequency** | **str** | Indicates the frequency at which the recurring transaction is processed. | [optional] 
**duration** | **str** | Specifies the period of time/occurrences the recurring transaction will be processed. Note, if the &#x60;Frequency&#x60; field is set to &#x60;OneTime&#x60; this field should be set to &#x60;NULL&#x60; as any submitted value will be ignored. | [optional] 

## Example

```python
from buildium_sdk.models.recurring_transaction_message import RecurringTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringTransactionMessage from a JSON string
recurring_transaction_message_instance = RecurringTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(RecurringTransactionMessage.to_json())

# convert the object into a dict
recurring_transaction_message_dict = recurring_transaction_message_instance.to_dict()
# create an instance of RecurringTransactionMessage from a dict
recurring_transaction_message_from_dict = RecurringTransactionMessage.from_dict(recurring_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


