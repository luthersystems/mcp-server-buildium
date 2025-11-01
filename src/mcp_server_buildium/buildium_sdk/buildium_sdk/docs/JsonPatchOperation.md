# JsonPatchOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**path** | **str** |  | 
**value** | **object** |  | [optional] 
**var_from** | **str** |  | [optional] 

## Example

```python
from buildium_sdk.models.json_patch_operation import JsonPatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchOperation from a JSON string
json_patch_operation_instance = JsonPatchOperation.from_json(json)
# print the JSON string representation of the object
print(JsonPatchOperation.to_json())

# convert the object into a dict
json_patch_operation_dict = json_patch_operation_instance.to_dict()
# create an instance of JsonPatchOperation from a dict
json_patch_operation_from_dict = JsonPatchOperation.from_dict(json_patch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


