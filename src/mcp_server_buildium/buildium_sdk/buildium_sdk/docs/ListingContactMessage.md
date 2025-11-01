# ListingContactMessage

The contact information for the listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Listing contact unique identifier. | [optional] 
**name** | **str** | Name of listing contact. | [optional] 
**email** | **str** | Email of the listing contact. | [optional] 
**phone_number** | **str** | Phone number of the listing contact. | [optional] 
**website** | **str** | Website of the listing contact. | [optional] 

## Example

```python
from buildium_sdk.models.listing_contact_message import ListingContactMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingContactMessage from a JSON string
listing_contact_message_instance = ListingContactMessage.from_json(json)
# print the JSON string representation of the object
print(ListingContactMessage.to_json())

# convert the object into a dict
listing_contact_message_dict = listing_contact_message_instance.to_dict()
# create an instance of ListingContactMessage from a dict
listing_contact_message_from_dict = ListingContactMessage.from_dict(listing_contact_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


