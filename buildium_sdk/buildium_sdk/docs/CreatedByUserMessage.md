# CreatedByUserMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] 
**first_name** | **str** | First name of the user. | [optional] 
**last_name** | **str** | Last name of the user. | [optional] 
**href** | **str** | A link to the user resource. | [optional] 

## Example

```python
from buildium_sdk.models.created_by_user_message import CreatedByUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedByUserMessage from a JSON string
created_by_user_message_instance = CreatedByUserMessage.from_json(json)
# print the JSON string representation of the object
print(CreatedByUserMessage.to_json())

# convert the object into a dict
created_by_user_message_dict = created_by_user_message_instance.to_dict()
# create an instance of CreatedByUserMessage from a dict
created_by_user_message_from_dict = CreatedByUserMessage.from_dict(created_by_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


