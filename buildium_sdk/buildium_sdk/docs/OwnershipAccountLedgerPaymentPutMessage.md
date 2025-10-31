# OwnershipAccountLedgerPaymentPutMessage

This is an object that represents a Payment made in a particular Ownership Account Ledger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the transaction. The date must be formatted as YYYY-MM-DD. | 
**payment_method** | **str** | The payment method used for the transaction. | 
**payee_user_id** | **int** | The payee&#39;s user unique identifier. | [optional] 
**memo** | **str** | A brief note describing the reason for the payment. The value cannot exceed 65 characters. | [optional] 
**reference_number** | **str** | The reference Number of the transaction. The value cannot exceed 30 characters. | [optional] 
**lines** | [**List[OwnershipAccountLedgerPaymentLineSaveMessage]**](OwnershipAccountLedgerPaymentLineSaveMessage.md) | A collection of line items included in the payment. At least one line item is required. | 

## Example

```python
from buildium_sdk.models.ownership_account_ledger_payment_put_message import OwnershipAccountLedgerPaymentPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountLedgerPaymentPutMessage from a JSON string
ownership_account_ledger_payment_put_message_instance = OwnershipAccountLedgerPaymentPutMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountLedgerPaymentPutMessage.to_json())

# convert the object into a dict
ownership_account_ledger_payment_put_message_dict = ownership_account_ledger_payment_put_message_instance.to_dict()
# create an instance of OwnershipAccountLedgerPaymentPutMessage from a dict
ownership_account_ledger_payment_put_message_from_dict = OwnershipAccountLedgerPaymentPutMessage.from_dict(ownership_account_ledger_payment_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


