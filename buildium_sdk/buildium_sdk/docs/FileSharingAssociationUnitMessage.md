# FileSharingAssociationUnitMessage

The file share settings for the association unit file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_owners** | **bool** | Indicates whether file is shared with association owners. | [optional] 
**board_members** | **bool** | Indicates whether file is shared with board members of the association. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_association_unit_message import FileSharingAssociationUnitMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingAssociationUnitMessage from a JSON string
file_sharing_association_unit_message_instance = FileSharingAssociationUnitMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingAssociationUnitMessage.to_json())

# convert the object into a dict
file_sharing_association_unit_message_dict = file_sharing_association_unit_message_instance.to_dict()
# create an instance of FileSharingAssociationUnitMessage from a dict
file_sharing_association_unit_message_from_dict = FileSharingAssociationUnitMessage.from_dict(file_sharing_association_unit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


