# RentalOwnerTaxInformationMessage

Rental owner tax information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_payer_id_type** | **str** | Indicates the type of tax payer id being specified in the request. | [optional] 
**tax_payer_id** | **str** | The tax payer identifier. | [optional] 
**tax_payer_name1** | **str** | Tax payer name line 1. | [optional] 
**tax_payer_name2** | **str** | Tax payer name line 2. | [optional] 
**include_in1099** | **bool** | Indicates whether the rental owner should be included in 1099 form generation. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the tax payer. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_tax_information_message import RentalOwnerTaxInformationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerTaxInformationMessage from a JSON string
rental_owner_tax_information_message_instance = RentalOwnerTaxInformationMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerTaxInformationMessage.to_json())

# convert the object into a dict
rental_owner_tax_information_message_dict = rental_owner_tax_information_message_instance.to_dict()
# create an instance of RentalOwnerTaxInformationMessage from a dict
rental_owner_tax_information_message_from_dict = RentalOwnerTaxInformationMessage.from_dict(rental_owner_tax_information_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


