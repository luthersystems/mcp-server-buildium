# VendorCreditLineItemMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor credit line item unique identifier. | [optional] 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the vendor credit. | [optional] 
**amount** | **float** | Amount of the vendor credit line item. | [optional] 
**memo** | **str** | Memo for the vendor credit line item. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | The accounting entity associated with the vendor credit line item. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_credit_line_item_message import VendorCreditLineItemMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCreditLineItemMessage from a JSON string
vendor_credit_line_item_message_instance = VendorCreditLineItemMessage.from_json(json)
# print the JSON string representation of the object
print(VendorCreditLineItemMessage.to_json())

# convert the object into a dict
vendor_credit_line_item_message_dict = vendor_credit_line_item_message_instance.to_dict()
# create an instance of VendorCreditLineItemMessage from a dict
vendor_credit_line_item_message_from_dict = VendorCreditLineItemMessage.from_dict(vendor_credit_line_item_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


