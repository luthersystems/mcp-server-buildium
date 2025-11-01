# LockPeriodSettingsGlobalMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_date** | **date** | Financial transactions on or prior to this date will be locked. | [optional] 

## Example

```python
from buildium_sdk.models.lock_period_settings_global_message import LockPeriodSettingsGlobalMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LockPeriodSettingsGlobalMessage from a JSON string
lock_period_settings_global_message_instance = LockPeriodSettingsGlobalMessage.from_json(json)
# print the JSON string representation of the object
print(LockPeriodSettingsGlobalMessage.to_json())

# convert the object into a dict
lock_period_settings_global_message_dict = lock_period_settings_global_message_instance.to_dict()
# create an instance of LockPeriodSettingsGlobalMessage from a dict
lock_period_settings_global_message_from_dict = LockPeriodSettingsGlobalMessage.from_dict(lock_period_settings_global_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


