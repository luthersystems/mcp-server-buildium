# ApplicationReferenceMessage

A reference to a rental application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Application id unique identifier. | [optional] 
**href** | **str** | A link to the application resource. | [optional] 

## Example

```python
from buildium_sdk.models.application_reference_message import ApplicationReferenceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationReferenceMessage from a JSON string
application_reference_message_instance = ApplicationReferenceMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationReferenceMessage.to_json())

# convert the object into a dict
application_reference_message_dict = application_reference_message_instance.to_dict()
# create an instance of ApplicationReferenceMessage from a dict
application_reference_message_from_dict = ApplicationReferenceMessage.from_dict(application_reference_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


