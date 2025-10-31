# UnsubmittedApplicationMessage

This object represents an unsubmitted application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unsubmitted application unique identifier | [optional] 

## Example

```python
from buildium_sdk.models.unsubmitted_application_message import UnsubmittedApplicationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UnsubmittedApplicationMessage from a JSON string
unsubmitted_application_message_instance = UnsubmittedApplicationMessage.from_json(json)
# print the JSON string representation of the object
print(UnsubmittedApplicationMessage.to_json())

# convert the object into a dict
unsubmitted_application_message_dict = unsubmitted_application_message_instance.to_dict()
# create an instance of UnsubmittedApplicationMessage from a dict
unsubmitted_application_message_from_dict = UnsubmittedApplicationMessage.from_dict(unsubmitted_application_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


