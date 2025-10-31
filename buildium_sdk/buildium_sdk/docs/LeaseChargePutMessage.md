# LeaseChargePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the charge. The date must be formatted as YYYY-MM-DD. | 
**memo** | **str** | Memo associated with the charge. The value cannot exceed 65 characters. | [optional] 
**lines** | [**List[LeaseChargeLineSaveMessage]**](LeaseChargeLineSaveMessage.md) | Collection of line items to be included in the charge. All existing line items will be deleted and replaced with the line items in this request. At least 1 line item is required. | 

## Example

```python
from buildium_sdk.models.lease_charge_put_message import LeaseChargePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseChargePutMessage from a JSON string
lease_charge_put_message_instance = LeaseChargePutMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseChargePutMessage.to_json())

# convert the object into a dict
lease_charge_put_message_dict = lease_charge_put_message_instance.to_dict()
# create an instance of LeaseChargePutMessage from a dict
lease_charge_put_message_from_dict = LeaseChargePutMessage.from_dict(lease_charge_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


