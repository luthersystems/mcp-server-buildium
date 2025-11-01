# UserRoleMessage

User role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User role unique identifier. | [optional] 
**name** | **str** | User role name. | [optional] 
**description** | **str** | User role description. | [optional] 
**number_of_users** | **int** | Number of users assigned to this user role. | [optional] 

## Example

```python
from buildium_sdk.models.user_role_message import UserRoleMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleMessage from a JSON string
user_role_message_instance = UserRoleMessage.from_json(json)
# print the JSON string representation of the object
print(UserRoleMessage.to_json())

# convert the object into a dict
user_role_message_dict = user_role_message_instance.to_dict()
# create an instance of UserRoleMessage from a dict
user_role_message_from_dict = UserRoleMessage.from_dict(user_role_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


