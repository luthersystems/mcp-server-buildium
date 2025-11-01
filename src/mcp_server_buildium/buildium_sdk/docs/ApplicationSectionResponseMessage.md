# ApplicationSectionResponseMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_fields** | [**List[ApplicationResponseFieldMessage]**](ApplicationResponseFieldMessage.md) |  | [optional] 

## Example

```python
from buildium_sdk.models.application_section_response_message import ApplicationSectionResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSectionResponseMessage from a JSON string
application_section_response_message_instance = ApplicationSectionResponseMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationSectionResponseMessage.to_json())

# convert the object into a dict
application_section_response_message_dict = application_section_response_message_instance.to_dict()
# create an instance of ApplicationSectionResponseMessage from a dict
application_section_response_message_from_dict = ApplicationSectionResponseMessage.from_dict(application_section_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


