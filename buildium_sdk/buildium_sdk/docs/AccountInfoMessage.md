# AccountInfoMessage

This is an object that represents account info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account unique identifier. | [optional] 
**company_name** | **str** | Account company name. | [optional] 
**url** | **str** | Url for this account. | [optional] 
**contact** | [**ContactInfoMessage**](ContactInfoMessage.md) | Account contact information. | [optional] 
**accounting_settings** | [**AccountingSettingsMessage**](AccountingSettingsMessage.md) | Accounting settings. | [optional] 

## Example

```python
from buildium_sdk.models.account_info_message import AccountInfoMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoMessage from a JSON string
account_info_message_instance = AccountInfoMessage.from_json(json)
# print the JSON string representation of the object
print(AccountInfoMessage.to_json())

# convert the object into a dict
account_info_message_dict = account_info_message_instance.to_dict()
# create an instance of AccountInfoMessage from a dict
account_info_message_from_dict = AccountInfoMessage.from_dict(account_info_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


