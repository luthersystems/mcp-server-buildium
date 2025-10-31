# CCPaymentsPutMessage

Credit card payment settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments_enabled** | **bool** | Indicates whether credit card payments are enabled in the Buildium Resident Center for all residents of this property. Note, to enable credit card payments the operating bank account for the property must have credit card payments provisioned. | 

## Example

```python
from buildium_sdk.models.cc_payments_put_message import CCPaymentsPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CCPaymentsPutMessage from a JSON string
cc_payments_put_message_instance = CCPaymentsPutMessage.from_json(json)
# print the JSON string representation of the object
print(CCPaymentsPutMessage.to_json())

# convert the object into a dict
cc_payments_put_message_dict = cc_payments_put_message_instance.to_dict()
# create an instance of CCPaymentsPutMessage from a dict
cc_payments_put_message_from_dict = CCPaymentsPutMessage.from_dict(cc_payments_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


