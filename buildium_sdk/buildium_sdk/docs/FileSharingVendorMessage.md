# FileSharingVendorMessage

The file share settings for the vendor file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **bool** | Indicates whether file is shared with the vendor. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_vendor_message import FileSharingVendorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingVendorMessage from a JSON string
file_sharing_vendor_message_instance = FileSharingVendorMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingVendorMessage.to_json())

# convert the object into a dict
file_sharing_vendor_message_dict = file_sharing_vendor_message_instance.to_dict()
# create an instance of FileSharingVendorMessage from a dict
file_sharing_vendor_message_from_dict = FileSharingVendorMessage.from_dict(file_sharing_vendor_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


