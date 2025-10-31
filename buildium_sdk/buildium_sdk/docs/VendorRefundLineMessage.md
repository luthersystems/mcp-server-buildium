# VendorRefundLineMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor refund line item unique identifier. | [optional] 
**accounting_entity** | [**AccountingEntityMessage**](AccountingEntityMessage.md) | The accounting entity associated with the vendor refund line item. | [optional] 
**gl_account_id** | **int** | Unique identifier of the general ledger account associated with the vendor refund. | [optional] 
**amount** | **float** | Amount of the vendor refund line item. | [optional] 
**memo** | **str** | Memo for the vendor refund line item. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_refund_line_message import VendorRefundLineMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRefundLineMessage from a JSON string
vendor_refund_line_message_instance = VendorRefundLineMessage.from_json(json)
# print the JSON string representation of the object
print(VendorRefundLineMessage.to_json())

# convert the object into a dict
vendor_refund_line_message_dict = vendor_refund_line_message_instance.to_dict()
# create an instance of VendorRefundLineMessage from a dict
vendor_refund_line_message_from_dict = VendorRefundLineMessage.from_dict(vendor_refund_line_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


