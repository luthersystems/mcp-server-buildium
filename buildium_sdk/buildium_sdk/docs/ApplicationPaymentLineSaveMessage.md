# ApplicationPaymentLineSaveMessage

This is an object that represents a line item on an application ledger payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | 
**gl_account_id** | **int** | The general ledger account identifier under which the line item amount will be recorded. | 

## Example

```python
from buildium_sdk.models.application_payment_line_save_message import ApplicationPaymentLineSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationPaymentLineSaveMessage from a JSON string
application_payment_line_save_message_instance = ApplicationPaymentLineSaveMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationPaymentLineSaveMessage.to_json())

# convert the object into a dict
application_payment_line_save_message_dict = application_payment_line_save_message_instance.to_dict()
# create an instance of ApplicationPaymentLineSaveMessage from a dict
application_payment_line_save_message_from_dict = ApplicationPaymentLineSaveMessage.from_dict(application_payment_line_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


