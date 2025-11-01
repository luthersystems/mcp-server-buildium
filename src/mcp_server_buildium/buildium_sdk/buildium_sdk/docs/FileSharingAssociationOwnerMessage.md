# FileSharingAssociationOwnerMessage

The file share settings for the association owner file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_owner** | **bool** | Indicates whether file is shared with the association owner. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_association_owner_message import FileSharingAssociationOwnerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingAssociationOwnerMessage from a JSON string
file_sharing_association_owner_message_instance = FileSharingAssociationOwnerMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingAssociationOwnerMessage.to_json())

# convert the object into a dict
file_sharing_association_owner_message_dict = file_sharing_association_owner_message_instance.to_dict()
# create an instance of FileSharingAssociationOwnerMessage from a dict
file_sharing_association_owner_message_from_dict = FileSharingAssociationOwnerMessage.from_dict(file_sharing_association_owner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


