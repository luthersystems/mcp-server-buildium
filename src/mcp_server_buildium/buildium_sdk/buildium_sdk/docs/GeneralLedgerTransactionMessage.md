# GeneralLedgerTransactionMessage

This is an object that represents a financial transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction unique identifier. | [optional] 
**var_date** | **date** | Date of the transaction. | [optional] 
**transaction_type** | **str** | Type of transaction that occurred | [optional] 
**total_amount** | **float** | Sum of all &#x60;Journal.Lines.Amount&#x60; entries in the transaction. | [optional] 
**check_number** | **str** | Check number associated with the transaction, if applicable. | [optional] 
**unit_agreement** | [**UnitAgreementMessage**](UnitAgreementMessage.md) | The unit agreement associated with the transaction, if applicable. Null if value is not set. | [optional] 
**unit_id** | **int** | Unit unique identifier associated with the transaction, if applicable. Null if value is not set. | [optional] 
**unit_number** | **str** | Unit number associated with the transaction, if applicable. Null if value is not set. | [optional] 
**payment_detail** | [**PaymentDetailMessage**](PaymentDetailMessage.md) | The payment details associated with the transaction. | [optional] 
**deposit_details** | [**DepositDetailMessage**](DepositDetailMessage.md) | The deposit details associated with the transaction. | [optional] 
**application** | [**ApplicationReferenceMessage**](ApplicationReferenceMessage.md) | The application associated with the transaction in case of an application transaction. Null if it is not an application transaction. | [optional] 
**journal** | [**GeneralLedgerJournalMessage**](GeneralLedgerJournalMessage.md) | Journal associated with the transaction. The journal describes how the transaction should be recorded for accounting purposes. | [optional] 
**last_updated_date_time** | **datetime** | The date and time the transaction was last updated. | [optional] 

## Example

```python
from buildium_sdk.models.general_ledger_transaction_message import GeneralLedgerTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerTransactionMessage from a JSON string
general_ledger_transaction_message_instance = GeneralLedgerTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerTransactionMessage.to_json())

# convert the object into a dict
general_ledger_transaction_message_dict = general_ledger_transaction_message_instance.to_dict()
# create an instance of GeneralLedgerTransactionMessage from a dict
general_ledger_transaction_message_from_dict = GeneralLedgerTransactionMessage.from_dict(general_ledger_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


