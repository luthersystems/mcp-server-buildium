# RetailCashUserDataMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] 
**first_name** | **str** | User first name. | [optional] 
**last_name** | **str** | User last name. | [optional] 
**email** | **str** | User email address. | [optional] 
**phone** | **str** | User phone number. | [optional] 
**user_type** | **str** | User type. | [optional] 
**href** | **str** | A link to the resource endpoint associated with the user. | [optional] 

## Example

```python
from buildium_sdk.models.retail_cash_user_data_message import RetailCashUserDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RetailCashUserDataMessage from a JSON string
retail_cash_user_data_message_instance = RetailCashUserDataMessage.from_json(json)
# print the JSON string representation of the object
print(RetailCashUserDataMessage.to_json())

# convert the object into a dict
retail_cash_user_data_message_dict = retail_cash_user_data_message_instance.to_dict()
# create an instance of RetailCashUserDataMessage from a dict
retail_cash_user_data_message_from_dict = RetailCashUserDataMessage.from_dict(retail_cash_user_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


