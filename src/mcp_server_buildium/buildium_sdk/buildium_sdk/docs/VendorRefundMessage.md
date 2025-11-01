# VendorRefundMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction unique identifier. | [optional] 
**entry_date** | **date** | Date the refund was recorded. | [optional] 
**bank_account_id** | **int** | Unique identifier of the bank account that the refund was deposited into. | [optional] 
**payment_method** | **str** | The payment method used for the vendor refund. | [optional] 
**reference_number** | **str** | Reference number for the vendor refund. | [optional] 
**memo** | **str** | Memo for the vendor refund. | [optional] 
**lines** | [**List[VendorRefundLineMessage]**](VendorRefundLineMessage.md) | A collection of line items associated with the vendor refund. | [optional] 

## Example

```python
from buildium_sdk.models.vendor_refund_message import VendorRefundMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRefundMessage from a JSON string
vendor_refund_message_instance = VendorRefundMessage.from_json(json)
# print the JSON string representation of the object
print(VendorRefundMessage.to_json())

# convert the object into a dict
vendor_refund_message_dict = vendor_refund_message_instance.to_dict()
# create an instance of VendorRefundMessage from a dict
vendor_refund_message_from_dict = VendorRefundMessage.from_dict(vendor_refund_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


