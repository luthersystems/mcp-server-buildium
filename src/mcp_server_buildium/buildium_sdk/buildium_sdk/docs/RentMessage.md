# RentMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rent unique identifier. | [optional] 
**lease_id** | **int** | The unique identifier of the lease that the rent will be applied to. | [optional] 
**start_date** | **date** | Start date of the rent. | [optional] 
**end_date** | **date** | End date of the rent. | [optional] 
**total_amount** | **float** | Total amount of the rent. | [optional] 
**rent_cycle** | **str** | Determines the frequency at which rent is charged. | [optional] 
**backdate_charges** | **bool** | Indicates whether backdated charges should be created when creating or editing rents. This field will always return false, even if backdated charges exist. | [optional] 
**created_date_time** | **datetime** | The date and time the rent was created. | [optional] 
**created_by_user_id** | **int** | Unique identifier of user that created the rent. | [optional] 
**last_updated_date_time** | **datetime** | Date and time the rent was last updated. | [optional] 
**charges** | [**List[LeaseRentChargeMessage]**](LeaseRentChargeMessage.md) | A collection of charges associated with the rent. | [optional] 

## Example

```python
from buildium_sdk.models.rent_message import RentMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RentMessage from a JSON string
rent_message_instance = RentMessage.from_json(json)
# print the JSON string representation of the object
print(RentMessage.to_json())

# convert the object into a dict
rent_message_dict = rent_message_instance.to_dict()
# create an instance of RentMessage from a dict
rent_message_from_dict = RentMessage.from_dict(rent_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


