# RentalOwnerContributionMessage

Rental owner contribution detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the contribution. | [optional] 
**amount** | **float** | Amount being requested for the contribution. | [optional] 

## Example

```python
from buildium_sdk.models.rental_owner_contribution_message import RentalOwnerContributionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOwnerContributionMessage from a JSON string
rental_owner_contribution_message_instance = RentalOwnerContributionMessage.from_json(json)
# print the JSON string representation of the object
print(RentalOwnerContributionMessage.to_json())

# convert the object into a dict
rental_owner_contribution_message_dict = rental_owner_contribution_message_instance.to_dict()
# create an instance of RentalOwnerContributionMessage from a dict
rental_owner_contribution_message_from_dict = RentalOwnerContributionMessage.from_dict(rental_owner_contribution_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


