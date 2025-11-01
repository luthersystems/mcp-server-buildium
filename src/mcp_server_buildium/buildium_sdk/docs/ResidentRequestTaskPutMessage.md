# ResidentRequestTaskPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Request title. The title can not exceed 127 characters. | 
**message** | **str** | Description of the request update. The message can not exceed 65500 characters. | [optional] 
**category_id** | **int** | The category identifier to assign the request. | [optional] 
**sub_category_id** | **int** | The subcategory identifier to assign the request. | [optional] 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the request. The user must be a &#x60;Staff&#x60; user type. | [optional] 
**task_status** | **str** | Request status. | 
**priority** | **str** | Request priority. | 
**due_date** | **date** | Request due date. The date must be formatted as YYYY-MM-DD. | [optional] 

## Example

```python
from buildium_sdk.models.resident_request_task_put_message import ResidentRequestTaskPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ResidentRequestTaskPutMessage from a JSON string
resident_request_task_put_message_instance = ResidentRequestTaskPutMessage.from_json(json)
# print the JSON string representation of the object
print(ResidentRequestTaskPutMessage.to_json())

# convert the object into a dict
resident_request_task_put_message_dict = resident_request_task_put_message_instance.to_dict()
# create an instance of ResidentRequestTaskPutMessage from a dict
resident_request_task_put_message_from_dict = ResidentRequestTaskPutMessage.from_dict(resident_request_task_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


