# ResidentCenterUserMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_agreement** | [**UnitAgreementMessage**](UnitAgreementMessage.md) | The user&#39;s unit agreement (lease or ownership account). | [optional] 
**user** | [**ResidentCenterUserReferenceMessage**](ResidentCenterUserReferenceMessage.md) | Information about the user. | [optional] 
**resident_center_user_status** | **str** | Resident center status for the user. | [optional] 
**is_auto_pay_enabled** | **bool** | Indicates if the user has an automatic payment scheduled for the future. | [optional] 

## Example

```python
from buildium_sdk.models.resident_center_user_message import ResidentCenterUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ResidentCenterUserMessage from a JSON string
resident_center_user_message_instance = ResidentCenterUserMessage.from_json(json)
# print the JSON string representation of the object
print(ResidentCenterUserMessage.to_json())

# convert the object into a dict
resident_center_user_message_dict = resident_center_user_message_instance.to_dict()
# create an instance of ResidentCenterUserMessage from a dict
resident_center_user_message_from_dict = ResidentCenterUserMessage.from_dict(resident_center_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


