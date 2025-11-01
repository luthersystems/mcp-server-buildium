# ApplicationAutoAllocatedPaymentPostMessage

This is an object that represents an auto-allocated Payment made in a particular application ledger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the transaction. The date must be formatted as YYYY-MM-DD. | 
**payment_method** | **str** | The payment method used for the transaction. | 
**memo** | **str** | A brief note describing the reason for the payment. The value cannot exceed 65 characters. | [optional] 
**reference_number** | **str** | The reference Number of the transaction. The value cannot exceed 30 characters. | [optional] 
**send_email_receipt** | **bool** | An indicator for whether to send an email receipt to the payee. If the payee does not have an email address set, no email will be sent. | 
**total_amount** | **float** | The total amount of the payment being created. | 

## Example

```python
from buildium_sdk.models.application_auto_allocated_payment_post_message import ApplicationAutoAllocatedPaymentPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationAutoAllocatedPaymentPostMessage from a JSON string
application_auto_allocated_payment_post_message_instance = ApplicationAutoAllocatedPaymentPostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationAutoAllocatedPaymentPostMessage.to_json())

# convert the object into a dict
application_auto_allocated_payment_post_message_dict = application_auto_allocated_payment_post_message_instance.to_dict()
# create an instance of ApplicationAutoAllocatedPaymentPostMessage from a dict
application_auto_allocated_payment_post_message_from_dict = ApplicationAutoAllocatedPaymentPostMessage.from_dict(application_auto_allocated_payment_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


