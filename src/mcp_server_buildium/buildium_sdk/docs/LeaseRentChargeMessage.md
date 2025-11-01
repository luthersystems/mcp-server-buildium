# LeaseRentChargeMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rent charge unique identifier. | [optional] 
**gl_account_id** | **int** | General ledger account unique identifier the rent charge is related to. | [optional] 
**amount** | **float** | Amount of the rent charge. | [optional] 
**memo** | **str** | Memo for the rent charge. | [optional] 
**first_charge_date** | **date** | First date for the rent charge. | [optional] 
**post_days_in_advance** | **int** | Number of days ahead of the due date the charge will post on the lease ledger. | [optional] 
**due_on_day_of_the_month** | **int** | The day of the month the rent charge is due. | [optional] 

## Example

```python
from buildium_sdk.models.lease_rent_charge_message import LeaseRentChargeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseRentChargeMessage from a JSON string
lease_rent_charge_message_instance = LeaseRentChargeMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseRentChargeMessage.to_json())

# convert the object into a dict
lease_rent_charge_message_dict = lease_rent_charge_message_instance.to_dict()
# create an instance of LeaseRentChargeMessage from a dict
lease_rent_charge_message_from_dict = LeaseRentChargeMessage.from_dict(lease_rent_charge_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


