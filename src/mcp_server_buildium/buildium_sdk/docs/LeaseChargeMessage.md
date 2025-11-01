# LeaseChargeMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Charge unique identifier. | [optional] 
**var_date** | **date** | Date of the charge. | [optional] 
**total_amount** | **float** | Sum of all &#x60;Lines.Amount&#x60; entries in the charge. | [optional] 
**memo** | **str** | Memo associated with the charge. | [optional] 
**bill_id** | **int** | The bill identifier this charge is associated with, if applicable. | [optional] 
**lines** | [**List[LeaseChargeLineMessage]**](LeaseChargeLineMessage.md) | A collection of line items associated with the charge. | [optional] 

## Example

```python
from buildium_sdk.models.lease_charge_message import LeaseChargeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseChargeMessage from a JSON string
lease_charge_message_instance = LeaseChargeMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseChargeMessage.to_json())

# convert the object into a dict
lease_charge_message_dict = lease_charge_message_instance.to_dict()
# create an instance of LeaseChargeMessage from a dict
lease_charge_message_from_dict = LeaseChargeMessage.from_dict(lease_charge_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


