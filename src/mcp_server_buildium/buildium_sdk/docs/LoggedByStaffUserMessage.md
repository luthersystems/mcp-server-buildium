# LoggedByStaffUserMessage

The staff member that logged the call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The staff user unique identifier. | [optional] 
**first_name** | **str** | First name of the staff user. | [optional] 
**last_name** | **str** | Last name of the staff user. | [optional] 
**href** | **str** | A link to the staff user resource. | [optional] 

## Example

```python
from buildium_sdk.models.logged_by_staff_user_message import LoggedByStaffUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LoggedByStaffUserMessage from a JSON string
logged_by_staff_user_message_instance = LoggedByStaffUserMessage.from_json(json)
# print the JSON string representation of the object
print(LoggedByStaffUserMessage.to_json())

# convert the object into a dict
logged_by_staff_user_message_dict = logged_by_staff_user_message_instance.to_dict()
# create an instance of LoggedByStaffUserMessage from a dict
logged_by_staff_user_message_from_dict = LoggedByStaffUserMessage.from_dict(logged_by_staff_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


