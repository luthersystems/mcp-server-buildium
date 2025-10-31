# ListingContactSaveMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the listing contact. This name must be unique across all listing contacts. | 
**email** | **str** | Email address for the listing contact. | [optional] 
**phone_number** | **str** | Phone number of the listing contact. The value must be between 10 and 20 characters, ideally formatted as (123) 123-1234. | [optional] 
**website** | **str** | Website associated with the listing contact. The value must be a valid URL including the HTTP protocol. For example http://www.example.com. | [optional] 

## Example

```python
from buildium_sdk.models.listing_contact_save_message import ListingContactSaveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingContactSaveMessage from a JSON string
listing_contact_save_message_instance = ListingContactSaveMessage.from_json(json)
# print the JSON string representation of the object
print(ListingContactSaveMessage.to_json())

# convert the object into a dict
listing_contact_save_message_dict = listing_contact_save_message_instance.to_dict()
# create an instance of ListingContactSaveMessage from a dict
listing_contact_save_message_from_dict = ListingContactSaveMessage.from_dict(listing_contact_save_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


