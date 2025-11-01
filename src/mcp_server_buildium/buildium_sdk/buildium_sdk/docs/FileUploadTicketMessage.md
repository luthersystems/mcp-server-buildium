# FileUploadTicketMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_url** | **str** | AWS S3 Bucket Url. | [optional] 
**form_data** | **Dict[str, Optional[str]]** | AWS Meta Data. | [optional] 
**physical_file_name** | **str** | The physical file name. | [optional] 

## Example

```python
from buildium_sdk.models.file_upload_ticket_message import FileUploadTicketMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadTicketMessage from a JSON string
file_upload_ticket_message_instance = FileUploadTicketMessage.from_json(json)
# print the JSON string representation of the object
print(FileUploadTicketMessage.to_json())

# convert the object into a dict
file_upload_ticket_message_dict = file_upload_ticket_message_instance.to_dict()
# create an instance of FileUploadTicketMessage from a dict
file_upload_ticket_message_from_dict = FileUploadTicketMessage.from_dict(file_upload_ticket_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


