# RetailCashUserMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_agreement** | [**UnitAgreementMessage**](UnitAgreementMessage.md) | The unit agreement associated with the retail cash user. | [optional] 
**user** | [**RetailCashUserDataMessage**](RetailCashUserDataMessage.md) | The user data associated with the retail cash user. | [optional] 
**var_property** | [**RetailCashPropertyMessage**](RetailCashPropertyMessage.md) | The property associated with the retail cash user. | [optional] 
**unit** | [**RetailCashUnitMessage**](RetailCashUnitMessage.md) | The unit associated with the retail cash user. | [optional] 
**is_account_created** | **bool** | Whether the user has a retail cash account created. | [optional] 
**is_eviction_pending** | **bool** | Whether the unit agreement associated with the retail cash user has a pending eviction. | [optional] 
**is_enabled** | **bool** | Whether retail cash is enabled for the user. | [optional] 

## Example

```python
from buildium_sdk.models.retail_cash_user_message import RetailCashUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RetailCashUserMessage from a JSON string
retail_cash_user_message_instance = RetailCashUserMessage.from_json(json)
# print the JSON string representation of the object
print(RetailCashUserMessage.to_json())

# convert the object into a dict
retail_cash_user_message_dict = retail_cash_user_message_instance.to_dict()
# create an instance of RetailCashUserMessage from a dict
retail_cash_user_message_from_dict = RetailCashUserMessage.from_dict(retail_cash_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


