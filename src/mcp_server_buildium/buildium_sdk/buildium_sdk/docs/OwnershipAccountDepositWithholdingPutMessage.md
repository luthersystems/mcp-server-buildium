# OwnershipAccountDepositWithholdingPutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date of the deposit withholding. The date must be formatted as YYYY-MM-DD. | 
**deposit_liability_gl_account_id** | **int** | The identifier of the liability general ledger account from which to withhold the funds. | 
**memo** | **str** | Memo associated with the withholding. Memo cannot exceed 65 characters. | [optional] 
**lines** | [**List[OwnershipAccountDepositWithholdingLinePutMessage]**](OwnershipAccountDepositWithholdingLinePutMessage.md) | Line items specifying the income accounts the deposit will be applied to. | [optional] 

## Example

```python
from buildium_sdk.models.ownership_account_deposit_withholding_put_message import OwnershipAccountDepositWithholdingPutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountDepositWithholdingPutMessage from a JSON string
ownership_account_deposit_withholding_put_message_instance = OwnershipAccountDepositWithholdingPutMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountDepositWithholdingPutMessage.to_json())

# convert the object into a dict
ownership_account_deposit_withholding_put_message_dict = ownership_account_deposit_withholding_put_message_instance.to_dict()
# create an instance of OwnershipAccountDepositWithholdingPutMessage from a dict
ownership_account_deposit_withholding_put_message_from_dict = OwnershipAccountDepositWithholdingPutMessage.from_dict(ownership_account_deposit_withholding_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


