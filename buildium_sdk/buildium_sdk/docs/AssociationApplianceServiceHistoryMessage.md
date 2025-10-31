# AssociationApplianceServiceHistoryMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Appliance service history unique identifier. | [optional] 
**service_type** | **str** | Type of service performed. | [optional] 
**var_date** | **date** | Date of the service. | [optional] 
**details** | **str** | Details of the service. | [optional] 

## Example

```python
from buildium_sdk.models.association_appliance_service_history_message import AssociationApplianceServiceHistoryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationApplianceServiceHistoryMessage from a JSON string
association_appliance_service_history_message_instance = AssociationApplianceServiceHistoryMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationApplianceServiceHistoryMessage.to_json())

# convert the object into a dict
association_appliance_service_history_message_dict = association_appliance_service_history_message_instance.to_dict()
# create an instance of AssociationApplianceServiceHistoryMessage from a dict
association_appliance_service_history_message_from_dict = AssociationApplianceServiceHistoryMessage.from_dict(association_appliance_service_history_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


