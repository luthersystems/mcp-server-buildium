# RentalFeaturesMessage

Rental property amenities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** | A list of overall property amenities. | [optional] 
**included_in_rent** | **List[str]** | A list of amenities that are included in rent. | [optional] 

## Example

```python
from buildium_sdk.models.rental_features_message import RentalFeaturesMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalFeaturesMessage from a JSON string
rental_features_message_instance = RentalFeaturesMessage.from_json(json)
# print the JSON string representation of the object
print(RentalFeaturesMessage.to_json())

# convert the object into a dict
rental_features_message_dict = rental_features_message_instance.to_dict()
# create an instance of RentalFeaturesMessage from a dict
rental_features_message_from_dict = RentalFeaturesMessage.from_dict(rental_features_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


