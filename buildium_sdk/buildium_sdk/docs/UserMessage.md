# UserMessage

Buildium user account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] 
**user_types** | **List[str]** | The user type assigned to the user account. | [optional] 
**is_active** | **bool** | Indicates whether the user account is still active. | [optional] 
**last_login** | **datetime** | Date and time the user last logged into Buildium. This value will be &#x60;NULL&#x60; if the user has never logged into Buildium. | [optional] 
**first_name** | **str** | First name of the user. | [optional] 
**last_name** | **str** | Last name of the user. | [optional] 
**company_name** | **str** | The company name. | [optional] 
**email** | **str** | Email address of the user. | [optional] 
**alternate_email** | **str** | Alternate email address of user. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers for the user. | [optional] 
**user_role** | [**UserRoleMessage**](UserRoleMessage.md) | The user role assigned to the user. | [optional] 
**is_company** | **bool** | Indicates with the user account represents company versus a person. | [optional] 

## Example

```python
from buildium_sdk.models.user_message import UserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UserMessage from a JSON string
user_message_instance = UserMessage.from_json(json)
# print the JSON string representation of the object
print(UserMessage.to_json())

# convert the object into a dict
user_message_dict = user_message_instance.to_dict()
# create an instance of UserMessage from a dict
user_message_from_dict = UserMessage.from_dict(user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


