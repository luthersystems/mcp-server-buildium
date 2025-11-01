# AssociationAppliancePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | **int** | The unit identifier the association appliance belongs to. Must be within the association property the appliance is in. | [optional] 
**name** | **str** | The name of the association appliance. The name cannot exceed 100 characters. | 
**make** | **str** | The make of the association appliance. The make cannot exceed 30 characters. | [optional] 
**model** | **str** | The model of the association appliance. The model cannot exceed 30 characters. | [optional] 
**description** | **str** | The description of the association appliance. The description cannot exceed 500 characters. | [optional] 
**warranty_end_date** | **date** | The end date for the association appliance&#39;s warranty. The warranty&#39;s end date cannot be before the installed date, if it exists. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 

## Example

```python
from buildium_sdk.models.association_appliance_put_message import AssociationAppliancePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationAppliancePutMessage from a JSON string
association_appliance_put_message_instance = AssociationAppliancePutMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationAppliancePutMessage.to_json())

# convert the object into a dict
association_appliance_put_message_dict = association_appliance_put_message_instance.to_dict()
# create an instance of AssociationAppliancePutMessage from a dict
association_appliance_put_message_from_dict = AssociationAppliancePutMessage.from_dict(association_appliance_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


