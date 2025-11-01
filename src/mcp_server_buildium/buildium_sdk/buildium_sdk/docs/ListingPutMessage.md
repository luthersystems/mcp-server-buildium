# ListingPutMessage

This is an object that represents a rental unit's Listing Contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rent** | **float** | Rent for the listing. | 
**deposit** | **float** | Deposit for the listing. | [optional] 
**lease_terms** | **str** | The lease term for the listing. | [optional] 
**available_date** | **date** | The date the listing is available. | 
**contact_id** | **int** | The contact Id for the listing. | [optional] 
**is_managed_externally** | **bool** |  | 

## Example

```python
from buildium_sdk.models.listing_put_message import ListingPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingPutMessage from a JSON string
listing_put_message_instance = ListingPutMessage.from_json(json)
# print the JSON string representation of the object
print(ListingPutMessage.to_json())

# convert the object into a dict
listing_put_message_dict = listing_put_message_instance.to_dict()
# create an instance of ListingPutMessage from a dict
listing_put_message_from_dict = ListingPutMessage.from_dict(listing_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


