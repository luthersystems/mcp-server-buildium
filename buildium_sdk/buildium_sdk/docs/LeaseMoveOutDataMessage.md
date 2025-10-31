# LeaseMoveOutDataMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | Tenant unique identifier. | [optional] 
**move_out_date** | **date** | Date the tenant will move out of the leased unit. | [optional] 
**notice_given_date** | **date** | Date the tenant move out notice was received. | [optional] 

## Example

```python
from buildium_sdk.models.lease_move_out_data_message import LeaseMoveOutDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseMoveOutDataMessage from a JSON string
lease_move_out_data_message_instance = LeaseMoveOutDataMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseMoveOutDataMessage.to_json())

# convert the object into a dict
lease_move_out_data_message_dict = lease_move_out_data_message_instance.to_dict()
# create an instance of LeaseMoveOutDataMessage from a dict
lease_move_out_data_message_from_dict = LeaseMoveOutDataMessage.from_dict(lease_move_out_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


