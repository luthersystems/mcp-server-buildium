# FileSharingRentalOwnerMessage

The file share settings for the rental owner file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rental_owner** | **bool** | Indicates whether file is shared with rental owner of the property. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_rental_owner_message import FileSharingRentalOwnerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingRentalOwnerMessage from a JSON string
file_sharing_rental_owner_message_instance = FileSharingRentalOwnerMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingRentalOwnerMessage.to_json())

# convert the object into a dict
file_sharing_rental_owner_message_dict = file_sharing_rental_owner_message_instance.to_dict()
# create an instance of FileSharingRentalOwnerMessage from a dict
file_sharing_rental_owner_message_from_dict = FileSharingRentalOwnerMessage.from_dict(file_sharing_rental_owner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


