# LookupMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from buildium_sdk.models.lookup_message import LookupMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LookupMessage from a JSON string
lookup_message_instance = LookupMessage.from_json(json)
# print the JSON string representation of the object
print(LookupMessage.to_json())

# convert the object into a dict
lookup_message_dict = lookup_message_instance.to_dict()
# create an instance of LookupMessage from a dict
lookup_message_from_dict = LookupMessage.from_dict(lookup_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


