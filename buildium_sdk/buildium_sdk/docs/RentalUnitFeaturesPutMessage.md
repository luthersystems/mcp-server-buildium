# RentalUnitFeaturesPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** | A list of unit amenities. Any existing amenities associated with the unit that are not submitted in the request will be removed from the unit. | [optional] 

## Example

```python
from buildium_sdk.models.rental_unit_features_put_message import RentalUnitFeaturesPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalUnitFeaturesPutMessage from a JSON string
rental_unit_features_put_message_instance = RentalUnitFeaturesPutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalUnitFeaturesPutMessage.to_json())

# convert the object into a dict
rental_unit_features_put_message_dict = rental_unit_features_put_message_instance.to_dict()
# create an instance of RentalUnitFeaturesPutMessage from a dict
rental_unit_features_put_message_from_dict = RentalUnitFeaturesPutMessage.from_dict(rental_unit_features_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


