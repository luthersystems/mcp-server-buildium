# AccountingSettingsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_book_id** | **int** | The accounting book entity unique identifier. | [optional] 
**default_bank_account_id** | **int** | The default bank account unique identifier. | [optional] 
**default_accounting_basis** | **str** | The default accounting basis. | [optional] 
**trust_account_warning** | **str** | Indicates the type of trust account warnings are enable within the account, if any. | [optional] 
**fiscal_year_end_month** | **int** | The month the fiscal year ends. | [optional] 
**fiscal_year_end_day** | **int** | The day the fiscal year ends. | [optional] 

## Example

```python
from buildium_sdk.models.accounting_settings_message import AccountingSettingsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingSettingsMessage from a JSON string
accounting_settings_message_instance = AccountingSettingsMessage.from_json(json)
# print the JSON string representation of the object
print(AccountingSettingsMessage.to_json())

# convert the object into a dict
accounting_settings_message_dict = accounting_settings_message_instance.to_dict()
# create an instance of AccountingSettingsMessage from a dict
accounting_settings_message_from_dict = AccountingSettingsMessage.from_dict(accounting_settings_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


