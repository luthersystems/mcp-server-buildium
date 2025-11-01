# RequestedByUserEntityMessage

Entity information for the user that submitted the task request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entity type. | [optional] 
**id** | **int** | Entity identifier. | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**is_company** | **bool** | Indicates whether entity is a company. | [optional] 
**href** | **str** | A link to the entity resource. | [optional] 

## Example

```python
from buildium_sdk.models.requested_by_user_entity_message import RequestedByUserEntityMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedByUserEntityMessage from a JSON string
requested_by_user_entity_message_instance = RequestedByUserEntityMessage.from_json(json)
# print the JSON string representation of the object
print(RequestedByUserEntityMessage.to_json())

# convert the object into a dict
requested_by_user_entity_message_dict = requested_by_user_entity_message_instance.to_dict()
# create an instance of RequestedByUserEntityMessage from a dict
requested_by_user_entity_message_from_dict = RequestedByUserEntityMessage.from_dict(requested_by_user_entity_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


