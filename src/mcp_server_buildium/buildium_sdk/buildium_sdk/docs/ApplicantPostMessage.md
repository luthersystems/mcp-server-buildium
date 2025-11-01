# ApplicantPostMessage

This object represents an applicant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | **int** | The rental property unit unique identifier to associate with the applicant. | [optional] 
**first_name** | **str** | The first name of the applicant. The value can not exceed 127 characters. | 
**last_name** | **str** | The last name of the applicant. The value can not exceed 127 characters. | 
**email** | **str** | The email address of the applicant. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers of the applicant. | [optional] 
**send_rental_application_email** | **bool** | Indicates whether to send the applicant an email with a link to the online rental application form. | 

## Example

```python
from buildium_sdk.models.applicant_post_message import ApplicantPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicantPostMessage from a JSON string
applicant_post_message_instance = ApplicantPostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicantPostMessage.to_json())

# convert the object into a dict
applicant_post_message_dict = applicant_post_message_instance.to_dict()
# create an instance of ApplicantPostMessage from a dict
applicant_post_message_from_dict = ApplicantPostMessage.from_dict(applicant_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


