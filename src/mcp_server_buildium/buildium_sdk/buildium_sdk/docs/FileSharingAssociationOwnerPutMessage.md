# FileSharingAssociationOwnerPutMessage

The file share settings for the association owner file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_owner** | **bool** | Indicates whether file is shared with the association owner. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_association_owner_put_message import FileSharingAssociationOwnerPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingAssociationOwnerPutMessage from a JSON string
file_sharing_association_owner_put_message_instance = FileSharingAssociationOwnerPutMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingAssociationOwnerPutMessage.to_json())

# convert the object into a dict
file_sharing_association_owner_put_message_dict = file_sharing_association_owner_put_message_instance.to_dict()
# create an instance of FileSharingAssociationOwnerPutMessage from a dict
file_sharing_association_owner_put_message_from_dict = FileSharingAssociationOwnerPutMessage.from_dict(file_sharing_association_owner_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


