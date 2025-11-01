# OwnershipAccountRecurringCreditMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the recurring credit schedule. | [optional] 
**ownership_account_id** | **int** | The unique identifier of the ownership account that the recurring credit will be applied to. | [optional] 
**credit_type** | **str** | Indicates how the credit will be applied.  &lt;ul&gt;&lt;li&gt;WaiveUnpaid - This credit type allows for reversing one or more charges without losing record of what has changed.&lt;/li&gt;&lt;li&gt;Exchange - This credit type allows for one of the following: 1) Reimburse a resident for a out-of-pocket expense, 2) Compensate for a service, 3) Write-off a resident balance considered uncollectable.&lt;/li&gt;&lt;li&gt;PreviouslyDeposited - This credit type allows for issuing a credit against payments that have already been deposited.&lt;/li&gt;&lt;/ul&gt; | [optional] 
**offsetting_gl_account_id** | **int** | Offsetting general ledger account identifier. The offsetting general ledger account acts as the expense account. | [optional] 
**posting_rule_gl_account_id** | **int** | Indicates whether to apply a posting rule when processing the transaction that would only record the credit if a prior payment has been made.        Set the field value to the &lt;b&gt;Rent Income&lt;/b&gt; general ledger account identifier if the credit should only be recorded when a payment was made and applied to the &lt;b&gt;Rent Income&lt;/b&gt; general ledger account.        Set the field value to the &lt;b&gt;Accounts Receivable&lt;/b&gt; general ledger account identifier if the credit should only be recorded when a payment was made and applied to *any* general ledger account.        Set the field value to &lt;b&gt;null&lt;/b&gt; to always record the credit. | [optional] 
**lines** | [**List[RecurringTransactionLineMessage]**](RecurringTransactionLineMessage.md) | Line items describing how the credit is to be allocated when the recurring transaction is processed. | [optional] 
**amount** | **float** | The total amount of the recurring credit based on sum of the &#x60;Lines.Amount&#x60;. | [optional] 
**occurrences_remaining** | **int** | The number of remaining times this recurring credit will be processed. | [optional] 
**first_occurrence_date** | **date** | The date the first occurrence this credit was processed. | [optional] 
**next_occurrence_date** | **date** | The next date the scheduled credit will be processed. | [optional] 
**post_days_in_advance** | **int** | Specifies the number of days ahead of the transaction date the credit will post on the lease ledger. This setting can be used to add the credit to the ledger ahead of the due date for visibility. For example, if the &#x60;FirstOccurrenceDate&#x60; is set to 8/10/2022 and this value is set to 5 then the charge will added to the ledger on 8/5/2022, but will have transaction date of 8/10/2022. | [optional] 
**memo** | **str** | Memo associated with the recurring credit. | [optional] 
**frequency** | **str** | Indicates the frequency at which the recurring credit is processed. | [optional] 
**duration** | **str** | Specifies the period of time/occurrences the recurring credit will be processed. Note, if the &#x60;Frequency&#x60; field is set to &#x60;OneTime&#x60; this field should be set to &#x60;NULL&#x60; as any submitted value will be ignored. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_recurring_credit_message import OwnershipAccountRecurringCreditMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountRecurringCreditMessage from a JSON string
ownership_account_recurring_credit_message_instance = OwnershipAccountRecurringCreditMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountRecurringCreditMessage.to_json())

# convert the object into a dict
ownership_account_recurring_credit_message_dict = ownership_account_recurring_credit_message_instance.to_dict()
# create an instance of OwnershipAccountRecurringCreditMessage from a dict
ownership_account_recurring_credit_message_from_dict = OwnershipAccountRecurringCreditMessage.from_dict(ownership_account_recurring_credit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


