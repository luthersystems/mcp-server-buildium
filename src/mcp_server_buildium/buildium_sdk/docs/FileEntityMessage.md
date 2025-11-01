# FileEntityMessage

The entity the file is associated to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Entity unique identifier. | [optional] 
**entity_type** | **str** | The entity type. | [optional] 
**href** | **str** | A link to the entity resource. | [optional] 

## Example

```python
from buildium_sdk.models.file_entity_message import FileEntityMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntityMessage from a JSON string
file_entity_message_instance = FileEntityMessage.from_json(json)
# print the JSON string representation of the object
print(FileEntityMessage.to_json())

# convert the object into a dict
file_entity_message_dict = file_entity_message_instance.to_dict()
# create an instance of FileEntityMessage from a dict
file_entity_message_from_dict = FileEntityMessage.from_dict(file_entity_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


