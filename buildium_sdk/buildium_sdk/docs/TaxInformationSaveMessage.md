# TaxInformationSaveMessage

Tax information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_payer_id** | **str** | The unique identifier of the tax payer. Required if &#x60;TaxPayerType&#x60; is set. Format the values based on the &#x60;TaxPayerIdType&#x60; that is specified in the request. &#x60;SSN&#x60; must be formatted as 123-45-6789. &#x60;EIN&#x60; must be formatted as 12-3456789. | [optional] 
**tax_payer_type** | **str** | The tax payer type. Required if &#x60;TaxPayerId&#x60; is set. | [optional] 
**tax_payer_name1** | **str** | The tax payer name 1. The value cannot exceed 40 characters. | [optional] 
**tax_payer_name2** | **str** | The tax payer name 2. The value cannot exceed 40 characters. | [optional] 
**include_in1099** | **bool** | Indicates whether the vendor should be included in 1099 form generation. | 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the tax payer if different from the vendor&#39;s primary address. | [optional] 

## Example

```python
from buildium_sdk.models.tax_information_save_message import TaxInformationSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaxInformationSaveMessage from a JSON string
tax_information_save_message_instance = TaxInformationSaveMessage.from_json(json)
# print the JSON string representation of the object
print(TaxInformationSaveMessage.to_json())

# convert the object into a dict
tax_information_save_message_dict = tax_information_save_message_instance.to_dict()
# create an instance of TaxInformationSaveMessage from a dict
tax_information_save_message_from_dict = TaxInformationSaveMessage.from_dict(tax_information_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


