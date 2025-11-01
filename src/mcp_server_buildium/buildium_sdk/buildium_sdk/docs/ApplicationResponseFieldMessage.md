# ApplicationResponseFieldMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_category_type** | **str** | Indicates the field category type the field is assigned. The &#x60;FieldCategoryType&#x60; can be used to identify specific data points within the application. For example, to identify the fields that contain the applicants full name you would filter the fields within the application where the &#x60;FieldCategoryType&#x60; is equal to &#x60;ApplicantName&#x60;. | [optional] 
**field_type** | **str** | Indicates the fields expected input value format and/or data type. For example, a field can be assigned a &#x60;FieldType&#x60; of &#x60;DateDayMonthYear&#x60; which indicates the input value must be a date containing a day, month and year. | [optional] 
**field_label** | **str** | A user defined description of the field. This value is typically displayed as the form field label on the application. | [optional] 
**value** | **str** | The field input value from the applicant. | [optional] 

## Example

```python
from buildium_sdk.models.application_response_field_message import ApplicationResponseFieldMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResponseFieldMessage from a JSON string
application_response_field_message_instance = ApplicationResponseFieldMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicationResponseFieldMessage.to_json())

# convert the object into a dict
application_response_field_message_dict = application_response_field_message_instance.to_dict()
# create an instance of ApplicationResponseFieldMessage from a dict
application_response_field_message_from_dict = ApplicationResponseFieldMessage.from_dict(application_response_field_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


