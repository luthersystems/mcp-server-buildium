# PartialPaymentSettingsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_payments_in_full** | **bool** | Partial payment settings. | [optional] 

## Example

```python
from buildium_sdk.models.partial_payment_settings_message import PartialPaymentSettingsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PartialPaymentSettingsMessage from a JSON string
partial_payment_settings_message_instance = PartialPaymentSettingsMessage.from_json(json)
# print the JSON string representation of the object
print(PartialPaymentSettingsMessage.to_json())

# convert the object into a dict
partial_payment_settings_message_dict = partial_payment_settings_message_instance.to_dict()
# create an instance of PartialPaymentSettingsMessage from a dict
partial_payment_settings_message_from_dict = PartialPaymentSettingsMessage.from_dict(partial_payment_settings_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


