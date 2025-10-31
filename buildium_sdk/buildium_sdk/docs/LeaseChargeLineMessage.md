# LeaseChargeLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | [optional] 
**gl_account_id** | **int** | Unique ientifier of the general ledger account associated with the charge. | [optional] 

## Example

```python
from buildium_sdk.models.lease_charge_line_message import LeaseChargeLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseChargeLineMessage from a JSON string
lease_charge_line_message_instance = LeaseChargeLineMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseChargeLineMessage.to_json())

# convert the object into a dict
lease_charge_line_message_dict = lease_charge_line_message_instance.to_dict()
# create an instance of LeaseChargeLineMessage from a dict
lease_charge_line_message_from_dict = LeaseChargeLineMessage.from_dict(lease_charge_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


