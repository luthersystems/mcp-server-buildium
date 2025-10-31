# RentalUnitFeaturesMessage

Rental unit amenities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** | A list of unit amenities. | [optional] 

## Example

```python
from buildium_sdk.models.rental_unit_features_message import RentalUnitFeaturesMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalUnitFeaturesMessage from a JSON string
rental_unit_features_message_instance = RentalUnitFeaturesMessage.from_json(json)
# print the JSON string representation of the object
print(RentalUnitFeaturesMessage.to_json())

# convert the object into a dict
rental_unit_features_message_dict = rental_unit_features_message_instance.to_dict()
# create an instance of RentalUnitFeaturesMessage from a dict
rental_unit_features_message_from_dict = RentalUnitFeaturesMessage.from_dict(rental_unit_features_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


