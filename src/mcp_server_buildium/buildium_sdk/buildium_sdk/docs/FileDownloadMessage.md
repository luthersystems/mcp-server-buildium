# FileDownloadMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | A transient URL that can be used to download the requested file. This URL expires after 5 minutes. | [optional] 

## Example

```python
from buildium_sdk.models.file_download_message import FileDownloadMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownloadMessage from a JSON string
file_download_message_instance = FileDownloadMessage.from_json(json)
# print the JSON string representation of the object
print(FileDownloadMessage.to_json())

# convert the object into a dict
file_download_message_dict = file_download_message_instance.to_dict()
# create an instance of FileDownloadMessage from a dict
file_download_message_from_dict = FileDownloadMessage.from_dict(file_download_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


