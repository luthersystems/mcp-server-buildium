# ApplicantGroupMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Applicant group unique identifier. | [optional] 
**property_id** | **int** | Rental property unique identifier that the applicant group is associated with. | [optional] 
**unit_id** | **int** | Rental property unit unique identifier that the applicant group is associated with. | [optional] 
**application_group_status** | **str** | Indicates the current applicant group status. Note, this status is independent from individual application statuses within the group. | [optional] 
**applicants** | [**List[ApplicantMessage]**](ApplicantMessage.md) | A collection of applicants in the group. | [optional] 

## Example

```python
from buildium_sdk.models.applicant_group_message import ApplicantGroupMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicantGroupMessage from a JSON string
applicant_group_message_instance = ApplicantGroupMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicantGroupMessage.to_json())

# convert the object into a dict
applicant_group_message_dict = applicant_group_message_instance.to_dict()
# create an instance of ApplicantGroupMessage from a dict
applicant_group_message_from_dict = ApplicantGroupMessage.from_dict(applicant_group_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


