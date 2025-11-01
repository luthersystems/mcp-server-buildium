# ApplicationPaymentPutMessage

This is an object that represents a Payment made in a particular application ledger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the transaction. The date must be formatted as YYYY-MM-DD. | 
**payment_method** | **str** | The payment method used for the transaction. | 
**memo** | **str** | Memo associated with the payment. The value cannot exceed 65 characters. | [optional] 
**reference_number** | **str** | The reference Number of the transaction. The value cannot exceed 30 characters. | [optional] 
**lines** | [**List[ApplicationPaymentLineSaveMessage]**](ApplicationPaymentLineSaveMessage.md) | A collection of line items included in the payment. At least one line item is required. | 

## Example

```python
from buildium_sdk.models.application_payment_put_message import ApplicationPaymentPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationPaymentPutMessage from a JSON string
application_payment_put_message_instance = ApplicationPaymentPutMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationPaymentPutMessage.to_json())

# convert the object into a dict
application_payment_put_message_dict = application_payment_put_message_instance.to_dict()
# create an instance of ApplicationPaymentPutMessage from a dict
application_payment_put_message_from_dict = ApplicationPaymentPutMessage.from_dict(application_payment_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


