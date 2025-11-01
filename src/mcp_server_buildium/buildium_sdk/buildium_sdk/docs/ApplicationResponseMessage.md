# ApplicationResponseMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_label** | **str** | A user defined description of the application section. | [optional] 
**section_type** | **str** | Indicates the application section type. The &#x60;SectionType&#x60; can be used to identify specific sections within the application. | [optional] 
**section_responses** | [**List[ApplicationSectionResponseMessage]**](ApplicationSectionResponseMessage.md) | A collection of form fields within the section. | [optional] 

## Example

```python
from buildium_sdk.models.application_response_message import ApplicationResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResponseMessage from a JSON string
application_response_message_instance = ApplicationResponseMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationResponseMessage.to_json())

# convert the object into a dict
application_response_message_dict = application_response_message_instance.to_dict()
# create an instance of ApplicationResponseMessage from a dict
application_response_message_from_dict = ApplicationResponseMessage.from_dict(application_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


