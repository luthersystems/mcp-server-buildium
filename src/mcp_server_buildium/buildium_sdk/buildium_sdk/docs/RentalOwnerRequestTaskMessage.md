# RentalOwnerRequestTaskMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Request unique identifier. | [optional] 
**category** | [**TaskCategoryResponseMessage**](TaskCategoryResponseMessage.md) | Request category. | [optional] 
**title** | **str** | Request title. | [optional] 
**description** | **str** | Request description. | [optional] 
**var_property** | [**PropertyMessage**](PropertyMessage.md) | The property details associated with the request. | [optional] 
**unit_id** | **int** | The unit unique identifier associated with the request. | [optional] 
**requested_by_user_entity** | [**RequestedByUserEntityMessage**](RequestedByUserEntityMessage.md) | The contact details for the rental owner who submitted the request. | [optional] 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the request. | [optional] 
**task_status** | **str** | Request status. | [optional] 
**priority** | **str** | Request priority. | [optional] 
**due_date** | **date** | Request due date. | [optional] 
**created_date_time** | **datetime** | Date and time the request was created. | [optional] 
**last_updated_date_time** | **datetime** | Date and time the request was last updated. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_request_task_message import RentalOwnerRequestTaskMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerRequestTaskMessage from a JSON string
rental_owner_request_task_message_instance = RentalOwnerRequestTaskMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerRequestTaskMessage.to_json())

# convert the object into a dict
rental_owner_request_task_message_dict = rental_owner_request_task_message_instance.to_dict()
# create an instance of RentalOwnerRequestTaskMessage from a dict
rental_owner_request_task_message_from_dict = RentalOwnerRequestTaskMessage.from_dict(rental_owner_request_task_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


