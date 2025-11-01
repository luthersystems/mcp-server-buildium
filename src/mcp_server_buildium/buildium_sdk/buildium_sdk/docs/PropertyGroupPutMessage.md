# PropertyGroupPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Property group name. The name can not exceed 127 characters. | 
**description** | **str** | Description of the property group. The description can not exceed 1000 characters. | [optional] 
**property_ids** | **List[int]** | A list of association and/or rental property unique identifiers to assign to the property group. Property groups cannot be updated using inactive associations and/or rental properties. | 

## Example

```python
from buildium_sdk.models.property_group_put_message import PropertyGroupPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyGroupPutMessage from a JSON string
property_group_put_message_instance = PropertyGroupPutMessage.from_json(json)
# print the JSON string representation of the object
print(PropertyGroupPutMessage.to_json())

# convert the object into a dict
property_group_put_message_dict = property_group_put_message_instance.to_dict()
# create an instance of PropertyGroupPutMessage from a dict
property_group_put_message_from_dict = PropertyGroupPutMessage.from_dict(property_group_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


