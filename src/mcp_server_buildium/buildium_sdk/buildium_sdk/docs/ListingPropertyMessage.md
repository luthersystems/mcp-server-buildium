# ListingPropertyMessage

Details of the unit property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rental property unique identifier. | [optional] 
**name** | **str** | Name of the rental property. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the rental property. | [optional] 
**number_units** | **int** | Number of units in the rental property. | [optional] 
**structure_description** | **str** | Description of the rental property structure. | [optional] 
**year_built** | **int** | Year the rental property was built. | [optional] 
**features** | **List[str]** | List of features for the property. | [optional] 
**included_in_rent** | **List[str]** | The list of amenities included in rent the property has. | [optional] 
**files** | [**List[ListingFileMessage]**](ListingFileMessage.md) | List of media files associated with the property. | [optional] 

## Example

```python
from buildium_sdk.models.listing_property_message import ListingPropertyMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingPropertyMessage from a JSON string
listing_property_message_instance = ListingPropertyMessage.from_json(json)
# print the JSON string representation of the object
print(ListingPropertyMessage.to_json())

# convert the object into a dict
listing_property_message_dict = listing_property_message_instance.to_dict()
# create an instance of ListingPropertyMessage from a dict
listing_property_message_from_dict = ListingPropertyMessage.from_dict(listing_property_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


