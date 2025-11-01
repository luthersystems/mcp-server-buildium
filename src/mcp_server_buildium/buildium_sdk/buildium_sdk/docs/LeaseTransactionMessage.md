# LeaseTransactionMessage

This is an object that represents a financial transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction unique identifier. | [optional] 
**var_date** | **date** | Date of the transaction. | [optional] 
**transaction_type** | **str** | Type of transaction that occurred. | [optional] 
**transaction_type_enum** | **str** | The type of transaction that occurred. | [optional] 
**total_amount** | **float** | Sum of all &#x60;Journal.Lines.Amount&#x60; entries in the transaction. | [optional] 
**check_number** | **str** | Check number associated with the transaction, if applicable. | [optional] 
**lease_id** | **int** | Lease unique identifier associated with the transaction, if applicable. Null if value is not set. | [optional] 
**payee_tenant_id** | **int** | The payee&#39;s tenant unique identifier associated with the transaction, where applicable. | [optional] 
**payment_method** | **str** | The payment method used for the transaction. | [optional] 
**journal** | [**JournalMessage**](JournalMessage.md) | Journal associated with the transaction. The journal describes how the transaction should be recorded for accounting purposes. | [optional] 

## Example

```python
from buildium_sdk.models.lease_transaction_message import LeaseTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseTransactionMessage from a JSON string
lease_transaction_message_instance = LeaseTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseTransactionMessage.to_json())

# convert the object into a dict
lease_transaction_message_dict = lease_transaction_message_instance.to_dict()
# create an instance of LeaseTransactionMessage from a dict
lease_transaction_message_from_dict = LeaseTransactionMessage.from_dict(lease_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


