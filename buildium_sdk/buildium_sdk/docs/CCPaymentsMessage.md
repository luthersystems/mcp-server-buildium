# CCPaymentsMessage

Credit card payment settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments_enabled** | **bool** | Indicates whether credit card payments are enabled in the Buildium Resident Center for all residents of this property. | [optional] 

## Example

```python
from buildium_sdk.models.cc_payments_message import CCPaymentsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CCPaymentsMessage from a JSON string
cc_payments_message_instance = CCPaymentsMessage.from_json(json)
# print the JSON string representation of the object
print(CCPaymentsMessage.to_json())

# convert the object into a dict
cc_payments_message_dict = cc_payments_message_instance.to_dict()
# create an instance of CCPaymentsMessage from a dict
cc_payments_message_from_dict = CCPaymentsMessage.from_dict(cc_payments_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


