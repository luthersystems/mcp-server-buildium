# LastUpdatedByUserMessage

Last updated details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] 
**first_name** | **str** | User first name. | [optional] 
**last_name** | **str** | User last name. | [optional] 
**href** | **str** | A link to the user resource. | [optional] 
**updated_date_time** | **datetime** | The date and time the note was last updated. | [optional] 

## Example

```python
from buildium_sdk.models.last_updated_by_user_message import LastUpdatedByUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LastUpdatedByUserMessage from a JSON string
last_updated_by_user_message_instance = LastUpdatedByUserMessage.from_json(json)
# print the JSON string representation of the object
print(LastUpdatedByUserMessage.to_json())

# convert the object into a dict
last_updated_by_user_message_dict = last_updated_by_user_message_instance.to_dict()
# create an instance of LastUpdatedByUserMessage from a dict
last_updated_by_user_message_from_dict = LastUpdatedByUserMessage.from_dict(last_updated_by_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


