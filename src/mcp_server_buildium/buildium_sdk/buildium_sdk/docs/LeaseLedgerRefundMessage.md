# LeaseLedgerRefundMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Refund unique identifier. | [optional] 
**var_date** | **date** | Date of the refund. | [optional] 
**payees** | [**List[PayeeMessage]**](PayeeMessage.md) | List of payees being refunded. | [optional] 
**memo** | **str** | Memo associated with the refund, if applicable. | [optional] 
**check_number** | **str** | Check number associated with the refund, if applicable. | [optional] 
**bank_account_id** | **int** | Unique identifier of the bank account that the refund was made from. | [optional] 
**address** | [**AddressMessage**](AddressMessage.md) | Address to be displayed on the refund check. | [optional] 
**total_amount** | **float** | Total amount of the refund. | [optional] 
**lines** | [**List[LeaseLedgerRefundLineMessage]**](LeaseLedgerRefundLineMessage.md) | A collection of line items included in the refund. | [optional] 

## Example

```python
from buildium_sdk.models.lease_ledger_refund_message import LeaseLedgerRefundMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerRefundMessage from a JSON string
lease_ledger_refund_message_instance = LeaseLedgerRefundMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerRefundMessage.to_json())

# convert the object into a dict
lease_ledger_refund_message_dict = lease_ledger_refund_message_instance.to_dict()
# create an instance of LeaseLedgerRefundMessage from a dict
lease_ledger_refund_message_from_dict = LeaseLedgerRefundMessage.from_dict(lease_ledger_refund_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


