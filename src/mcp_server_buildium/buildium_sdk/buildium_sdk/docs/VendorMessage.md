# VendorMessage

This is an object that represents a vendor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor unique identifier. | [optional] 
**is_company** | **bool** | Indicates whether the vendor is a company. | [optional] 
**is_active** | **bool** | Indicates whether the vendor is active within the Buildium platform. | [optional] 
**first_name** | **str** | First name of the vendor. Empty if &#x60;IsCompany&#x60; is &#x60;true&#x60;. | [optional] 
**last_name** | **str** | Last name of the vendor. Empty if &#x60;IsCompany&#x60; is &#x60;true&#x60;. | [optional] 
**primary_email** | **str** | Primary email for the vendor. | [optional] 
**alternate_email** | **str** | Alternate email for the vendor. | [optional] 
**company_name** | **str** | Company name for the vendor. Empty if &#x60;IsCompany&#x60; is &#x60;false&#x60; | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | List of phone numbers for the vendor. | [optional] 
**website** | **str** | Website of the vendor. | [optional] 
**category** | [**LookupMessage**](LookupMessage.md) | Vendor category. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Vendor address. | [optional] 
**vendor_insurance** | [**VendorInsuranceMessage**](VendorInsuranceMessage.md) | Vendor insurance information. | [optional] 
**comments** | **str** | General comments about the vendor. | [optional] 
**account_number** | **str** | Vendor account number. | [optional] 
**expense_gl_account_id** | **int** | The unique identifier of the default expense general ledger account to associate with the vendor. | [optional] 
**tax_information** | [**VendorTaxInformationMessage**](VendorTaxInformationMessage.md) | The tax information of the vendor. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_message import VendorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorMessage from a JSON string
vendor_message_instance = VendorMessage.from_json(json)
# print the JSON string representation of the object
print(VendorMessage.to_json())

# convert the object into a dict
vendor_message_dict = vendor_message_instance.to_dict()
# create an instance of VendorMessage from a dict
vendor_message_from_dict = VendorMessage.from_dict(vendor_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


