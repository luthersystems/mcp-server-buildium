# ArchitecturalRequestsPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_id** | **int** | The ID of the association  to tie the architectural request to. | 
**ownership_account_id** | **int** | The ID of the ownership account to tie the architectural request to. | 
**name** | **str** | The name of the architectural request. Must be 30 characters or less. | 
**submitted_date_time** | **datetime** | The date and time the architectural request was submitted. Must not be in the future. | 
**status** | **str** | The status of the architectural request. If no value is submitted the Status will be set to \&quot;New\&quot;. | [optional] 
**decision** | **str** | The decision of the architectural request. If no value is submitted the Decision will be set to \&quot;Pending\&quot;. | [optional] 

## Example

```python
from buildium_sdk.models.architectural_requests_post_message import ArchitecturalRequestsPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ArchitecturalRequestsPostMessage from a JSON string
architectural_requests_post_message_instance = ArchitecturalRequestsPostMessage.from_json(json)
# print the JSON string representation of the object
print(ArchitecturalRequestsPostMessage.to_json())

# convert the object into a dict
architectural_requests_post_message_dict = architectural_requests_post_message_instance.to_dict()
# create an instance of ArchitecturalRequestsPostMessage from a dict
architectural_requests_post_message_from_dict = ArchitecturalRequestsPostMessage.from_dict(architectural_requests_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


