# ApplicationPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_status** | **str** | Sets the status of the application. | 

## Example

```python
from buildium_sdk.models.application_put_message import ApplicationPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationPutMessage from a JSON string
application_put_message_instance = ApplicationPutMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationPutMessage.to_json())

# convert the object into a dict
application_put_message_dict = application_put_message_instance.to_dict()
# create an instance of ApplicationPutMessage from a dict
application_put_message_from_dict = ApplicationPutMessage.from_dict(application_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


