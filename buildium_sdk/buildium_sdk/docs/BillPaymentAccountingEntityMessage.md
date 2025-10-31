# BillPaymentAccountingEntityMessage

The accounting entity associated with the payment line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The accounting entity unique identifier. | [optional] 
**accounting_entity_type** | **str** | Indicates the type of the accounting entity. | [optional] 
**unit_id** | **int** | The unit unique identifier for the accounting entity | [optional] 

## Example

```python
from buildium_sdk.models.bill_payment_accounting_entity_message import BillPaymentAccountingEntityMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentAccountingEntityMessage from a JSON string
bill_payment_accounting_entity_message_instance = BillPaymentAccountingEntityMessage.from_json(json)
# print the JSON string representation of the object
print(BillPaymentAccountingEntityMessage.to_json())

# convert the object into a dict
bill_payment_accounting_entity_message_dict = bill_payment_accounting_entity_message_instance.to_dict()
# create an instance of BillPaymentAccountingEntityMessage from a dict
bill_payment_accounting_entity_message_from_dict = BillPaymentAccountingEntityMessage.from_dict(bill_payment_accounting_entity_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


