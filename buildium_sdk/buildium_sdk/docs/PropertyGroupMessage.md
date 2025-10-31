# PropertyGroupMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Property group unique identifier. | [optional] 
**name** | **str** | Property group name. | [optional] 
**description** | **str** | Property group description. | [optional] 
**properties** | [**List[PropertyMessage]**](PropertyMessage.md) | A list of association and/or rental property unique identifiers assigned to the property group. | [optional] 
**created_by_user** | [**CreatedByUserMessage**](CreatedByUserMessage.md) | User who created the property group. | [optional] 

## Example

```python
from buildium_sdk.models.property_group_message import PropertyGroupMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyGroupMessage from a JSON string
property_group_message_instance = PropertyGroupMessage.from_json(json)
# print the JSON string representation of the object
print(PropertyGroupMessage.to_json())

# convert the object into a dict
property_group_message_dict = property_group_message_instance.to_dict()
# create an instance of PropertyGroupMessage from a dict
property_group_message_from_dict = PropertyGroupMessage.from_dict(property_group_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


