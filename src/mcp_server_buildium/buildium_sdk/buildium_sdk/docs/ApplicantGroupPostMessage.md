# ApplicantGroupPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | **int** | Rental property unit unique identifier to associate with the applicant group. | [optional] 
**applicant_ids** | **List[int]** | The applicant unique identifiers to include in the applicant group. Note, that applicants can only be included in one applicant group. | 

## Example

```python
from buildium_sdk.models.applicant_group_post_message import ApplicantGroupPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicantGroupPostMessage from a JSON string
applicant_group_post_message_instance = ApplicantGroupPostMessage.from_json(json)
# print the JSON string representation of the object
print(ApplicantGroupPostMessage.to_json())

# convert the object into a dict
applicant_group_post_message_dict = applicant_group_post_message_instance.to_dict()
# create an instance of ApplicantGroupPostMessage from a dict
applicant_group_post_message_from_dict = ApplicantGroupPostMessage.from_dict(applicant_group_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


