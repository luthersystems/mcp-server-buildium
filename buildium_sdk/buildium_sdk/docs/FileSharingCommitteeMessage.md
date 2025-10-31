# FileSharingCommitteeMessage

The file share settings for the committee file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_owners** | **bool** | Indicates whether file is shared with association owners. | [optional] 
**board_members** | **bool** | Indicates whether file is shared with board members of the association. | [optional] 
**committee** | **bool** | Indicates whether file is shared with association committee. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_committee_message import FileSharingCommitteeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingCommitteeMessage from a JSON string
file_sharing_committee_message_instance = FileSharingCommitteeMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingCommitteeMessage.to_json())

# convert the object into a dict
file_sharing_committee_message_dict = file_sharing_committee_message_instance.to_dict()
# create an instance of FileSharingCommitteeMessage from a dict
file_sharing_committee_message_from_dict = FileSharingCommitteeMessage.from_dict(file_sharing_committee_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


