# VendorRefundLinePostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the vendor refund. | 
**amount** | **float** | Amount of the vendor refund line item. | 
**memo** | **str** | Memo for the vendor refund line item. Memo cannot exceed 215 characters. | [optional] 
**accounting_entity** | [**AccountingEntitySaveMessage**](AccountingEntitySaveMessage.md) | The accounting entity associated with the vendor refund line item. | 

## Example

```python
from buildium_sdk.models.vendor_refund_line_post_message import VendorRefundLinePostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRefundLinePostMessage from a JSON string
vendor_refund_line_post_message_instance = VendorRefundLinePostMessage.from_json(json)
# print the JSON string representation of the object
print(VendorRefundLinePostMessage.to_json())

# convert the object into a dict
vendor_refund_line_post_message_dict = vendor_refund_line_post_message_instance.to_dict()
# create an instance of VendorRefundLinePostMessage from a dict
vendor_refund_line_post_message_from_dict = VendorRefundLinePostMessage.from_dict(vendor_refund_line_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


