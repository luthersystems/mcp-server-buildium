# BillLineMessage

Bill line items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The bill line item unique identifier. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | The accounting entity associated with the bill line item. | [optional] 
**gl_account** | [**GLAccountMessage**](GLAccountMessage.md) | The general ledger account the line item is allocated to. | [optional] 
**amount** | **float** | Line item amount. | [optional] 
**markup** | [**BillMarkupMessage**](BillMarkupMessage.md) | Line item mark up. | [optional] 
**memo** | **str** | Description of the line item. | [optional] 

## Example

```python
from buildium_sdk.models.bill_line_message import BillLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of BillLineMessage from a JSON string
bill_line_message_instance = BillLineMessage.from_json(json)
# print the JSON string representation of the object
print(BillLineMessage.to_json())

# convert the object into a dict
bill_line_message_dict = bill_line_message_instance.to_dict()
# create an instance of BillLineMessage from a dict
bill_line_message_from_dict = BillLineMessage.from_dict(bill_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


