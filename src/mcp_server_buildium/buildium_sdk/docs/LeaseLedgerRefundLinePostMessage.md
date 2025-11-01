# LeaseLedgerRefundLinePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the refund. | 

## Example

```python
from buildium_sdk.models.lease_ledger_refund_line_post_message import LeaseLedgerRefundLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerRefundLinePostMessage from a JSON string
lease_ledger_refund_line_post_message_instance = LeaseLedgerRefundLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerRefundLinePostMessage.to_json())

# convert the object into a dict
lease_ledger_refund_line_post_message_dict = lease_ledger_refund_line_post_message_instance.to_dict()
# create an instance of LeaseLedgerRefundLinePostMessage from a dict
lease_ledger_refund_line_post_message_from_dict = LeaseLedgerRefundLinePostMessage.from_dict(lease_ledger_refund_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


