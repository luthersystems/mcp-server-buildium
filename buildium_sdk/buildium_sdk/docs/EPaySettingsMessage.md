# EPaySettingsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eft_payments** | [**EFTPaymentsMessage**](EFTPaymentsMessage.md) | The property EFT payment settings. | [optional] 
**credit_card_payments** | [**CCPaymentsMessage**](CCPaymentsMessage.md) | The property credit card payment settings. | [optional] 
**offline_payments** | [**OfflinePaymentsMessage**](OfflinePaymentsMessage.md) | The property offline payment settings. | [optional] 

## Example

```python
from buildium_sdk.models.e_pay_settings_message import EPaySettingsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EPaySettingsMessage from a JSON string
e_pay_settings_message_instance = EPaySettingsMessage.from_json(json)
# print the JSON string representation of the object
print(EPaySettingsMessage.to_json())

# convert the object into a dict
e_pay_settings_message_dict = e_pay_settings_message_instance.to_dict()
# create an instance of EPaySettingsMessage from a dict
e_pay_settings_message_from_dict = EPaySettingsMessage.from_dict(e_pay_settings_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


