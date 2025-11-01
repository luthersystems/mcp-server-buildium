# RentalOwnerMessage

This is an object that represents a rental property owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rental property owner unique identifier. | [optional] 
**is_company** | **bool** | Indicates whether the rental owner is a company. | [optional] 
**is_active** | **bool** | Indicates whether the rental owner is active within the Buildium platform. | [optional] 
**first_name** | **str** | First name of the rental owner. Empty if &#x60;IsCompany&#x60; is &#x60;true&#x60;. | [optional] 
**last_name** | **str** | Last name of the rental owner. Empty if &#x60;IsCompany&#x60; is &#x60;true&#x60;. | [optional] 
**phone_numbers** | [**List[PhoneNumberMessage]**](PhoneNumberMessage.md) | Phone numbers associated with the rental owner. | [optional] 
**email** | **str** | Email of the rental owner. | [optional] 
**alternate_email** | **str** | Alternate email of the rental owner. | [optional] 
**comment** | **str** | Comments about the rental owner. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the rental owner. | [optional] 
**management_agreement_start_date** | **date** | Start date of the management agreement with the rental owner. Null if value is not set. | [optional] 
**management_agreement_end_date** | **date** | End date of the management agreement with the rental owner. Null if value is not set. | [optional] 
**company_name** | **str** | Company name of the rental owner. Empty if &#x60;IsCompany&#x60; is &#x60;false&#x60;. | [optional] 
**property_ids** | **List[int]** | A list of rental property ID&#39;s associated with this rental owner. | [optional] 
**tax_information** | [**RentalOwnerTaxInformationMessage**](RentalOwnerTaxInformationMessage.md) | The tax information of the rental owner. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_message import RentalOwnerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerMessage from a JSON string
rental_owner_message_instance = RentalOwnerMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerMessage.to_json())

# convert the object into a dict
rental_owner_message_dict = rental_owner_message_instance.to_dict()
# create an instance of RentalOwnerMessage from a dict
rental_owner_message_from_dict = RentalOwnerMessage.from_dict(rental_owner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


