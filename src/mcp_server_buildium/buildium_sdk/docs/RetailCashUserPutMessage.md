# RetailCashUserPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether retail cash is enabled for the user. If no retail cash account exists for the user, enabling will create one for the user. You cannot disable a user who does not have an account yet. | 

## Example

```python
from buildium_sdk.models.retail_cash_user_put_message import RetailCashUserPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RetailCashUserPutMessage from a JSON string
retail_cash_user_put_message_instance = RetailCashUserPutMessage.from_json(json)
# print the JSON string representation of the object
print(RetailCashUserPutMessage.to_json())

# convert the object into a dict
retail_cash_user_put_message_dict = retail_cash_user_put_message_instance.to_dict()
# create an instance of RetailCashUserPutMessage from a dict
retail_cash_user_put_message_from_dict = RetailCashUserPutMessage.from_dict(retail_cash_user_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


