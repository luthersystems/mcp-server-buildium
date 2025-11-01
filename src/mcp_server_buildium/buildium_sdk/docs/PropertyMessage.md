# PropertyMessage

Property information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The property unique identifier. | [optional] 
**type** | **str** | The property type. | [optional] 
**href** | **str** | A link to the property entity resource. | [optional] 

## Example

```python
from buildium_sdk.models.property_message import PropertyMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyMessage from a JSON string
property_message_instance = PropertyMessage.from_json(json)
# print the JSON string representation of the object
print(PropertyMessage.to_json())

# convert the object into a dict
property_message_dict = property_message_instance.to_dict()
# create an instance of PropertyMessage from a dict
property_message_from_dict = PropertyMessage.from_dict(property_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


