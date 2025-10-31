# AssociationTaxInformationMessage

Association tax information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_payer_id_type** | **str** | Indicates the type of tax payer id being specified in the request. | [optional] 
**tax_payer_id** | **str** | The tax payer identifier. | [optional] 
**tax_payer_name1** | **str** | Tax payer name line 1. | [optional] 
**tax_payer_name2** | **str** | Tax payer name line 2. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the tax payer. | [optional] 

## Example

```python
from buildium_sdk.models.association_tax_information_message import AssociationTaxInformationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTaxInformationMessage from a JSON string
association_tax_information_message_instance = AssociationTaxInformationMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationTaxInformationMessage.to_json())

# convert the object into a dict
association_tax_information_message_dict = association_tax_information_message_instance.to_dict()
# create an instance of AssociationTaxInformationMessage from a dict
association_tax_information_message_from_dict = AssociationTaxInformationMessage.from_dict(association_tax_information_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


