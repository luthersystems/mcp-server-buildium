# ApplicationReversePaymentChargePostMessage

Non-sufficient funds (NSF) charge to the application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | Income general ledger income account to record the charge under. | 
**total_amount** | **float** | Total amount to charge the applicant. | 

## Example

```python
from buildium_sdk.models.application_reverse_payment_charge_post_message import ApplicationReversePaymentChargePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationReversePaymentChargePostMessage from a JSON string
application_reverse_payment_charge_post_message_instance = ApplicationReversePaymentChargePostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationReversePaymentChargePostMessage.to_json())

# convert the object into a dict
application_reverse_payment_charge_post_message_dict = application_reverse_payment_charge_post_message_instance.to_dict()
# create an instance of ApplicationReversePaymentChargePostMessage from a dict
application_reverse_payment_charge_post_message_from_dict = ApplicationReversePaymentChargePostMessage.from_dict(application_reverse_payment_charge_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


