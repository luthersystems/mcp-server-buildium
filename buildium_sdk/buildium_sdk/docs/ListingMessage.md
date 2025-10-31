# ListingMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_date** | **date** | The date the listing was created in Buildium. It does not reflect when the listing was syndicated and listed in external systems. It can take 24-48 hours for a listing to be syndicated once it is created in Buildium. | [optional] 
**rent** | **float** | The asking rent amount for this unit. | [optional] 
**deposit** | **float** | The deposit amount for the unit. | [optional] 
**lease_terms** | **str** | A summary of the lease terms. | [optional] 
**available_date** | **date** | The date the unit will be available to move in. | [optional] 
**is_managed_externally** | **bool** | Indicates if the listing is managed by an external vendor. Note, the &#x60;Contact&#x60; property will be &#x60;null&#x60; if the this property is &#x60;true&#x60; as the contact information is managed by a vendor outside of Buildium. | [optional] 
**rental_application_url** | **str** | The URL to the online rental application hosted by Buildium. | [optional] 
**contact** | [**ListingContactMessage**](ListingContactMessage.md) | The contact information for the listing. | [optional] 
**var_property** | [**ListingPropertyMessage**](ListingPropertyMessage.md) | Details of the unit property. | [optional] 
**unit** | [**ListingUnitMessage**](ListingUnitMessage.md) | Details of the unit. | [optional] 

## Example

```python
from buildium_sdk.models.listing_message import ListingMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingMessage from a JSON string
listing_message_instance = ListingMessage.from_json(json)
# print the JSON string representation of the object
print(ListingMessage.to_json())

# convert the object into a dict
listing_message_dict = listing_message_instance.to_dict()
# create an instance of ListingMessage from a dict
listing_message_from_dict = ListingMessage.from_dict(listing_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


