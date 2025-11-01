# ResidentCenterUserReferenceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Resident center user unique identifier. | [optional] 
**first_name** | **str** | First name of the resident center user. | [optional] 
**last_name** | **str** | Last name of the resident center user. | [optional] 
**user_type** | **str** | Indicates if the resident center user is a tenant or association owner | [optional] 
**href** | **str** | A link to the user resource. | [optional] 

## Example

```python
from buildium_sdk.models.resident_center_user_reference_message import ResidentCenterUserReferenceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ResidentCenterUserReferenceMessage from a JSON string
resident_center_user_reference_message_instance = ResidentCenterUserReferenceMessage.from_json(json)
# print the JSON string representation of the object
print(ResidentCenterUserReferenceMessage.to_json())

# convert the object into a dict
resident_center_user_reference_message_dict = resident_center_user_reference_message_instance.to_dict()
# create an instance of ResidentCenterUserReferenceMessage from a dict
resident_center_user_reference_message_from_dict = ResidentCenterUserReferenceMessage.from_dict(resident_center_user_reference_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


