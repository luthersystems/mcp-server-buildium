# VendorCreditLineItemPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the vendor credit. The account cannot be a bank account. | 
**amount** | **float** | Amount of the vendor credit line item. Must be between 0.01 and 9999999.99. | 
**memo** | **str** | Memo for the vendor credit line item. Cannot exceed 240 characters. | [optional] 
**accounting_entity** | [**AccountingEntitySaveMessage**](AccountingEntitySaveMessage.md) | The accounting entity associated with the vendor credit line item. | 

## Example

```python
from buildium_sdk.models.vendor_credit_line_item_post_message import VendorCreditLineItemPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCreditLineItemPostMessage from a JSON string
vendor_credit_line_item_post_message_instance = VendorCreditLineItemPostMessage.from_json(json)
# print the JSON string representation of the object
print(VendorCreditLineItemPostMessage.to_json())

# convert the object into a dict
vendor_credit_line_item_post_message_dict = vendor_credit_line_item_post_message_instance.to_dict()
# create an instance of VendorCreditLineItemPostMessage from a dict
vendor_credit_line_item_post_message_from_dict = VendorCreditLineItemPostMessage.from_dict(vendor_credit_line_item_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


