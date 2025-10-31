# ListingUnitMessage

Details of the unit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rental unit unique identifier. | [optional] 
**unit_number** | **str** | Unit number. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address of the unit. | [optional] 
**unit_bedrooms** | **str** | Number of bedrooms in the unit. Null if no value is set. | [optional] 
**unit_bathrooms** | **str** | Number of bathrooms in the unit. Null if no value is set. | [optional] 
**unit_size** | **int** | Size of the unit. Null if no value is set. | [optional] 
**description** | **str** | Description of the unit. | [optional] 
**market_rent** | **float** | Market rent of the unit. This value is separate from the lease rent and is typically used for rental listings. Null if no value is set. | [optional] 
**features** | **List[str]** | List of features for the unit. | [optional] 
**files** | [**List[ListingFileMessage]**](ListingFileMessage.md) | List of media files associated with the unit. | [optional] 

## Example

```python
from buildium_sdk.models.listing_unit_message import ListingUnitMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingUnitMessage from a JSON string
listing_unit_message_instance = ListingUnitMessage.from_json(json)
# print the JSON string representation of the object
print(ListingUnitMessage.to_json())

# convert the object into a dict
listing_unit_message_dict = listing_unit_message_instance.to_dict()
# create an instance of ListingUnitMessage from a dict
listing_unit_message_from_dict = ListingUnitMessage.from_dict(listing_unit_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


