# EPaySettingsPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eft_payments** | [**EFTPaymentsPutMessage**](EFTPaymentsPutMessage.md) | The property EFT payment settings. | 
**credit_card_payments** | [**CCPaymentsPutMessage**](CCPaymentsPutMessage.md) | The property credit card payment settings. | 
**offline_payments** | [**OfflinePaymentsPutMessage**](OfflinePaymentsPutMessage.md) | The property offline payment settings. | 

## Example

```python
from buildium_sdk.models.e_pay_settings_put_message import EPaySettingsPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EPaySettingsPutMessage from a JSON string
e_pay_settings_put_message_instance = EPaySettingsPutMessage.from_json(json)
# print the JSON string representation of the object
print(EPaySettingsPutMessage.to_json())

# convert the object into a dict
e_pay_settings_put_message_dict = e_pay_settings_put_message_instance.to_dict()
# create an instance of EPaySettingsPutMessage from a dict
e_pay_settings_put_message_from_dict = EPaySettingsPutMessage.from_dict(e_pay_settings_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


