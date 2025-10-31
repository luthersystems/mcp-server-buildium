# OwnershipAccountDepositWithholdingLinePutMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | General Ledger Account identifier under which the line item amount will be recorded. Must be an Income account. | 

## Example

```python
from buildium_sdk.models.ownership_account_deposit_withholding_line_put_message import OwnershipAccountDepositWithholdingLinePutMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountDepositWithholdingLinePutMessage from a JSON string
ownership_account_deposit_withholding_line_put_message_instance = OwnershipAccountDepositWithholdingLinePutMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountDepositWithholdingLinePutMessage.to_json())

# convert the object into a dict
ownership_account_deposit_withholding_line_put_message_dict = ownership_account_deposit_withholding_line_put_message_instance.to_dict()
# create an instance of OwnershipAccountDepositWithholdingLinePutMessage from a dict
ownership_account_deposit_withholding_line_put_message_from_dict = OwnershipAccountDepositWithholdingLinePutMessage.from_dict(ownership_account_deposit_withholding_line_put_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


