# LeaseLedgerRefundPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the refund. The date must be formatted as YYYY-MM-DD. | 
**payee_user_ids** | **List[int]** | Unique identifiers of the users receiving the refund. | 
**memo** | **str** | A brief note describing the reason for the refund. The value cannot exceed 65 characters. | [optional] 
**check_number** | **str** | Check number associated with the refund, if applicable. The value cannot exceed 30 characters. | [optional] 
**bank_account_id** | **int** | Unique identifier of the bank account the refund is issued from. | 
**address** | [**SaveAddressMessage**](SaveAddressMessage.md) | Address to be displayed on the refund check. | 
**lines** | [**List[LeaseLedgerRefundLinePostMessage]**](LeaseLedgerRefundLinePostMessage.md) | A collection of line items included in the refund. At least one line item is required. | 

## Example

```python
from buildium_sdk.models.lease_ledger_refund_post_message import LeaseLedgerRefundPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerRefundPostMessage from a JSON string
lease_ledger_refund_post_message_instance = LeaseLedgerRefundPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerRefundPostMessage.to_json())

# convert the object into a dict
lease_ledger_refund_post_message_dict = lease_ledger_refund_post_message_instance.to_dict()
# create an instance of LeaseLedgerRefundPostMessage from a dict
lease_ledger_refund_post_message_from_dict = LeaseLedgerRefundPostMessage.from_dict(lease_ledger_refund_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


