# VendorRefundPostMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **date** | Date the vendor refund was made. | 
**bank_account_id** | **int** | Unique identifier of the bank account that the refund was deposited into. | [optional] 
**payment_method** | **str** | The payment method used for the refund. | 
**reference_number** | **str** | The invoice or reference number that the vendor assigned to the refund. Reference number cannot exceed 45 characters. | [optional] 
**memo** | **str** | Memo associated with the vendor refund, if applicable. Memo cannot exceed 65 characters | [optional] 
**lines** | [**List[VendorRefundLinePostMessage]**](VendorRefundLinePostMessage.md) | A collection of line items associated with the vendor refund. | 

## Example

```python
from buildium_sdk.models.vendor_refund_post_message import VendorRefundPostMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRefundPostMessage from a JSON string
vendor_refund_post_message_instance = VendorRefundPostMessage.from_json(json)
# print the JSON string representation of the object
print(VendorRefundPostMessage.to_json())

# convert the object into a dict
vendor_refund_post_message_dict = vendor_refund_post_message_instance.to_dict()
# create an instance of VendorRefundPostMessage from a dict
vendor_refund_post_message_from_dict = VendorRefundPostMessage.from_dict(vendor_refund_post_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


