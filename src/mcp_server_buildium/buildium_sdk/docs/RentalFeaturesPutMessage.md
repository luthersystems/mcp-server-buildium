# RentalFeaturesPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** | A list of overall property amenities. Any previously saved values that are not submitted in the update request will be deleted. | [optional] 
**included_in_rent** | **List[str]** | A list of amenities that are included in rent. Any previously saved values that are not submitted in the update request will be deleted. | [optional] 

## Example

```python
from buildium_sdk.models.rental_features_put_message import RentalFeaturesPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalFeaturesPutMessage from a JSON string
rental_features_put_message_instance = RentalFeaturesPutMessage.from_json(json)
# print the JSON string representation of the object
print(RentalFeaturesPutMessage.to_json())

# convert the object into a dict
rental_features_put_message_dict = rental_features_put_message_instance.to_dict()
# create an instance of RentalFeaturesPutMessage from a dict
rental_features_put_message_from_dict = RentalFeaturesPutMessage.from_dict(rental_features_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


