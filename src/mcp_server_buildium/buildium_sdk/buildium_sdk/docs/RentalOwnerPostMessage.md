# RentalOwnerPostMessage

This is an object that represents a rental property owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the rental owner. Required if &#x60;IsCompany&#x60; is &#x60;false&#x60;. The value cannot exceed 127 characters. | [optional] 
**last_name** | **str** | Last name of the rental owner. Required if &#x60;IsCompany&#x60; is &#x60;false&#x60;. The value cannot exceed 127 characters. | [optional] 
**is_company** | **bool** | Indicates whether the rental owner should be considered a company or person. | 
**company_name** | **str** | Company name of the rental owner. Required if &#x60;IsCompany&#x60; is &#x60;true&#x60;. The value cannot exceed 127 characters. | [optional] 
**date_of_birth** | **date** | Date of birth of the rental owner. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**management_agreement_start_date** | **date** | Start date of the management agreement with the rental owner. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**management_agreement_end_date** | **date** | End date of the management agreement with the rental owner. Must be formatted as &#x60;YYYY-MM-DD&#x60;. | [optional] 
**email** | **str** | Email of the rental owner. | [optional] 
**alternate_email** | **str** | Alternate email of the rental owner. | [optional] 
**phone_numbers** | [**PhoneNumbersMessage**](PhoneNumbersMessage.md) | Phone numbers for the rental owner. | [optional] 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address of the rental owner. | 
**comment** | **str** | Comments about the rental owner. The comments cannot exceed 65,535 characters. | [optional] 
**property_ids** | **List[int]** | A list of rental property ID&#39;s to associate with this rental owner. At least one property ID must be provided. | 
**tax_information** | [**TaxInformationPostMessage**](TaxInformationPostMessage.md) | The tax information of the rental owner. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_post_message import RentalOwnerPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerPostMessage from a JSON string
rental_owner_post_message_instance = RentalOwnerPostMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerPostMessage.to_json())

# convert the object into a dict
rental_owner_post_message_dict = rental_owner_post_message_instance.to_dict()
# create an instance of RentalOwnerPostMessage from a dict
rental_owner_post_message_from_dict = RentalOwnerPostMessage.from_dict(rental_owner_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


