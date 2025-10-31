# ResidentRequestTaskMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Request unique identifier. | [optional] 
**category** | [**TaskCategoryResponseMessage**](TaskCategoryResponseMessage.md) | Request category. | [optional] 
**title** | **str** | Request title. | [optional] 
**description** | **str** | Request description. | [optional] 
**var_property** | [**PropertyMessage**](PropertyMessage.md) | The property details associated with the request. | [optional] 
**unit_id** | **int** | The unit unique identifier associated with the request. | [optional] 
**unit_agreement** | [**UnitAgreementMessage**](UnitAgreementMessage.md) | The unit agreement unique identifier associated with the request. | [optional] 
**requested_by_user_entity** | [**RequestedByUserEntityMessage**](RequestedByUserEntityMessage.md) | The contact details for the resident who submitted the request. | [optional] 
**assigned_to_user_id** | **int** | The unique identifier of the staff user assigned to the request. | [optional] 
**task_status** | **str** | Request status. | [optional] 
**priority** | **str** | Request priority. | [optional] 
**due_date** | **date** | Request due date. | [optional] 
**created_date_time** | **datetime** | The date and time the request was created. | [optional] 
**last_updated_date_time** | **datetime** | The date and time the request was last updated. | [optional] 
**appliance** | [**ApplianceMessage**](ApplianceMessage.md) | Appliance information. | [optional] 
**is_entry_permitted_by_resident** | **bool** | Indicates whether the resident has permitted entry. A null value represents no response was provided from the resident. | [optional] 
**does_resident_have_pets** | **bool** | Indicates whether the resident has pets. A null value represents no response was provided from the resident. | [optional] 
**resident_entry_notes** | **str** | Notes provided by the resident specific to entering the premises. | [optional] 

## Example

```python
from buildium_sdk.models.resident_request_task_message import ResidentRequestTaskMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ResidentRequestTaskMessage from a JSON string
resident_request_task_message_instance = ResidentRequestTaskMessage.from_json(json)
# print the JSON string representation of the object
print(ResidentRequestTaskMessage.to_json())

# convert the object into a dict
resident_request_task_message_dict = resident_request_task_message_instance.to_dict()
# create an instance of ResidentRequestTaskMessage from a dict
resident_request_task_message_from_dict = ResidentRequestTaskMessage.from_dict(resident_request_task_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


