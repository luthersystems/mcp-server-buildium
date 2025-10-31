# ApplicationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rental application unique identifier. | [optional] 
**application_number** | **str** | An alpha numeric value that can be used to uniquely identify the application. This is typically provided to an applicant to use as a reference when making inquiries about their application. | [optional] 
**application_status** | **str** | Indicates the current application status. | [optional] 
**application_submitted_date_time** | **datetime** | Date and time the application was submitted. | [optional] 
**application** | [**List[ApplicationResponseMessage]**](ApplicationResponseMessage.md) | A submitted rental application. | [optional] 

## Example

```python
from buildium_sdk.models.application_message import ApplicationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMessage from a JSON string
application_message_instance = ApplicationMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationMessage.to_json())

# convert the object into a dict
application_message_dict = application_message_instance.to_dict()
# create an instance of ApplicationMessage from a dict
application_message_from_dict = ApplicationMessage.from_dict(application_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


