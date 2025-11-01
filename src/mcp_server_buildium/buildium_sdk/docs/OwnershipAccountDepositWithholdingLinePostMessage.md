# OwnershipAccountDepositWithholdingLinePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Line item amount. | 
**gl_account_id** | **int** | General Ledger Account identifier under which the line item amount will be recorded. Must be an Income account. | 

## Example

```python
from buildium_sdk.models.ownership_account_deposit_withholding_line_post_message import OwnershipAccountDepositWithholdingLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipAccountDepositWithholdingLinePostMessage from a JSON string
ownership_account_deposit_withholding_line_post_message_instance = OwnershipAccountDepositWithholdingLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(OwnershipAccountDepositWithholdingLinePostMessage.to_json())

# convert the object into a dict
ownership_account_deposit_withholding_line_post_message_dict = ownership_account_deposit_withholding_line_post_message_instance.to_dict()
# create an instance of OwnershipAccountDepositWithholdingLinePostMessage from a dict
ownership_account_deposit_withholding_line_post_message_from_dict = OwnershipAccountDepositWithholdingLinePostMessage.from_dict(ownership_account_deposit_withholding_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


