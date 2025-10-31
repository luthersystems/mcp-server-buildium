# AssociationArchitecturalRequestMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Architectural request unique identifier. | [optional] 
**association_id** | **int** | Association unique identifier. | [optional] 
**ownership_account_id** | **int** | Ownership account unique identifier. | [optional] 
**name** | **str** | Architectural request name. | [optional] 
**submitted_date_time** | **datetime** | Date and time the architectural request was submitted. | [optional] 
**status** | **str** | Status of the architectural request. | [optional] 
**decision** | **str** | Decision of the architectural request. | [optional] 
**created_date_time** | **datetime** | Date and time the architectural request was created. | [optional] 
**created_by_user** | [**CreatedByUserMessage**](CreatedByUserMessage.md) | User who created the architectural request. | [optional] 
**last_updated_date_time** | **datetime** | Date and time the architectural request was last updated. | [optional] 
**last_updated_by_user** | [**LastUpdatedByUserMessage**](LastUpdatedByUserMessage.md) | User who most recently updated the architectural request. | [optional] 

## Example

```python
from buildium_sdk.models.association_architectural_request_message import AssociationArchitecturalRequestMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationArchitecturalRequestMessage from a JSON string
association_architectural_request_message_instance = AssociationArchitecturalRequestMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationArchitecturalRequestMessage.to_json())

# convert the object into a dict
association_architectural_request_message_dict = association_architectural_request_message_instance.to_dict()
# create an instance of AssociationArchitecturalRequestMessage from a dict
association_architectural_request_message_from_dict = AssociationArchitecturalRequestMessage.from_dict(association_architectural_request_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


