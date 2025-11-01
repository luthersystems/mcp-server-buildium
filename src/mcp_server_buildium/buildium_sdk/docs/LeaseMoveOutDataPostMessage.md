# LeaseMoveOutDataPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | Tenant unique identifier. | 
**move_out_date** | **date** | Date the tenant(s) will move out of the leased unit. | 
**notice_given_date** | **date** | Date the tenant(s) gave their move out notice. | [optional] 

## Example

```python
from buildium_sdk.models.lease_move_out_data_post_message import LeaseMoveOutDataPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseMoveOutDataPostMessage from a JSON string
lease_move_out_data_post_message_instance = LeaseMoveOutDataPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseMoveOutDataPostMessage.to_json())

# convert the object into a dict
lease_move_out_data_post_message_dict = lease_move_out_data_post_message_instance.to_dict()
# create an instance of LeaseMoveOutDataPostMessage from a dict
lease_move_out_data_post_message_from_dict = LeaseMoveOutDataPostMessage.from_dict(lease_move_out_data_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


