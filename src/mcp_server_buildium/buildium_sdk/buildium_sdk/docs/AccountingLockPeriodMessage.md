# AccountingLockPeriodMessage

Accounting lock period settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | [**LockPeriodSettingsGlobalMessage**](LockPeriodSettingsGlobalMessage.md) | Global settings. | [optional] 
**overrides** | [**List[LockPeriodSettingsOverridesMessage]**](LockPeriodSettingsOverridesMessage.md) | Settings overrides for specific properties. | [optional] 
**financial_administrator_user_ids** | **List[int]** | A collection of identifiers for users that have been designated financial administrators. These users will have permission to add, edit, and delete transactions during a locked period. This won&#39;t conflict with any property-level permissions for this account. By default, account administrators have permission to add, edit, and delete transactions within a locked period. | [optional] 

## Example

```python
from buildium_sdk.models.accounting_lock_period_message import AccountingLockPeriodMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingLockPeriodMessage from a JSON string
accounting_lock_period_message_instance = AccountingLockPeriodMessage.from_json(json)
# print the JSON string representation of the object
print(AccountingLockPeriodMessage.to_json())

# convert the object into a dict
accounting_lock_period_message_dict = accounting_lock_period_message_instance.to_dict()
# create an instance of AccountingLockPeriodMessage from a dict
accounting_lock_period_message_from_dict = AccountingLockPeriodMessage.from_dict(accounting_lock_period_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


