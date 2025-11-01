# LeaseLedgerDepositWithholdingPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date of the deposit withholding. The date must be formatted as YYYY-MM-DD. | 
**deposit_liability_gl_account_id** | **int** | The identifier of the liability general ledger account from which to withhold the funds. Note, the specified liability account must have a positive balance. | 
**memo** | **str** | Memo associated with the withholding. Memo cannot exceed 65 characters. | [optional] 
**lines** | [**List[LeaseLedgerDepositWithholdingLinePostMessage]**](LeaseLedgerDepositWithholdingLinePostMessage.md) | Line items specifying the income accounts the deposit will be applied to. The total amount of the line items can not exceed the balance of the liability account. | [optional] 

## Example

```python
from buildium_sdk.models.lease_ledger_deposit_withholding_post_message import LeaseLedgerDepositWithholdingPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LeaseLedgerDepositWithholdingPostMessage from a JSON string
lease_ledger_deposit_withholding_post_message_instance = LeaseLedgerDepositWithholdingPostMessage.from_json(json)
# print the JSON string representation of the object
print(LeaseLedgerDepositWithholdingPostMessage.to_json())

# convert the object into a dict
lease_ledger_deposit_withholding_post_message_dict = lease_ledger_deposit_withholding_post_message_instance.to_dict()
# create an instance of LeaseLedgerDepositWithholdingPostMessage from a dict
lease_ledger_deposit_withholding_post_message_from_dict = LeaseLedgerDepositWithholdingPostMessage.from_dict(lease_ledger_deposit_withholding_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


