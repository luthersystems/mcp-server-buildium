# ApplicationTransactionMessage

This is an object that represents a financial transaction tied to an application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction unique identifier. | [optional] 
**var_date** | **date** | Date of the transaction. | [optional] 
**transaction_type_enum** | **str** | The type of transaction that occurred. | [optional] 
**total_amount** | **float** | Sum of all &#x60;Journal.Lines.Amount&#x60; entries in the transaction. | [optional] 
**check_number** | **str** | Check number associated with the transaction, if applicable. | [optional] 
**application_id** | **int** | Application unique identifier associated with the transaction, if applicable. Null if value is not set. | [optional] 
**payee_applicant_id** | **int** | The payee&#39;s applicant unique identifier associated with the transaction, where applicable. | [optional] 
**payment_method** | **str** | The payment method used for the transaction. | [optional] 
**journal** | [**JournalMessage**](JournalMessage.md) | Journal associated with the transaction. The journal describes how the transaction should be recorded for accounting purposes. | [optional] 

## Example

```python
from buildium_sdk.models.application_transaction_message import ApplicationTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationTransactionMessage from a JSON string
application_transaction_message_instance = ApplicationTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationTransactionMessage.to_json())

# convert the object into a dict
application_transaction_message_dict = application_transaction_message_instance.to_dict()
# create an instance of ApplicationTransactionMessage from a dict
application_transaction_message_from_dict = ApplicationTransactionMessage.from_dict(application_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


