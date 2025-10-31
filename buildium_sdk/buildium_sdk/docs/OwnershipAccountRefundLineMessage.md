# OwnershipAccountRefundLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the account on the line item. | [optional] 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the refund. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_refund_line_message import OwnershipAccountRefundLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountRefundLineMessage from a JSON string
ownership_account_refund_line_message_instance = OwnershipAccountRefundLineMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountRefundLineMessage.to_json())

# convert the object into a dict
ownership_account_refund_line_message_dict = ownership_account_refund_line_message_instance.to_dict()
# create an instance of OwnershipAccountRefundLineMessage from a dict
ownership_account_refund_line_message_from_dict = OwnershipAccountRefundLineMessage.from_dict(ownership_account_refund_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


