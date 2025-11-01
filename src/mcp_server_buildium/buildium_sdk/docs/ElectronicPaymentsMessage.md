# ElectronicPaymentsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debit_transaction_limit** | **float** | Debit transaction limit | [optional] 
**credit_transaction_limit** | **float** | Credit transaction limit | [optional] 
**debit_monthly_limit** | **float** | Monthly debt limit | [optional] 
**credit_monthly_limit** | **float** | Monthly credit limit | [optional] 
**resident_eft_convience_fee_amount** | **float** | Fee charged per transaction by EFT | [optional] 
**resident_credit_card_convenience_fee_amount** | **float** | Fee charged per transaction by Credit Card | [optional] 
**credit_card_service_fee_percentage** | **float** | Fee charged for using a Credit Card in transactions | [optional] 
**is_credit_card_service_fee_paid_by_resident** | **bool** | Whether the credit card service fee is paid by residents | [optional] 

## Example

```python
from buildium_sdk.models.electronic_payments_message import ElectronicPaymentsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicPaymentsMessage from a JSON string
electronic_payments_message_instance = ElectronicPaymentsMessage.from_json(json)
# print the JSON string representation of the object
print(ElectronicPaymentsMessage.to_json())

# convert the object into a dict
electronic_payments_message_dict = electronic_payments_message_instance.to_dict()
# create an instance of ElectronicPaymentsMessage from a dict
electronic_payments_message_from_dict = ElectronicPaymentsMessage.from_dict(electronic_payments_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


