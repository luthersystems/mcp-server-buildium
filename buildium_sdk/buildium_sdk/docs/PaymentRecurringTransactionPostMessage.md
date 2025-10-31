# PaymentRecurringTransactionPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_user_id** | **int** | The unique identifier of the user making the payment. | [optional] 
**payment_method** | **str** | The payment method for the transaction. | 
**lines** | [**List[RecurringTransactionLinePostMessage]**](RecurringTransactionLinePostMessage.md) | Line items describing how the payment is to be allocated when the payment is processed. | [optional] 
**memo** | **str** | Memo associated with the recurring payment. This value cannot exceed 65 characters. | [optional] 
**first_occurrence_date** | **date** | The date the payment will first be processed. This value along with the &#x60;Frequency&#x60; is also used as the basis for the date set on the transactions in future occurrences. | 
**post_days_in_advance** | **int** | Specifies the number of days ahead of the transaction date the payment will post on the lease ledger. This setting can be used to add the payment to the ledger ahead of the due date for visibility. For example, if the &#x60;FirstOccurrenceDate&#x60; is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022. Note, the value must be between 0 to 45 or set to 60, 75 or 90. | 
**frequency** | **str** | Specifies the frequency at which the recurring payment will be processed. | 
**duration** | **str** | Specifies the period of time/occurrences the recurring payment will be processed. Note, if the &#x60;Frequency&#x60; field is set to &#x60;OneTime&#x60; this field should be set to &#x60;NULL&#x60; as any submitted value will be ignored. | [optional] 
**number_of_occurrences** | **int** | Indicates the number of times the recurring payment should be processed. This value is required if the &#x60;Duration&#x60; field is set to &#x60;SpecificNumber&#x60;. This value can not exceed 100. | [optional] 

## Example

```python
from buildium_sdk.models.payment_recurring_transaction_post_message import PaymentRecurringTransactionPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRecurringTransactionPostMessage from a JSON string
payment_recurring_transaction_post_message_instance = PaymentRecurringTransactionPostMessage.from_json(json)
# print the JSON string representation of the object
print(PaymentRecurringTransactionPostMessage.to_json())

# convert the object into a dict
payment_recurring_transaction_post_message_dict = payment_recurring_transaction_post_message_instance.to_dict()
# create an instance of PaymentRecurringTransactionPostMessage from a dict
payment_recurring_transaction_post_message_from_dict = PaymentRecurringTransactionPostMessage.from_dict(payment_recurring_transaction_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


