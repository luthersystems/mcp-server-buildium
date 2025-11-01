# VendorTaxInformationMessage

Vendor tax information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_payer_id_type** | **str** | Indicates the type of tax payer id being specified in the request. | [optional] 
**tax_payer_id** | **str** | The tax payer identifier. | [optional] 
**tax_payer_name1** | **str** | Tax payer name line 1. | [optional] 
**tax_payer_name2** | **str** | Tax payer name line 2. | [optional] 
**include_in1099** | **bool** | Indicates whether the vendor should be included in 1099 form generation. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the tax payer. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_tax_information_message import VendorTaxInformationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorTaxInformationMessage from a JSON string
vendor_tax_information_message_instance = VendorTaxInformationMessage.from_json(json)
# print the JSON string representation of the object
print(VendorTaxInformationMessage.to_json())

# convert the object into a dict
vendor_tax_information_message_dict = vendor_tax_information_message_instance.to_dict()
# create an instance of VendorTaxInformationMessage from a dict
vendor_tax_information_message_from_dict = VendorTaxInformationMessage.from_dict(vendor_tax_information_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


