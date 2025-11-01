# LeaseLedgerPaymentPostMessage

This is an object that represents a Payment made in a particular lease ledger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the transaction. The date must be formatted as YYYY-MM-DD. | 
**payment_method** | **str** | The payment method used for the transaction. | 
**payee_user_id** | **int** | The payee&#39;s user unique identifier. | [optional] 
**memo** | **str** | A brief note describing the reason for the payment. The value cannot exceed 65 characters. | [optional] 
**reference_number** | **str** | The reference Number of the transaction. The value cannot exceed 30 characters. | [optional] 
**send_email_receipt** | **bool** | An indicator for whether or not to send an email receipt to the payee. If the payee does not have an email address set, no email will be sent. | 
**lines** | [**List[LeaseLedgerPaymentLineSaveMessage]**](LeaseLedgerPaymentLineSaveMessage.md) | A collection of line items included in the payment. At least one line item is required. | 

## Example

```python
from buildium_sdk.models.lease_ledger_payment_post_message import LeaseLedgerPaymentPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerPaymentPostMessage from a JSON string
lease_ledger_payment_post_message_instance = LeaseLedgerPaymentPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerPaymentPostMessage.to_json())

# convert the object into a dict
lease_ledger_payment_post_message_dict = lease_ledger_payment_post_message_instance.to_dict()
# create an instance of LeaseLedgerPaymentPostMessage from a dict
lease_ledger_payment_post_message_from_dict = LeaseLedgerPaymentPostMessage.from_dict(lease_ledger_payment_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


