# FileSharingAccountPutMessage

The file share settings for the account file entity type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_residents** | **bool** | Indicates whether file is shared with all residents via the Resident Center. | [optional] 
**property_ids** | **List[int]** | A list of rental property unique identifiers whose residents should receive the file. | [optional] 
**all_rental_owners** | **bool** | Indicates whether file is shared with all rental owners via the portal. | [optional] 
**rental_owner_ids** | **List[int]** | A list of rental owner unique identifiers that should receive the file. | [optional] 
**website_visitors** | **bool** | Indicates whether file is shared with anyone visiting the company&#39;s public site. | [optional] 

## Example

```python
from buildium_sdk.models.file_sharing_account_put_message import FileSharingAccountPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingAccountPutMessage from a JSON string
file_sharing_account_put_message_instance = FileSharingAccountPutMessage.from_json(json)
# print the JSON string representation of the object
print(FileSharingAccountPutMessage.to_json())

# convert the object into a dict
file_sharing_account_put_message_dict = file_sharing_account_put_message_instance.to_dict()
# create an instance of FileSharingAccountPutMessage from a dict
file_sharing_account_put_message_from_dict = FileSharingAccountPutMessage.from_dict(file_sharing_account_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


