# LockPeriodSettingsOverridesMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**PropertyMessage**](PropertyMessage.md) | The property to which the override will be applied. | [optional] 
**lock_date** | **date** | Accounting transactions related to the property specified in the Property field on or prior to this date will be locked. | [optional] 

## Example

```python
from buildium_sdk.models.lock_period_settings_overrides_message import LockPeriodSettingsOverridesMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LockPeriodSettingsOverridesMessage from a JSON string
lock_period_settings_overrides_message_instance = LockPeriodSettingsOverridesMessage.from_json(json)
# print the JSON string representation of the object
print(LockPeriodSettingsOverridesMessage.to_json())

# convert the object into a dict
lock_period_settings_overrides_message_dict = lock_period_settings_overrides_message_instance.to_dict()
# create an instance of LockPeriodSettingsOverridesMessage from a dict
lock_period_settings_overrides_message_from_dict = LockPeriodSettingsOverridesMessage.from_dict(lock_period_settings_overrides_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


