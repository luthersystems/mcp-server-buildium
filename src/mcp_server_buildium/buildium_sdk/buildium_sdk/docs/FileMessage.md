# FileMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File unique identifier. | [optional] 
**file_entity** | [**FileEntityMessage**](FileEntityMessage.md) | The entity associated with the file. | [optional] 
**category_id** | **int** | The category identifier assigned to this file. | [optional] 
**title** | **str** | Title of the file. | [optional] 
**description** | **str** | Description of the file. | [optional] 
**physical_file_name** | **str** | Physical name of the file on the server. | [optional] 
**size** | **int** | Size of the file. Unit of measure is bytes. | [optional] 
**content_type** | **str** | MIME type of the file. | [optional] 
**uploaded_date_time** | **datetime** | Date the file was uploaded. | [optional] 

## Example

```python
from buildium_sdk.models.file_message import FileMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileMessage from a JSON string
file_message_instance = FileMessage.from_json(json)
# print the JSON string representation of the object
print(FileMessage.to_json())

# convert the object into a dict
file_message_dict = file_message_instance.to_dict()
# create an instance of FileMessage from a dict
file_message_from_dict = FileMessage.from_dict(file_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


