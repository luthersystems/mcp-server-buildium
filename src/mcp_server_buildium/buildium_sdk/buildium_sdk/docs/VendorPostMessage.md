# VendorPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the vendor. Required if &#x60;IsCompany&#x60; is &#x60;false&#x60;. The value cannot exceed 127 characters. | [optional] 
**last_name** | **str** | Last name of the vendor. Required if &#x60;IsCompany&#x60; is &#x60;false&#x60;. The value cannot exceed 127 characters. | [optional] 
**is_company** | **bool** | Indicates whether the vendor should be considered a company or person. | 
**company_name** | **str** | Company name of the vendor. Required if &#x60;IsCompany&#x60; is &#x60;true&#x60;. The value cannot exceed 127 characters. | [optional] 
**primary_email** | **str** | Primary email for the vendor. | [optional] 
**alternate_email** | **str** | Alternate email for the vendor. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers for the vendor. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the vendor. | [optional] 
**category_id** | **int** | The unique identifier of the vendor category. | 
**expense_gl_account_id** | **int** | The unique identifier of the default expense general ledger account to associate with the vendor. | [optional] 
**account_number** | **str** | The account number of the vendor. The value cannot exceed 30 characters. | [optional] 
**website** | **str** | The website of the vendor. The value must be a valid URL. For example &#x60;http://www.example.com&#x60;. The value cannot exceed 100 characters. | [optional] 
**vendor_insurance** | [**VendorInsuranceSaveMessage**](VendorInsuranceSaveMessage.md) | The insurance information for the vendor. | [optional] 
**comments** | **str** | Comments about the vendor. The value cannot exceed 65,535 characters. | [optional] 
**tax_information** | [**TaxInformationPostMessage**](TaxInformationPostMessage.md) | The tax information of the vendor. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_post_message import VendorPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorPostMessage from a JSON string
vendor_post_message_instance = VendorPostMessage.from_json(json)
# print the JSON string representation of the object
print(VendorPostMessage.to_json())

# convert the object into a dict
vendor_post_message_dict = vendor_post_message_instance.to_dict()
# create an instance of VendorPostMessage from a dict
vendor_post_message_from_dict = VendorPostMessage.from_dict(vendor_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


