# ApplicantPayeeMessage

This is an object that represents an applicant payee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the applicant payee. | [optional] 
**name** | **str** | The name of the payee. | [optional] 
**type** | **str** | The payee user entity type. | [optional] 
**href** | **str** | A link to the resource endpoint associated with the payee. | [optional] 

## Example

```python
from buildium_sdk.models.applicant_payee_message import ApplicantPayeeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicantPayeeMessage from a JSON string
applicant_payee_message_instance = ApplicantPayeeMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicantPayeeMessage.to_json())

# convert the object into a dict
applicant_payee_message_dict = applicant_payee_message_instance.to_dict()
# create an instance of ApplicantPayeeMessage from a dict
applicant_payee_message_from_dict = ApplicantPayeeMessage.from_dict(applicant_payee_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


