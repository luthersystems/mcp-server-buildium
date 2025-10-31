# AssociationMessage

This is an object that represents home owner associations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association unique identifier. | [optional] 
**name** | **str** | Association name. | [optional] 
**is_active** | **bool** | Indicates whether the association is active within the Buildium platform. | [optional] 
**reserve** | **float** | A property reserve is cash that a property manager keeps on hand in case of unexpected expenses. It is available cash that simply isn&#39;t disbursed in an owner draw. | [optional] 
**description** | **str** | Description of the association. | [optional] 
**year_built** | **int** | Indicates the year the association was built. Null if no value is set. | [optional] 
**operating_bank_account** | **str** | Primary bank account that an association uses for its income and expenses. | [optional] 
**operating_bank_account_id** | **int** | Primary bank account unique identifier that an association uses for its income and expenses. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Association address. | [optional] 
**association_manager** | [**PropertyManagerMessage**](PropertyManagerMessage.md) | Property manager associated with this association. | [optional] 
**fiscal_year_end_day** | **int** | The day the fiscal year ends for the association. | [optional] 
**fiscal_year_end_month** | **int** | The month the fiscal year ends for the association. | [optional] 
**tax_information** | [**AssociationTaxInformationMessage**](AssociationTaxInformationMessage.md) | The tax information of the association. | [optional] 

## Example

```python
from buildium_sdk.models.association_message import AssociationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationMessage from a JSON string
association_message_instance = AssociationMessage.from_json(json)
# print the JSON string representation of the object
print(AssociationMessage.to_json())

# convert the object into a dict
association_message_dict = association_message_instance.to_dict()
# create an instance of AssociationMessage from a dict
association_message_from_dict = AssociationMessage.from_dict(association_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


