# LeaseLedgerRefundLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the line item. | [optional] 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the refund. | [optional] 

## Example

```python
from buildium_sdk.models.lease_ledger_refund_line_message import LeaseLedgerRefundLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerRefundLineMessage from a JSON string
lease_ledger_refund_line_message_instance = LeaseLedgerRefundLineMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerRefundLineMessage.to_json())

# convert the object into a dict
lease_ledger_refund_line_message_dict = lease_ledger_refund_line_message_instance.to_dict()
# create an instance of LeaseLedgerRefundLineMessage from a dict
lease_ledger_refund_line_message_from_dict = LeaseLedgerRefundLineMessage.from_dict(lease_ledger_refund_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


