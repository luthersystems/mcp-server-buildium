# ResidentRequestTaskPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Request title. The title can not exceed 127 characters. | 
**description** | **str** | Request description. The description can not exceed 65500 characters. | [optional] 
**category_id** | **int** | The category identifier to assign the request. | [optional] 
**sub_category_id** | **int** | The subcategory identifier to assign the request. | [optional] 
**unit_agreement_id** | **int** | The unique identifier of the unit agreement associated with the request. | 
**requested_by_entity_id** | **int** | The unique identifier of the resident that submitted the request. | 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the request. The user must be a &#x60;Staff&#x60; user type. If not provided, assignment rules in the resident center settings (if configured) will be used for assignment. | [optional] 
**task_status** | **str** | Request status. | 
**priority** | **str** | Request priority. | 
**due_date** | **date** | Request due date. The date must be formatted as YYYY-MM-DD. | [optional] 
**is_entry_permitted_by_resident** | **bool** | Indicates whether the resident has explicitly granted permission to enter the unit. Set this value to null if the resident has not provided a response. | [optional] 
**does_resident_have_pets** | **bool** | Indicates whether the resident has pets. Set this value to null if the resident has not provided a response. | [optional] 
**resident_entry_notes** | **str** | Notes provided by the resident specific to entering the premises. The value cannot exceed 65535 characters. | [optional] 
**share_with_rental_owners** | **bool** | Indicates whether the request is shared with rental owners (applies to requests for rentals only). Defaults to False if not set or for association requests. | [optional] 
**share_with_board_members** | **bool** | Indicates whether the request is shared with board members (applies to requests for associations only). Defaults to False if not set or for rental requests. | [optional] 

## Example

```python
from buildium_sdk.models.resident_request_task_post_message import ResidentRequestTaskPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ResidentRequestTaskPostMessage from a JSON string
resident_request_task_post_message_instance = ResidentRequestTaskPostMessage.from_json(json)
# print the JSON string representation of the object
print(ResidentRequestTaskPostMessage.to_json())

# convert the object into a dict
resident_request_task_post_message_dict = resident_request_task_post_message_instance.to_dict()
# create an instance of ResidentRequestTaskPostMessage from a dict
resident_request_task_post_message_from_dict = ResidentRequestTaskPostMessage.from_dict(resident_request_task_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


