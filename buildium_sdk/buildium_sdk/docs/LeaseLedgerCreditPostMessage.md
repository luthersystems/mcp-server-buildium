# LeaseLedgerCreditPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the transaction. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | Description of the transaction. The value cannot exceed 65 characters. | [optional] 
**credit_type** | **str** | Indicates how the credit should be applied.  &lt;ul&gt;&lt;li&gt;WaiveUnpaid - This credit type allows for reversing one or more charges without losing record of what has changed.&lt;/li&gt;&lt;li&gt;Exchange - This credit type allows for one of the following: 1) Reimburse a resident for a out-of-pocket expense, 2) Compensate for a service, 3) Write-off a resident balance considered uncollectable.&lt;/li&gt;&lt;li&gt;PreviouslyDeposited - This credit type allows for issuing a credit against payments that have already been deposited.&lt;/li&gt;&lt;/ul&gt; | 
**offsetting_gl_account_id** | **int** | Sets the offsetting general ledger account identifier for the credit.    This value must be provided when the &#x60;CreditType&#x60; field is set to &#x60;Exchange&#x60; or &#x60;PreviouslyDeposited&#x60;.    When the &#x60;CreditType&#x60; is &#x60;Exchange&#x60; this must be an *expense* general ledger account type.    When the &#x60;CreditType&#x60; is &#x60;PreviouslyDeposited&#x60; this must be an *equity* general ledger account type. | [optional] 
**lines** | [**List[LeaseLedgerCreditLinePostMessage]**](LeaseLedgerCreditLinePostMessage.md) | A collection of line items included in the credit. At least one line item is required. | 

## Example

```python
from buildium_sdk.models.lease_ledger_credit_post_message import LeaseLedgerCreditPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerCreditPostMessage from a JSON string
lease_ledger_credit_post_message_instance = LeaseLedgerCreditPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerCreditPostMessage.to_json())

# convert the object into a dict
lease_ledger_credit_post_message_dict = lease_ledger_credit_post_message_instance.to_dict()
# create an instance of LeaseLedgerCreditPostMessage from a dict
lease_ledger_credit_post_message_from_dict = LeaseLedgerCreditPostMessage.from_dict(lease_ledger_credit_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


