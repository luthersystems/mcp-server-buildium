# FileSharingRentalOwnerPutMessage

The file share settings for the rental owner file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rental_owner** | **bool** | Indicates whether file is shared with the rental owner of the property. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_rental_owner_put_message import FileSharingRentalOwnerPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingRentalOwnerPutMessage from a JSON string
file_sharing_rental_owner_put_message_instance = FileSharingRentalOwnerPutMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingRentalOwnerPutMessage.to_json())

# convert the object into a dict
file_sharing_rental_owner_put_message_dict = file_sharing_rental_owner_put_message_instance.to_dict()
# create an instance of FileSharingRentalOwnerPutMessage from a dict
file_sharing_rental_owner_put_message_from_dict = FileSharingRentalOwnerPutMessage.from_dict(file_sharing_rental_owner_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


