# ApplicantDetailsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Applicant unique identifier. | [optional] 
**applicant_group_id** | **int** | Applicant group unique identifier. | [optional] 
**property_id** | **int** | Rental property unique identifier that the applicant is associated with. | [optional] 
**unit_id** | **int** | Rental property unit unique identifier that the applicant is associated with. | [optional] 
**tenant_id** | **int** | The rental tenant identifier associated with the applicant. This value will be null if the applicant never transitioned into a tenant. | [optional] 
**first_name** | **str** | Applicant first name. | [optional] 
**last_name** | **str** | Applicant last name. | [optional] 
**email** | **str** | Applicant email address. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | Applicant phone numbers. | [optional] 
**status** | **str** | Applicant status. | [optional] 
**applications** | [**List[ApplicantApplicationMessage]**](ApplicantApplicationMessage.md) | A collection of applications associated with the applicant. | [optional] 
**unsubmitted_applications** | [**List[UnsubmittedApplicationMessage]**](UnsubmittedApplicationMessage.md) | A collection of unsubmitted applications associated with the applicant. | [optional] 
**last_updated_date_time** | **datetime** | Date and time the applicant was last updated. | [optional] 

## Example

```python
from buildium_sdk.models.applicant_details_message import ApplicantDetailsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicantDetailsMessage from a JSON string
applicant_details_message_instance = ApplicantDetailsMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicantDetailsMessage.to_json())

# convert the object into a dict
applicant_details_message_dict = applicant_details_message_instance.to_dict()
# create an instance of ApplicantDetailsMessage from a dict
applicant_details_message_from_dict = ApplicantDetailsMessage.from_dict(applicant_details_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


