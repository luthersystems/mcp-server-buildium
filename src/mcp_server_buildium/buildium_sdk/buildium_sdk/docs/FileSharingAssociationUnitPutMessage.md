# FileSharingAssociationUnitPutMessage

The file share settings for the association unit file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_owners** | **bool** | Indicates whether file is shared with association owners. | [optional] 
**board_members** | **bool** | Indicates whether file is shared with board members of the association. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_association_unit_put_message import FileSharingAssociationUnitPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingAssociationUnitPutMessage from a JSON string
file_sharing_association_unit_put_message_instance = FileSharingAssociationUnitPutMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingAssociationUnitPutMessage.to_json())

# convert the object into a dict
file_sharing_association_unit_put_message_dict = file_sharing_association_unit_put_message_instance.to_dict()
# create an instance of FileSharingAssociationUnitPutMessage from a dict
file_sharing_association_unit_put_message_from_dict = FileSharingAssociationUnitPutMessage.from_dict(file_sharing_association_unit_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


