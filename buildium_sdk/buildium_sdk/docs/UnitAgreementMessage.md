# UnitAgreementMessage

Unit agreement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unit agreement unique identifier. | [optional] 
**type** | **str** | The type of unit agreement. | [optional] 
**href** | **str** | A link to the unit agreement resource. | [optional] 

## Example

```python
from buildium_sdk.models.unit_agreement_message import UnitAgreementMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UnitAgreementMessage from a JSON string
unit_agreement_message_instance = UnitAgreementMessage.from_json(json)
# print the JSON string representation of the object
print(UnitAgreementMessage.to_json())

# convert the object into a dict
unit_agreement_message_dict = unit_agreement_message_instance.to_dict()
# create an instance of UnitAgreementMessage from a dict
unit_agreement_message_from_dict = UnitAgreementMessage.from_dict(unit_agreement_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


