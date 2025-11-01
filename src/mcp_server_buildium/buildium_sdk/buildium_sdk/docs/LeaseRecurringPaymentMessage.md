# LeaseRecurringPaymentMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the recurring payment schedule. | [optional] 
**lease_id** | **int** | The unique identifier of the lease that the recurring payment will be applied to. | [optional] 
**payer** | [**PayeeMessage**](PayeeMessage.md) | User information for the resident making the payment. | [optional] 
**payment_method** | **str** | The method of payment for the transaction. | [optional] 
**lines** | [**List[RecurringTransactionLineMessage]**](RecurringTransactionLineMessage.md) | Line items describing how the payment is to be allocated when the recurring transaction is processed. | [optional] 
**amount** | **float** | The total amount of the recurring payment based on sum of the &#x60;Lines.Amount&#x60;. | [optional] 
**occurrences_remaining** | **int** | The number of remaining times this recurring payment will be processed. | [optional] 
**first_occurrence_date** | **date** | The date the first occurrence this payment was processed. | [optional] 
**next_occurrence_date** | **date** | The next date the scheduled payment will be processed. | [optional] 
**post_days_in_advance** | **int** | Specifies the number of days ahead of the transaction date the payment will post on the lease ledger. This setting can be used to add the charge to the ledger ahead of the due date for visibility. For example, if the &#x60;FirstOccurrenceDate&#x60; is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022. | [optional] 
**frequency** | **str** | Indicates the frequency at which the recurring payment is processed. | [optional] 
**duration** | **str** | Specifies the period of time/occurrences the recurring payment will be processed. Note, if the &#x60;Frequency&#x60; field is set to &#x60;OneTime&#x60; this field should be set to &#x60;NULL&#x60; as any submitted value will be ignored. | [optional] 
**memo** | **str** | Memo associated with the recurring payment. | [optional] 

## Example

```python
from buildium_sdk.models.lease_recurring_payment_message import LeaseRecurringPaymentMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRecurringPaymentMessage from a JSON string
lease_recurring_payment_message_instance = LeaseRecurringPaymentMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseRecurringPaymentMessage.to_json())

# convert the object into a dict
lease_recurring_payment_message_dict = lease_recurring_payment_message_instance.to_dict()
# create an instance of LeaseRecurringPaymentMessage from a dict
lease_recurring_payment_message_from_dict = LeaseRecurringPaymentMessage.from_dict(lease_recurring_payment_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


