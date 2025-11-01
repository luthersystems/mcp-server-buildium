# PartialPaymentSettingsPatchMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_payments_in_full** | **bool** | Whether or not the ownership account payments are required in full. | [optional] 

## Example

```python
from buildium_sdk.models.partial_payment_settings_patch_message import PartialPaymentSettingsPatchMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PartialPaymentSettingsPatchMessage from a JSON string
partial_payment_settings_patch_message_instance = PartialPaymentSettingsPatchMessage.from_json(json)
# print the JSON string representation of the object
print(PartialPaymentSettingsPatchMessage.to_json())

# convert the object into a dict
partial_payment_settings_patch_message_dict = partial_payment_settings_patch_message_instance.to_dict()
# create an instance of PartialPaymentSettingsPatchMessage from a dict
partial_payment_settings_patch_message_from_dict = PartialPaymentSettingsPatchMessage.from_dict(partial_payment_settings_patch_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


