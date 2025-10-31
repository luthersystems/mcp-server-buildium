# ContactRequestTaskMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Request unique identifier. | [optional] 
**category** | [**TaskCategoryResponseMessage**](TaskCategoryResponseMessage.md) | Request category. | [optional] 
**title** | **str** | Request title. | [optional] 
**description** | **str** | Request description. | [optional] 
**var_property** | [**PropertyMessage**](PropertyMessage.md) | The property details associated with the request. | [optional] 
**unit_id** | **int** | The unit unique identifier associated with the request. | [optional] 
**contact_detail** | [**ContactDetailMessage**](ContactDetailMessage.md) | The contact details for the person who submitted the request. | [optional] 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the request. | [optional] 
**task_status** | **str** | Request status. | [optional] 
**priority** | **str** | Request priority. | [optional] 
**due_date** | **date** | Request due date. | [optional] 
**created_date_time** | **datetime** | The date and time the request was created. | [optional] 
**last_updated_date_time** | **datetime** | The date and time the request was last updated. | [optional] 

## Example

```python
from buildium_sdk.models.contact_request_task_message import ContactRequestTaskMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ContactRequestTaskMessage from a JSON string
contact_request_task_message_instance = ContactRequestTaskMessage.from_json(json)
# print the JSON string representation of the object
print(ContactRequestTaskMessage.to_json())

# convert the object into a dict
contact_request_task_message_dict = contact_request_task_message_instance.to_dict()
# create an instance of ContactRequestTaskMessage from a dict
contact_request_task_message_from_dict = ContactRequestTaskMessage.from_dict(contact_request_task_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


