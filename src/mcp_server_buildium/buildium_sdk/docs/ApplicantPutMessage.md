# ApplicantPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | **int** | The rental property unit unique identifier to associate with the applicant. | [optional] 
**first_name** | **str** | The first name of the applicant. The value can not exceed 127 characters. | 
**last_name** | **str** | The last name of the applicant. The value can not exceed 127 characters. | 
**email** | **str** | The email address of the applicant. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers for the applicant. | [optional] 

## Example

```python
from buildium_sdk.models.applicant_put_message import ApplicantPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicantPutMessage from a JSON string
applicant_put_message_instance = ApplicantPutMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicantPutMessage.to_json())

# convert the object into a dict
applicant_put_message_dict = applicant_put_message_instance.to_dict()
# create an instance of ApplicantPutMessage from a dict
applicant_put_message_from_dict = ApplicantPutMessage.from_dict(applicant_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


